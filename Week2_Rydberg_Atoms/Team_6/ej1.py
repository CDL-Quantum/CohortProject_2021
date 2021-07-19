import numpy as np
import matplotlib.pyplot as plt

from abstract_udmis import AbstractUDMIS

%matplotlib inline


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

u = 1.35
graph = [(0.3461717838632017, 1.4984640297338632), 
         (0.6316400411846113, 2.5754677320579895), 
         (1.3906262250927481, 2.164978861396621), 
         (0.66436005100802, 0.6717919819739032), 
         (0.8663329771713457, 3.3876341010035995), 
         (1.1643107343501296, 1.0823066243402013)
        ]

udmis = UDMIS(u, graph) 


N = 5000
i = np.arange(N)
T_i = 100
T_f = 0.01


#Schedule 1
T1 = T_i * ((T_f/T_i) ** (i/N))
E1 = []
for t in range(N):
    # take a look at the abstract_udmis.py file to see how mc_step works
    temp = T1[t]
    E = udmis.mc_step(T=temp)
    E1.append(E)
    if t % 100 == 0:
        print(t, E, udmis.occupations)
        


             
        
#schedule2 exponential :    
a = 1
T2 = T_i * np.exp(-a *i)
  
E2 = []
for t in range(N):
     # take a look at the abstract_udmis.py file to see how mc_step works
     temp = T2[t]
     E = udmis.mc_step(T=temp)
     E2.append(E)
     if t % 100 == 0:
         print(t, E, udmis.occupations)        
        
      
        
#Schedule 3: 
T3 = T_i  / np.log (1 + i )  
E3 = []
for t in range(N):
     # take a look at the abstract_udmis.py file to see how mc_step works
     temp = T3[t]
     E = udmis.mc_step(T=temp)
     E3.append(E)
     if t % 100 == 0:
         print(t, E, udmis.occupations)     
      
      
     
fig, ax = plt.subplots()
ax.plot(i, T1,   label='Schedule 1')
ax.plot(i, T2,  label='Schedule 2')
ax.plot(i, T3,  label='Schedule 3')
ax.set(xlabel='Step', ylabel='Temperature',
       title='Temperature schedule')
ax.grid()
ax.legend()
fig.savefig("temperature.png")
plt.show()    
            

E1= np.array(E1)  
E2 = np.array(E2)
E3 = np.array(E3)    
valores = list (range(0,N, 100))

fig, ax = plt.subplots()
ax.plot(i[valores], E1[valores],  label='Schedule 1')
ax.plot(i[valores], E2[valores], label='Schedule 2')
ax.plot(i[valores], E3[valores], label='Schedule 3')
ax.set(xlabel='Step', ylabel='Energy',
       title='Temperature schedule')

ax.grid()
ax.legend()
fig.savefig("energy.png")
plt.show()    
              
        
        
                
