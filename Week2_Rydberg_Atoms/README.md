![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 2: Optimization problems \& Rydberg atom arrays

Team 8 Alex Khan, Theo Cleland, Henry Makhanov, Ehsan Torabizadeh, Darshit Mehta

In this project we are going to demonstrate the amazing power of classical and quantum annealers. Throughout a series of tasks we will demonstrate the existing annealing techniques to solving a variety of problems. Crucially, we will show a solution to the unit-disk maximum independent set (UD-MIS) problem using both a simulated classical annealer with different schedules and a quantum annealer. For the third task, we have also solved the Gotham City Cell Tower problem using both classical annealer and quantum annealer. Finally, we have mapped a real-world protein redundancy problem to the UD-MIS problem and found very promising results that will serve as a founding block for our business proposal. 

### Table of Contents  
1. [Simulating the UD-MIS Problem Using Classical Simulated Annealing](#toc1)
2. [Finding a Better Annealing Schedule](#toc2)
3. [Simulating the Same Problem but Using Quantum Annealing](#toc3)
4. [Comparing the Classical and Quantum Methods](#toc4)
5. [Gotham City Problem](#toc5)
6. [Finding Non-Redundant Protein Sequences](#toc6)

### Resources
- [Notebook for task 1](./Task%201.ipynb)
- [Notebook for task 2](./Task%202.ipynb)
- [Notebook for task 3 (Gotham city) + running on real quantum hardware](./Task%203,%20Additional-Challenges%20b,%20d-ak.ipynb)
- [Notebook for extra challenge: Finding the least redundant set of protein sequences](./real_world_protein_redundancy.ipynb)

This project will guide you through using the foundations of quantum hardware to demonstrate a quantum advantage in real-world problems.

<a name="toc1"></a>

## Task 1
## Simulating the UD-MIS Problem Using Classical Simulated Annealing

Please view [this notebook](./Task%201.ipynb) for the code used to solve this section. 

We simulate the UD-MIS using classical simulated annealing for the following abstract graph (truncated to 2 decimal places). Edges are created whenever a node is closer than a unit distance of 1.

|Table Representation of Graph | Visual Representation of Graph|
| :--------------: | :---------: 
| <table>   <thead>   <tr> <th>X Coordinate</th>  <th>Y Coordinate</th>  </tr>   </thead>   <tbody>   <tr>  <td>0.35</td>  <td>1.50</td> </tr> <tr>  <td>0.63</td>  <td>2.58</td> </tr> <tr>  <td>1.39</td>  <td>2.16</td> </tr> <tr>  <td>0.66</td>  <td>0.67</td> </tr> <tr>  <td>0.87</td>  <td>3.39</td> </tr> <tr>  <td>1.16</td>  <td>1.08</td> </tr> </tbody> </table> | ![Unsolved Graph](./resources/task1-graph-fixed.png)

Next we simulate annealing to solve the ground state of the following Hamiltonian:

![Hamiltonian Equation](https://latex.codecogs.com/gif.latex?H%20%3D%20-%5Csum_%7Bi%20%5Cin%20V%7D%20n_i%20&plus;%20u%20%5Csum_%7Bi%2Cj%20%5Cin%20E%7D%20n_i%20n_j)

With the following annealing schedule: 

![Annealing Schedule](https://latex.codecogs.com/gif.latex?T_i%20*%20%28T_f/T_i%29%5E%7Bt/N%7D)

We find a ground state energy level of `-3` after about 4000 iterations. We plot in the following corresponding occupations in green which yield the ground state:

![Solved Graph](./resources/task1-graph-solution-fixed.png)



<a name="toc2"></a>

## Finding a Better Annealing Schedule

Please view [this notebook](./Task%201.ipynb) for the code used to solve this section. 

We test 3 different annealing temperatures summarized by the following table (left) and visualized in the follow plot (right): 

| Table of Different Annealing Schedules | Plots of Each Annealing Schedule |
| :--------------: | :---------: 
| <table>   <thead>    <tr> <th>Annealing Schedule</th>  <th>Name</th>  </tr>    </thead>   <tbody>    <tr>  <td>![Annealing Schedule](https://latex.codecogs.com/gif.latex?T_i%20*%20%28T_f/T_i%29%5E%7Bt/N%7D)</td>  <td>exponential ~x (benchmark)</td> </tr>  <tr>  <td>![Annealing Schedule 2](https://latex.codecogs.com/gif.latex?T_i%20*%20%28T_f/T_i%29%5E%7B2t/N%7D)</td>  <td>exponential ~2x</td> </tr>  <tr>  <td>![Annealing Schedule 3](https://latex.codecogs.com/gif.latex?T_i%20*%20%28T_f/T_i%29%5E%7B4t/N%7D)</td>  <td>exponential ~4x</td> </tr>  </tbody> </table> | ![Visualization of Annealing Schedules](./resources/visualization-of-annealing-schedules.png) |

To test the speed of convergence, we consider a "stable" solution one where the energy has not changed after 100 iterations. After simulating the annealing for each schedule, we plot the energy versus the number iterations in the following table:

![Annealing Schedule Comparison](./resources/task1-annealing-comparison.png)

We see clearly that the `exponential ~4x` schedule converges the fastest, and is more than 3x faster than the benchmark provided in the sample code. These results are further summarized in the following table:

| Annealing Schedule   | Iterations to Stable Solution | Time to Stable Solution (seconds) | 
| :------------- | :----------: | :----------: |
| ![Annealing Schedule](https://latex.codecogs.com/gif.latex?T_i%20*%20%28T_f/T_i%29%5E%7Bt/N%7D) | 3676 | 0.61 |
| ![Annealing Schedule 2](https://latex.codecogs.com/gif.latex?T_i%20*%20%28T_f/T_i%29%5E%7B2t/N%7D)  | 2007 | 0.34 |
| ![Annealing Schedule 3](https://latex.codecogs.com/gif.latex?T_i%20*%20%28T_f/T_i%29%5E%7B4t/N%7D)  | 1044 | 0.17 |



<a name="toc3"></a>

## Task 2
## Simulating the Same Problem but Using Quantum Annealing

Please view [this notebook](./Task%202.ipynb) for the code used to solve this section. 

We simulate the UD-MIS using simulated quantum annealing for the following abstract graph (truncated to 2 decimal places). Edges are created whenever a node is closer than a unit distance of 1.This graph will look a bit different from the one used in the previous section because we are using a different programming language ([Julia](https://julialang.org/)) and because we use a different plotting package([GraphPlots.jl](https://juliagraphs.org/GraphPlot.jl/)). 


|Table Representation of Graph | Visual Representation of Graph|
| :--------------: | :---------: 
| <table>   <thead>   <tr> <th>X Coordinate</th>  <th>Y Coordinate</th>  </tr>   </thead>   <tbody>   <tr>  <td>0.35</td>  <td>1.50</td> </tr> <tr>  <td>0.63</td>  <td>2.58</td> </tr> <tr>  <td>1.39</td>  <td>2.16</td> </tr> <tr>  <td>0.66</td>  <td>0.67</td> </tr> <tr>  <td>0.87</td>  <td>3.39</td> </tr> <tr>  <td>1.16</td>  <td>1.08</td> </tr> </tbody> </table> | <img src="./resources/task2_top5/yellow.png" width="300">

In the instructions we were tasked with applying quantum annealing to solve the UD-MIS problem. Our approach will be different from the classical annealing as we will be considering a time-dependent Hamiltonian:

![Time-dependent Hamiltonian](https://latex.codecogs.com/gif.latex?%5Chat%7BH%7D%28t%29%20%3D%20%5COmega%28t%29%20%5Csum_%7Bi%20%5Cin%20V%7D%20%5Chat%7B%5Csigma%7D_i%5Ex%20-%20%5Cdelta%28t%29%20%5Csum_%7Bi%20%5Cin%20V%7D%20%5Chat%7Bn%7D_i%20&plus;%20u%20%5Csum_%7Bi%2Cj%20%5Cin%20E%7D%20%5Chat%7Bn%7D_i%20%5Chat%7Bn%7D_j)

Mathematically and algorithmically, Quantum Annealing looks like the following

![Quantum Annealing 1](https://latex.codecogs.com/gif.latex?%7C%5Cpsi%20%28t%29%3E%20%3D%20U%28t%29%20U%28t%20-%20%5Cdelta%20t%29%5Ccdots%20U%28t_0%20&plus;%20%5Cdelta%20t%29%20U%28t_0%29%7C%5Cpsi%20%28t%20%3D%20t_0%29%3E)

where ![U(t)](https://latex.codecogs.com/gif.latex?U%28t%29) is the time-evolution operator

![Quantum Annealing 2](https://latex.codecogs.com/gif.latex?U%28t%29%20%3D%20%5Cexp%28-%5Cfrac%7Bi%7D%7B%5Chbar%7D%20%5Cdelta%20t%20%5Chat%7BH%7D%28t%29%29)

We can see the top five solutions and their frequency on the following graph. Additonally you can look at the [file with all the available solutions](./task2_data.dat)

We can see that simulated quantum annealing found several suitable solutions. Most notably, the top 3 solutions are very close to each other. We have made the corresponding frequency distribution and graph that maps the top 5 solutions:
|Solutions | Solutions on the Graph|
| :--------------: | :---------: 
| <table>   <thead>   <tr> <th>Solution</th>  <th>Frequency</th>  </tr>   </thead>   <tbody> <tr>  <td>010101</td>  <td>28581</td> </tr> <tr>  <td>011100</td>  <td>28457</td> </tr> <tr>  <td>110100</td>  <td>28204</td> </tr> <tr>  <td>111100</td>  <td>3052</td> </tr> <tr>  <td>011101</td>  <td>2953</td> </tr>  </tbody> </table> | <img src="./resources/task2_top5.gif" width="300">

Additionally we have run the simulated quantum annealer on a more complicated graph with 11 nodes, where top 5 solutions are much more evenly distributed. We suspect it was due to inherently different structure of the graphs.
|Solutions | Solutions on the Graph|
| :--------------: | :---------: 
| <table>   <thead>   <tr> <th>Solution</th>  <th>Frequency</th>  </tr>   </thead>   <tbody>   <tr>  <td>01111001100</td>  <td>6827</td> </tr> <tr>  <td>11011011000</td>  <td>6774</td> </tr> <tr>  <td>01111011000</td>  <td>6713</td> </tr> <tr>  <td>11011001100</td>  <td>6709</td> </tr> <tr>  <td>11011001001</td>  <td>6682</td> </tr></tbody> </table> | <img src="./resources/task2_compl_graph/compl_graph.gif" width="300">

Simulated quantum annealing presents a promising option for solving the UD-MIS problem, but perhaps it would be more interesting how will the real quantum hardware perform.

<a name="toc4"></a>

## Comparing the Classical and Quantum Methods

Please view [this notebook](./benchmarking_quantum.ipynb) for the code used to solve this section. 

We will be comparing classical and quantum solutions to the UD-MIS problem. D-Wave will be our quantum hardware of choice for this task. Our experiment will consist of running UD-MIS algorithm until there is no change in energy, during our experiments we found that this occurs after roughly 300 steps. For our experiments we tried different size graphs of the UD-MIS formulation and also tracked the lowest energy found with both the classical UD-MIS solver and the D-Wave quantum annealer. We have used both D-Wave 2000Q and D-Wave Advantage in our comparison to classical annealing. With D-Wave 2000Q we were only able to go up to a maximum node size of 70, and in the case of D-Wave Advantage we have increased the number of nodes to 100.

Through experimentation we determined that these were the optimal parameters:

`chain_strength = number_of_nodes / 5`

`annealing_time = number_of_nodes * 7`

`number_of_runs = number_of_nodes * 10`

Here are the results of our time to execute experiment:

|D-Wave 2000Q vs Classical | D-Wave Advantage vs Classical|
| :--------------: | :---------: 
| <img src="./resources/dwave2000q_vs_classical_time.png" width="300"> | <img src="./resources/dwaveadvantage_vs_classical_time.png" width="300">

Here are the results of our lowest energy experiment:

|D-Wave 2000Q vs Classical | D-Wave Advantage vs Classical|
| :--------------: | :---------: 
| <img src="./resources/dwave2000q_vs_classical_energy.png" width="300"> | <img src="./resources/dwaveadvantage_vs_classical_energy.png" width="300">

We can see that both D-Wave machines can't find the lowest energy solution. Despite a large amount of sampling both quantum machines found very few results in the lower values, as can be seen in the following graphs:

|40 Nodes | 100 Nodes|
| :--------------: | :---------: 
| <img src="./resources/40_nodes_sampling.png" width="300"> | <img src="./resources/advantage_energy_sampling.png" width="300">

While it is true that current quantum machines fail to find the solutions with the lowest value, we can clearly see that they perform much faster than classical methods. We expect that with general quantum hardware improvements, quantum methods will become better at finding the lowest energy solutions for the UD-MIS problem, whilst keeping their speed advantage. 

<a name="toc5"></a>
## Task 3
## Gotham City Problem

This work was generated from [this notebook](./Task%203,%20Additional-Challenges%20b,%20d-ak.ipynb). The goal was to map the UD-MIS problem to a real world problem relating to finding optimal placements for cell phone towers in the city of Gotham.

We are given the follow nodes representing the potential position of cell phone towers in Gotham (edges in the graph represent towers whose signals overlap):

|Table Representation of Graph | Visual Representation of Graph|
| :--------------: | :---------: 
| <table>   <thead>   <tr> <th>X Coordinate</th>  <th>Y Coordinate</th>  </tr>   </thead>   <tbody>    <tr>  <td>1.19</td>  <td>4.25</td> </tr>  <tr>  <td>2.71</td>  <td>3.48</td> </tr>  <tr>  <td>1.19</td>  <td>3.51</td> </tr>  <tr>  <td>2.00</td>  <td>3.38</td> </tr>  <tr>  <td>1.12</td>  <td>2.86</td> </tr>  <tr>  <td>1.70</td>  <td>2.42</td> </tr>  <tr>  <td>2.36</td>  <td>2.54</td> </tr>  <tr>  <td>1.52</td>  <td>1.48</td> </tr>  <tr>  <td>2.15</td>  <td>1.54</td> </tr>  <tr>  <td>2.14</td>  <td>1.87</td> </tr>  <tr>  <td>1.72</td>  <td>0.86</td> </tr>  <tr>  <td>2.29</td>  <td>0.87</td> </tr>  </tbody> </table> | ![Gotham Nodes](./resources/gotham-nodes.png)

Our goal is to optimize the cell locations of each tower to best cover Gotham City, while only purchasing the required number of towers such that the tower signals do not overlap and as much of Gotham City is within signal range. 

### Why can this problem be mapped easily to the UD-MIS problem?

The requirements of the problem to maximize the tower coverage (use as many nodes as possible) and that the signal range not overlap (penalize node pairs with some condition) fits the UD-MIS formulation:

![Hamiltonian Equation](https://latex.codecogs.com/gif.latex?H%20%3D%20-%5Csum_%7Bi%20%5Cin%20V%7D%20n_i%20&plus;%20u%20%5Csum_%7Bi%2Cj%20%5Cin%20E%7D%20n_i%20n_j)

### Solve Gotham City's Problem

We solve this problem in four ways using a simulated classical annealing approach, a quantum annealing algorithm as well as on real quantum hardware using Microsoft QIO and D-Wave.

#### Simulated Classical Annealing

Running the algorithm on a simulated classical annealing algorithm yields a lowest energy level of -5. This ground state has 5 nodes (indicated in green). We reached convergance after about 3700 iterations using the default cooling schedule ![Annealing Schedule](https://latex.codecogs.com/gif.latex?T_i%20*%20%28T_f/T_i%29%5E%7Bt/N%7D). We plot one solution in the figure below, where the green nodes indicate cell phone towers and the yellow nodes are potential locations that are not ideal:

![Graph with Solution](./resources/image%20b21.png)

#### Simulated Quantum Annealing

We have used a time-dependent Hamiltonian to reach the ground state. We have placed the coordinates into the quantum annealer, run for `100000 nshots`  and got the following solutions:

|Gotham Solutions | Gotham Solutions Graph|
| :--------------: | :---------: 
| <table>   <thead>   <tr> <th>Solution</th>  <th>Frequency</th>  </tr>   </thead>   <tbody> <tr>  <td>100001010011</td>  <td>17686</td> </tr> <tr>  <td>010001010011</td>  <td>17443</td> </tr> <tr>  <td>101000010011</td>  <td>12414</td> </tr> <tr>  <td>011000010011</td>  <td>12403</td> </tr> <tr>  <td>000011010011</td>  <td>9648</td> </tr>  </tbody> </table> | <img src="./resources/quantum_gotham/quantum_gotham.gif" width="300">

#### Real Quantum Hardware: Microsoft QIO

Repeated runs on Microsoft QIO gave the same answer as the simulated quantum annealing approach.

This solver (similar to most simulated annealing solvers) seems to give only one answer. It did not appear to be probabilistic and so, we did not see the value in proceeding any further with this algorithm.

#### Real Quantum Hardware: D-Wave

We also solve this problem on real quantum hardware using D-Wave. Here, we found multiple potential solutions with the same lowest energy of -5. We display the top potential solutions found in the left, along with an awesome GIF displaying some of them on the right (green nodes are occupied, edges represent signals that overlap).

| D-Wave Solutions for Gotham Problem | GIF of the Multiple Best Solutions Found |
| :--------------: | :---------: |
| <img src="./resources/image%20b22.png" alt="drawing" width="340"/> | ![Gotham Dwave energy solutions](./resources/Gotham%20Solutions%201.gif) |

However, one of Bruce's conditions is that the signals **must not** overlap. Therefore, we must exclude some of the ground states because they overlap (indicated by green nodes with connected edges). With this in mind, we show three non-overlapping solutions for breivity:

||||
| :--------------: | :---------: | :---------: |
|![Solution 1](./resources/image%20b21.png) | ![Solution 2](./resources/graph1-2.png) | ![Solution 3](./resources/graph1-1.png)|

We also show the graph representation of the problem in D-Wave (left), the actual embedding on D-Wave 2000Q (middle) along with the energies sampled from Dwave (right).

| Graph Representation on D-Wave | Embeddings on D-Wave | Energies Sampled on D-Wave |
| :--------------: | :---------: |  :---------: |
| ![D-Wave Graph](./resources/image%20b41.png) | ![D-Wave Embeddings](./resources/image%20b42.png) | ![D-Wave Energy Samples](.//resources/image%20b43.png) |

### Should Bruce pay for a few more cell towers?

It depends on if Bruce can tolerate some overlap between the tower signals. 
- If Bruce insists that there cannot be any signal overlap: he **should not** purchase more towers. 
- If Bruce can tolerate some overlap: he **should** purchase more towers. 

Let's examine this in more detail...

For the case where Bruce can not afford any signal overlap, we already found a handful of optimal solutions with 5 towers and a ground state energy of -5. These are shown again here for convenience. We notice that no two green node is connected - indicating no overlap.

||||
| :--------------: | :---------: | :---------: |
|![Solution 1](./resources/image%20b21.png) | ![Solution 2](./resources/graph1-2.png) | ![Solution 3](./resources/graph1-1.png)|

However, if Bruce allowed some overlap, he should purchase an extra tower (total of 6 towers). We found a handful of ground states (energy -5) with 6 occupied nodes. These states indicate some of the best coverage with a little bit of signal overlap. We believe that the trade off between overlap and city-wide coverage is worth it, and insist that Bruce purchase the extra tower! We display some of these solutions below:

||||
| :--------------: | :---------: | :---------: |
|![Solution 1](./resources/graph3-1.png) | ![Solution 2](./resources/graph3-2.png) | ![Solution 3](./resources/graph3-3.png)|

We could push this even further. If Bruce would consider even a little bit more overlap, he could purchase a second tower (for a total of 7 towers!). We justify this descision because we found 2 ground state solutions with 7 nodes! With this combination, he will be covering the most amount of Gotham - the only tradeoff is that he will have to make peace with a little bit more overlap. We display the solutions below: 

|||
| :--------------: | :---------: |
|![Solution 1](./resources/graph-7nodes-1.png) | ![Solution 2](./resources/graph-7nodes-2.png) |

The only issue with the above solution is that it does not determine which of the solutions for either the 6 towers of 7 towers solution is the best. This is due to the formulation of the UD-MIS problem which basically "bins" the amount of overlap between two nodes into a simple "yes" or "no". For example, two nodes that are 0.99 units away will be penalized in the same way as two nodes that are 0.1 units away. To solve this after the fact is trivial, we simply need to compute the amount of overlap between the solution set and determine the solution that minimizes it. However, we try to re-formulate the problem in such a way where that comes out naturally.

#### New Formulation of the Problem

**Note: Unfortunately, we could not find the proper solution with our new formulation. We warn the reader that this solution is not correct - but it is still fun nonetheless!**

The UD-MIS formulation where the range overlap is descretized does not give solutions that would indicate the optimum solution since a large overlap and a small overlap both have the same penalty (higher energy of +1).

Thus a modified solution is found with a different solver (D-Wave) which uses the equation:

![Modified Hamiltonian](https://latex.codecogs.com/gif.latex?f%28x%29%20%3D%20%5Csum_%7Bi%7D%20%7BQ_%7Bi%2Ci%7D%7D%7Bx_i%7D%20&plus;%20%5Csum_%7Bi%3Cj%7D%20%7BQ_%7Bi%2Cj%7D%7D%7Bx_i%7D%7Bx_j%7D)

Where ![Modified Distance](https://latex.codecogs.com/gif.latex?Q_%7Bi%2Cj%7D%3D1/D_%7Bij%7D) and the energy of each tower is -3.

As can be seen, in this solver the coefficient ![Q Expression](https://latex.codecogs.com/gif.latex?Q_%7Bi%2Cj%7D) can be used to indicate higher penalty for higher overlap.

Using this formula and the execution below, we get the following best energy solution of -9.513712 using D-Wave. Although, note that this solution was only found 1 time with 100 samples. We notice that even with the new formulation, only 5 towers are needed. 

With this formulation, we get a sampling given by the following two figures. On the left, we show the sampling from D-Wave and on the right, a similar GIF as above displaying the various solutions.

| D-Wave Solutions for Modified Gotham Problem | GIF of the Multiple Best Solutions Found |
| :--------------: | :---------: |
| <img src="./resources/image%20b32.png" alt="drawing" width="340"/>| ![Gotham Dwave energy solutions](./resources/Gotham%20Solutions%202.gif) |

From D-Wave, we also show the resulting qubit graph (left), embedding (center) and energy spectrum (right):

| Graph Representation on D-Wave | Embeddings on D-Wave | Energies Sampled on D-Wave |
| :---------: | :---------: |  :---------: |
| ![D-Wave Embeddings](./resources/task3-2-dwave-graph.png) | ![D-Wave Embeddings](./resources/task3-2-dwave-embeddings.png) | ![D-Wave Energy Samples](./resources/task3-2-dwave-energy-spectrum.png) |

**Again, we note that the above section is not correct. We believe that we simply have the wrong hamiltonian for the problem.**

<a name="toc6"></a>

## Finding Non-Redundant Protein Sequences

We take this project one step further by solidifying our business case with a real application: finding the least redundant set of proteins from real data! See [this notebook](./real_world_protein_redundancy.ipynb) for the implementation. 

Qamino strives in finding non-redundant protein sets to enable our customers to efficiently produce drugs without having to waste time experimenting with proteins that have already been tested. We test our algorithm on data found from the [Dali Protein Structure Comparison Server](http://ekhidna.biocenter.helsinki.fi/dali/). [Our data](./protein_similarities.csv) is a matrix of the "similarity" scores between 59 different protein sequences. Here are the following protein sequences we investigate:

`1bksA,  3f2bA,  2yb1A,  3e38A,  2anuA,  3qy6A,  1v77A,  3dcpA,  3au2A, 1m65A,  2a3lA,  2qpxA,  3iacA,  1j5sA,  1itqA,  4mupB,  4dlfA,  2ffiA, 3irsA,  3cjpA,  4dziC,  2gwgA,  4ofcA,  4hk5D,  4qrnA,  2dvtA,  3gg7A, 2y1hB,  2vc5A,  2ob3A,  3k2gB,  1bf6A,  1a4mA,  2ogjA,  1a5kC,  1yrrB, 3nqbA,  2vunA,  1onxA,  3pnuA,  3giqA,  3griA,  3e74A,  4b3zD,  1gkpA, 2imrA,  3ooqA,  3icjA,  2oofA,  4c5yA,  3mtwA,  3mkvA,  4cqbA,  1k6wA, 4rdvB,  2uz9A,  2pajA,  3ls9A,  1j6pA`

To formulate this problem as a UD-MIS problem, we simply need to construct the edge matrix based on the similarity values from the [Dali Protein Structure Comparison Server](http://ekhidna.biocenter.helsinki.fi/dali/). To do so, we must choose a good threshold to consider an edge. We use the following histogram to arbitrarily determine the best threshold. We chose a threshold of 25 indicated by the red dotted line on the histogram. On the right, we show the graph created (node positions are randomly assigned).

| Histogtam of Similarity Values | Graph Visualization |
| :--------------: | :---------: |
|![Protein Similarities](./resources/protein-histogram-take2.png) | <img src="./resources/protein-case-graph.png" style="margin-bottom:55px">

We then solve the UD-MIS problem using a clasical simulated annealing schedule T_i * (T_f/T_i)^(t/N) where T_i = 100 and T_f = 0. We find a ground state for an energy level of -28. We plot the corresponding energies per iteration (left) and the graph solution in green (right) in the following figures:


| Energy Values | Graph Visualization |
| :--------------: | :---------: |
| ![Protein Energy History](./resources/protein-energy-history.png) | <img src="./resources/protein-solution-graph.png" style="margin-bottom:25px"> |

The solution set yielded from the classical simulation found 28 non-redundant proteins at a ground state energy of -28:

`1bksA, 3f2bA, 2yb1A, 3e38A, 2anuA, 3qy6A, 1v77A, 3dcpA, 3au2A, 2a3lA, 2qpxA, 3iacA, 1itqA, 2ffiA, 3irsA, 3cjpA, 4dziC, 2gwgA, 2y1hB, 2vc5A, 1a4mA, 2ogjA, 1a5kC, 1yrrB, 3pnuA, 2imrA, 3ooqA, 3icj`

#### Implementation on D-Wave

Since our company name is Qamino (standing for Quantum Amino), we needed a solution using real quantum hardware as well! Thus we tested this out using D-Wave. We were able to find the -28 energy ground state (although it was only sampled once out of 100 samples). We display graph representation of the problem in D-Wave (left), the actual embedding on D-Wave 2000Q (middle) along with the energies sampled from Dwave (right).

| Graph Representation on D-Wave | Embeddings on D-Wave | Energies Sampled on D-Wave |
| :--------------: | :---------: |  :---------: |
| ![D-Wave Graph](./resources/protein-dwave-2.png) | ![D-Wave Embeddings](./resources/protein-dwave-embeddings-2.png) | ![D-Wave Energy Samples](./resources/protein-dwave-energies-2.png) |


## References

<a name="ref1">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5835207/<a>



<br/><br/><br/><br/><br/><br/><br/>

Open up [instructions.pdf](https://github.com/CDL-Quantum/CohortProject_2021/tree/main/Week2_Rydberg_Atoms/instructions.pdf) to begin learning about your tasks for this week!

**Please edit this markdown file directly with links to your completed tasks and challenges.**

## Tasks include:
* (DONE) Simulating the unit-disk maximum independent set (UD-MIS) problem using classical simulated annealing.
* (DONE) Finding a better annealing schedule to arrive at solutions to the problem quicker.
* (DONE) Simulating the same problem but using quantum annealing.
* (DONE) Comparing the classical and quantum methods.
* (DONE) Solving a real-world problem involving cell phone tower placement in Gotham City.

## Further Challenges:
* (DONE) Comparing the methods used to solve the UD-MIS problem.
* (DONE) Benchmarking other quantum and classical optimization methods to solve your UD-MIS problems.
* (DONE) Demonstrating how other problems can be mapped to UD-MIS and solving said problems.
* (DONE) Solving the problem with real quantum hardware.

## Business Application
For each week, your team is asked to complete a Business Application. Questions you will be asked are:

* Explain to a layperson the technical problem you solved in this exercise.
* Explain or provide examples of the types of real-world problems this solution can solve.
* Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved.
* Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language.

For more details refer to the [Business Application found here](./Business_Application.md)
