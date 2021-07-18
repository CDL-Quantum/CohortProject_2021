# Simulating the same problem but using quantum annealing



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

Additionally we have run the simulated quantum annealer on a more complicated graph with 11 nodes
|Solutions | Solutions on the Graph|
| :--------------: | :---------: 
| <table>   <thead>   <tr> <th>Solution</th>  <th>Frequency</th>  </tr>   </thead>   <tbody>   <tr>  <td>01111001100</td>  <td>6827</td> </tr> <tr>  <td>11011011000</td>  <td>6774</td> </tr> <tr>  <td>01111011000</td>  <td>6713</td> </tr> <tr>  <td>11011001100</td>  <td>6709</td> </tr> <tr>  <td>11011001001</td>  <td>6682</td> </tr></tbody> </table> | <img src="./resources/task2_compl_graph/compl_graph.gif" width="300">

<img src="./resources/quantum_gotham/quantum_gotham.gif" width="300">

