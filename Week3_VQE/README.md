![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)


# Questions 

## Step #1: Generating PES using classical methods
1. Among classical methods, there are techniques based on the variational approach and thosethat are not.  Identify variational methods among those that were used and explain advantages ofthe variational approach.  Are there any arguments for using non-variational techniques?

| Method |                 |   |
|:------:|:---------------:|:-:|
|   HF   |   Variational   |   |
|  CCSD  | NOT Variational |   |
|  CISD  |   Variational   |   |
|   FCI  |   Variational   |   |

Are there any arguments for using non-variational techniques?
The scalability of post-Hartree Fock (HF) methods, e.g., CISD and FCI, is the main bottleneck to properly simulate larger molecules. 
One possiblity to improbe the correlation energy is through the Coupled Cluster (CC) theory.
In the CC theory, the improvement of the wave function is through the application of the exponential of cluster operators  to the HF wave function, $| CC \rangle = e^{T}| HF \rangle$ 
This exponetial form is what makes CC a methodology that could be better suited in quantum computer.


<> Coupled cluster (CC) theory provides a compelling framework of approximate infinite-order perturbation theory, in the form of an exponential of cluster operators describing the true quantum many-body effects of the electronic wave function at a computational cost that, despite being significantly more expensive than DFT, scales polynomially with system size. 



|  |  | 
| :---------: | :---------: |
| ![Unsolved Graph](./resources/plots_task1/h2_dissociation.png)  | ![Unsolved Graph](./resources/plots_task1/h2o_dissociation.png) |
| ![Unsolved Graph](./resources/plots_task1/lih_dissociation.png) | ![Unsolved Graph](./resources/plots_task1/h4_dissociation.png) |
