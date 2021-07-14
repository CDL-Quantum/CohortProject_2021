from itertools import product
from typing import Tuple, List, Optional

import matplotlib.pyplot as plt
import numpy as np


class DrawGraph(object):
    def __init__(self,
                 coordinates: List[Tuple[float, float]],
                 radius: float):
        self.coordinates = coordinates
        self.radius = radius
        self.num_vertices = len(coordinates)

    def draw(self,
             answer: Optional[List[bool]] = None):
        xs = [c[0] for c in self.coordinates]
        ys = [c[1] for c in self.coordinates]
        margin = self.radius * 1.05
        fig, axe = plt.subplots(figsize=(max(xs)-min(xs) + 2 * margin, max(ys)-min(ys) + 2 * margin))

        # Draw Points
        point_to_radius_ratio = 0.1
        points = list()
        for i, (x, y) in enumerate(self.coordinates):
            points.append(plt.Circle((x, y),
                                     radius=self.radius * point_to_radius_ratio,
                                     color='r' if answer is not None and answer[i] else 'k'))

        # Draw Circles
        circles = list()
        for x, y in self.coordinates:
            circles.append(plt.Circle((x, y), radius=self.radius, alpha=0.3, color='grey'))

        # Draw Edges
        edges = list()
        for (i, (x1, y1)), (j, (x2, y2)) in product(enumerate(self.coordinates), repeat=2):
            if i == j:
                continue
            dist = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if dist <= 2 * self.radius:
                edges.append(plt.Line2D((x1, x2), (y1, y2)))

        # Render
        _ = [axe.add_patch(c) for c in circles]
        _ = [axe.add_line(e) for e in edges]
        _ = [axe.add_patch(p) for p in points]

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
    g = DrawGraph(graph, 1.0)
    g.draw()
