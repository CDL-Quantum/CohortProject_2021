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



Yes the arguments to use non-variational techniques have to do with improving accuracy at low or medium computational cost and in addition, non-variational techniques can ensure size consistency which is not ensured by truncated CISD (see response 2.). Different techniques have different implementations on quantum hardware, so it's worth exploring diffrent options.

The scalability of post-Hartree Fock (HF) methods, such as CISD and FCI, is the main bottleneck to simulate larger molecules with high accuracy. 
A non-variational method that can improve the accuracy without increasing substantially the computational cost is Coupled Clusters Single Doubles (CCSD), which is a truncated version of Coupled Cluster (CC) theory. In the CC theory, the improvement of the wave function is through the application of the exponential of cluster operators  to the HF wave function, ![CC_angle](https://latex.codecogs.com/gif.latex?%7C%20CC%20%5Crangle%20%3D%20e%5E%7BT%7D%7C%20HF%20%5Crangle) .

Coupled cluster (CC) theory provides a compelling framework of approximate infinite-order perturbation theory, in the form of an exponential of cluster operators describing the true quantum many-body effects of the electronic wave function at a computational cost that, despite being significantly more expensive than DFT, scales polynomially with system size. 


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
We computed the energies for a planar H4 molecule when the separation between the two H2 fragments is as large as 100A (see table). The calculations were performed for a planar H4 molecule dissociating into 2 H2 molecules with separation corresponding to the minimum energy (see figure for dissociation curve H2 above)(is that the case for your calcs Rodrigo?).  The first rows correspond to energies computed using the PYSCF package and the last rows to energies computed with the tequila package.
We observe that CCSD is size consistent but CISD isn't. That is also what is claimed in the literature (add ref joh).

The primary source of error for HF, the inability to describe systems with multiple electronic configurations.
On the other hand, CCSD, CISD and FCI, do account for multiple electronic configurations in the wave function.

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
Frequently, the gate count reduction is particularly large in the number of expensive entan
gling gates required ( ref BKvsJW).
Such a reduction is crucial in the NISQ era.

In order to simulate fermionic operators with qubits we need the information on the
occupation of the target orbital, and the information on the parity of the set of orbitals with index less than
the target orbital. 
When using the Jordan-Wigner transformation and its associated occupatio basis the occupation information is stored locally but the parity information is non-local. In the case of The Bravyi-Kitaev transformation and basis  the locality of the occupation information and
and of the parity information are balanced and this fact results in an improved simulation efficiency.
It has been claimed that Bravyi-Kitaev mapping is superior in all cases aside from
the lexicographic ordering (ref BKvsJW).
For VQEs however there is a claim that no major differences exist in the accuracy between the Bravyi-Kitaev and the Jordan-Wigner transformations (it's in Artur's lecture but no ref found yet!).

2. What are the requirements for a function of qubit operators to be a valid mapping for the fermionic operators?
Any mapping protocol should size consistent, meaning the N sites from the Fock space should be represented with n qubits. 
Additionally given that electrons are fermions, the mapping should also follow a fermionic statistics. 
Since the desired quantity is the energy <H>, the mapping should also be iso-spectra, meaning that the eigen values of the Hamiltonian in the qubit space are the same as in the Fermionic basis. 

3. The electronic Hamiltonian is real (due to time-reversal symmetry), what consequences does that have on the terms in the qubit Hamiltonian after the Jordan-Wigner transformation?
(how to ensure JW creates a hermitian mapping)
(since H is hermitian means all we should only have quadratic terms? (not sure) but is the only way to have a hermitian operator)


# Step #3: Unitary transformations

1. Standard Hamiltonian symmetries are i) number of electrons ![number of electrons](https://latex.codecogs.com/gif.latex?%5Chat%7BN%7D_%7Be%7D%3D%5Csum_k%20%5Chat%7Ba%7D_%7Bk%7D%5E%5Cdagger%20%5Chat%7Ba%7D_%7Bk%7D), ii) electron spin ![S2z](https://latex.codecogs.com/gif.latex?%5Chat%7BS%7D%5E%7B2%7D), iii) electron spin projection ![Sz](https://latex.codecogs.com/gif.latex?%5Chat%7BS%7D_%7Bz%7D), iv) time-reversal symmetry, and v) point-group symmetry forsymmetric molecules.  Which of these symmetries are conserved in a) UCC and b) QCC ?

2. Why symmetries are helpful for constructing a unitary operator which rotates the initial state  ![init q state](https://latex.codecogs.com/gif.latex?%7C%20%5Cbar%7B0%7D%20%5Crangle) to the eigenstate  ![eigen state](https://latex.codecogs.com/gif.latex?%7C%20%5CPsi%20%5Crangle)?
 
 They can help reduce the complexity of the unitary transformation corresponding to the rotation needed for the preparation of the state. And the state will have the proper physical symmeties by construction. (ref IZmaelov20)

 
3. What are the ways to restore symmetries if your unitary transformation break them?
 
 Two different ways have been proposed to restore symmetry. One is to add correlation using entangling gates. The other is to constraint the VQE by imposing the conservation of symmetries such as spin or particle conservation (ref  10 in the instructions,QCCIzmaelov18 )
 
 # Step #4: Hamiltonian measurements
 
 
# Step #5: Use   of  quantum   hardware
 First we carry out the entire VQE optimization procedure by optimizing amplitudes of step 3 unitaries. Given the entanglers and their amplitudes found in Step 3, we find the corresponding representation of these operators in terms of elementary gates and verify that the expectation value is near the ground state energy. We have done this by running IBM Quantum Experience (ibmq) with a backend simulator. We found a 1.856 % of difference.
 The results show:
 | Classical software       | IBM-Q quantum software (IBM Qasm simulator)              |  Difference       |  
|:------:|:---------------:|:---------------:|  
|   -0.9486411121761   |   -0.930076203543293   |  1.856%  | 
 
Additional  questions:
1) Implement an error-mitigation protocol based on removing measurement results correspond- ing to a wrong number of electrons, which is described in Ref. [14](see Sec. 3.4. Post-processing Procedure). How diﬀerent are the results of simulations with and without error-mitigation?
 
 
