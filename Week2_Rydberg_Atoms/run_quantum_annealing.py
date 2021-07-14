import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

# d'wave pkgs
import dimod
import dwave_networkx as dnx
from dwave_qbsolv import QBSolv

# pkgs to run the code on the QPU
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite


def get_edges(graph):
    Nv = len(graph)
    edges = np.zeros((Nv, Nv))
    for i in range(Nv - 1):
        xi, yi = graph[i]
        for j in range(i + 1, Nv):
            xj, yj = graph[j]
            dij = np.sqrt((xi - xj) ** 2. + (yi - yj) ** 2.)
            if dij <= 1.0:
                edges[i, j] = 1
    return np.argwhere(edges == 1)


if __name__ == "__main__":
    # Define the graph
    graph = [(0.3461717838632017, 1.4984640297338632),
             (0.6316400411846113, 2.5754677320579895),
             (1.3906262250927481, 2.164978861396621),
             (0.66436005100802, 0.6717919819739032),
             (0.8663329771713457, 3.3876341010035995),
             (1.1643107343501296, 1.0823066243402013)
             ]
    edges = get_edges(graph)

    # choose whether to use:
    # 1. the simulated annealing sampler
    # sampler = dimod.SimulatedAnnealingSampler()  # Simulated annealing

    # 2. the quantum simulator
    sampler = QBSolv()

    # 3. running on the actual D-Wave QPU
    # sampler = EmbeddingComposite(DWaveSampler())

    G = nx.Graph()
    for edge in edges:
        G.add_edge(edge[0], edge[1])

    indep_nodes = dnx.maximum_independent_set(G, sampler)

    print(f'Independent nodes: {indep_nodes}')

    # plot MIS nodes with different color
    pos = nx.circular_layout(G)  # positions for all nodes

    # nodes from MIS
    nx.draw_networkx_nodes(G, pos, nodelist=indep_nodes, node_size=700, node_color='red')
    nx.draw_networkx_nodes(G, pos, nodelist=[n for n in list(G.nodes) if n not in indep_nodes], node_size=700)
    # edges
    nx.draw_networkx_edges(G, pos)
    # labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
    plt.axis("off")
    plt.show()
