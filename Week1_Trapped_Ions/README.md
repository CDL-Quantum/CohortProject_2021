
![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)


## Project 1: Quantum Advantage with Trapped Ions 

------

### Introduction

Simulating matter at the quantum level is a difficult task to do on conventional computers. As the size of the system increases, exponential resources in both memory and time are required. This led Richard Feynman in 1982, one of the most brilliant physicists of the century, to suggest that such simulations should be performed on a computer that runs natively in the quantum domain. The field of quantum computing was born.

Decades later, his prophecy came true, though not completely, with the advent of quantum computers built by various big tech companies. John Preskill coined them Noisy Intermediate-Scale Quantum (NISQ) devices. Despite their noise, NISQ devices have been shown to have a quantum advantage. In this project we will guide you through the recent Google quantum supremacy result, and its possible implementation using near-term quantum computers built with trapped ions.

------

### CDL Project Instructions

Open up [instructions.pdf](https://github.com/CDL-Quantum/CohortProject_2021/tree/main/Week1_Trapped_Ions/instructions.pdf) to begin learning about your tasks for this week!

Please edit this markdown file directly with links to your completed tasks and challenges.  

#### Task List
* Simulating a random circuit with a Matrix Product State code, and producing a speckle pattern.
* Adding a single bit-flip error and exploring the change in the speckle pattern.
* Exploring convergence of the Porter-Thomas Distribution.
* Exploring the effect of 2-qubit gate errors.
* Describe a business that could be build around random circuits.  (See below Business Application)

#### Further Challenges
* Animate your speckle pattern.
* Reproduce the Google cross entropy results.
* Implement this circuit on a real trapped ion computer!


#### Business Application
For each week, your team is asked to complete a Business Application. Questions you will be asked are:

* Explain to a layperson the technical problem you solved in this exercise.
* Explain or provide examples of the types of real-world problems this solution can solve.
* Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved.
* Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language.

For more details refer to the [Business Application found here](./Business_Application.md)

------

### Team Contributions

This project  folder contains contributions from CDL Cohort Team 3 members: Oleg Fonarev, Estelle Inack, Alex Khan, Ziwei Qiu, Yuval Sanders. 

- The [first Jupyter notebook](run_random_circuit_ZQ.ipynb) contains classical simulations using Julia language (Tasks 1-4 and Additional Challenges 1,2). You will also find a "Polock art" piece at the end of the notebook.  Please see [instructions](setup.md) for setting up your local environment with required prerequisites for running this Notebook.
- The [second Jupyter notebook](run_random_circuit_braket_ionq_ak.ipynb) contains Amazon bracket code that was executed on IonQ's IonTrap (Additional Challenge 3)
- Our proposed Business Application can be found [here](Business_Application.pdf)
- The [video](Business_presentation_AK.mp4) and the [executive summary](Presentation.pdf) summarize our business proposal for potential customers

