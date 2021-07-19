import numpy as np
import matplotlib.pyplot as plt

from abstract_udmis import AbstractUDMIS

#matplotlib inline


class UDMIS(AbstractUDMIS):
    def __init__(self, u, graph):
        super().__init__()
        self.u, self.graph = u, graph
        self.num_vertices = len(self.graph)
        print(self.num_vertices)
        # initialize system at infinite temperature
        # i.e. vertices are completely random and uncorrelated
        self.occupations = np.random.rand(self.num_vertices) < 0.5
        self.edges = self.find_edges()
    
    def find_edges(self):
        #num_pairs = int(self.num_vertices*(self.num_vertices)*0.5)
        edges = np.zeros((self.num_vertices, self.num_vertices), dtype=bool)
        
        for i in range(self.num_vertices-1):
            x_i, y_i = graph[i] # these are the x, y coordinates of the i'th vertex in the graph
            for j in range(i+1, self.num_vertices):
                x_j, y_j = graph[j] # these are the x, y coordinates of the j'th vertex in the graph
                
                # calculate the distance between vertices
                dij = np.sqrt((x_i - x_j)**2. + (y_i - y_j)**2.)
                if dij <= 1.0:
                    edges[i,j] = True
                    edges[j,i] = True
                    
        return edges
        
    def energy(self):
        """Returns the energy of the current spin configuration"""
        # interaction term
        interaction_term = 0
        vertex_term = 0
        for i in range(self.num_vertices-1):
            for j in range(i+1, self.num_vertices):
                
                # check if there is an edge
                if self.edges[i,j]:
                    interaction_term += self.occupations[i]*self.occupations[j]
                
            vertex_term += self.occupations[i]
        
        # missed the last vertex
        vertex_term += self.occupations[self.num_vertices-1]
    
        return u*interaction_term - vertex_term

    def energy_diff(self, i):
        connections = np.where(self.edges[i,:])[0]
        num_adjacent_occupied = sum(self.occupations[connections])
        
        if self.occupations[i] == 1:
            # flipping an occupied vertex increases the vertex term, decreases the interaction term
            vertex_term_change = 1.
            interaction_term_change = -u*num_adjacent_occupied
        
        elif self.occupations[i] == 0:
            # flipping an unoccupied vertex decreases the vertex term, increases the interaction term
            vertex_term_change = -1.
            interaction_term_change = u*num_adjacent_occupied 

        return interaction_term_change + vertex_term_change
    
    def rand_vertex(self):
        """Selects a site in the graph at random"""
        return np.random.randint(self.num_vertices)       



def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


u = 1.35
graph = [(1.19, 4.25), (2.71, 3.48), (1.19, 3.51),  (2, 3.38), (1.12, 2.86), (1.70, 2.42), (2.36, 2.54), (1.52, 1.48), (2.15, 1.54), (2.14, 1.87),(1.72, 0.86), (2.29, 0.87)]

udmis = UDMIS(u, graph) 


N = 10000
i = np.arange(N)
T_i = 1000
T_f = 0.01


#Schedule 1
T1 = T_i * ((T_f/T_i) ** (i/N))
E1 = []
resultados = []
soluciones = []
for t in range(N):
    # take a look at the abstract_udmis.py file to see how mc_step works
    temp = T1[t]
    E = udmis.mc_step(T=temp)
    E1.append(E)
    ocupacion = list(udmis.occupations * 1)
    ocupacion.append(E)
    resultado = ocupacion.copy()
  
    if len(soluciones) ==0:
        soluciones.append(resultado)
    elif round(E, 5) == soluciones[-1][-1]: 
        soluciones.append(resultado)
    elif round(E, 5) < soluciones[-1][-1]: 
        soluciones = [resultado]
    #resultado = list(np.append([round(E, 5)], udmis.occupations * 1))
    #resultados.append(resultado)
    if t % 100 == 0:
        print(t,round(E, 5), udmis.occupations)
        


sol = np.array(get_unique_numbers(soluciones))
print(sol)
print('Cantidad de soluciones: ',  len(sol) )
   

        
        
                
