import matplotlib.pyplot as plt
import numpy as np


"""
General figure setup
"""


plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)
plt.rc('legend', fontsize=8)
plt.rc('figure', facecolor='white')


"""
Plotting tools
"""


def speckle_pattern(vector, ax=None):

    ax = ax if ax is not None else plt.gca()

    color = 'red'
    max_r = 0.45

    ax.set_aspect('equal', 'box')

    ax.set_facecolor('None')
    ax.set_frame_on(False)

    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    for (x, y), r in np.ndenumerate(vector):
        max_speckle = plt.Circle(
            (x, 0), max_r, facecolor='None', edgecolor=color, linewidth=0.5
        )
        ax.add_patch(max_speckle)

        speckle = plt.Circle(
            (x, 0), np.sqrt(r) * max_r, facecolor=color, edgecolor=color
        )
        ax.add_patch(speckle)

    ax.set_xlim([-0.55, len(vector)-1 + 0.55])
    ax.set_ylim([-0.55, 0.55])


def cumulative(samples, x):
    """
    Simple function for computing the cumulative distribution of a set of samples at
    values defined by x
    """
    counts = []
    for xi in x:
        counts.append((samples < xi).sum())
        samples = samples[samples >= xi]
    cdf = np.cumsum(counts)
    cdf = cdf / max(cdf)
    return cdf