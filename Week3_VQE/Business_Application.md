![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Team 3 Quantum Cohort Project Business Application

## Variational Qubit Characterization

Characterization of a new superconducting qubit (SCQ) device design is critical for understanding the performance of a new device.  In particular, a SCQ designer needs to know the operating points of the qubits (frequencies) and their spacing with respect to excited states.  A poorly designed device may exhibit frequency crowding, crosstalk, leakage and other decoherence processes.  Given a device Hamiltonian, derived, for example, through intuition or first principles, the SCQ designer can determine the spectrum by obtaining a matrix representation and numerically solving an eigenvalue problem.  However, the designer must truncate the operators with a small number of levels and make other approximations to reduce the size of the matrix Hamiltonian.  This can be done for a single transmon (or similar), however, as the industry scales up designs, characterizing multiple qubit devices will require new methods that  scale with the size of the underlying Hilbert space.

Variational Qubit Characterization fights Hilbert space with Hilbert space!   

Here's how it works:

![system figure](../figures/VQC.jpg)

The process starts with a SQC circuit design. Analytical methods are known that quantize the circuit to construct a Hamiltonian that describes the time evolution of the quantum degrees of freedom of the device.  Now, instead of constructing a huge matrix and calling numerical linear algebra routines, VQC transforms the Hamiltonian to a Pauli representation that can be programmed and measured on a NISQ computer.  Given a suitable ansatz, the Variational Quantum Eigensolver algorithm can determine the lowest eigenvalue of the device Hamiltonian.  Additional VQE runs and classical post-processing can also determine excited states [1], thereby providing an estimate of the lowest energy levels of the device.  VQC thus provides a scalable method for quantum device characterization that can be used for SQC design -- without the need for costly device manufacturing and manual characterization.

[1] Higgott, Oscar, Daochen Wang, and Stephen Brierley. "Variational quantum computation of excited states." Quantum 3 (2019): 156

## Customers

Quantum hardware companies using superconducting qubits will benefit from this technology.  Potential customers include IBM, Rigetti, Google and IQM.

## Video

https://drive.google.com/file/d/1Y5z6hldL7Hs4U-0R5_WK5K-4qlbdi8Hc/view?usp=sharing
