import numpy as np
import tncontract as tn
import qutip as qt

def bit_flip_layer(p, n_sites):
    """
    Return a circuit layer each site experiences a bitflip error with
    probability p
    """
    x_error = tn.Tensor(qt.sigmax().full().reshape(2, 2, 1, 1), ['physout', 'physin', 'left', 'right'])
    id_tensor = tn.Tensor(np.eye(2).reshape(2, 2, 1, 1), ['physout', 'physin', 'left', 'right'])
    return tn.onedim.MatrixProductOperator([x_error if error_site else id_tensor for error_site in np.random.binomial(1, p, n_sites)])


def single_qubit_gate(theta, phi):
    """
    Return a generic single qubit unitary gate
    """
    gate = np.array([[np.cos(theta / 2), -1j * np.exp(-1j * phi) * np.sin(theta / 2)],
                     [-1j * np.exp(1j * phi) * np.sin(theta / 2), np.cos(theta / 2)]])
    return tn.Tensor(gate.reshape(2, 2, 1, 1), ['physout', 'physin', 'left', 'right'])


def two_qubit_ms_gate(theta):
    """
    Return a two qubit addressed molmer sorenson gate
    """
    gate = qt.operations.molmer_sorensen(theta, 2).full()

    # turn the gate into Tensor with physical and virtual bonds
    gate_tensor = tn.Tensor(gate.reshape(4, 4, 1, 1), ['physout', 'physin', 'left', 'right'])

    # split physical bonds into single qubit sites
    gate_tensor.split_index('physout', (2, 2), ['physout_1', 'physout_2'])
    gate_tensor.split_index('physin', (2, 2), ['physin_1', 'physin_2'])

    # SVD cut the two qubit gate into small 2-site MPO
    U, V = tn.tensor_svd(gate_tensor, row_labels=['physout_1', 'physin_1', 'left'], absorb_singular_values='left')
    U.replace_label(['physout_1', 'physin_1', 'svd_in'], ['physout', 'physin', 'right'])
    V.replace_label(['physout_2', 'physin_2', 'svd_out'], ['physout', 'physin', 'left'])
    return [U, V]


def two_qubit_gate_layer(n_sites, thetas, align=0):
    """
    Return an MPO with MS gates along the chain with angles.
    Parameters
        ----------
        n_sites : int
        thetas: list
            list of MS gate angles
        align : int
            If n_sites is an odd number, align determines wether the two qubit gates begin from
            qubit 0 (aligned left) or 1 (aligned right).
    """
    if align != 0 and align != 1:
        raise ValueError("align={}. Can only take the value 0 or 1".format(align))

    id_tensor = tn.Tensor(np.eye(2).reshape(2, 2, 1, 1), ['physout', 'physin', 'left', 'right'])
    mpo = []
    for theta in thetas:
        mpo += two_qubit_ms_gate(theta)

    if n_sites % 2 == 0:
        return tn.onedim.MatrixProductOperator(mpo)
    else:
        if align == 0:
            # put an identity tensor at end qubit
            return tn.onedim.MatrixProductOperator(mpo + [id_tensor])
        else:
            # put and identity tensor on the first qubits
            return tn.onedim.MatrixProductOperator([id_tensor] + mpo)


def random_two_qubit_gate_layer(n_sites, align=0):
    """
    Return an MPO with random angle MS gates along the chain.
    Parameters
        ----------
        n_sites : int
        align : int
            If n_sites is an odd number, align determines wether the two qubit gates begin from
            qubit 0 (aligned left) or 1 (aligned right).
    """
    thetas = 2 * np.pi * np.random.rand(int(np.floor(n_sites / 2)))
    return two_qubit_gate_layer(n_sites, thetas, align=align)

def single_qubit_gate_layer(n_sites, angles):
    """
    Return an MPO with MS gates along the chain with angles.
    Parameters
        ----------
        n_sites : int
        thetas: list
            list of tuples containing the single qubit rotation angles. Each site
            needs (\theta_i, \phi_i)

    """
    mpo = [single_qubit_gate(*site_angles) for site_angles in angles]
    return tn.onedim.MatrixProductOperator(mpo)

def random_single_qubit_gate_layer(n_sites):
    """
    Return an MPO with random single qubit rotations along the chain.
    Parameters
        ----------
        n_sites : int
    """
    angles = [(2 *np.pi * np.random.rand(), 2 *np.pi * np.random.rand()) for _ in range(n_sites)]
    return single_qubit_gate_layer(n_sites, angles)