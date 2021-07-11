![CDL 2021 cohort Project](../figures/CDL_logo.jpg)

# Quantum Cohort Project Business Application
- - -
##**_Week 1: Simulating quantum advantage with trapped ions_**
###Author: QuNova Computing, Inc.
- - -



## Step 1: Explain the technical problem you solved in this exercise

In this exercise, we created a random matrix product state (MPS) on a classical computer
and investigated several aspects by applying errors on the state.
We now explain what we have done.

###Task 1
We first produce a random MPS by using the modified _script run_random_circuit.jl_.
We take the number of qubits is four, and the depth equals 512.
After measuring the state in the computational basis multiple times,
we can estimate the probability that each bit string is obtained as a measurement result.
The following speckle pattern is our result when we take 1000 shots.
In the figure, the circles represent 0000, 0001, ..., 1111, respectively, from the left.
The radius of each circle is proportional to the probability of the corresponding bit string.

![CDL 2021 cohort Project](../figures/Fig.2-1.png)

###Task 2
In Task 2, we run the circuit we used to create the state in Task 1 many times, 
but we add a single bit flip error in a random place each time.
Our result is shown in the speckle pattern below.
As we can see, the average probabilities are nearly equal.
This result implies that the circuit is susceptible to slight perturbations.
We can achieve the same result with any other random circuit selection.

![CDL 2021 cohort Project](../figures/Fig.2-2.png)

###Task 3
It is known that the distribution of the probabilities for a fixed output bit-string converges 
to the "Porter-Thomas distribution" as the depth of the random circuits is increased.
We show this by plotting a graph as shown below.
We choose eight qubits, and the fixed bit string is 00000111.
Empirical cumulative distribution functions for depths 1, 2, 10, 30, and 512 are shown in the graph.

![CDL 2021 cohort Project](../figures/Fig.3.png)

###Task 4
As the final main task, we compute the linear XEB fidelity. 
If a quantum circuit is not perfectly implemented as in NISQ, 
it could affect the distribution of the probabilities of the bit string. 
This fidelity can be used to check the change in the probability distribution.
We investigate the change in the fidelity 
by selecting one circuit and 
changing the angle that determines the 2-qubit gate composing the circuit little by little.
In the graph below, the number of qubits is 15, and the depth is 1024.
As we can see from the graph, even a tiny change in angle can make a big difference in the fidelity.
In other words, a quantum computer should implement random circuits almost perfectly 
to achieve sufficiently high fidelity.

![CDL 2021 cohort Project](../figures/Fig.4.png)

###Additional Challenges
We did two additional challenges, and the results can be found at the following links.

_Additional challenge 1_
https://github.com/QuNovaComputing/CohortProject_2021/tree/week1/Week1_Trapped_Ions/animation_taskA1

_Additional challenge 2_
https://github.com/QuNovaComputing/CohortProject_2021/blob/week1/Week1_Trapped_Ions/TaskA2.ipynb

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

Several quantum sampling problems can be used to demonstrate the supremacy of quantum computers.
Companies that develop quantum computers would try to solve sampling problems through their computers 
to prove that their quantum computers can provide quantum advantages. 
They need a tool that can numerically check the performance of their computers,
and the linear XEB fidelity could be that tool.
Because, as seen from the above results, its value significantly changes even with tiny errors.

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Companies that want to develop quantum computers can be potential customers. 
If we create a tool that can readily check the performance of their computers using the linear XEB fidelity, 
the companies would feel that our tool is worth paying for.
Companies that are not familiar with quantum computers but want to use quantum benefits would also think our tools necessary.
It may be important to show results numerically rather than verbose explanations.

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language