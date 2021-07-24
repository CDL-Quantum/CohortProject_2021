![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 3: VQE: Constructing potential energy surfaces for small molecules

#### Alex Khan, Dr. Maninder Kaur, Ritaban Chowdhury, Theo Cleland, Yuval Sanders

Here we provide our work on project 3. Our Business Application is [here](./Business_Application.md) and our video introduction is [here](https://drive.google.com/file/d/1EHxNry_KGci-1Ssjv0kMTpVQdF3DyLml/view?usp=sharing).

Below we answer the various questions found in [the instructions](https://github.com/CDL-Quantum/CohortProject_2021/tree/main/Week3_VQE/Instructions.pdf).

## Step 1

We were asked to investigate the relative quality of three approximation methods:
Hartree-Fock (HF),
Configuration Interaction Singles and Doubles (CISD), and
Coupled Cluster Singles and Doubles (CCSD).
The quality of these approximations were assessed relative to the answer obtained numerically via the
Full Configuration Interaction (FCI) representation.
Our work can be found in [this notebook](./S1_Classical_Methods.ipynb).

### Question 1
>Among classical methods, there are techniques based on the variational approach and those that are not. Identify variational methods among those that were used and explain advantages of the variational approach. Are there any arguments for using non-variational techniques?

**Hartree-Fock:**
As explained in the [provided notebook](https://github.com/CDL-Quantum/CohortProject_2021/tree/main/Week3_VQE/S1_Classical_Methods.ipynb), HF neglects electron-electron correlations and models the 
electronic structure as isolated electrons interacting with the mean field of the remaining particles.
[Scholarpedia](http://www.scholarpedia.org/article/The_Hartree-Fock_method) describes HF as a *variational method* because it seeks to extremise the single-electron wavefunctions and enforce antisymmetry under particle exchange by computing the corresponding [Slater determinant](http://www.scholarpedia.org/article/Second_quantization#Second_Quantization_of_the_Fermi-Dirac_Assemblies).

**Configuration Interaction Singles and Doubles:**
Configuration Interaction (CI) methods are an example of what are called "post-Hartree-Fock" methods
in that they use the HF solution as a starting point but then attempt to rectify the shortcomings of HF in various ways. In CI, we start to account for electron-electron correlations by enlargening the
configuration space of the electrons. This is done by starting with the HF solution and then creating a
basis set for the configuration space by applying various combinations of mode creation/annihilation 
operators to the HF solution. Having established a basis set and hence the configuration space, CI methods
seek the ground state of the resulting restricted form of the electronic structure Hamiltonian.
Because the result is a minimal energy result, CI methods are also *variational*. The restriction to "singles" and "doubles" means that we consider only two-body creation/annihilation operator terms
(i.e. two creation and two annihilation).

**Coupled Cluster Singles and Doubles:**
Coupled Cluster (CC) methods are *variational in principle* but *not variational in practice*.
This is a subtle distinction that is explained reasonably well in [this Stack Exchange answer](https://chemistry.stackexchange.com/a/99236). Briefly put, the idea of CC methods is to assume that the solution to the Schrödinger equation takes the form of the exponential of a "cluster" operator as applied to some given state (say, the HF solution). A cluster operator is some linear combination of all *N*-particle (*N*=1,2,...) creation/annihilation operators with coefficients determined by the ansatz. Eventually *N* exceeds the number of electrons present in the system and so the exponential function evaluates to a polynomial of creation/annihilation operator terms, and the method is variational if the full exponential operator is considered. If restricting to singles and doubles as we do here, CCSD would be variational for H<sub>2</sub>, which only has two electrons, but not for Li<sub>2</sub>, which has six.

**Reasons to use non-variational techniques:**
A very nice discussion appears in [this online textbook](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Book%3A_Quantum_Mechanics__in_Chemistry_(Simons_and_Nichols)/19%3A_Multi-Determinant_Wavefunctions/19.03%3A_Strengths_and_Weaknesses_of_Various_Methods).
To summarise, variational methods lack *size-extensivity*, meaning that the energy of the solution cannot be trusted to scale correctly with the size of the system—"For example, a calculation performed on
two CH<sub>3</sub> species at large separation may not yield an energy equal to twice the energy obtained
by performing the same kind of calculation on a single CH<sub>3</sub> species."
This weakness precludes the use of variational methods for material simulation, as such approaches
would simulate a small piece of the material and then extrapolate to large-scale behaviour.


## Further Challenges:
* How to obtain excited electronic states of the same or different symmetry?
* Partitioning in the fermionic operator space.
* Applying unitary transformations on the Hamiltonian.
* Compress larger basis sets into smaller number of qubits.

## Business Application

For more details refer to the [Business Application found here](./Business_Application.md)
