from itertools import product
from typing import List, Tuple, Optional
import numpy as np


def int_to_bin(x: int, num_digit: int) -> List[bool]:
    return [bool(x >> i & 1) for i in range(num_digit)]


def get_edges(coordinates: List[Tuple[float, float]],
              radius: float) -> List[Tuple[int, int]]:
    edges = list()
    for (i, (x1, y1)), (j, (x2, y2)) in product(enumerate(coordinates), repeat=2):
        if i >= j:
            continue
        dist = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if dist <= 2 * radius:
            edges.append((i, j))
    return edges


def sanity_check(coordinates: List[Tuple[float, float]],
                 answer: List[bool],
                 radius: Optional[float] = None,
                 edges: Optional[List[Tuple[int, int]]] = None) -> Tuple[bool, int]:
    if len(answer) != len(coordinates):
        print("The length of answer should be equal to the number of vertices.")
        raise ValueError
    if (radius is None) == (edges is None):
        print("Only one of arguments between radius and edges should be given.")
        raise ValueError
    if radius is not None:
        edges = get_edges(coordinates, radius)
    selected = np.argwhere(answer).flatten()
    check = not any([i in selected and j in selected for i, j in edges])
    return check, len(selected)
