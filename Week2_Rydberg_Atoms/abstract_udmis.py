import abc

import numpy as np

class AbstractUDMIS(abc.ABC):
    @abc.abstractmethod
    def energy(self):
        """Returns the energy of the current Rydberg occupation configuration"""

    @abc.abstractmethod
    def energy_diff(self, *coords):
        """Returns the energy difference resulting from flipping the occupation at the given coordinates"""
        
    @abc.abstractmethod
    def rand_vertex(self):
        """Selects a site in the graph at random"""
    
    # initial fucntion
    # def mc_step(self, T):
    #     """Performs a full update of the Rydberg model using the Metropolis-Hastings algorithm"""
    #     current_energy = self.energy()
    #     for _ in range(self.num_vertices):
    #         vertex = self.rand_vertex()
    #         dE = self.energy_diff(vertex)

    #         if (dE < 0) or (np.random.rand() < np.exp(-dE / T)):
    #             current_energy += dE
    #             self.occupations[vertex] ^= 1

    #     return current_energy

    def mc_step(self, T):
        """Performs a full update of the Rydberg model using the Metropolis-Hastings algorithm"""
        current_energy = self.energy()
        for _ in range(self.num_vertices):
            vertex = self.rand_vertex()
            dE = self.energy_diff(vertex)

            if (dE < 0) or (np.random.rand() < np.exp(-dE / T)):
                current_energy += dE
                self.occupations[vertex] ^= 1 
                # flips occupation 0 --> 1 OR 1 --> 0

        return current_energy