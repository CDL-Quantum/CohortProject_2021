![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 3: VQE: Constructing potential energy surfaces for small molecules

## Tasks include:
### Part 1: Generating PES using classical methods.
**Analysis:**

**Qestion**: Among Classical methods, there are techniques based on the variational approach and those that are not. Identify variational methods among those that were sued and explain advantages of the variational approach. Are there any arguments for using non-variational techniques?
<br />
**Answer**:

**Question**: There is another division between classical methods, it is based on so-called separability or size-consistency. Simply speaking, if one investigates, two molecular fragments (A and B) at large distance from each other (~ 100 A), then the total electronic energy should be equal to the sum E<sub>A+B</sub> = E<sub>A</sub> + E<sub>B</sub>, where the energy of each fargment (E<sub>A</sub> or E<sub>B</sub>) can be obtained in a calculation that does not involve the other fragment. If this condition is satisfied for a particular method, this method is separable or size-consistent. Check separability of HF, CISD, and CCSD by taking 2 H2 fragments at a large distance from each other and comparing the total energy with 2 energies of one H2 molecule. Explain your results.
<br />
**Answer**:

**Question**: If one is interested in converging to the exact non-relativistic electronic energires, there are two independent coordinates: 1) accuracy of accounting for many-body effects beyond the Hartree-Fock method (electronic correlation) and 2) accuracy of representation of one-electron states or convergence with respect tot the one-electron basis size. Convergence along the first coordinate can be illustrated by monitoring reduction of the energy deviations from the Full CI answer in a particular basis set for a series of increasingly accurate approaches, ie. HF, CCSD, CCSD(t), CCSDT. Convergences along the second coordinate requries the basis set extension from STO3G to a series like cc-pVDZ, co-pVTZ, co-pVQZ, cc-pV5Z. Explore for a small system like H2 both convergences. Which energies should be expected to be closer to experimentally measured ones?
<br />
**Answer**:

### Part 2: Generating the qubit Hamiltonian.
**Analysis:** In this section, we were able to generate the qubit hamiltonian for the following molecules: H2, H4, LiH, H20, and N2. Due to the size of each hamiltonian, we wont directly write them (but they are generated in the netebook S2_Hamiltonian_gen.ipynb. For reference of how computationally difficult they are, we have listed the number of qubits required to specify each molecule.

![Qubit Count](../Week3_VQE/imgs/task_2_qubit_count.png)

### H2 Ground state analysis
We found the following information for H2:

![h2 ground state energy](../Week3_VQE/imgs/h2_ground_energy.png)

### H4 Ground state analysis
We found the following information for H4 (we omitted some eigenvalues for ease of reading):

![h4 ground state energy](../Week3_VQE/imgs/h4_ground_state_energy.png)

### LiH Ground state analysis
We found the following infromation for LiH:

![liH ground state energy](../Week3_VQE/imgs/lih_ground_state_energy.png)

**Question**: What are the requirements for a function of qubit operators to be a valid mapping for the fermionic operators?
<br />
**Answer**: The requirements for a function of qubit operators to be a valid mapping is the following:
(1) The function must preserve the anti-commutativity nature of the fermion (Typically seen with the spin).

**Question**: The electronic Hamiltonian is real (due to time-reversal symmetry), what consequences does that have on the terms in the qubit Hamiltonian after the Jordan-Wigner transformation?
<br />
**Answer**: 

**Question**: What are the cons and pros of the Bravyi-Kitaev transformation compared to the Jordan-Wigner transfomrations?
<br />
**Answer**:

### Part 3: Unitary transformations.
**Analysis:**

**Question**: Standard Hamiltonian symmetries are i) number of electrons N<sub>e</sub> = sigma<sub>k</sub> a<sup>t</sup><sub>k</sub>a<sub>k</sub>, ii) electron spin S<sup>2</sup>, iii) electron spin project S<sub>Zz</sub> iv) time-reversal symmetry and v) point-group symmetry for symmetric molecules. Which of these symmetries are conserved in a) UCC and b) QCC?
<br />
**Answer**:
  
**Question**: Why symmetries are helpful for constructing a unitary operator which rotates the initial state |0> to the eigenstate |psi>?
<br />
**Answer:**

**Question**: What are the ways to restore symmetries if your unitary transformation break them?
<br />
**Answer**:

### Part 4: Hamiltonian measurements.
**Analysis:**

### Part 5: Use of quantum hardware.
**Analysis:**

## Further Challenges:
### How to obtain excited electronic states of the same or different symmetry?
**Analysis:**
### Partitioning in the fermionic operator space.
**Analysis:**
### Applying unitary transformations on the Hamiltonian.
**Analysis:**
### Compress larger basis sets into smaller number of qubits.
**Analysis:**

## Business Application

For more details refer to the [Business Application found here](./Business_Application.md)
