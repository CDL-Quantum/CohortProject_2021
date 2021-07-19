import numpy as np
import qutip as qt
import src.local as lo

class AbstractUDMIS():
    def __init__(self, u, graph):
        """
        Find edges in the graph.
        """
        self.u, self.graph = u, graph
        self.num_vertices = len(self.graph)
        self.edges = self.find_edges()

    def find_edges(self):
        """
        Calculate the distance between vertices; vertices within distance 1 share an edge.
        """
        edges = np.zeros((self.num_vertices, self.num_vertices), dtype=bool)
        for i in range(self.num_vertices-1):
            x_i, y_i = self.graph[i]
            for j in range(i+1, self.num_vertices):
                x_j, y_j = self.graph[j]
                if np.sqrt((x_i - x_j) ** 2. + (y_i - y_j) ** 2.) <= 1.0:
                    edges[i, j], edges[j, i] = True, True
        return edges

    def rand_vertex(self):
        """
        Selects a site in the graph at random.
        """
        return np.random.randint(self.num_vertices)


class ClassicalUDMIS(AbstractUDMIS):
    def __init__(self, u, graph):
        """
        Initialize system with vertices randomly occupied.
        """
        super().__init__(u, graph)
        self.state = np.random.rand(self.num_vertices) < 0.5

    def energy(self):
        """
        Returns the energy of the current Rydberg occupation configuration.
        """
        onsite_term, interaction_term = 0, 0
        for i in range(self.num_vertices):
            onsite_term += self.state[i]
            for j in range(i+1, self.num_vertices):
                if self.edges[i, j]:
                    interaction_term += self.state[i] * self.state[j]
        return - onsite_term + self.u * interaction_term

    def energy_diff(self, i):
        """
        Returns the energy difference caused by flipping the state at the given vertex.
        """
        num_adjacent_occupied = sum(self.state[np.where(self.edges[i, :])[0]])
        if self.state[i] == 1:
            onsite_term_change = 1.
            interaction_term_change = -self.u * num_adjacent_occupied
        elif self.state[i] == 0:
            onsite_term_change = -1.
            interaction_term_change = self.u * num_adjacent_occupied
        return onsite_term_change + interaction_term_change

    def monte_carlo_step(self, T):
        """
        Performs a full update of the Rydberg model using the Metropolis-Hastings algorithm.
        """
        current_energy = self.energy()
        for _ in range(self.num_vertices):
            vertex = self.rand_vertex()
            dE = self.energy_diff(vertex)
            if (dE < 0) or (np.random.rand() < np.exp(-dE / T)):
                current_energy += dE
                self.state[vertex] ^= 1
        return current_energy


class MPOClassicalUDMIS(AbstractUDMIS):
    def __init__(self, u, graph):
        """
        Initialize system with vertices randomly occupied.
        """
        super().__init__(u, graph)
        self.hamiltonian = self._hamiltonian()

    def _hamiltonian(self):
        # We will define the local Hamiltonian as a sum of local Paulis
        couplings = {}
        for i in range(self.num_vertices):
            couplings[(i, "Z")] = couplings.get((i, "Z"), 0) + 0.5
            couplings[(i, "I")] = couplings.get((i, "I"), 0) - 0.5
            for j in range(i + 1, self.num_vertices):
                if self.edges[i, j]:
                    # Add the two single site (Z_i / Z_j) terms
                    couplings[(i, "Z")] = couplings.get((i, "Z"), 0) - self.u / 4
                    couplings[(j, "Z")] = couplings.get((j, "Z"), 0) - self.u / 4

                    # Add the edge term
                    weight = j - i
                    string = "Z" + "".join(["I" for _ in range(weight - 1)]) + "Z"
                    couplings[(i, string)] = couplings.get((i, string), 0) + self.u / 4
                    couplings[(i, "I")] = couplings.get((i, "I"), 0) + self.u / 4
        H = lo.LocalHamiltonian(couplings, self.num_vertices)
        H.mpo = lo.svd_compress_mpo(H.mpo)
        #still want to compress this as it will be highly inefficient
        return H

    def ground_state(self):
        return self.hamiltonian.ground_state()

    def gs_bitstring(self):
        gs = self.ground_state()[0]
        bs = []
        for s in gs:
            bs.append(site_to_bitstring(s))
        return bs

class QuantumUDMIS(AbstractUDMIS):
    def __init__(self, u, graph, omega_max, delta_0, delta_max):
        """
        Initialize system with all qubits in the |0> state.
        """
        super().__init__(u, graph)
        self.omega_max, self.delta_0, self.delta_max = omega_max, delta_0, delta_max
        self.state = qt.tensor([qt.basis(2) for _ in range(self.num_vertices)])

    def omega(self, t):
        """
        Calculate omega as a function of t.
        """
        if 0 <= t <= 0.25:
            return (self.omega_max / 0.25) * t
        elif 0.25 < t <= 0.69:
            return self.omega_max
        elif 0.69 < t <= 1:
            return - self.omega_max * t / 0.31 + self.omega_max * (1 + 0.69 / 0.31)

    def delta(self, t):
        """
        Calculate delta as a function of t.
        """
        slope = (self.delta_0 - self.delta_max) / (0.25 - 0.69)
        if 0 <= t <= 0.25:
            return self.delta_0
        elif 0.25 < t <= 0.69:
            return t * slope + (self.delta_max - slope * 0.69)
        elif 0.69 < t <= 1:
            return self.delta_max

    def hamiltonian(self, t):
        """
        Returns the UD-MIS Hamiltonian.
            H(t) = Ω(t) ∑_i σ_i^x - δ(t) ∑_i n_i + u ∑_ij n_i n_j
        """
        drive_term, onsite_term, interaction_term = 0, 0, 0
        for i in range(self.num_vertices):
            drive_term += identity_wrap(qt.sigmax(), self.num_vertices, i)
            onsite_term += identity_wrap(qt.num(2), self.num_vertices, i)
            for j in range(i + 1, self.num_vertices):
                if self.edges[i, j]:
                    interaction_term += identity_wrap(qt.num(2), self.num_vertices, i) * \
                                        identity_wrap(qt.num(2), self.num_vertices, j)
        return self.omega(t) * drive_term - self.delta(t) * onsite_term + self.u * interaction_term

    def energy(self, t):
        """
        Returns the energy of the current Rydberg occupation configuration.
        """
        return qt.expect(self.hamiltonian(t), self.state)

    def time_evolution_step(self, t, dt):
        """
        Returns the time evolved quantum state.
        """
        return qt.sesolve(self.hamiltonian(t), self.state, [0, dt]).states[1]


"""
Useful functions
"""


def identity_wrap(operator, num_sites, i):
    operators = [qt.qeye(2) for _ in range(num_sites)]
    operators[i] = operator
    return qt.tensor(operators)

def site_to_bitstring(A):
     # expects a site from an mps
     outcomes = [np.linalg.norm((A.data[0].T @ qt.basis(2, 0).full())).round(2),
                 np.linalg.norm((A.data[0].T @ qt.basis(2, 1).full())).round(2)]
     return sorted(range(2), key=lambda i: np.linalg.norm(outcomes[i]), reverse=True)[0]
