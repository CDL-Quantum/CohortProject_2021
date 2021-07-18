import ray
import pickle
import numpy as np

from Week2_Rydberg_Atoms.abstract_udmis import AbstractUDMIS
from Week2_Rydberg_Atoms.utils import sanity_check, normalize_coordinates


class UDMIS(AbstractUDMIS):
    def __init__(self, u, graph):
        super().__init__()
        self.u, self.graph = u, graph
        self.num_vertices = len(self.graph)
        # initialize system at infinite temperature
        # i.e. vertices are completely random and uncorrelated
        self.occupations = np.random.rand(self.num_vertices) < 0.5
        self.edges = self.find_edges()

    def find_edges(self):
        # num_pairs = int(self.num_vertices*(self.num_vertices)*0.5)
        edges = np.zeros((self.num_vertices, self.num_vertices), dtype=bool)

        for i in range(self.num_vertices - 1):
            x_i, y_i = self.graph[i]  # these are the x, y coordinates of the i'th vertex in the graph
            for j in range(i + 1, self.num_vertices):
                x_j, y_j = self.graph[j]  # these are the x, y coordinates of the j'th vertex in the graph

                # calculate the distance between vertices
                dij = np.sqrt((x_i - x_j) ** 2. + (y_i - y_j) ** 2.)
                if dij <= 1.0:
                    edges[i, j] = True
                    edges[j, i] = True

        return edges

    def energy(self):
        """Returns the energy of the current spin configuration"""
        # interaction term
        interaction_term = 0
        vertex_term = 0
        for i in range(self.num_vertices - 1):
            for j in range(i + 1, self.num_vertices):

                # check if there is an edge
                if self.edges[i, j]:
                    interaction_term += self.occupations[i] * self.occupations[j]

            vertex_term += self.occupations[i]

        # missed the last vertex
        vertex_term += self.occupations[self.num_vertices - 1]

        return self.u * interaction_term - vertex_term

    def energy_diff(self, i):
        connections = np.where(self.edges[i, :])[0]
        num_adjacent_occupied = sum(self.occupations[connections])

        if self.occupations[i] == 1:
            # flipping an occupied vertex increases the vertex term, decreases the interaction term
            vertex_term_change = 1.
            interaction_term_change = -self.u * num_adjacent_occupied

        elif self.occupations[i] == 0:
            # flipping an unoccupied vertex decreases the vertex term, increases the interaction term
            vertex_term_change = -1.
            interaction_term_change = self.u * num_adjacent_occupied

        else:
            raise RuntimeError

        return interaction_term_change + vertex_term_change

    def rand_vertex(self):
        """Selects a site in the graph at random"""
        return np.random.randint(self.num_vertices)


@ray.remote
def Task_add2(args):
    N, th, g, name = args
    t = np.arange(N + 1)
    T_i = 100
    T_f = 0.01
    T = T_i * ((T_f / T_i) ** (t / N))
    N_it = 10000
    m = 0
    udmis = UDMIS(u=1.35, graph=g)

    for j in range(N_it):
        for t in range(N + 1):
            temp = T[t]
            E = udmis.mc_step(T=temp)

            if t == N:
                num_violated, num_vertices = sanity_check(udmis.graph, answer=udmis.occupations, radius=0.5)
                if num_violated == 0 and num_vertices == th:
                    m += 1
    pr = m / N_it
    print(name, N, pr)
    return name, N, pr


N_list = [10, 50, 100, 500, 1000]

if __name__ == "__main__":
    with open('city_example_dataset.txt', 'rb') as of:
        cities = pickle.load(of)
    sorted_key = sorted(list(cities.keys()), key=lambda x: len(cities[x]['graph']))[:-2]
    worklist = list()
    th_list = [2, 4, 5, 6]
    for i, key in enumerate(sorted_key):
        g = normalize_coordinates(cities[key]['graph'], radius=cities[key]['radius'])
        for N in N_list:
            worklist.append((N, th_list[i], g, key))  # N, th, udmis, name
    ray.init()
    result = ray.get([Task_add2.remote(args) for args in worklist])
    with open('classical_ann.txt', 'wb') as of:
        pickle.dump(result, of)
