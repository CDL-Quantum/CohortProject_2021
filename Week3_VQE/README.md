![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)


# Questions 

## Step #1: Generating PES using classical methods
1. Among classical methods, there are techniques based on the variational approach and thosethat are not.  Identify variational methods among those that were used and explain advantages ofthe variational approach.  Are there any arguments for using non-variational techniques?

| Method |                 | 
|:------:|:---------------:|
|   HF   |   Variational   |
|  CCSD  | NOT Variational | 
|  CISD  |   Variational   | 
|   FCI  |   Variational   |

Are there any arguments for using non-variational techniques?
The scalability of post-Hartree Fock (HF) methods, e.g., CISD and FCI, is the main bottleneck to properly simulate larger molecules. 
One possiblity to improbe the correlation energy is through the Coupled Cluster (CC) theory.
In the CC theory, the improvement of the wave function is through the application of the exponential of cluster operators  to the HF wave function, ![CC_angle](https://latex.codecogs.com/gif.latex?%7C%20CC%20%5Crangle%20%3D%20e%5E%7BT%7D%7C%20HF%20%5Crangle) 
This exponetial form is what makes CC a methodology that could be better suited in quantum computer.

<!---
Coupled cluster (CC) theory provides a compelling framework of approximate infinite-order perturbation theory, in the form of an exponential of cluster operators describing the true quantum many-body effects of the electronic wave function at a computational cost that, despite being significantly more expensive than DFT, scales polynomially with system size. 
-->

Bellow we present the pontential energy surfaces (PESs) for the dissociation of H<sub>2</sub>, LiH, H<sub>2</sub>O and H<sub>4</sub> molecules using different methods.
|  |  | 
| :---------: | :---------: |
| ![Unsolved Graph](./resources/plots_task1/h2_dissociation.png)  | ![Unsolved Graph](./resources/plots_task1/h2o_dissociation.png) |
| ![Unsolved Graph](./resources/plots_task1/lih_dissociation.png) | ![Unsolved Graph](./resources/plots_task1/h4_dissociation.png) |


2. There is another division between classical methods, it is based on so-called separability or size-consistency.   Simply speaking, if one investigates two molecular fragments (A and B) at a large distance from each other (∼100 ̊A) then the total electronic energy should be equalto the ![Sum of energies](https://latex.codecogs.com/gif.latex?%5Csum%20E_%7BA&plus;B%7D%3DE_%7BA%7D&plus;E_%7BB%7D), where the energy of each fragment (![E_a](https://latex.codecogs.com/gif.latex?E_%7BA%7D) or ![E_b](https://latex.codecogs.com/gif.latex?E_%7BB%7D)) can be obtained in a calculation that does not involve the other fragment.  If this condition is satisfied for a particular method, this method is separable or size-consistent.  Check separability of HF, CISD, and CCSD by taking 2 ![H_2](https://latex.codecogs.com/gif.latex?H_%7B2%7D) fragments at a large distance from each other and comparing the total energy with 2 energies of one ![H_2](https://latex.codecogs.com/gif.latex?H_%7B2%7D) molecule.  Explain your results.


|        | Energy   | Energy   | Energy        |
|--------|----------|----------|---------------|
| Method |  H2 [Ha] | H4 [Ha]  | H4 -2 H2 [Ha] |
|   UHF  | -1.06610 | -1.19557 | 0.93665       |
|  RHF   | -1.06610 | -2.13222 | 2.12E-12      |
|  CCSD  |  -1.1012 | -2.2023  | 1.568E-12     |
|  CISD  | -1.1012  | -2.2003  | 0.00203       |
|   FCI  |  -1.1012 | -2.2023  | 1.59E-12      |

In the limit of infinite internuclear distance between the hydrogen atoms, the energy must be twice the indivisual energy of the atoms. Any discrepancy between these two energies.
HF can only represent one electornig configuration, which for the H<sub>2</sub> molecule is Singlet, however, in the limit of separated atoms, each Hydrong atom's electron has a multiplicity of a triple. This is the primary source of error for HF, the lack of possibilty to describe systems with multiple electornic configurations.
On the other hand, CCSD, CISD and FCI, do account for multiple electronic confugurations in the wave function. 

3. Optional:  If one is interested in converging to the exact non-relativistic electronic energies, there  are  two  independent  coordinates:  
  1. accuracy  of  accounting  for  many-body  effects  beyondthe Hartree-Fock method (electronic correlation)
  2. accuracy of representation of one-electronstates,  or  convergence  with  respect  to  the  one-electron  basis  size.   
Convergence  along  the  firstcoordinate  can  be  illustrated  by  monitoring  reduction  of  the  energy  deviations  from  the  Full  CI answer in a particular basis set for a series of increasingly accurate approaches, e.g.  HF, CCSD,CCSD(T), CCSDT. Convergences along the second coordinate requires the basis set extension from STO3G to a series like cc-pVDZ, cc-pVTZ, cc-pVQZ, cc-pV5Z. Explore for a small system like H2 both  convergences.   
Which  energies  should  be  expected  to  be  closer  to  experimentally  measure dones?

![Unsolved Graph](./resources/H2_energy_methods_vs_basis_set.png)
