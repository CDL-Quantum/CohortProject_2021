![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 3: VQE: Constructing potential energy surfaces for small molecules

#### Alex Khan, Dr. Maninder Kaur, Ritaban Chowdhury, Theo Cleland, Yuval Sanders

Here we provide our work on project 3. 

- Our Business Application is [here](./Business_Application.md).
- Our video introduction is [here](https://drive.google.com/file/d/1EHxNry_KGci-1Ssjv0kMTpVQdF3DyLml/view?usp=sharing).
- Code execution using Tequila for H<sub>2</sub> is in [here](./Ritaban%20Code/H2).
- Code execution using Tequila for LiH is in [here](./Ritaban%20Code/LiH).

Below we answer the various questions found in [the instructions](https://github.com/CDL-Quantum/CohortProject_2021/tree/main/Week3_VQE/Instructions.pdf).

## Step \#1: Generating PES using classical methods

We were asked to investigate the relative quality of three approximation methods:
Hartree-Fock (HF),
Configuration Interaction Singles and Doubles (CISD), and
Coupled Cluster Singles and Doubles (CCSD).
The quality of these approximations were assessed relative to the answer obtained numerically via the
Full Configuration Interaction (FCI) representation.

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

## Step \#2: Generating the qubit Hamiltonian

### Question 1

> What are the requirements for a function of qubit operators to be a valid mapping for the fermionic operators?

We need the mapping of fermionic operators to preserve the algebraic relations between fermionic operators (i.e. it needs to be the proper kind of algebra homomorphism).
I ([Yuval](http://ysanders.github.io)) have yet to find a good reference explaining this point of view, but my suspicion is that the function should be a Grassman algebra homomorphism ([nLab](https://ncatlab.org/nlab/show/Fock+space) makes the point that this is the mathematician's name for fermionic Fock space).

In practice, the condition to check is that the *canonical commutation relations* for the fermionic mode operators hold.
The other mathematical machinery of whatever homomorphism seems usually to be implied. [Michael Nielsen](https://michaelnielsen.org/blog/archive/notes/fermions_and_jordan_wigner.pdf) wrote a useful note on enforcing these canonical commutation relations for the Jordan-Wigner transformation,
which leads to the well-known irritation that the qubit creation/annihilation operators are highly non-local—see Eq. (31) in Nielsen's note and the discussion around Eq. (5) in [this paper](https://doi.org/10.1021/acs.jctc.8b00450). In particular, Sec. II.B of Nielsen's note gives a detailed list of mathematical relations that need to be enforced.

### Question 2

> The electronic Hamiltonian is real (due to time-reversal symmetry), what consequences does that have on the terms in the qubit Hamiltonian after the Jordan-Wigner transformation?

I ([Yuval](http://ysanders.github.io)) am not sure what a *complete* answer to this question would look like. However, the most obvious consequence seems to be that a Hamiltonian containing only nearest neighbour two-qubit terms could not
contain cross-terms, i.e. of the form *X<sub>j</sub> Y<sub>j±1</sub>*.
See discussion before Eq. (35) in Nielsen's note cited above.
Sorry, I didn't really have time to do this question justice.

### Question 3

> *Optional:* What are the cons and pros of the Bravyi-Kitaev transformation compared to the Jordan-Wigner transformations?

[This paper](https://doi.org/10.1021/acs.jctc.8b00450) gives a detailed comparison, though its conclusions are of the "more research is needed" type. In principle, Bravyi-Kitaev should be generally superior to Jordan-Wigner because Bravyi-Kitaev avoids the need for highly non-local fermionic creation/annihilation operators.
However, the paper points out that this advantage of Bravyi-Kitaev can be accomplished with clever orderings for Trotter-Suzuki expansions of the time-evolution operator, and that these optimised Jordan-Wigner circuits seem to have shorter depth in some cases than the Bravyi-Kitaev circuits.
Because this depends on numerical details of the Hamiltonian to be simulated, the point is well made that the tradeoff needs to be numerically investigated in practical circumstances.

## Step \#3: Unitary transformations

### Question 1

> Standard Hamiltonian symmetries are
i) number of electrons N<sub>e</sub> = Σ <sub>k</sub> a<sub>k</sub><sup>†</sup> a<sub>k</sub>,
ii) electron spin S<sup>2</sup>,
iii) electron spin projection S<sub>z</sub>,
iv) time-reversal symmetry, and
v) point-group symmetry for symmetric molecules.
Which of these symmetries are conserved in a) UCC and b) QCC?

I ([Yuval](http://ysanders.github.io)) simply do not have enough background
in theoretical chemistry to do the calculation necessary, though I might be able to
if I had an extra few days for this. Oh well. But I did watch one of
[Artur Izmaylov's videos](https://youtu.be/sYJ5Ib-8k_8?t=810) on coupled cluster
methods and it seems to me that all the symmetries would be conserved, which is why
it is even possible to control the "algebraic explosion" by making such symmetries
explicit.

I did have a nice but brief conversation with [Lukas Konecny](https://scholar.google.com/citations?user=sxKTPdQAAAAJ&hl=en),
who repeatedly and emphatically stressed to me that he knows very little about coupled cluster methods and works mostly on DFT approaches to relativistic systems.
He had the intuition that all five symmetries should be preserved simply because we are dealing with a non-relativistic Hamiltonian and hence there would be no physical processes breaking any of these symmetries. I thought that was a good argument, so I'm
"borrowing" it so that I don't have to figure out what calculation to do to back up what I'm saying (much less actually do that calculation).

As for qubit coupled cluster, I spent about an hour reading [this paper](https://doi.org/10.1021/acs.jctc.8b00932) (or, more accurately, [the arXiv version](https://arxiv.org/abs/1809.03827)) but I think I don't have enough background in theoretical chemistry to be able to come up with a good answer.
[From this video](https://youtu.be/981jc3Xdgvc?t=890), it seems like all five symmetries can be broken, though.

Sorry. I really appreciate how good the assignment is and I wish I had more time to do it justice.

### Question 3

> What are the ways to restore symmetries if your unitary transformation break them?

We can do what Artur calls [symmetry projection](https://www.youtube.com/watch?v=mhlgldoCfx4). 