import pickle
from collections import Counter

from tqdm import tqdm

from Week2_Rydberg_Atoms.julia_run_quantum_annealing import run_annealing, get_edges, measure

if __name__ == "__main__":
    graph = [
        (1.19, 4.25),
        (2.71, 3.48),
        (1.19, 3.51),
        (2.00, 3.38),
        (1.12, 2.86),
        (1.70, 2.42),
        (2.36, 2.54),
        (1.52, 1.48),
        (2.15, 1.54),
        (2.14, 1.87),
        (1.72, 0.86),
        (2.29, 0.87),
    ]
    edges = get_edges(graph)
    dt_list = [0.1, 0.025, 0.01, 0.0025, 0.001, 0.00025, 0.0001]

    pkl_file = "./simulations/task3_verbose.txt"
    pkl_data = dict()
    for dt in tqdm(dt_list):
        psi = run_annealing(graph, edges, dt)
        samples = [s for s in measure(psi, nshots=10000)]
        occurrence = Counter(samples)
        pkl_data.update({
            dt: occurrence
        })

    with open(pkl_file, 'wb') as of:
        pickle.dump(pkl_data, of)
