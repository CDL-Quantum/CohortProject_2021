![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)


# Questions 

## Step #1: Generating PES using classical methods
1. Among classical methods, there are techniques based on the variational approach and thosethat are not.  Identify variational methods among those that were used and explain advantages ofthe variational approach.  Are there any arguments for using non-variational techniques?

|        |                 |   
|:------:|:---------------:|    
|   HF   |   Variational   |    
|  CCSD  | NOT Variational |    
|  CISD  |   Variational   |    
|   FCI  |   Variational   |     


Yes the arguments to use non-variational techniques such as Cupled Clusters (CC) have to do with improving accuracy and in addition, non-variational techniques can ensure size consistency which is not ensured by truncated CISD (see response to question 2.). Different techniques have different implementations on quantum hardware, so it's worth exploring different options to find that best fits quantum computers. 

The scalability of post-Hartree Fock (HF) methods, such as CISD and FCI, is the main bottleneck to simulate larger molecules with high accuracy. 
A non-variational method that can improve the accuracy without increasing substantially the computational cost is Coupled Clusters Single Doubles (CCSD), which is a truncated version of Coupled Cluster (CC) theory. In the CC theory, the improvement of the wave function is through the application of the exponential of cluster operators  to the HF wave function, ![CC_angle](https://latex.codecogs.com/gif.latex?%7C%20CC%20%5Crangle%20%3D%20e%5E%7BT%7D%7C%20HF%20%5Crangle) .
CC scales polynomially in the system size.



In the figures bellow we present the pontential energy surfaces (PESs) for the dissociation of H<sub>2</sub>, LiH, H<sub>2</sub>O and H<sub>4</sub> molecules using different methods. We left out CISD in the cases it didn't converge. We observe that CISD improves the PES over HF in all the cases under study. 
|  |  | 
| :---------: | :---------: |
| ![Unsolved Graph](./resources/plots_task1/h2_dissociation.png)  | ![Unsolved Graph](./resources/plots_task1/h2o_dissociation.png) |
| ![Unsolved Graph](./resources/plots_task1/lih_dissociation.png) | ![Unsolved Graph](./resources/plots_task1/h4_dissociation.png) |


2. There is another division between classical methods, it is based on so-called separability or size-consistency.   Simply speaking, if one investigates two molecular fragments (A and B) at a large distance from each other (∼100 ̊A) then the total electronic energy should be equalto the ![Sum of energies](https://latex.codecogs.com/gif.latex?%5Csum%20E_%7BA&plus;B%7D%3DE_%7BA%7D&plus;E_%7BB%7D), where the energy of each fragment (![E_a](https://latex.codecogs.com/gif.latex?E_%7BA%7D) or ![E_b](https://latex.codecogs.com/gif.latex?E_%7BB%7D)) can be obtained in a calculation that does not involve the other fragment.  If this condition is satisfied for a particular method, this method is separable or size-consistent.  Check separability of HF, CISD, and CCSD by taking 2 ![H_2](https://latex.codecogs.com/gif.latex?H_%7B2%7D) fragments at a large distance from each other and comparing the total energy with 2 energies of one ![H_2](https://latex.codecogs.com/gif.latex?H_%7B2%7D) molecule.  Explain your results.

For the follwing calculations we used 0.7 a0 as the interatomic distance for the H2 molecule, and for the H4, we separeted each H2 fragment by 100 A (188.973 a0). 

|  Method       | Energy  | Energy   | Energy  | 
|--------|----------|----------|---------------|
| platform: PYSCF   |  H<sub>2</sub> [Ha] | H<sub>4</sub> [Ha]  | H<sub>4</sub> -2 * H<sub>2</sub> [Ha] | 
|  RHF   | -1.1173 | -2.2347 | 3.11E-14      | 
|  CCSD  | -1.1362 | -2.2723  | 2.22-14     |  
|  CISD  | -1.1362  | -2.2720 | 0.000404       |
|   FCI  |  -1.1362 | -2.2724  |  2.975E-14     | 
|--------|----------|----------|---------------|
| platform: tequila||||
|  RHF   | --1.1173 |-2.2347  | 3.15 E-14      | 
|  CCSD  | -1.1362 | -2.2724  | 1.78 E-14     |  
|  CISD  | -1.1362  | -2.2720 | 0.000404       |
|   FCI  |  -1.1362 | -2.2723  |  2.75E-14     | 
|--------|----------|----------|---------------|


For an infinitely stretched molecule we expect the energy to be the sum of the energies of the individual fragments. In the limit of infinite internuclear separation, the energy of H4 should equal twice the energy of the H2 molecule. Any discrepancy between these two energies would imply that the method is not size consistent. 
We computed the energies for a planar H4 molecule when the separation between the two H2 fragments is as large as 100A (see table). The calculations were performed for a planar rectangular H4 geometry and we stretched the horizontal distance and left the vertical fixed to approx the equilibrium distance for H2 (0.7 a0).  The first rows in th etable correspond to energies computed using the PYSCF package and the last rows to energies computed with the tequila package.
We observe that CCSD is size consistent but CISD isn't. That is also what is claimed in the literature.

On the other hand we see that FCI is size consistent and HF as well as long as we use the restricted version of HF.


3. Optional:  If one is interested in converging to the exact non-relativistic electronic energies, there  are  two  independent  coordinates:  


1) accuracy  of  accounting  for  many-body  effects  beyondthe Hartree-Fock method (electronic correlation)
 
2) accuracy of representation of one-electronstates,  or  convergence  with  respect  to  the  one-electron  basis  size.   
3) 
Convergence  along  the  firstcoordinate  can  be  illustrated  by  monitoring  reduction  of  the  energy  deviations  from  the  Full  CI answer in a particular basis set for a series of increasingly accurate approaches, e.g.  HF, CCSD,CCSD(T), CCSDT. Convergences along the second coordinate requires the basis set extension from STO3G to a series like cc-pVDZ, cc-pVTZ, cc-pVQZ, cc-pV5Z. 

Explore for a small system like H<sub>2</sub> both  convergences.   
Which  energies  should  be  expected  to  be  closer  to  experimentally  measure dones?

Below we show the ground state energy of H2 computed with different wavefunction techniques and using different basis sets, where STO3G is the smallest basis. We observe that as we go to larger basis we obtain lower ground state energies. Given that HF and CI methods are variational and give a lower bound for the energy we know that lower energies are closer to the true (experimental) value. 

![Unsolved Graph](./resources/H2_energy_methods_vs_basis_set.png)


# Step #2: Generating the qubit Hamiltonian


1.  What are the cons and pros of the Bravyi-Kitaev transformation compared to the Jordan-Wigner transformations?

In the Jordan-Wigner transformation a single fermionic creation or annihilation operator is represented by O(n) qubit operations while in the Bravyi-Kitaev transformation only O(log n) qubit operations are required, thus 
the Bravyi-Kitaev transformation is a more compact one, i.e. a lower number of gates are needed in the quantum circuit. 
Frequently, the gate count reduction is particularly large in the number of expensive entangling gates required [ref "A comparison of the Bravyi-Kitaev and Jordan-Wigner transformations for the quantum simulation of quantum chemistry" ](https://arxiv.org/abs/1812.02233 ).
Such a reduction is crucial in the NISQ era. 

In order to simulate fermionic operators with qubits we need the information on the
occupation of the target orbital, and the information on the parity of the set of orbitals with index less than
the target orbital. 
When using the Jordan-Wigner transformation and its associated occupation basis the occupation information is stored locally but the parity information is non-local. In the case of The Bravyi-Kitaev transformation and basis  the locality of the occupation information and
and of the parity information are balanced and this fact results in an improved simulation efficiency.
It has been claimed that Bravyi-Kitaev mapping is superior in all cases aside from
the lexicographic ordering. Ultimately the comparison between the two methods should be done in a case by case basis.

2. What are the requirements for a function of qubit operators to be a valid mapping for the fermionic operators?
Any mapping protocol should size consistent, meaning the N sites from the Fock space should be represented with n qubits. 
Additionally given that electrons are fermions, the mapping should also follow a fermionic statistics. 
Since the desired quantity is the energy <H>, the mapping should also be iso-spectra, meaning that the eigen values of the Hamiltonian in the qubit space are the same as in the Fermionic basis. 

3. The electronic Hamiltonian is real (due to time-reversal symmetry), what consequences does that have on the terms in the qubit Hamiltonian after the Jordan-Wigner transformation?
 All terms need to be hermitian.
 
*(how to ensure JW creates a hermitian mapping)
(since H is hermitian means all we should only have quadratic terms? (not sure) but is the only way to have a hermitian operator)*


# Step #3: Unitary transformations

1. Standard Hamiltonian symmetries are i) number of electrons ![number of electrons](https://latex.codecogs.com/gif.latex?%5Chat%7BN%7D_%7Be%7D%3D%5Csum_k%20%5Chat%7Ba%7D_%7Bk%7D%5E%5Cdagger%20%5Chat%7Ba%7D_%7Bk%7D), ii) electron spin ![S2z](https://latex.codecogs.com/gif.latex?%5Chat%7BS%7D%5E%7B2%7D), iii) electron spin projection ![Sz](https://latex.codecogs.com/gif.latex?%5Chat%7BS%7D_%7Bz%7D), iv) time-reversal symmetry, and v) point-group symmetry forsymmetric molecules.  Which of these symmetries are conserved in a) UCC and b) QCC ?
 
 
 Since in the UCC method the unitary operators are constructed from fermionic operators before doing the WJ or BK transformation the fermionic symmetries such as particle number N, spin Sz and spin projection S^2 are conserved. That's not the case for QCC where the unitaries are constructed in the qubit space. The QCC is more ressource efficient but needs extra care to ensure conservation of physical symmetries. This could be done by introducing constraints in the VQE minimization or discarding solutions in an error mitigation scheme like the one discussed in task 5. 
 Time-reversal is conserved in both techniques since the unitary oparators used in both are hermitian. In fact ensuring hermiticity of the unitaries in UCC is the reason why the exponential exponents are not sums, which makes the computation much harder.
 Regarding point-like symmetries of the symmetric molecules I would think that they could also be imposed with an error mitigation protocol by discarding solution of the wavefunction that violate them. But more easily they could probably be imposed at the level of the architecture, because probably they can help reduce degrees of freedom such as number of qubits or connections. I don't think UCC nor QCC ensure the conservation of these point-like symmetries.

2. Why symmetries are helpful for constructing a unitary operator which rotates the initial state  ![init q state](https://latex.codecogs.com/gif.latex?%7C%20%5Cbar%7B0%7D%20%5Crangle) to the eigenstate  ![eigen state](https://latex.codecogs.com/gif.latex?%7C%20%5CPsi%20%5Crangle)?
 
 They can help reduce the complexity of the unitary transformation corresponding to the rotation needed for the preparation of the state. And the state will have the proper physical symmeties by construction. (ref IZmaelov20)

 
3. What are the ways to restore symmetries if your unitary transformation break them?
 
 One way is to implement an error mitigation protocol like the one suggested in task 5 where the symmetries are enforced in the final wavefunction by discarding the measuremnets corresponding to contributions that violate the symmetry. One could also enforce the symmetry by introducing the variance of the symmetry operator in the minimization squeme of the VQE in the form of a Lagrangian multipliers (constraints). (QCCIzmaelov18 ref 10 )
 In ref.(ref kink) is has been suggested that the symmetry violation can be corrected by adding more correlation (entanglers).
 
 # Step #4: Hamiltonian measurements
 
 
# Step #5: Use   of  quantum   hardware
 First we carry out the entire VQE optimization procedure by optimizing amplitudes of step 3 unitaries. Given the entanglers and their amplitudes found in Step 3, we find the corresponding representation of these operators in terms of elementary gates and verify that the expectation value is near the ground state energy. We have done this by running IBM Quantum Experience (ibmq) with a backend simulator. We found a 1.856 % of difference.
 The results show:
 | Classical software       | IBM-Q quantum software (IBM Qasm simulator)              |  Difference       |  
|:------:|:---------------:|:---------------:|  
|   -0.9486411121761   |   -0.930076203543293   |  1.856%  | 
 
Additional  questions:
1) Implement an error-mitigation protocol based on removing measurement results correspond- ing to a wrong number of electrons, which is described in Ref. [14](see Sec. 3.4. Post-processing Procedure). How diﬀerent are the results of simulations with and without error-mitigation?
 
 
# Further challenges 
 
##  How to obtain excited electronic states of the same or different symmetry?
 
The variational theorem is the key element for VQE-based algorithms. However, for excited electronic states there is not such theorem that ensures a lower-bound on the first excited state. One possibilty to modify the VQE protocol for excited states is by including a lagrange multiplier that ensures the excited state and ground staet must be orthogolan to each other, 
 
![L excited state](https://latex.codecogs.com/gif.latex?%5Cboldsymbol%7B%5Ctheta%7D%5E*%20%3D%20%5Carg%5Cmin_%7B%5Cboldsymbol%7B%5Ctheta%7D%7D%20%5C%3B%7B%5Ccal%20L%7D%28%5Cboldsymbol%7B%5Ctheta%7D%29%20%3D%20%5Carg%5Cmin_%7B%5Cboldsymbol%7B%5Ctheta%7D%7D%20%5Cleft%20%5Clangle%20%5CPsi_1%28%5Cboldsymbol%7B%5Ctheta%7D%29%20%5Cmiddle%20%7C%20%5Chat%7BH%7D%20%5Cmiddle%20%7C%20%5CPsi_1%28%5Cboldsymbol%7B%5Ctheta%7D%29%20%5Cright%20%5Crangle%20&plus;%20%5Clambda%20%5Cleft%20%7C%20%5Cleft%20%5Clangle%20%5CPsi_1%28%5Cboldsymbol%7B%5Ctheta%7D%29%20%5Cmiddle%20%7C%20%5CPsi_0%20%5Cright%20%5Crangle%20%5Cright%20%7C) 

However, this approach has multiple local minima since all excited staes are orthogonal to the ground state.

Another possiblity is to use symmety constrains as penalizers in the expectation value of the energy,
 
![excited states symmetries](https://latex.codecogs.com/gif.latex?%5Cboldsymbol%7B%5Ctheta%7D%5E*%20%3D%20%5Carg%5Cmin_%7B%5Cboldsymbol%7B%5Ctheta%7D%7D%20%5C%3B%7B%5Ccal%20L%7D%28%5Cboldsymbol%7B%5Ctheta%7D%29%20%3D%20%5Carg%5Cmin_%7B%5Cboldsymbol%7B%5Ctheta%7D%7D%20%5Cleft%20%5Clangle%20%5CPsi_1%28%5Cboldsymbol%7B%5Ctheta%7D%29%20%5Cmiddle%20%7C%20%5Chat%7BH%7D%20%5Cmiddle%20%7C%20%5CPsi_1%28%5Cboldsymbol%7B%5Ctheta%7D%29%20%5Cright%20%5Crangle%20&plus;%20%5Clambda%20%5Cleft%20%7C%20%5Cleft%20%5Clangle%20%5CPsi_1%28%5Cboldsymbol%7B%5Ctheta%7D%29%20%5Cmiddle%20%7C%20%5Chat%7BS%7D%20%5Cmiddle%20%7C%20%5CPsi_1%28%5Cboldsymbol%7B%5Ctheta%7D%29%20%5Cright%20%5Crangle-S%20%5Cright%20%7C)
 
 where the symmetry operator ![symmetry operator](https://latex.codecogs.com/gif.latex?%5Chat%7BS%7D) must commute with the electornic Hamiltonian, ![commutator H S](https://latex.codecogs.com/gif.latex?%5B%5Chat%7BH%7D%2C%5Chat%7BS%7D%5D%20%3D%200), so both share the same eigenstates.
 
## How to utilize larger basis sets into smaller number of qubits?
 
As it has been shown through this tutorial. The number of qubits required to compute the electornig energy of a molecule scales linear with the number of molecular spin-orbitals. This has limited the use of small basis sets since for example, methane (CH4) with a STO-3G basis set requires 18 qubits. 
One possibility is to restricting the orbitals where the single and doubles excitations could happen, for example, only the  m-electrons with the highest energy or a reduce set of orbitals. This technique has been exploited for many years in classical electronic structure problems,   multiconfigurational  self-consistent-field  (MCSCF). This idea was explored in more detail in Phys. Rev. X **10**, 011004 (2020). 
However, while this approach seems to be a viable route to simualate bigger molecules in a quantum computer, the authors point that the number of measurementes increased, so different samples schemes may be developed in the future to this overhead. 
 

## What are alternatives to VQE for the electronic structure problem using quantum computerswith shallow circuits without error-correction?
 
One alternative is to simulate the eletronic problem using a quantum analog. This was proposed in Nature **574**, 215 (2019) using cold atoms trapped in an optical lattice. This approach is based on mapping the electron-electorn interactions with the dipole-dipole interaction of the atoms.
The cons of this porposal is the difficulty on engeniering of the electron-electorn interactions.
 
Quantum gate computing is not the only possiblity, quantum annealing computers permit us to know the lowest state of a problem hamiltonian by addiabatically evolving from the quantum state of an initial Hamiltonian which groudn state is known. For more insigth you can visit [DWave](https://docs.dwavesys.com/docs/latest/c_gs_2.html). 
The electronic structure could be mapped into an Ising Hamiltonian that can be solved with a quantum annealer [arXiv:1901.04715
](https://arxiv.org/abs/1901.04715). For this approach the first bottleneck is how to map the Helectronic Hamiltonian in the Jorda-Wigner transformation to the 
Ising model. There have been two main approaches, [arXiv:1706.00271](https://arxiv.org/abs/1706.00271) and [arXiv:1901.04715](https://arxiv.org/abs/1901.04715).
 

 
 
 
