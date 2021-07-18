import os
from collections import Counter
from typing import Tuple, List, Any, Union

import numpy as np
from scipy.optimize import minimize

from Week2_Rydberg_Atoms.draw_graph import draw_graph
from Week2_Rydberg_Atoms.utils import int_to_bin, sanity_check

if not any([x in os.environ['PATH'] for x in ['julia', 'Julia']]):
    try:
        from envvir import JULIA_PATH

        os.environ['PATH'] = JULIA_PATH + ":" + os.environ['PATH']
    except (ImportError, ModuleNotFoundError):
        print("julia is not in PATH")
        raise FileNotFoundError

from julia import Julia

jl = Julia(compiled_modules=False)

jl.include("./run_qaoa.jl")
_run_qaoa_circuit = jl.run_qaoa_circuit
_measure = jl.measure
_get_edges = jl.get_edges
_convert_edge = jl.convert_edge


def run_qaoa_circuit(num_vertices: int,
                     edges: Union[List[List[bool]], np.ndarray],
                     durations: List[float],
                     dt: float) -> Any:
    return _run_qaoa_circuit(num_vertices, edges, durations, dt)


def measure(state: Any,
            nshots: int) -> str:
    return _measure(state, nshots=nshots)


def get_edges(graph: List[Tuple[float, float]]) -> List[Any]:
    return _get_edges(graph)


def convert_edges(edges: List[Any]) -> List[Tuple[int, int]]:
    return [(_convert_edge(e)[0] - 1, _convert_edge(e)[1] - 1) for e in edges]


if __name__ == "__main__":
    def func(param, *args):
        nshots = 10000
        num_vertices = 6
        panelty = 2
        _graph = args[0]
        _edges = args[1]
        psi = run_qaoa_circuit(num_vertices=num_vertices, edges=_edges, durations=param, dt=0.0001)
        samples = [s for s in measure(psi, nshots=nshots)]
        occurrence = Counter(samples)
        cost = 0
        for k in occurrence:
            violated, num_sel = sanity_check(coordinates=_graph,
                                             answer=int_to_bin(k, num_vertices),
                                             edges=convert_edges(_edges))
            cost += (violated * panelty - num_sel) * occurrence[k] / nshots
        return cost


    graph = [(0.3461717838632017, 1.4984640297338632),
             (0.6316400411846113, 2.5754677320579895),
             (1.3906262250927481, 2.164978861396621),
             (0.66436005100802, 0.6717919819739032),
             (0.8663329771713457, 3.3876341010035995),
             (1.1643107343501296, 1.0823066243402013)
             ]
    num_params = 6
    x0 = [1 for _ in range(num_params)]
    edges = get_edges(graph)
    '''
    opt_res = minimize(func,
                       args=(graph, edges),
                       x0=np.array(x0),
                       method='Nelder-Mead',
                       tol=1e-5,
                       options={'maxiter': None})
    '''
    opt_res = minimize(func,
                       args=(graph, edges),
                       x0=np.array(x0),
                       method="Powell",
                       tol=1e-5)
    opt_param = opt_res.x
    opt_psi = run_qaoa_circuit(num_vertices=6, edges=edges, durations=opt_param, dt=0.0001)
    samples = [s for s in measure(opt_psi, nshots=10000)]
    occurrence = Counter(samples)
    max_occ = sorted([k for k in occurrence], key=lambda k: occurrence[k], reverse=True)
    print(occurrence)
    print(max_occ)
    print(opt_res)
    draw_graph(graph, radius=0.5, answer=int_to_bin(max_occ[0], len(graph)))