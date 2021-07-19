from functools import reduce
from itertools import product

import numpy as np
import qutip as qt
import scipy as sp
import tncontract as tn


def site_contract(t1, t2): return tn.contract(t1, t2, 'right', 'left')

def mps_expect(mps, gate, site):
    # gate should be a qutip operator
    dims = gate.dims[0]
    locality = len(dims)
    # gatetensor = tn.Tensor(gate.full().reshape(tuple(dims * 2)), ['in' + str(
    #     i) for i in range(locality)] + ['out' + str(i) for i in range(locality)])
    return mps.expval(gate, site, 
                    gate_inputs=['in' + str(i) for i in range(locality)],
                    gate_outputs=['out' + str(i) for i in range(locality)]
                    )


class LocalOperator(object):
    """
    Implements a simple model for a local 1-D operator defined on k sites (qubits)
    with a string of basis elements (Paulis  by default).

    Parameters
    ----------
    site : int
        Location of the first operator in the local operator
    key : string
        keystring e.g. 'XXZ'
    Nsites: int
    basis: dict
        Single site operators. {key: basis} if None then the Paulis are used as
        the basis elements
    """

    def __init__(self, site, key, Nsites, basis=None, phase=1.0):
        self.site = site
        self.key = key
        self.Nsites = Nsites
        self.support = set([i for i,k in zip(range(self.site, self.site + len(self.key)),self.key) if k!='I'])
        self.locality = len(self.support)
        self.phase = phase
        if basis is None:
            self.basis = {'I': qt.qeye(2),
                          'X': qt.sigmax(),
                          'Y': qt.sigmay(),
                          'Z': qt.sigmaz()}
            self._comm = {
                ('X', 'Y'): ('Z', 1j),
                ('X', 'Z'): ('Y', -1j),
                ('Y', 'X'): ('Z', -1j),
                ('Y', 'Z'): ('X', 1j),
                ('Z', 'Y'): ('X', -1j),
                ('Z', 'X'): ('Y', 1j)
            }
        else:
            Exception("Not implemented for non-Pauli basis.")
            self.basis = basis
        super(LocalOperator, self).__init__()

    def __repr__(self):
        return "Local Operator Object.\nNsites:\t{}\nsite:\t{}\nString:\t{}\n".format(
            self.Nsites, self.site, self.key)

    def local_operator(self):
        "Return the local operator on the defined support only"
        siteoperators = [self.basis[k] for k in self.key]
        return self.phase * reduce(qt.tensor, siteoperators)

    def full_operator(self):
        "Return the full operator defined on the whole spin chain"
        X = self.local_operator()
        string = [qt.qeye(2) for _ in range(self.site)] + [X] + [qt.qeye(2)
                                                                 for _ in range(self.site + len(self.key), self.Nsites)]
        return reduce(qt.tensor, string)

    def expect(self, mps):
        # A here should be a LocalOperator instance
        " Compute the expectation of a MatrixProductState with a LocalOperator"
        gates = tuple([tn.Tensor(self.basis[k].full(), ["out{}".format(i),
                        "in{}".format(i)]) for i, k in enumerate(self.key)])
        gate = self.phase * tn.tensor_product(*gates)
        return mps.expval(gate,self.site,
                            gate_inputs=['in' + str(i) for i in range(len(self.key))],
                            gate_outputs=['out' + str(i) for i in range(len(self.key))]).data

    def commutator(self, L):
        "Determine the LocalOperator that defines the commutator of two LocalOperators"
        intersect = self.support.intersection(L.support)
        if not(intersect):
            return LocalOperator(self.site, self.key, self.Nsites, phase=0.0)
        union = self.support.union(L.support)
        lsupport = [i for i in union if i < min(intersect)]
        rsupport = [i for i in union if i > max(intersect)]
        # intialise
        parity = 0
        phase = 1
        intstring = ''
        for i in sorted(list(intersect)):
            # look for non identical operators at each site
            if self.key[i - self.site] != L.key[i - L.site]:
                parity += 1
                si, pi = self._comm[(self.key[i - self.site],
                                    L.key[i - L.site])]
                intstring += si
                phase *= pi
            else:
                intstring += 'I'
        if (parity % 2) == 0:
            # operators commute if the parity is even, set the phase to 0. Not
            # pretty but will do for now.
            return LocalOperator(self.site, 'I', self.Nsites, phase=0.0)
        else:
            if lsupport:
                if self.site < min(intersect):
                    intstring = "".join([self.key[i - self.site]
                                         for i in lsupport]) + intstring
                else:
                    intstring = "".join([L.key[i - L.site]
                                         for i in lsupport]) + intstring
            if rsupport:
                if (self.site + self.locality - 1) > max(intersect):
                    intstring = intstring + \
                        "".join([self.key[i - self.site] for i in rsupport])
                else:
                    intstring = intstring + \
                        "".join([L.key[i - L.site] for i in rsupport])
            # we now know what the nontrivial commutator is
            return LocalOperator(
                min(union),
                intstring,
                self.Nsites,
                phase=(
                    2 * phase))


class LocalHamiltonian(object):
    """
    Implements a simple model for a local 1-D Hamiltonian defined on N qubits.

    Parameters
    ----------
    c : dict
        {(site,key): coupling coefficient}
    Nsites: int
    """

    def __init__(self, c, Nsites, B=None):
        self.c = c  # dictionary of {(site,key): c_i}
        self.locality = max([len(k) for _, k in c.keys()])
        self.Nsites = Nsites
        self.B = {'I': qt.qeye(2).full(),
                  'X': qt.sigmax().full(),
                  'Y': qt.sigmay().full(),
                  'Z': qt.sigmaz().full()}
        self.mpo = self.matrix_product_operator()
        super(LocalHamiltonian, self).__init__()

    def __repr__(self):
        return "Local Hamiltonian Object:\nNsites:\t\t{}\nLocality:\t{}".format(
            self.Nsites, self.locality)

    def __add__(self, H):
        if self.Nsites != H.Nsites:
            raise Exception(
                "Hamiltonians have different systems sizes: {} and {}-qubits are incompatible".format(
                    self.Nsites, H.nsites))
        newkeys = set(self.c.keys()).union(H.c.keys())
        sum_couplings = {k: self.c.get(k, 0) + H.c.get(k, 0) for k in newkeys}
        return LocalHamiltonian(sum_couplings, self.Nsites)

    def full_operator(self):
        # initialize Hamiltonian
        H = qt.Qobj(np.zeros([2 ** self.Nsites, 2 ** self.Nsites],
                             dtype='complex128'), dims=[[2] * self.Nsites] * 2)
        for i, key in self.c.keys():
            H = H + self.c[(i, key)] * LocalOperator(i, key,
                                                     self.Nsites).full_operator()
        return H

    def _site_tensor(self, i):
        c = self.c
        B = self.B
        chi = sum([3**k for k in range(self.locality)]) + 1
        if i == 0:
            M = np.zeros((2, 2, chi), dtype='complex128')
            paulis = ['X', 'Y', 'Z']
            suffices = []
            for k in range(self.locality):
                r = tuple([range(3) for _ in range(k)])
                suffices += ["".join(reversed([paulis[j] for j in ranges]))
                             for ranges in product(*r)]
            for j in range(chi - 1):
                M[:,
                  :,
                  j] = c.get((i,
                              'X' + suffices[j]),
                             0) * B['X'] + c.get((i,
                                                  'Y' + suffices[j]),
                                                 0) * B['Y'] + c.get((i,
                                                                      'Z' + suffices[j]),
                                                                     0) * B['Z']
            M[:, :, -1] = B['I']
            return tn.Tensor(M, ['physout', 'physin', 'right'])
        elif i == (self.Nsites - 1):
            M = np.zeros((2, 2, chi), dtype='complex128')
            M[:, :, 0] = B['I']
            M[:, :, 1] = B['X']
            M[:, :, 2] = B['Y']
            M[:, :, 3] = B['Z']
            M[:, :, -1] = c.get((i, 'X'), 0) * B['X'] + c.get((i, 'Y'), 0) * \
                B['Y'] + c.get((i, 'Z'), 0) * B['Z']  # single site terms
            return tn.Tensor(M, ['physout', 'physin', 'left'])
        else:
            M = np.zeros((2, 2, chi, chi), dtype='complex128')
            M[:, :, 0, 0] = B['I']
            for j in range(int((chi - 2) / 3)):
                M[:, :, 3 * j + 1, j] = B['X']
                M[:, :, 3 * j + 2, j] = B['Y']
                M[:, :, 3 * j + 3, j] = B['Z']
            paulis = ['X', 'Y', 'Z']
            suffices = []
            for k in range(self.locality):
                r = tuple([range(3) for _ in range(k)])
                suffices += ["".join(reversed([paulis[j] for j in ranges]))
                             for ranges in product(*r)]
            for j in range(chi - 1):
                M[:, :, -1, j] = c.get((i, 'X' + suffices[j]), 0) * B['X'] + c.get(
                    (i, 'Y' + suffices[j]), 0) * B['Y'] + c.get((i, 'Z' + suffices[j]), 0) * B['Z']
            M[:, :, -1, -1] = B['I']
            return tn.Tensor(M, ['physout', 'physin', 'left', 'right'])

    def couplings(self, B):
        return np.array([[self.c[(b.site, b.key)]] for b in B])

    def matrix_product_operator(self):
        assert self.Nsites > 2
        return tn.onedim.MatrixProductOperator(
            [self._site_tensor(i) for i in range(self.Nsites)])

    def ground_state(
            self,
            chi=8,
            Nsweeps=100,
            threshold=1e-9,
            eps=1e-12,
            algorithm='2-site'):
        D = DMRG(self, chi)
        if algorithm == '2-site':
            D.run_2(Nsweeps=Nsweeps, threshold=threshold, eps=eps)
        elif algorithm == 'single-site':
            D.run(Nsweeps=Nsweeps, eps=eps)
        else:
            raise Exception(
                "algorithm should be either 'single-site' or '2-site'. {} not defined".format(algorithm))
        return D.mps

    def correlation_matrix(self,psi,B):
        K = 1j*np.zeros([len(B),len(B)])
        for i in range(len(B)):
            for j in range(i,len(B)):
                #simplest check is to see if operator (at least) overlap
                if B[i].support.intersection(B[j].support):
                    C = B[i].commutator(B[j])
                    # C.phase will be zero if they commute
                    if C.phase:
                        if type(psi) is tn.onedim.MatrixProductState:
                            K[i,j] = C.expect(psi)
                        else:
                            K[i,j] = qt.expect(C.full_operator(),psi)
                        K[j,i] = -K[i,j]
        return 1j * K


class DMRG(object):
    def __init__(self, H, chi=1, mps=None):
        self.H = H
        self.Nsites = H.Nsites
        self.chi = chi
        if mps is None:
            self.mps = self._random_mps(chi, self.Nsites)
        else:
            self.mps = mps
        self.env_sites = self._env_sites()
        super(DMRG, self).__init__()

    def __repr__(self):
        return "DMRG Instance.\nNsites:\t{}\nchi:\t{}".format(
            self.Nsites, self.chi)

    def _random_mps(self, chi, Nsites):
        mps = []
        for i in range(Nsites):
            if i == 0:
                # we will start here so doesn't matter what this tensor is
                M = tn.Tensor(np.random.randn(2, chi) + 1j *
                              np.random.randn(2, chi), ['phys', 'right'])
            elif i == (Nsites - 1):
                M = tn.Tensor(np.random.randn(2, chi) + 1j *
                              np.random.randn(2, chi), ['phys', 'left'])
            else:
                M = tn.Tensor(np.random.randn(2, chi, chi) + 1j *
                              np.random.randn(2, chi, chi), ['phys', 'left', 'right'])
            mps.append(M)
        mps = tn.onedim.MatrixProductState(mps)
        mps.right_canonise(normalise=True)
        return mps

    def _env_sites(self):
        env_sites = []
        for site in range(self.Nsites):
            psi_i = self.mps[site].copy()
            H_i = self.H.mpo[site].copy()
            psi_i_d = self._conj(psi_i)
            psi_i.replace_label(['left', 'right'], ['left_top', 'right_top'])
            H_i.replace_label(['left', 'right'], [
                              'left_middle', 'right_middle'])
            psi_i_d.replace_label(['left', 'right'], [
                                  'left_bottom', 'right_bottom'])
            env_sites.append(
                tn.contract(
                    tn.contract(
                        psi_i,
                        H_i,
                        'phys',
                        'physin'),
                    psi_i_d,
                    'physout',
                    'phys'))
        return env_sites

    def _conj(self, T):
        return tn.Tensor(T.data.conj(), T.labels)

    def _env_contract(self, E1, E2):
        return tn.contract(
            E1, E2, [
                'right_top', 'right_middle', 'right_bottom'], [
                'left_top', 'left_middle', 'left_bottom'])

    def _update_env_tensor(self, site):
        psi_i = self.mps[site].copy()
        H_i = self.H.mpo[site].copy()
        psi_i_d = self._conj(psi_i)
        psi_i.replace_label(['left', 'right'], ['left_top', 'right_top'])
        H_i.replace_label(['left', 'right'], ['left_middle', 'right_middle'])
        psi_i_d.replace_label(['left', 'right'], [
                              'left_bottom', 'right_bottom'])
        self.env_sites[site] = tn.contract(
            tn.contract(
                psi_i,
                H_i,
                'phys',
                'physin'),
            psi_i_d,
            'physout',
            'phys')

    def _environment(self, site, left=None, right=None):
        center = self.H.mpo[site]
        if site == 0:  # Left end
            if right is None:
                right = reduce(
                    self._env_contract, [
                        self.env_sites[i] for i in range(
                            site + 1, self.Nsites)])
            e = tn.contract(center, right, 'right', 'left_middle')
        elif site == (self.Nsites - 1):  # right end
            if left is None:
                left = reduce(
                    self._env_contract, [
                        self.env_sites[i] for i in range(site)])
            e = tn.contract(left, center, 'right_middle', 'left')
        else:  # in the middle of the chain
            if left is None:
                left = reduce(
                    self._env_contract, [
                        self.env_sites[i] for i in range(site)])
            if right is None:
                right = reduce(
                    self._env_contract, [
                        self.env_sites[i] for i in range(
                            site + 1, self.Nsites)])
            e = tn.contract(
                tn.contract(
                    left,
                    center,
                    'right_middle',
                    'left'),
                right,
                'right',
                'left_middle')
        e.consolidate_indices()
        e.remove_all_dummy_indices()
        return e

    def _cummulative_contracted_env(self, direction):
        if direction == 'left':
            lefts = [self.env_sites[0]]
            for i in range(1, self.Nsites):
                lefts.append(self._env_contract(lefts[-1], self.env_sites[i]))
            return lefts
        else:
            rights = [self.env_sites[-1]]
            for i in reversed(range(self.Nsites - 1)):
                rights = [
                    self._env_contract(
                        self.env_sites[i],
                        rights[0])] + rights
            return rights

    def _environment_2_site(self, site, direction, left=None, right=None):
        if direction == 'left':
            lsite = site - 1
            rsite = site
        else:
            lsite = site
            rsite = site + 1
        center_left = self.H.mpo[lsite].copy()
        center_left.replace_label(['physin', 'physout'], [
                                  'physin_left', 'physout_left'])
        center_right = self.H.mpo[rsite].copy()
        center_right.replace_label(['physin', 'physout'], [
                                   'physin_right', 'physout_right'])
        center = tn.contract(center_left, center_right, 'right', 'left')
        if (site == 0) or (site == 1 and direction == 'left'):  # Left end
            if right is None:
                right = reduce(
                    self._env_contract, [
                        self.env_sites[i] for i in range(
                            rsite + 1, self.Nsites)])
            e = tn.contract(center, right, 'right', 'left_middle')
        elif site == (self.Nsites - 1) or (site == (self.Nsites - 2) and direction == 'right'):  # right end
            if left is None:
                left = reduce(
                    self._env_contract, [
                        self.env_sites[i] for i in range(
                            lsite - 1)])
            e = tn.contract(left, center, 'right_middle', 'left')
        else:  # in the middle of the chain
            if left is None:
                left = reduce(
                    self._env_contract, [
                        self.env_sites[i] for i in range(lsite)])
            if right is None:
                right = reduce(
                    self._env_contract, [
                        self.env_sites[i] for i in range(
                            rsite + 1, self.Nsites)])
            e = tn.contract(
                tn.contract(
                    left,
                    center,
                    'right_middle',
                    'left'),
                right,
                'right',
                'left_middle')
        e.consolidate_indices()
        e.remove_all_dummy_indices()
        return e

    def _optimise_site(self, site, direction):
        # direction is the handedness of the canonisation (opposite to the
        # sweep direction)
        env = self._environment(site).copy()
        # save the initial labels to reshape back to original
        ls = {l: s for (l, s) in zip(env.labels, list(env.shape))}
        env.fuse_indices(['right_top', 'physin', 'left_top'], 'top')
        env.fuse_indices(['right_bottom', 'physout', 'left_bottom'], 'bottom')
        _, V = np.linalg.eigh(env.data)
        M = tn.Tensor(V.T[0])
        M.split_index(
            'i0', (ls.get(
                'right_top', 1), 2, ls.get(
                'left_top', 1)), [
                'left', 'phys', 'right'])
        self.mps[site] = M
        self._canonise(site, direction)

    def _optimise_2_sites(
            self,
            site,
            direction,
            threshold,
            left=None,
            right=None):
        if direction == 'left':
            lsite = site - 1
            rsite = site
        else:
            lsite = site
            rsite = site + 1
        # direction is the handedness of the canonisation (opposite to the
        # sweep direction)
        env = self._environment_2_site(
            site, direction, left=left, right=right).copy()
        # save the initial labels to reshape back to original
        ls = {l: s for (l, s) in zip(env.labels, list(env.shape))}
        env.fuse_indices(['right_top', 'physin_left',
                          'physin_right', 'left_top'], 'top')
        env.fuse_indices(['right_bottom', 'physout_left',
                          'physout_right', 'left_bottom'], 'bottom')
        _, V = np.linalg.eigh(env.data)
        M = tn.Tensor(V.T[0])
        M.split_index(
            'i0', (ls.get(
                'right_top', 1), 2, 2, ls.get(
                'left_top', 1)), [
                'left', 'phys_left', 'phys_right', 'right'])
        Mleft, Mright, _ = tn.truncated_svd(
            M, ['left', 'phys_left'], threshold=threshold, absorb_singular_values=direction)
        Mleft.replace_label(['svd_in', 'phys_left'], ['right', 'phys'])
        Mright.replace_label(['svd_out', 'phys_right'], ['left', 'phys'])
        self.mps[lsite] = Mleft
        self.mps[rsite] = Mright
        self._update_env_tensor(lsite)
        self._update_env_tensor(rsite)
        if direction == 'left':
            if site < (self.Nsites - 1):
                # return the new right hand environment tensor
                return self._env_contract(self.env_sites[rsite], right)
            else:
                return self.env_sites[-1]
        else:
            if site > 0:
                # return the new left hand environment tensor
                return self._env_contract(left, self.env_sites[lsite])
            else:
                return self.env_sites[0]

    def _canonise(self, site, direction):
        # direction is the sweep direction, canonisation is the opposite
        if direction == 'left':
            self.mps.right_canonise(site, site + 1, normalise=False)
        else:
            self.mps.left_canonise(site, site + 1, normalise=False)
        self._update_env_tensor(site)

    def energy(self):
        contracted = self._cummulative_contracted_env('left')[-1]
        contracted.consolidate_indices()
        contracted.remove_all_dummy_indices()
        return np.real(contracted.data)

    def covariance(self):
        Hmps = tn.onedim.contract_mps_mpo(self.mps, self.H.mpo)
        return tn.onedim.inner_product_mps(
            Hmps, Hmps) - tn.onedim.inner_product_mps(self.mps, Hmps) ** 2

    def mps_state(self):
        psi = reduce(site_contract, self.mps)
        psi.remove_all_dummy_indices()
        psi.consolidate_indices()
        return qt.Qobj(psi.data, dims=[[2] * self.Nsites, [1] * self.Nsites])

    def run(self, Nsweeps=100, eps=1e-16):
        energyprev = self.energy()
        for _ in range(Nsweeps):
            for site in range(self.Nsites - 1):
                self._optimise_site(site, 'right')
            for site in reversed(range(1, self.Nsites)):
                self._optimise_site(site, 'left')
            energy = self.energy()
            if abs(energy - energyprev) < eps:
                break
            energyprev = energy
            # bar.update(Energy=np.real(self.energy()))

    def run_2(self, Nsweeps=100, threshold=1e-12, eps=1e-15):
        energyprev = self.energy()
        for _ in range(Nsweeps):
            # First sweep from left to right
            rights = self._cummulative_contracted_env('right')
            left = None
            for site in range(self.Nsites - 2):
                left = self._optimise_2_sites(
                    site, 'right', threshold, left=left, right=rights[site + 2])
            lefts = self._cummulative_contracted_env('left')
            right = None
            for site in reversed(range(1, self.Nsites)):
                right = self._optimise_2_sites(
                    site, 'left', threshold, left=lefts[site - 2], right=right)
            energy = self.energy()
            if abs(energy - energyprev) < eps:
                break
            energyprev = energy

def svd_compress_mpo(mpo):
    # fuse the physical indices to make the mpo mps-like
    mps = []
    for site in mpo:
        site.fuse_indices(['physin', 'physout'], 'phys')
        mps.append(site)
    # this like the purification of the mpo
    mps = tn.onedim.MatrixProductState(mps)
    # canonise it to compress it
    mps.svd_compress()
    mpo_compressed = []
    # convert it back into an mpo
    for site in mps:
        site.split_index('phys', [2, 2], ['physin', 'physout'])
        mpo_compressed.append(site)
    return tn.onedim.MatrixProductOperator(mpo_compressed)