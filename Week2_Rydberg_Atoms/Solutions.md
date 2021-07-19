![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 2: Optimization problems \& Rydberg atom arrays

## Solving Tasks 1 and 2 using Classical and Quantum Brute Force

The graph corresponding to the unit-disk maximum independent set (UD-MIS) for this problem is

<center><img src='Team_6/01-problem1_2.png' width='200'></center>

Given its small size, we begin by solving the problem using classical and quantum brute-force using the following [Jupyter notebook](./Team_6/UD-MIS_Problem-Brute_force.ipynb). For the classical case, we computed all possible outcomes and evaluated the cost function. Then, the solutions are the configurations with the lower cost.   
For the quantum version, we built the Hamiltonian associated to the cost function and calculated its eigenvalues and eigenvectors. The solutions are encoded on the eigenvectors of the ground state eigenspace. In order to extract the solutions, we computed

<img src="https://render.githubusercontent.com/render/math?math=n_i=< Gs(k) \left| n_i \right| Gs(k)>,">

were *k* is the degeneracy index.

<center><img src='Team_6/02-solutions_1_2.png' width='600'></center>

The quantum and classical sets of solutions are the same and, if one is looking for the least-overlapping-disks solution, the second is the winner!  

### Task 1: Simulated classical Annealing

Using [ej1.py](./Team_6/ej1.py), we tested three annealing schedules and compared their computational costs of convergence.

<center><img src='Team_6/03-ann_schedule.png' width='800'></center>

In this case, the second annealing scheme yields the best results. 

### Task 2: Quantum Annealing
We proposed smoother time dependent controls and tested their performance using the following [Jupyter notebook](./Team_6/run_quantum_annealing.ipynb).

<center><img src='Team_6/04-q_annealing_controls.png' width='1000'></center>

We ran 1000 samples for both sets of controls and constructed the histogram dropping out the configurations with less than samples/10 counts.

<center><img src='Team_6/05-problem1_q_annealing.png' width='800'></center>

In this case, the number of samples chosen was enough to obtain all the solutions.

### Task 3: Solving Gotham City's problem

Once again, we begun by plotting the graph for Bruce Wayne's problem:

<center><img src='Team_6/06-wayne_problem.png' width='250'></center>

Given its size, we followed the same sequence to solve it. First, [the brute force solutions](./Team_6/UD-MIS_Problem-Brute_force.ipynb)):

<center><img src='Team_6/07-wayne_solutions.png' width='600'></center>

We tried different schedules used for classical annealing to study [this problem](./Team_6/ej3.py) and the best results were obtained with the second scheme. 

For the quantum annealing, we tried running 10000 samples for each scheme ([run_quantum_annealing.ipynb](./Team_6/Team_6/run_quantum_annealing.ipynb)), and the new controls  for the annealing show an advantange with regard to the previous version. We constructed the histograms by dropping out the configurations with less than samples/40 counts. From the histograms, its clear that the smoothed versions of the controls increase the number of counts for the right configurations. 

<center><img src='Team_6/08-Wayne_q_annealing.png' width='800'></center>

From the obtained results, we can conclude that if applying brute force is not possible then it is easier to find the solutions using quantum annealing than classical Montecarlo simulations. For all cases, we found that it is crucial to evaluate the cost function in order to validate its performance.
