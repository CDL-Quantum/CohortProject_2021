![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 1: Quantum Advantage with Trapped Ions 

This project will guide you through the recent Google quantum supremacy result, and its possible implementation using near-term quantum computers built with trapped ions.

## Solutions

All solution in Julia can be found in [this notebook](./solution_julia.ipynb). We've also created an analogous [notebook](./solutions_python.ipynb) in python in for those who are more familiar the language.

### Task 1: Plot the probability of each bit string for various circuit widths and depths

We implemented the rotation gates and sampled the outputs from the quantum circuit to obtain a random distribution of bit string probabilities. In the Julia implementation, we chose to test combinations of 4, 8, 12 qubits with varying depths of 1, 256 and 512 gates. We generated speckle patterns of each combination which is shown here in the following figure. *Note: these speckle patterns are normalized.*

![Task 1: Speckle Patterns](./img/task-1-speckle-patterns.svg)

## Bonus Task 1: Investegating Entaglement Entropy with MPS index





### Task 2: Adding random bit flip errors

We modified the circuits in the notebooks to randomly generate bit flip errors. We demonstrate that this substantially changes the probability distributions by plotting the speckle patterns for 9 different iterations. This yields completely random distributions which is shown in the following animation:

![Speckle pattern probabilities animation](../Week1_Trapped_Ions/img/speckle.gif)

We demonstrate the same animation in a single figure shown here:

![Speckle pattern probabilities](../Week1_Trapped_Ions/img/task-2-speckle-pattern-subplots.svg)

We also show another set as a collection of line graphs:

![Line grap probabilities](../Week1_Trapped_Ions/img/task-2-probs-line-graph.svg)

And checkout out this heatmap displaying the random probabilities:

![Heatmap](../Week1_Trapped_Ions/tutorial_heatmap_anim.gif)

### Task 3: Convergence of the Emprical CDF of P(x) (probability distribution for each state PSI can take)





### Task 4: Studying the Linear Fidelity








### Bonus: Implement the circuit on a real trapped ion computer

We implemented the random circuit on the IonQ trapped ion computer by connecting to their API. We built a sweet NodeJs repository to be able to so with simple commands via the command line. Checkout the repo's [README](./ionq-implementation/README.md) for more information. 

We could choose to implement the circuit on their quantum machine or a simulator. So we did both. Unfortunately, the results from the quantum machine was not very precise and only gave us up to 3 decimal places in precision (we are on the free plan), so the plots may be a little crude. 

Here are the probability distributions for an 8 qubit system on a 512 deep circuit on the trapped ion machine:

![QPU Probabilities](../Week1_Trapped_Ions/img/qpu-histo-deep.png)

Next we tried to replicate the analysis in task 3 by showing that the cumulative distribution function of p would tend to the Porter-Thomas (exponential) distribution. Recall though, that the low precision of the free tier yielded very choppy graphs:

![QPU CDF](../Week1_Trapped_Ions/img/qpu-cdf-deep.png)

Compared to the true Porter-Thomas (exponential) distribution: 

![QPU True CDF](../Week1_Trapped_Ions/img/qpu-true-cdf-deep.png)

Due to the coarseness of the predictions, we tried the simulator with a higher precision of 9 decimal places. To replicate the work in task 3, we first tried a circuit of depth 1 as shown here: 

![Simulator depth 1 CDF](../Week1_Trapped_Ions/img/simulator-cdf-shallow.png)

And by increasing the depth we achieved a very similar CDF to the Porter-Thomas distribution: 

![Simulator depth 1 CDF](../Week1_Trapped_Ions/img/simulator-cdf-deep.png)

Which can be compared to the true Porter-Thomas distribution shown here:

![QPU CDF](../Week1_Trapped_Ions/img/simulator-true-cdf-deep.png)


## Business Application

For more details refer to the [Business Application found here](./Business_Application.md)

## References
