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

Are there any arguments for using non-variational techniques?

Yes, to improve accuracy and in addition, non-variational techniques can ensure size consistency which is not ensured by truncated CISD (see response 2.).

The scalability of post-Hartree Fock (HF) methods, such as CISD and FCI, is the main bottleneck to simulate larger molecules with high accuracy. 
A non-variational method that can improve the accuracy without increasing substantially the computational cost is Coupled Clusters Single Doubles (CCSD), which is a truncated version of Coupled Cluster (CC) theory. In the CC theory, the improvement of the wave function is through the application of the exponential of cluster operators  to the HF wave function, ![CC_angle](https://latex.codecogs.com/gif.latex?%7C%20CC%20%5Crangle%20%3D%20e%5E%7BT%7D%7C%20HF%20%5Crangle) .
It has been claimed that the exponetial  makes the CC methodology a good fit for quantum computing (ref?).

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
| Method |  H<sub>2</sub> [Ha] | H<sub>4</sub> [Ha]  | H<sub>4</sub> -2 * H<sub>2</sub> [Ha] |
|   UHF  | -1.06610 | -1.19557 | 0.93665       |
|  RHF   | -1.06610 | -2.13222 | 2.12E-12      |
|  CCSD  |  -1.1012 | -2.2023  | 1.568E-12     |
|  CISD  | -1.1012  | -2.2003  | 0.00203       |
|   FCI  |  -1.1012 | -2.2023  | 1.59E-12      |

For an infinitely stretched molecule we expect the energy to be the sum of the energies of the individual fragments. In the limit of infinite internuclear separation, the energy of H4 should equal twice the energy of the H2 molecule. Any discrepancy between these two energies would imply that the method is not size consistent. 
HF can only represent one electronic configuration, which for the H<sub>2</sub> molecule is a singlet, however, in the limit of infinitevely separated atoms, each Hydrogen atom's electron has a multiplicity of a triple (I don't understand this Rodrigo). This is the primary source of error for HF, the inability to describe systems with multiple electronic configurations.
On the other hand, CCSD, CISD and FCI, do account for multiple electronic configurations in the wave function.
We computed the energies for a planar H4 molecule when the separation between the two H2 fragments is as large as 100A (see table). The calculations were performed for a planar H4 molecule dissociating into 2 H2 molecules with separation corresponding to the minimum energy (see figure for dissociation curve H2 above)(is that the case for your calcs Rodrigo?).  The first 3 columns correspond to energies computed using the program ... and the last 3 to energies computed with tequila.
We observe that CCSD is size consistent but CISD isn't. That is also what is claimed in the literature (add ref joh).
On the other hand we see that FCI is size consistent and HF as well as long as we use the restricted version of HF (Rodrigo can ypu comment on UHF/RHF?).


3. Optional:  If one is interested in converging to the exact non-relativistic electronic energies, there  are  two  independent  coordinates:  
  1. accuracy  of  accounting  for  many-body  effects  beyondthe Hartree-Fock method (electronic correlation)
  2. accuracy of representation of one-electronstates,  or  convergence  with  respect  to  the  one-electron  basis  size.   
Convergence  along  the  firstcoordinate  can  be  illustrated  by  monitoring  reduction  of  the  energy  deviations  from  the  Full  CI answer in a particular basis set for a series of increasingly accurate approaches, e.g.  HF, CCSD,CCSD(T), CCSDT. Convergences along the second coordinate requires the basis set extension from STO3G to a series like cc-pVDZ, cc-pVTZ, cc-pVQZ, cc-pV5Z. Explore for a small system like H<sub>2</sub> both  convergences.   
Which  energies  should  be  expected  to  be  closer  to  experimentally  measure dones?

![Unsolved Graph](./resources/H2_energy_methods_vs_basis_set.png)
