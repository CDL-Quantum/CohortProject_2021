import numpy as np
import qutip as qt


class AbstractUDMIS():
    def __init__(self, u, graph):
        super().__init__()
        self.u, self.graph = u, graph
        self.num_vertices = len(self.graph)

        # Initialize system at infinite temperature (i.e. vertices are completely random and uncorrelated).
        self.occupations = np.random.rand(self.num_vertices) < 0.5
        self.edges = self.find_edges()

    def find_edges(self):
        """
        Calculate the distance between vertices; vertices within distance 1 share an edge.
        """
        edges = np.zeros((self.num_vertices, self.num_vertices), dtype=bool)
        for i in range(self.num_vertices - 1):
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
    def energy(self):
        """
        Returns the energy of the current Rydberg occupation configuration.
        """
        onsite_term, interaction_term = 0, 0
        for i in range(self.num_vertices):
            onsite_term += self.occupations[i]
            for j in range(i+1, self.num_vertices):
                if self.edges[i, j]:
                    interaction_term += self.occupations[i] * self.occupations[j]
        return self.u * interaction_term - onsite_term

    def energy_diff(self, i):
        """
        Returns the energy difference resulting from flipping the occupation at the given coordinates.
        """
        num_adjacent_occupied = sum(self.occupations[np.where(self.edges[i, :])[0]])
        if self.occupations[i] == 1:
            onsite_term_change = 1.
            interaction_term_change = -self.u * num_adjacent_occupied
        elif self.occupations[i] == 0:
            onsite_term_change = -1.
            interaction_term_change = self.u * num_adjacent_occupied
        return interaction_term_change + onsite_term_change

    def mc_step(self, T):
        """
        Performs a full update of the Rydberg model using the Metropolis-Hastings algorithm.
        """
        current_energy = self.energy()
        for _ in range(self.num_vertices):
            vertex = self.rand_vertex()
            dE = self.energy_diff(vertex)
            if (dE < 0) or (np.random.rand() < np.exp(-dE / T)):
                current_energy += dE
                self.occupations[vertex] ^= 1
        return current_energy


class QuantumUDMIS(AbstractUDMIS):
    def omega(self, t):
        """
        Calculate omega as a function of t.
        """
        if 0 <= t <= 0.25:
            return (omega_max / 0.25) * t
        elif 0.25 < t <= 0.69:
            return omega_max
        elif 0.69 < t <= 1:
            return - omega_max * t / 0.31 + omega_max * (1 + 0.69 / 0.31)

    def delta(self, t):
        """
        Calculate delta as a function of t.
        """
        slope = (delta_0 - delta_max) / (0.25 - 0.69)
        if 0 <= t <= 0.25:
            return delta_0
        elif 0.25 < t <= 0.69:
            return t * slope + (delta_max - slope * 0.69)
        elif 0.69 < t <= 1:
            return delta_max

    def hamiltonian(self, t):
        """
        Returns the UD-MIS Hamiltonian.
            H(t) = Ω(t) ∑_i σ_i^x - δ(t) ∑_i n_i + u ∑_ij n_i n_j
        """
        drive_term, onsite_term, interaction_term = 0, 0, 0
        for i in range(self.num_vertices):
            drive_term += identity_wrap(qt.sigmax(), i, self.num_vertices)
            onsite_term += identity_wrap(qt.num(2), i, self.num_vertices)
            for j in range(i + 1, self.num_vertices):
                if self.edges[i, j]:
                    interaction_term += \
                        identity_wrap(qt.num(2), i, self.num_vertices) * identity_wrap(qt.num(2), j, self.num_vertices)
        H = self.omega(t) * drive_term - self.delta(t) * onsite_term + self.u * interaction_term
        return H

    def time_evolution(self, dt):
        """
        Returns the time evolved state.
        """


"""
Useful functions
"""


def identity_wrap(operator, i, n):
    wrap = [qt.qeye(2) for _ in range(n)]
    wrap[i] = operator
    return qt.tensor(wrap)
