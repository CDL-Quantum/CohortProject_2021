## Project 3: VQE: Constructing potential energy surfaces for small molecules

## Tasks 

### Task 1 : classical simulation

#### Question 1
We generated potential energy surfaces on the sto-3g basis for several moldecules using classical methods. The classical methods include variational methods such as Hartree-Fock (HF), Configuration Interaction Singles and Doubles (CISD),  and the exact answer within the chosen basis Full Configuration Interaction (FCI) and non-variational methods such as Coupled Cluster Singles and Doubles (CCSD). The molecules on which we tested the above methods are H2, H2O, H4, LiH, N2 and NH3.

Weak interaction

<table><tr>
    <td><img src="./img/Task1_Qu1_H2.png" style="width: 350px;"></td> 
    <td><img src="./img/Task1_Qu1_LiH.png" style="width: 350px;"></td>
    </tr>
</table>

Strong interaction

<table><tr>
    <td><img src="./img/Task1_Qu1_H2O.png" style="width: 350px;"></td> 
    <td><img src="./img/Task1_Qu1_H4.png" style="width: 350px;"></td>
    </tr>
</table>

## Answers to theoretical Questions:

Which methods are variational?

The Hartree-Fock, CISD & FCI methods are variational methods. The CCSD method is non-variational.

Advantages of the Variational approach?

- quite accurate if a good trial function is chosen
- efficient (do not need full exact solution)

Disadvantages?

- Requires Hermition operators with a bounded spectrum (for example, the position operator does not have a bounded spectrum)
- Need contraints to get excited states
- Very innaccurate if you do not have a good trial solution

#### Question 2
We checked the separability of exact solving FCI and approximate methods HF, FCI and CCSD. In order to do that we placed two H2 molecules far from each other (20, 50 and 100 A) and compared the computes energy against twice the enrgy of a single H2. the difference of energy as a function of the bonds can be seen below.

Below is a plot of the PES of the H2 molecule, followed by plots of PES for two H2 molecules apart respectivelu 20, 50 and 100A

![PES](./img/Task1_Qu2_energy.png)

Below is a plot of the log of the difference of PES between two H2 molecules incresingly apart and twice the PES of a single H2 molecule. The least seprable method is CCISD, while FCI is perfectly seperable.

![PES siff](./img/Task1_Qu2_diff.png)

## Answers to the Theoretical Questions

What are the requirements for a function of qubit operators to be a valid mapping for the
fermionic operators?

You must tensor multiply pauli matrices of the previous qubits to ensure we keep the parity odd property of fermions.

The electronic Hamiltonian is real (due to time-reversal symmetry), what consequences does
that have on the terms in the qubit Hamiltonian after the Jordan-Wigner transformation?

The qubit hamiltonian & electric hamiltonian are isospectral - they contain the same eigenvalues

What are the cons and pros of the Bravyi-Kitaev transformation compared to the
Jordan-Wigner transformations?

Main difference in the locality of qubit Hamiltonians. Also, JW mapping requires O(N) qubit operations to simulate one electronic operation.
JW mapping requires O(log(N)) qubit operations to simulate one electronic operation, i.e. electronic creation or annihilation operation can be simulated in O(log(N)) qubit operations. It is argued that the breaking point where BK definitely outperformed JW is at N=32. It is also argued that BK transformation frequently results in substantial reduction of gate count.


#### Question 3
For the above benchmarks we used the simple basis sto-3g, which is a  minimal basis set, where 3 primitive Gaussian orbitals are fitted to a single Slater-type orbital (STO). However other more complex basis exist such as cc-pVDZ,cc-pVDZ,cc-pVTZ,cc-pVQZ and cc-pV5Z. We benchmarked these basis for some methods (HF,CCSD,FCI) on the simplest molecule H2.

The graph belows shows a comparaison of potential energy surfaces  between basis for each method. The sto stands out as yielding the most different results.

![PES](./img/Task1_Qu3_plot1_energy.png)

The graph belows shows the difference of potential energy surfaces between the CC basis and sto basis for each method. The HF methods stands out as showing different results.

![PES diff](./img/Task1_Qu3_plot1_diff.png)

The graph belows shows the logarithm of the maximum inter basis difference of potential energy surfaces, in other words the Hinfinity distance on the considered bond distance range between each pair of basis for the  FCI method. For example cc-PV5Z has a difference of 10^-2 with the sto-3g basis. The basis are ordered in increasing ability to model reality, and chances to be close to experiments.

![diff matrix](./img/Task1_Qu3_plot1_diff_matrix.png)

The table below shows the times that each computation has taken for the H2 molecule, together with the precision matrix above, it can help to do a trade off between the time to compute and the precision needed.

![times](./img/Task1_Qu3_plot1_times.png)

Standard Hamiltonian symmetries are i) number of electrons ˆNe = ∑k ˆa†kˆak, ii) electron spin ˆS2, iii) electron spin projection ˆSz, iv) time-reversal symmetry, and v) point-group symmetry for
symmetric molecules. Which of these symmetries are conserved in a) UCC and b) QCC ?

UCC: conserves N, Sz, and S (requires symmetrization)
QCC: can break any symmetries individually upon entanglement, but collective action of entanglers preserves symmetries (if one pays attention to it)

Why symmetries are helpful for constructing a unitary operator which rotates the initial state
| ̄0〉 to the eigenstate |Ψ〉?

They are not only helpful, they are necessary. Symmetries correspond to conservation laws, and so by observing symmetries you automatically observe conservation of corresponding quantities.

They can also be used to reduce noise during measurements and add contraints for the expectation of the energy due to symmetry breaking.

What are the ways to restore symmetries if your unitary transformation break them?

Symmetrization at every step of transformation.

Another option is to rotate the symmetry by applying unitary transformations (since you can't rotate the measurement device).

## Task 5: Simulation on a Quantum Computer

The following plots are taken from the IBM quantum website and are the result of multiple simulations on IBM's quantum computer (we used ibmq_bogata)


![CDL 2020 Cohort Project](img/1.jpg)


![CDL 2020 Cohort Project](img/2.jpg)


![CDL 2020 Cohort Project](img/3.jpg)

## Business Application

For more details refer to the [Business Application found here](./Business_Application.md)

![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
