import os
from typing import Tuple, List, Optional, Any

from julia import Julia

if not any([x in os.environ['PATH'] for x in ['julia', 'Julia']]):
    try:
        from ..envvir import JULIA_PATH
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
        -> Any:
    """
    Julia-Python interface for run_random_circuit function.

    :param num_qubits:
    :param depth:
    :param num_shots:
    :param rand_x: If true, an x gate is introduced to random position in the circuit.
    :param ret_params: If true, returns the parameters for each gates.
    :param ret_x_pos: If true, returns the random position and idx of qubit which random x gate is inserted.
    :param in_r_param: If not None, the circuit doesn't generate random parameters, instead, use this as parameters for r gates.
    :param in_m_param: If not None, the circuit doesn't generate random parameters, instead, use this as parameters for m gates.
    :return:
        result : A list of lists of int containing the sampling.
        (optional)
        r_params, m_params, pos_x, qubit_x
    """
    return _run_random_circuit(num_qubits, depth, num_shots, rand_x, ret_params, ret_x_pos, in_r_param, in_m_param)
