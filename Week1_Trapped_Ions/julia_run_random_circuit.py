import os
from typing import Tuple, List, Optional, Union

from julia import Julia

if not any([x in os.environ['PATH'] for x in ['julia', 'Julia']]):
    try:
        print(os.environ['PATH'])
        from envvir import JULIA_PATH

        os.environ['PATH'] = JULIA_PATH + ":" + os.environ['PATH']
    except (ImportError, ModuleNotFoundError):
        print("julia is not in PATH")
        raise FileNotFoundError

jl = Julia(compiled_modules=False)
_run_random_circuit = jl.include("./run_random_circuit.jl")


def run_random_circuit(num_qubits: int,
                       depth: int,
                       num_shots: int = 0,
                       rand_x: bool = False,
                       ret_params: bool = False,
                       ret_x_pos: bool = False,
                       in_r_param: Optional[List[Tuple[float]]] = None,
                       in_m_param: Optional[List[float]] = None) \
        -> Union[List[List[int]], Tuple[List[List[int]], List[Tuple[float]], List[float]]]:
    return _run_random_circuit(num_qubits, depth, num_shots, rand_x, ret_params, ret_x_pos, in_r_param, in_m_param)
