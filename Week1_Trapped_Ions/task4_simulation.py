"""
    Generates RQC results with two qubit gate errors.
"""

import numpy as np
import pickle
from tqdm import tqdm

from Week1_Trapped_Ions.src.julia_run_random_circuit import run_random_circuit
from Week1_Trapped_Ions.src.utils import get_histogram_from_outcomes_large

if __name__ == "__main__":
    N = 15
    D = 1024
    shots = 5000
    log_file_name = "simulation_results/task4_simulation_result_large.txt"

    orig_result, r_params, m_params = run_random_circuit(N, D, shots,
                                                         ret_params=True)
    orig_hist = get_histogram_from_outcomes_large(orig_result)
    delta_thetas = np.arange(-np.pi / 20, np.pi / 20, np.pi / 1000)
    ret = dict()
    for dt in tqdm(delta_thetas):
        if abs(dt) < 1e-7:
            ret.update({0: orig_hist})
            continue
        shifted_m_params = [th + dt for th in m_params]
        shifted_result = run_random_circuit(N, D, shots,
                                            in_r_param=r_params,
                                            in_m_param=shifted_m_params)
        shifted_hist = get_histogram_from_outcomes_large(shifted_result)
        ret.update({dt: shifted_hist})
    with open(log_file_name, 'wb') as of:
        pickle.dump({
            'num_qubits': N,
            'depth': D,
            'num_shots': shots,
            'data': ret
        }, of)
