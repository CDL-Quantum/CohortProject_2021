import numpy as np


class AbstractUDMIS():
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


class UDMIS(AbstractUDMIS):
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
            for j in range(i + 1, self.num_vertices):
                x_j, y_j = self.graph[j]
                if np.sqrt((x_i - x_j) ** 2. + (y_i - y_j) ** 2.) <= 1.0:
                    edges[i, j], edges[j, i] = True, True
        return edges

    def energy(self):
        """
        Returns the energy of the current Rydberg occupation configuration.
        """
        onsite_term, interaction_term = 0, 0
        for i in range(self.num_vertices):
            onsite_term += self.occupations[i]
            for j in range(i + 1, self.num_vertices):
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

    def rand_vertex(self):
        """
        Selects a site in the graph at random.
        """
        return np.random.randint(self.num_vertices)
