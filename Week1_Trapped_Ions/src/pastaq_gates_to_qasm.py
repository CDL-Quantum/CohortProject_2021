from qiskit import QuantumRegister, QuantumCircuit

import numpy as np
from numpy import pi


def _R_gate(theta, phi, idx):
    return f"u3({theta}, {phi - np.pi / 2}, {-phi + np.pi / 2}) q[{idx}];\n"


def _M_gate(theta, idx1, idx2):
    return '\n'.join([f"u3({pi * 0.5},0,{pi}) q[{idx1}];",
                      f"u3({pi * 0.5},0,{pi}) q[{idx2}];",
                      f"cx q[{idx1}],q[{idx2}];",
                      f"u3(0,0,{theta}) q[{idx2}];",
                      f"cx q[{idx1}],q[{idx2}];",
                      f"u3({pi * 0.5},0,{pi}) q[{idx1}];",
                      f"u3({pi * 0.5},0,{pi}) q[{idx2}];"
                      ]) + '\n'


def _X_gate(idx):
    return f"x q[{idx}];\n"


def pastaq_gates_to_qasm(input_arr, num_qubits):
    qasm_txt = f'OPENQASM 2.0;\ninclude "qelib1.inc";\nqreg q[{num_qubits}];\n'
    for gate_layer in input_arr:
        for gate in gate_layer:
            if len(gate) == 3:
                gate_name, qubit_idx, params = gate
            elif len(gate) == 2:
                gate_name, qubit_idx = gate
                params = 0
            else:
                raise ValueError
            if gate_name == 'R':
                qasm_txt += _R_gate(params.theta, params.phi, qubit_idx - 1)
            elif gate_name == 'M':
                qasm_txt += _M_gate(params.Theta, qubit_idx[0] - 1, qubit_idx[1] - 1)
            elif gate_name == 'X':
                qasm_txt += _X_gate(qubit_idx - 1)
            else:
                raise ValueError
    return qasm_txt


def pastaq_gates_to_qiskit(input_arr, num_qubits):
    qb = QuantumRegister(num_qubits)
    qc = QuantumCircuit(qb)
    count = dict()
    for gate_layer in input_arr:
        for gate in gate_layer:
            if len(gate) == 3:
                gate_name, qubit_idx, params = gate
            elif len(gate) == 2:
                gate_name, qubit_idx = gate
                params = 0
            else:
                raise ValueError
            if gate_name not in count:
                count.update({})
            if gate_name == 'R':
                qc.u3(params.theta, params.phi - np.pi / 2, -params.phi + np.pi / 2, qubit_idx - 1)
            elif gate_name == 'M':
                qc.ms(params.Theta, [qubit_idx[0] - 1, qubit_idx[1] - 1])
            elif gate_name == 'X':
                qc.x(qubit_idx - 1)
            else:
                raise ValueError
    return qc
