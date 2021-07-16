import matplotlib.pyplot as plt
import numpy as np
import qutip as qt

"""
General figure setup
"""

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)
plt.rc('legend', fontsize=8)
plt.rc('figure', facecolor='white')


"""
Plotting functions
"""


def plot_classical_annealing(ax, steps, energy, temperature):
    """
    Plot the energy and temperature as a function of annealing steps.
    """
    # Energy as a function of steps (blue).
    ax.plot(steps, energy, c='tab:blue')
    ax.tick_params(axis='y', labelcolor='tab:blue', color='tab:blue')
    ax.set_xlabel('Steps')
    ax.set_ylabel(r'Energy', color='tab:blue')
    ax.set_yticks(np.linspace(-3, 0, 4))
    # On the same axis, temperature as a function of steps (red).
    ax = ax.twinx()
    ax.plot(steps, temperature, c='tab:red')
    ax.tick_params(axis='y', labelcolor='tab:red', color='tab:red')
    ax.set_yticks(np.linspace(0, 100, 3))
    ax.set_ylabel(r'Temperature', color='tab:red')
    # Recolor spines.
    ax.spines['left'].set_color('tab:blue')
    ax.spines['right'].set_color('tab:red')


def plot_classical_udmis(ax, udmis):
    """
    Plot the sites, connections and occupations for a given UD-MIS problem.
    """
    # Draw the edges.
    for i in range(udmis.num_vertices):
        xi, yi = udmis.graph[i]
        for j in range(i + 1, udmis.num_vertices):
            xj, yj = udmis.graph[j]
            if udmis.edges[i, j]:
                ax.plot([xi, xj], [yi, yj], 'k')
    # Draw the sites.
    for i, (x, y) in enumerate(udmis.graph):
        if udmis.state[i]:
            ax.plot(x, y, 'ko', mfc='k', ms=15)
        else:
            ax.plot(x, y, 'ko', mfc='w', ms=15)
    # Adjust plotting area.
    ax.set_xlim([0.05, 1.65])
    ax.set_ylim([0.4, 3.65])
    ax.set_xticks([0.5, 1.5])
    ax.set_yticks([0.5, 1.5, 2.5, 3.5])
    ax.set_aspect('equal', adjustable='box')


def plot_quantum_annealing(ax, steps, energy, omega, delta):
    """
    Plot the energy and temperature as a function of annealing steps.
    """
    # Energy as a function of steps (blue).
    ax.plot(steps, energy, c='tab:blue')
    ax.tick_params(axis='y', labelcolor='tab:blue', color='tab:blue')
    ax.set_xlabel('t')
    ax.set_ylabel(r'$\langle \psi (t) | \hat H (t=1) | \psi (t) \rangle$', color='tab:blue')
    ax.set_yticks(np.linspace(-3, 0, 4))
    # On the same axis, temperature as a function of steps (red).
    ax = ax.twinx()
    ax.plot(steps, omega, c='tab:red', label=r'$\Omega(t)$')
    ax.plot(steps, delta, c='tab:green', label=r'$\delta(t)$')
    ax.set_yticks(np.linspace(-1, 2, 4))
    ax.set_ylabel(r'$\Omega(t), \delta(t)$')
    ax.legend()
    # Recolor spines.
    ax.spines['left'].set_color('tab:blue')


def plot_quantum_udmis(ax, udmis):
    """
    Plot the sites, connections and occupations for a given UD-MIS problem.
    """
    # Draw the edges.
    for i in range(udmis.num_vertices):
        xi, yi = udmis.graph[i]
        for j in range(i + 1, udmis.num_vertices):
            xj, yj = udmis.graph[j]
            if udmis.edges[i, j]:
                ax.plot([xi, xj], [yi, yj], 'k')
    # Draw the sites.
    occupancies = qt.state_index_number(
        udmis.state.dims[0], udmis.state.full().argmax()
    )
    for i, (x, y) in enumerate(udmis.graph):
        if occupancies[i]:
            ax.plot(x, y, 'ko', mfc='k', ms=15)
        else:
            ax.plot(x, y, 'ko', mfc='w', ms=15)
    # Adjust plotting area.
    ax.set_xlim([0.05, 1.65])
    ax.set_ylim([0.4, 3.65])
    ax.set_xticks([0.5, 1.5])
    ax.set_yticks([0.5, 1.5, 2.5, 3.5])
    ax.set_aspect('equal', adjustable='box')
