# Benchmarking various classical and simulated quantum optimization solutions to the UD-MIS problem
Team 1\
Ziwei Qiu (ziweiqiu29@gmail.com), Jack Sarkissian, Uchenna Chukwu, David Orrell, Maninder Kaur

In this study, we compare computation performances across a number of classical and quantum algorithms for the UD-MIS problem.
Classical methods include simulated annealing, an approximation algorithm based on subgraph-excluding subroutine (using the software [igraph](https://igraph.org/python/))[1] and an exact solution based on backtracking efficient search (using the software [NetworkX](https://networkx.org/))[2]. The simulated quantum method we study here is simulated quantum annealing based on neutral atom systems [3,4]. 

## Simulated Annealing

Simulated annealing is a probabilistic technique for approximating the global optimum of a certain function. The algorithm mimics the annealing procedure in metallurgy, where slowly cooling a material from a high temperature will allow material to eventually reach a stable ground state. At different temperatures, material systems can be found in different states with probabilities determined by the state energy and the Boltzmann distribution. In simulated annealing, variables can take different values with probabilites determined by the cost function at those values and the Boltzmann distribution. Metropolis–Hastings algorithm is a Markov Chain Monte Carlo (MCMC) method to simulate this probabilistic distribution. 

## Quantum Annealing

## Benchmarking with Apprximation solution and Exact solution
![alt text](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/benchmarking_imgs/Benchmarking.png)




### References
[1] Boppana, R. and Halldórsson, M.M., 1992. Approximating maximum independent sets by excluding subgraphs. BIT Numerical Mathematics, 32(2), pp.180-196.\
[2] Tsukiyama, S., Ide, M., Ariyoshi, H. and Shirakawa, I., 1977. A new algorithm for generating all the maximal independent sets. SIAM Journal on Computing, 6(3), pp.505-517.\
[3] Serret, M.F., Marchand, B. and Ayral, T., 2020. Solving optimization problems with Rydberg analog quantum computers: Realistic requirements for quantum advantage using noisy simulation and classical benchmarks. Physical Review A, 102(5), p.052617.\
[4] Pichler, H., Wang, S.T., Zhou, L., Choi, S. and Lukin, M.D., 2018. Quantum optimization for maximum independent set using Rydberg atom arrays. arXiv preprint arXiv:1808.10816.
