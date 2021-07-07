#!/usr/bin/env python
# coding: utf-8

from matplotlib import pyplot as plt
from math import pi

#import pudb as dbg
import sys

import pennylane as qml
import numpy as onp

# circuit depth
num_layers = 2

# number of qubit
num_wires  = 4

# set Pauli Z measurment operator
Z_obs = qml.PauliZ(0)
for j in range(1,num_wires):
    Z_obs = Z_obs @ qml.PauliZ(j)

#exact_tensornet = qml.device("default.tensor", wires=num_wires, contraction_method="greedy")
#mps_tensornet = qml.device("default.tensor", wires=num_wires, representation="mps")
dev_qubit = qml.device("default.qubit", wires=num_wires)
dev = dev_qubit

theta_single = onp.random.rand(num_layers,num_wires,3)
theta_two    = onp.random.rand(num_layers,num_wires-1,1)

@qml.qnode(dev)
def ion_circuit(qubit_theta, MS_theta):
    for ell in range(num_layers):
        qml.broadcast(qml.Rot, wires=dev.wires, pattern='single', parameters=qubit_theta[ell])
        qml.broadcast(qml.ops.IsingXX, wires=dev.wires, pattern='chain',  parameters=MS_theta[ell])
    qml.broadcast(qml.Rot, wires=dev.wires, pattern='single', parameters=qubit_theta[-1])
    return qml.probs(wires=range(num_wires))

probs = ion_circuit(theta_single, theta_two)
bit_strings = ion_circuit.device.generate_basis_states(num_wires)

plt.scatter(range(len(probs)),onp.zeros(len(probs)), s=200*onp.array(probs))
plt.axis('off')
plt.show()






#





#






#
