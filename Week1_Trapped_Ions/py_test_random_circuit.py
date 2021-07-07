import cirq
import numpy as np
from matplotlib import pyplot as plt


class r_gate(cirq.Gate):
    """Rotation gate."""
    def __init__(self, theta, phi):
        super(r_gate, self)
        self.theta = theta
        self.phi = phi

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        return np.array([
            [np.cos(self.theta / 2), -1j * np.exp(-1j * self.phi) * np.sin(self.theta / 2)],
            [-1j * np.exp(1j * self.phi) * np.sin(self.theta / 2), -np.cos(self.theta / 2)]
        ])

    def _circuit_diagram_info_(self, args):
        return f"R({self.theta},{self.phi})"


class m_gate(cirq.TwoQubitGate):
    """M gate"""
    def __init__(self, theta):
        super(m_gate, self)
        self.theta = theta

    def _unitary_(self):
        return np.array([
            [1.0 * np.cos(self.theta), 0.0, 0.0, -1j * np.sin(self.theta)],
            [0.0, 1.0 * np.cos(self.theta), -1j * np.sin(self.theta), 0.0],
            [0.0, -1j * np.sin(self.theta), 1.0 * np.cos(self.theta), 0.0],
            [-1j * np.sin(self.theta), 0.0, 0.0, 1.0 * np.cos(self.theta)]])

    def _circuit_diagram_info_(self, args):
        return f"M_rot({self.theta})", f"M_rot({self.theta})"


def run(N, depth):
    qreg = [cirq.LineQubit(i) for i in range(N)]
    circuit = cirq.Circuit()

    for i in range(depth):
        for j in range(N):
            # random single-bit gate
            theta = 2 * np.pi * np.random.rand()
            phi = 2 * np.pi * np.random.rand()
            R_gate = r_gate(theta=theta, phi=phi)
            # circuit.append(cirq.XPowGate(exponent=theta, global_shift=phi)(qreg[x]))
            circuit.append(R_gate(qreg[j]))

        # Alternate start qubit for pairs.
        idx_first = i % 2

        for j in np.arange(idx_first, N - 1, 2):
            M_gate = m_gate(theta=2 * np.pi * np.random.rand())
            circuit.append(M_gate(qreg[j], qreg[j + 1]))

    circuit.append([cirq.measure(qreg[i]) for i in range(N)])

    # print('Circuit:')
    # print(circuit)

    sim = cirq.Simulator()

    result = sim.run(circuit, repetitions=100)

    # print('Results:')
    # print(result)
    return qreg, circuit, result


if __name__ == "__main__":
    # basic run of the random circuit
    np.random.seed(123)
    N = 4
    depth = 3

    qreg, circuit, result = run(N, depth)
    _ = cirq.vis.plot_state_histogram(result)

    # Add sigma_x randomly and run of the random circuit
    n_sims = 8
    n_pl = int(np.ceil(np.sqrt(n_sims)))
    fig, ax = plt.subplots(n_pl, n_pl)

    for x in range(n_sims):
        i = x % n_pl
        j = int(np.floor(x / n_pl))

        circuit.insert(np.random.randint(0, len(circuit)),
                       cirq.X(qreg[np.random.randint(0, N)]))

        sim = cirq.Simulator()
        result = sim.run(circuit, repetitions=100)

        # result = run(N, depth, sigma_x=True)
        _ = cirq.vis.plot_state_histogram(result, ax[i,j])

    # Test different depths
    N = 8
    depths = [2**n for n in range(8)]
    n_sims = len(depths)
    n_pl = int(np.ceil(np.sqrt(n_sims)))
    fig2, ax2 = plt.subplots(n_pl, n_pl)

    for x in range(n_sims):
        np.random.seed(123)
        i = x % n_pl
        j = int(np.floor(x / n_pl))

        qreg, circuit, result = run(N, depths[x])
        # _ = cirq.vis.plot_state_histogram(result, ax2[i, j], title=f"depth={depths[x]}")
