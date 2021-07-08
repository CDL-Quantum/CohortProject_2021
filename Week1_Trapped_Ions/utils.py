from typing import List, Any

import matplotlib.pyplot as plt

import numpy as np
import os


def bin_to_int(bin_l: list) -> int:
    l = len(bin_l)
    ret = 0
    for i, v in enumerate(bin_l):
        ret += 2 ** (l - i - 1) if v else 0
    return ret


def get_histogram_from_outcomes(result: List[List[int]]) -> np.ndarray:
    shots = len(result)
    n_qubits = len(result[0])
    histogram_list = np.zeros(2 ** n_qubits)
    for r in result:
        histogram_list[bin_to_int(r)] += 1 / shots
    return histogram_list


def get_xeb_from_outcomes(result: List[List[int]]) -> float:
    shots = len(result)
    n_qubits = len(result[0])
    hist = get_histogram_from_outcomes(result)
    ret = 0
    for r in result:
        i = bin_to_int(r)
        ret += hist[i]
    return ((2**n_qubits) * ret / shots) - 1


def draw_circles(histogram_list: List[float], fig=None, ax=None, **kwargs) -> Any:
    if fig is None or ax is None:
        fig, ax = plt.subplots()
        ax.set(xlim=(0, 2 * len(histogram_list)), ylim=(-1, 1))
        fig.set_size_inches(2 * len(histogram_list), 2)
    for x in range(len(histogram_list)):
        c = plt.Circle((2 * x + 1, 0), np.sqrt(histogram_list[x]), **kwargs)
        ax.add_artist(c)
    return fig, ax


def hamming_distance(x: List, y: List) -> Any:
    if len(x) != len(y):
        raise ValueError
    return sum([abs(x[i] - y[i]) for i in range(len(x))])



