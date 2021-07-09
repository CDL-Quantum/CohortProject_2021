from typing import List, Any, Union

import matplotlib.pyplot as plt

import numpy as np
import os


def bin_to_int(bin_l: list) -> int:
    l = len(bin_l)
    ret = 0
    for i, v in enumerate(bin_l):
        ret += 2 ** (l - i - 1) if v else 0
    return ret


def get_histogram_from_outcomes_small(result: List[List[int]]) -> np.ndarray:
    shots = len(result)
    n_qubits = len(result[0])
    histogram_list = np.zeros(2 ** n_qubits)
    for r in result:
        histogram_list[bin_to_int(r)] += 1 / shots
    return histogram_list


def get_histogram_from_outcomes_large(result: List[List[int]]) -> dict:
    shots = len(result)
    n_qubits = len(result[0])
    histogram_list = dict()
    for r in result:
        b = bin_to_int(r)
        if b not in histogram_list:
            histogram_list.update({b: 0.0})
        histogram_list[b] += 1 / shots
    return histogram_list


def get_xeb_from_hist_small(obsvd_hist: Union[List[float], np.ndarray],
                            ideal_hist: Union[List[float], np.ndarray]) -> float:
    if len(obsvd_hist) != len(ideal_hist):
        raise ValueError
    ret = 0
    for p_o, p_i in zip(obsvd_hist, ideal_hist):
        ret += p_o * p_i
    return len(obsvd_hist) * ret - 1


def get_xeb_from_hist_large(obsvd_hist: dict,
                            ideal_hist: dict,
                            num_qubits: int) -> float:
    ret = 0
    if not isinstance(obsvd_hist, dict):
        raise TypeError
    if not isinstance(ideal_hist, dict):
        raise TypeError
    for o_key in obsvd_hist:
        if o_key in ideal_hist:
            ret += ideal_hist[o_key] * obsvd_hist[o_key]
    return (2 ** num_qubits) * ret - 1


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
