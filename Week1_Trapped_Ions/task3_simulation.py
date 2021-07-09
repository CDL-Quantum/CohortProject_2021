import pickle
from itertools import product

from tqdm import tqdm

from Week1_Trapped_Ions.julia_run_random_circuit import run_random_circuit
from Week1_Trapped_Ions.utils import get_histogram_from_outcomes_small

if __name__ == "__main__":
    N = 8
    MAX_D = 512
    STEP_D = 256
    depths = [1, 2, 10, 30, 512]
    shots = 10000
    num_trials = 1000

    hist_list = {D: list() for D in depths}
    for D, _ in tqdm(list(product(depths, range(num_trials)))):
        result = run_random_circuit(N, D, shots)
        hist_list[D].append(list(get_histogram_from_outcomes_small(result)))

    with open("task3_simulation_result_more_d.txt", 'wb') as of:
        pickle.dump({
            'num_qubits': N,
            'num_shots': shots,
            'data': hist_list
        }, of)
