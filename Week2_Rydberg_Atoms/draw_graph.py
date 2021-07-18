from typing import Tuple, List, Optional, TypedDict, Dict, Union

import matplotlib.pyplot as plt

from Week2_Rydberg_Atoms.utils import get_edges


class TextArgs(TypedDict):
    x: float
    y: float
    s: str
    zorder: int


def _get_drawing_objects(coordinates: List[Tuple[float, float]],
                         radius: float,
                         edges: Optional[List[Tuple[int, int]]] = None,
                         texts: Optional[List[str]] = None,
                         answer: Optional[List[bool]] = None) \
        -> Tuple[List[plt.Circle], List[plt.Circle], List[plt.Line2D], List[TextArgs]]:
    # Draw Points
    point_to_radius_ratio = 0.1
    txt_offset = 0.10 * radius
    points = list()
    texts_drawing = list()
    for i, (x, y) in enumerate(coordinates):
        points.append(plt.Circle((x, y),
                                 radius=radius * point_to_radius_ratio,
                                 color='r' if answer is not None and answer[i] else 'k',
                                 zorder=2))
        t = str(i) if texts is None else texts[i]
        texts_drawing.append({"x": x + txt_offset, "y": y + txt_offset, "s": t, "zorder": 3})

    # Draw Circles
    circles = list()
    for x, y in coordinates:
        circles.append(plt.Circle((x, y), radius=radius, alpha=0.3, color='grey',
                                  zorder=0))

    # Draw Edges
    edges_drawing = list()
    for i, j in edges:
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        edges_drawing.append(plt.Line2D((x1, x2), (y1, y2),
                                        zorder=1))

    return points, circles, edges_drawing, texts_drawing


def draw_graph(coordinates: List[Tuple[float, float]],
               radius: float,
               texts: Optional[List[str]] = None,
               answer: Optional[List[bool]] = None) -> None:
    if answer is not None and len(answer) != len(coordinates):
        print("The length of answer should be equal to the number of vertices. Or, it should be None.")
        raise ValueError

    # Get edges
    edges = get_edges(coordinates, radius)

    # Determine size
    xs = [c[0] for c in coordinates]
    ys = [c[1] for c in coordinates]
    margin = radius * 1.05
    # figsize = ((max(xs) - min(xs) + 2 * margin) * 2, (max(ys) - min(ys) + 2 * margin) * 2)
    fig, axe = plt.subplots()
    plt.xlim([min(xs) - margin, max(xs) + margin])
    plt.ylim([min(ys) - margin, max(ys) + margin])

    # Get drawing objects
    points, circles, edges_drawing, texts_drawing = _get_drawing_objects(coordinates, radius, edges, texts, answer)

    # Render
    _ = [axe.add_patch(c) for c in circles]
    _ = [axe.add_line(e) for e in edges_drawing]
    _ = [axe.add_patch(p) for p in points]
    _ = [axe.text(**t) for t in texts_drawing]

    plt.axis('scaled')
    plt.show()


def draw_multi_graph(coordinates: List[Tuple[float, float]],
                     radius: float,
                     texts: Optional[List[str]] = None,
                     answer_list: Optional[List[List[bool]]] = None,
                     titles: Optional[List[str]] = None
                     ) -> None:
    if answer_list is not None and any([len(a) != len(coordinates) for a in answer_list]):
        print("The length of answer should be equal to the number of vertices. Or, it should be None.")
        raise ValueError

    # Get edges
    edges = get_edges(coordinates, radius)

    # Determine size per plots
    xs = [c[0] for c in coordinates]
    ys = [c[1] for c in coordinates]
    margin = radius * 1.05

    # Design plot placement
    num_plots = len(answer_list) if answer_list is not None else 1
    num_col = 2 if num_plots >= 2 else 1
    num_row = (num_plots + 1) // 2 if num_plots >= 2 else 1
    figsize = ((max(xs) - min(xs) + 2 * margin) * 2 * num_col, (max(ys) - min(ys) + 2 * margin) * 2 * num_row)

    fig, axes = plt.subplots(num_row, num_col, figsize=figsize)
    axes = axes.flatten()
    # Get drawing objects
    for i, ax in enumerate(axes):
        if i >= num_plots:
            ax.axis('off')
            continue
        ax.set_xlim([min(xs) - margin, max(xs) + margin])
        ax.set_ylim([min(ys) - margin, max(ys) + margin])

        points, circles, edges_drawing, texts_drawing = \
            _get_drawing_objects(coordinates, radius, edges, texts, answer_list[i] if answer_list is not None else None)

        # Render
        _ = [ax.add_patch(c) for c in circles]
        _ = [ax.add_line(e) for e in edges_drawing]
        _ = [ax.add_patch(p) for p in points]
        _ = [ax.text(**t) for t in texts_drawing]
        if titles is not None:
            ax.title.set_text(titles[i])
            ax.title.set_fontsize(24)

    plt.show()


def draw_distributions(dist: List[Tuple[str, Union[float, int]]],
                       check_list: List[bool]):
    color_list = ['r' if check_list[i] else 'k' for i, (key, _) in enumerate(dist)]
    plt.figure(figsize=(12, 6))
    plt.xlabel("bitstrings")
    plt.ylabel("counts")
    plt.bar([d[0] for d in dist], [d[1] for d in dist], width=0.5, color=color_list)
    plt.xticks(rotation='vertical')
    plt.show()


if __name__ == "__main__":
    graph = [(0.3461717838632017, 1.4984640297338632),
             (0.6316400411846113, 2.5754677320579895),
             (1.3906262250927481, 2.164978861396621),
             (0.66436005100802, 0.6717919819739032),
             (0.8663329771713457, 3.3876341010035995),
             (1.1643107343501296, 1.0823066243402013)
             ]
    ex_answer_list = [[False, False, False, False, False, True],
                      [False, False, False, False, True, False],
                      [False, False, False, False, True, True],
                      [False, True, False, False, False, True],
                      [True, True, False, False, True, True]]
    ex_texts = ["a", "b", "c", "d", "e", "f"]
    titles = ["Q", "W", "E", "R", "T", "Y"]
    draw_graph(coordinates=graph,
               radius=0.5,
               answer=ex_answer_list[0])
    draw_graph(coordinates=graph,
               radius=0.5,
               texts=ex_texts,
               answer=ex_answer_list[1])
    draw_multi_graph(coordinates=graph,
                     radius=0.5,
                     texts=ex_texts,
                     answer_list=ex_answer_list,
                     titles=titles)
