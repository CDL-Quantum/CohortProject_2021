import os
import pickle
import re
import numpy as np

from tqdm import tqdm

if __name__ == "__main__":
    root_dataset_path = './dataset/'
    dir_pattern = r'n(\d+)_m(\d+)'
    meas_file_pattern = r'measurements_n(\d+)_m(\d+)_s(\d+)_e(\d+)_p((EFGH)|(ABCDCDAB)).txt'
    worklist = list()
    for dir_name in os.listdir(root_dataset_path):
        mat1 = re.match(dir_pattern, dir_name)
        if mat1 is None:
            continue
        n, m = int(mat1.group(1)), int(mat1.group(2))
        for file_name in os.listdir(root_dataset_path + dir_name):
            mat2 = re.match(meas_file_pattern, file_name)
            if mat2 is None:
                continue
            assert n == int(mat2.group(1)) and m == int(mat2.group(2))
            s, e, p = int(mat2.group(3)), int(mat2.group(4)), mat2.group(5)
            worklist.append({
                "path": os.path.join(root_dataset_path + dir_name, file_name),
                "n": n,
                "m": m,
                "s": s,
                "e": e,
                "p": p
            })

    print(f"Screening Done. {len(worklist)} found.")

    if not os.path.isdir(root_dataset_path + "histograms/"):
        os.mkdir(root_dataset_path + "histograms/")

    for i in tqdm(range(len(worklist))):
        job = worklist[i]
        n, m, s, e, p = job['n'], job['m'], job['s'], job['e'], job['p']
        logfile_path = os.path.join(root_dataset_path + "histograms/", f"n{n}_m{m}_s{s}_e{e}_p{p}.txt")
        if os.path.isfile(logfile_path):
            print(f"{logfile_path} exists. skipping it.")
            continue
        with open(job['path'], 'r') as of:
            hist = dict()
            while True:
                bin_str = of.readline()
                bin_str = bin_str.replace('\n', '')
                if len(bin_str) < 1:
                    break
                if len(bin_str) != job['n']:
                    raise ValueError
                v = np.uint64(0)
                for j, b in enumerate(bin_str):
                    v += 2 ** j if b == "1" else 0
                if v not in hist:
                    hist.update({v: 1})
                else:
                    hist[v] += 1
        with open(logfile_path, 'wb') as of:
            pickle.dump({"hist": hist, **job}, of)
