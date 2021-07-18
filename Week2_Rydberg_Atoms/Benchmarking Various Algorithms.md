# Benchmarking various classical and simulated quantum optimization solutions to the UD-MIS problem
Team 1: Ziwei Qiu (ziweiqiu29@gmail.com), Jack Sarkissian, Uchenna Chukwu, David Orrell, Maninder Kaur

We compare computation performances across a number of classical and quantum algorithms for the UD-MIS (unit disk - maximal independent set) problem. Classical methods include simulated annealing, an approximation algorithm based on subgraph-excluding subroutine (using the software [iGraph](https://igraph.org/python/))[1] and an exact solution based on backtracking efficient search (using the software [NetworkX](https://networkx.org/))[2]. The simulated quantum method we study here is simulated quantum annealing based on neutral atom systems [3,4]. 

Among the four solutions, we found that the simulated annealing has the best performance in terms of both time complexity and result accuracy. The iGraph exact solution always gives the correct global optimum, however its running time scales exponentially as the problem size. The NetworkX approximation solution is most efficient, however its result is often sub-optimal. Simulated quantum annealing takes exponential time in order to do matrix operations and is most inefficient among all programs (however, this will not be a problem if quantum annealing runs on real hardware). An additional advantage of simulated annealing is that we can tune the u parameter and number of steps based on our preference for the time efficiency or result accuracy. 

The notebook [Benchmarking_UDMIS_Algorithms.ipynb](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Benchmarking_UDMIS_Algorithms.ipynb) written in Python has the codes for the three classical solutions. 
The notebook [run_quantum_annealing_zq.ipynb](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/run_quantum_annealing_zq.ipynb) written in Julia has the codes for simulated quantum annealing. 
The project instruction [instructions.pdf](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/instructions.pdf) provides more background of the UD-MIS problem.




## Simulated Annealing

Simulated annealing is a probabilistic technique for approximating the global optimum of a certain function. The algorithm mimics the annealing procedure in metallurgy, where slowly cooling a material from a high temperature will allow material to eventually reach a stable ground state. At different temperatures, material systems can be found in different states with probabilities determined by the state energy and the Boltzmann distribution. In simulated annealing, at at certain 'temperature', variables can take different values with probabilites determined by the cost function at those values and the Boltzmann distribution. Metropolis–Hastings algorithm is a Markov Chain Monte Carlo (MCMC) method to simulate this probabilistic distribution. The temperature decreases gradually from kT = 100 Joule to kT = 0.01 Joule, where k is the Boltzman constant. The cooling rate decreases exponentially as the system gets colder. At each temperature step, the variable explores different values; it either accepts or rejects the new value with a probability determined by the current tempeature. The number of explorations is equal to the number of vertices in the graph. Here is an example of simulated annealing result for solving the UD-MIS problem, where dots in red are selected to be in the independent set. 

<img src="https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/benchmarking_imgs/c_annealing_example.png" width="625" height="250">

### Optimal cooling speed
We study the effect of cooling speed by varying the number of steps in simulated annealing. More steps corresponds to a slower or finer cooling process. Ideally, we should cool the system infinitely slowly so the system can reach equilibrium at each step, which will eventually gives us the global optimal answer. However, we want to run our algorithm more efficiently by speeding up the cooling process with the risk of not getting to the global optimum. Therefore there is a tradeoff between running time and result accuracy. As shown below, we vary the number of steps from 5000 to 10 and run annealing repeatly on the same randomly generated graph containing 200 vertices, and we tried two different u parameters. The blue curves represent the linear reduction of running time, and the orange curves represent the size of the MIS (maximal independent set). The optimal MIS size is 93 for the graph and we see the algorithm starts deviating from the optimal solution when the number of steps is <1000. So 1000 steps is optimal in this case for both u values.

<img src="https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/benchmarking_imgs/cannealing_vary_steps.png" width="350" height="250">

### Effect of the u parameter
Next, we study the effect of the u parameter. u is the penalty factor to avoid selecting vertices closer than unit length. When u is too small, the algorithm is more likely to include more vertices in the set while ignoring their unit disk overlapping. When u is too large, the penalty term dominates. The algorithm will choose an independent set, however it may not be the largest/maximum independent set, as the first term in the cost function is negligible. u also determines the energy landscape of the cost function, hence affects the energy evolution during annealing. As seen in the following plot, when u is large, the slope between optimal and non-optimal configurations is so steep that the system can reach the optimal solution much faster. We fixed the number of annealing steps to be 2000 when varying u, and a large u more likely results in suboptimal set.

<img src="https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/benchmarking_imgs/cannealing_vary_u.png" width="680" height="250">

## Simulated Quantum Annealing
In quantum annealing, the cost function of the UD-MIS problem is represented by a Hamiltonian of a quantum system. The optimal solution corresponds to the ground state of the Hamiltonian. We start from a simple Hamiltonian and prepare the system in its ground state, and then slowly vary the Hamiltonian to achieve an adiabatic evolution, in which the system always stays in the ground state of the time-varying Hamiltonian. The final Hamiltonian corresponds to the original problem, so the final ground state will be our solution. To  classically simulate this Hamiltonian evolution, we decretize time and approximate the Hamiltonian to be constant within each small time step dt. Here is an example of the UD-MIS result solved by simulated quantum annealing.

<img src="https://user-images.githubusercontent.com/29555981/126050731-38c1e2d4-496e-4f0d-a839-bfe22b8070f7.png" width="150" height="150">

As in the simulated annealing, there is a tradeoff between how fast we vary the Hamiltonian and the final result accuracy. In a physical system, the Hamiltonian evolution rate should be much smaller than the energy gap between the ground state and excited state. In the classical simulation, the time step dt represents the evolution rate. As shown in the following plot, the run time decreases exponentially with and when dt is too large, the result is obviously not an optimal solution.  

<img src="https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/benchmarking_imgs/qannealing_vary_dt.png" width="600" height="250">


## Benchmarking with Approximation solution and Exact solution

We also implement an approximate solution (using NetworkX software) and an exact solution (using iGraph software) to solve the UD-MIS problem, as shown in the following examples:

<img src="https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/benchmarking_imgs/NetworkX_example.png" width="300" height="170">

<img src="https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/benchmarking_imgs/igraph_example.png" width="300" height="180">


In simulated annealing, when the number of annealing steps N is fixed, the running time scales **linearly** as the number of vertices in the graph |V|. This is because we run MCMC sampling for |V| times at each temperature step. In simulated quantum annealing, when the time step dt is fixed, the running time scales **exponentially** as the number of vertices |V|. This is because each vertex is represented by a qubit and the state evolution is calculated by matrix operations. Matrix size grows exponentially as number of qubits in the system. Quantum annealing running real hardware is expected to be much more efficient than the exponential scaling. For the NetworkX approximation solution based on the subgraph-excluding subroutine, the time complexity is O(|V|/(log|V|)^2) [1]. For the iGraph exact solution based on backtracking search, the processing time and memory space are bounded by O(|V|*|E|*S) and O(|V|+|E|), respectively, where |V|, |E|, and S are the numbers of vertices, edges, and maximal independent sets of a graph.

To compare the computation efficiency across different algorithms, we first generate random graphs with different number of vertices, and then run each algorithm on those graphs to find the maximum independent set (MIS). The simulated annealing program, NetworkX approximation solution and iGraph exact solution all run on the same graphs so their MIS results are plotted in the same graph as shown below (while simulated quantum annealing uses separately generated graphs). The running time of all four programs on plotted on the left.

<img src="https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/benchmarking_imgs/Benchmarking.png" width="550" height="250">

In terms of running time, simulated quantum annealing has the worst performance. When the graph size is relatively small (|V|<50), all the three classical solutions are fairly efficient, however the exact solution running time shoots up rapidly as the graph grows large. In terms of the optimization result, simulated annealing result is consistent with the exact solution, while the approximation solution oftens gives suboptimal results. Therefore, simulated annealing has the best overall performance.


### References
[1] Boppana, R. and Halldórsson, M.M., 1992. Approximating maximum independent sets by excluding subgraphs. BIT Numerical Mathematics, 32(2), pp.180-196.\
[2] Tsukiyama, S., Ide, M., Ariyoshi, H. and Shirakawa, I., 1977. A new algorithm for generating all the maximal independent sets. SIAM Journal on Computing, 6(3), pp.505-517.\
[3] Serret, M.F., Marchand, B. and Ayral, T., 2020. Solving optimization problems with Rydberg analog quantum computers: Realistic requirements for quantum advantage using noisy simulation and classical benchmarks. Physical Review A, 102(5), p.052617.\
[4] Pichler, H., Wang, S.T., Zhou, L., Choi, S. and Lukin, M.D., 2018. Quantum optimization for maximum independent set using Rydberg atom arrays. arXiv preprint arXiv:1808.10816.
