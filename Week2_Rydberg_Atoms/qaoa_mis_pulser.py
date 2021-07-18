from typing import List, Tuple

import numpy as np
from pulser import Register, Sequence, Pulse, Simulation
from pulser.devices import Chadoq2
from scipy.optimize import minimize

from Week2_Rydberg_Atoms.utils import get_edges, normalize_coordinates

'''
def pos_to_graph(pos: List[Tuple[float, float]],
                 radius: float = 0.5) -> igraph.Graph:  # d is the rbr
    d = radius * 2
    g = igraph.Graph()
    edges = []
    for n in range(len(pos) - 1):
        for m in range(n + 1, len(pos)):
            pwd = ((pos[m][0] - pos[n][0]) ** 2 + (pos[m][1] - pos[n][1]) ** 2) ** 0.5
            if pwd < d:
                edges.append([n, m])  # Below rbr, vertices are connected
    g.add_vertices(len(pos))
    g.add_edges(edges)
    return g


'''


def normalize_coordinates_pulser(pos: List[Tuple[float, float]],
                                 radius: float):
    return normalize_coordinates(pos, radius / Chadoq2.rydberg_blockade_radius(1))


def quantum_loop(param: Tuple[float],
                 r: Register):
    seq = Sequence(r, Chadoq2)
    seq.declare_channel('ch0', 'rydberg_global')
    middle = int(len(param) / 2)
    param = np.array(param) * 1  # wrapper
    t = param[:middle]  # associated to H_c
    tau = param[middle:]  # associated to H_0
    p = len(t)
    for i in range(p):
        pulse_1 = Pulse.ConstantPulse(duration=tau[i],
                                      amplitude=1.,
                                      detuning=0,
                                      phase=0)  # H_M
        pulse_2 = Pulse.ConstantPulse(duration=t[i],
                                      amplitude=1.,
                                      detuning=1.,
                                      phase=0)  # H_M + H_c
        seq.add(pulse_1, 'ch0')
        seq.add(pulse_2, 'ch0')
    seq.measure('ground-rydberg')
    simul = Simulation(seq, sampling_rate=.001)
    results = simul.run()
    count_dict = results.sample_final_state(N_samples=10000)  # sample from the state vector
    return count_dict


def get_cost_colouring(ans: str,
                       edges: List[Tuple[int, int]],
                       penalty=10):
    cost = 0
    ans = np.array(tuple(ans), dtype=int)
    for i, j in edges:
        # if there's an edge between i,j and they are both in |1> state.
        cost += ans[i] * ans[j] * penalty
    cost -= np.sum(ans)  # to count for the 0s instead of the 1s
    return cost


def get_cost(counter, edges):
    cost = 0
    for key in counter.keys():
        cost_col = get_cost_colouring(key, edges)
        cost += cost_col * counter[key]
    return cost / sum(counter.values())


def qaoa_mis_pulser(pos: List[Tuple[float, float]],
                    radius: float,
                    num_params: int = 2
                    ):
    def func(param, *args):
        _edges = args[0]
        counter = quantum_loop(param, r=reg)
        cost = get_cost(counter, _edges)
        return cost

    norm_coord = normalize_coordinates_pulser(pos, radius)
    qubits = dict(enumerate(norm_coord))
    reg = Register(qubits)
    edges = get_edges(pos, radius)
    x0 = [1000 * (i + 1) if i < num_params // 2 else 10000 - 1000 * (num_params - i) for i in range(num_params)]
    res = minimize(func,
                   args=(edges,),
                   x0=np.array(x0),
                   method='Nelder-Mead',
                   tol=1e-5,
                   options={'maxiter': 30000})
    return res


if __name__ == "__main__":
    graph = [(0.3461717838632017, 1.4984640297338632),
             (0.6316400411846113, 2.5754677320579895),
             (1.3906262250927481, 2.164978861396621),
             (0.66436005100802, 0.6717919819739032),
             (0.8663329771713457, 3.3876341010035995),
             (1.1643107343501296, 1.0823066243402013)
             ]
    opt_res = qaoa_mis_pulser(pos=graph,
                              radius=0.5,
                              num_params=4)
    print(opt_res)
