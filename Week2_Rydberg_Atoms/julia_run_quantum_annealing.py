import os
from typing import Tuple, List, Any, Union

import numpy as np

if not any([x in os.environ['PATH'] for x in ['julia', 'Julia']]):
    try:
        from envvir import JULIA_PATH

        os.environ['PATH'] = JULIA_PATH + ":" + os.environ['PATH']
    except (ImportError, ModuleNotFoundError):
        print("julia is not in PATH")
        raise FileNotFoundError

from julia import Julia

jl = Julia(compiled_modules=False)

jl.include("./run_quantum_annealing.jl")

ex_graph = jl.graph
ex_edges = jl.edges
ex_dt = jl.dt
_run_annealing = jl.run_annealing
_get_edges = jl.get_edges
_convert_edge = jl.convert_edge
# _hamiltonian = jl.hamiltonian
_measure = jl.measure


def run_annealing(graph: List[Tuple[float, float]],
                  edges: Union[List[List[bool]], np.ndarray],
                  dt: float) -> Any:
    return _run_annealing(graph, edges, dt)


def measure(state: Any,
            nshots: int) -> str:
    return _measure(state, nshots=nshots)


def get_edges(graph: List[Tuple[float, float]]) -> List[Any]:
    return _get_edges(graph)


def convert_edges(edges: List[Any]) -> List[Tuple[int, int]]:
    return [(_convert_edge(e)[0]-1, _convert_edge(e)[1]-1) for e in edges]


if __name__ == "__main__":
    psi = run_annealing(ex_graph, ex_edges, ex_dt)
    print(psi)
    for i, sample in enumerate(measure(psi, nshots=10000)):
        if i % 100 == 0:
            print(sample, type(sample))
    print(ex_edges)
    print(convert_edges(ex_edges))
