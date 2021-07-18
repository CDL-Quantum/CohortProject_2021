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
    t_list = [0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]

    pkl_file = "task3_verbose_2.txt"
    pkl_data = dict()
    for t in tqdm(t_list):
        dt = t / 1000
        psi = run_annealing(graph, edges, dt, t)
        samples = [s for s in measure(psi, nshots=10000)]
        occurrence = Counter(samples)
        pkl_data.update({
            t: occurrence
        })

    with open(pkl_file, 'wb') as of:
        pickle.dump(pkl_data, of)
