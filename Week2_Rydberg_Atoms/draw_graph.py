from itertools import product
from typing import Tuple, List, Optional

import matplotlib.pyplot as plt
import numpy as np


def draw_graph(coordinates: List[Tuple[float, float]],
               radius: float,
               answer: Optional[List[bool]] = None):
    if answer is not None and len(answer) != len(coordinates):
        raise ValueError

    xs = [c[0] for c in coordinates]
    ys = [c[1] for c in coordinates]
    margin = radius * 1.05
    fig, axe = plt.subplots(figsize=(max(xs) - min(xs) + 2 * margin, max(ys) - min(ys) + 2 * margin))

    # Draw Points
    point_to_radius_ratio = 0.1
    txt_offset = 0.05 * radius
    points = list()
    texts = list()
    for i, (x, y) in enumerate(coordinates):
        points.append(plt.Circle((x, y),
                                 radius=radius * point_to_radius_ratio,
                                 color='r' if answer is not None and answer[i] else 'k',
                                 zorder=2))
        texts.append({"x": x+txt_offset, "y": y+txt_offset, "s": str(i), "zorder": 3})

    # Draw Circles
    circles = list()
    for x, y in coordinates:
        circles.append(plt.Circle((x, y), radius=radius, alpha=0.3, color='grey',
                                  zorder=0))

    # Draw Edges
    edges = list()
    for (i, (x1, y1)), (j, (x2, y2)) in product(enumerate(coordinates), repeat=2):
        if i == j:
            continue
        dist = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if dist <= 2 * radius:
            edges.append(plt.Line2D((x1, x2), (y1, y2),
                                    zorder=1))

    # Render
    _ = [axe.add_patch(c) for c in circles]
    _ = [axe.add_line(e) for e in edges]
    _ = [axe.add_patch(p) for p in points]
    _ = [axe.text(**t) for t in texts]

    plt.xlim([min(xs) - margin, max(xs) + margin])
    plt.ylim([min(ys) - margin, max(ys) + margin])
    plt.show()


if __name__ == "__main__":
    graph = [(0.3461717838632017, 1.4984640297338632),
             (0.6316400411846113, 2.5754677320579895),
             (1.3906262250927481, 2.164978861396621),
             (0.66436005100802, 0.6717919819739032),
             (0.8663329771713457, 3.3876341010035995),
             (1.1643107343501296, 1.0823066243402013)
             ]
    g = draw_graph(coordinates=graph,
                   radius=0.5,
                   answer=[True, True, False, False, True, True])
