![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 2: Optimization problems \& Rydberg atom arrays

This project will guide you through using the foundations of quantum hardware to demonstrate a quantum advantage in real-world problems.

## Code and Notebooks
For each of the sections below a notebook with the same name is associated. The task and challenges were taken from the following  [instructions.pdf](./instructions.pdf).


## Tasks 

### Task 1
associated [notebook](./Task1.ipynb)

We solved the unit-disk maximum independent set (UD-MIS) problem using classical simulated annealing, for the proposed Toy Graph.
![Task 1: Result](./img/Task1_ToyGraph.png)

On the above plot, each circle is centered on the coordinates of the vertex, with a unit diameter. The vertices which are connected by an edge are the ones for which the two circles intersect, meaning that the distance between the centers is less than the unit. Circles in gray in the background are non occupied vertices, while blue circles in the foreground are occupied vertices. The result is compliant with the constraint of non overlap, and solving the problem with brute force confirms that it is indeed an optimal solution. 

For the above Toy Graph, the brute force solver goes faster than the classical annealing. To start demonstrating an advantage of simulated classic annealing, we solved the problem for a random problem. The random graphs are parametrized by two values : the number of vertices **N** and the density **d**. The vertices coordinates are uniformly sampled in a square of side length **c**. The size of the square is chosen such as its surface equals the number of vertices divided by the density **d = N /c^2**. Therefore, the two coordinates are sampled over **0** to **c = \sqrt{N/d}**

The two implementations start to be equivalent in term of runtime around **N = 20** for density **d = 1**. Several solutions are optimal
![Task 1: Result](./img/Task1_RandomGraph20.png)

We tried to find a better annealing schedule to arrive at solutions to the problem quicker.

**TODO Felipe**

### Task 2
associated [notebook](./Task2.ipynb)
We solved the same Toy Graph problem, but using quantum annealing with the Yao library implementation. Plotting the frequency of occurrence of each bit string, we find that the solver has identified thre optimal solutions :
![Task 2: Result](./img/Task1_RandomGraph20.png)

However, it seems that the quantum annealing solver yields an error, with an noncompliant solution proposed as optimal
![Task 2: Result](./img/Task2_ToyGraph.png)

### Task 3
associated [notebook](./Task3.ipynb)

### original problem

The City of Gotham is looking at putting in new cell phone towers. Some possible locations of the cell phone towers have been identified. To avoid overheads, Gotham should only purchase the required number of cell phone towers such that 
1. the cell phone tower signal ranges do not overlap
2. as much of Gotham City can be within cell signal range

This problem can be mapped to a UD-MIS problem. In that case each potential location corresponds to a vertex and can hold a tower, which corresponds to being activated or not. Constraint 1 translates into the disk constraint, which define the edges of the graph. Constraint 2 corresponds to the fact that a maximum of tower shall be installed, which translates into optimisation of the cardinality of independent set.

We solve the problem with the simulated classical annealing and the brute force solver. The problem is not complex enough for the simulated annealing to beat the brute force implementation in runtime (3s vs 0.2s) Moreover the brute force solver outputs a set of possible options :
![Task 3: Result](./img/Task3_Gotham.png)

### reformulation of the problem

However, one can argue that the constraint of no overlap is suboptimal. Let's take the toy case where there are only two potential sites at a distance of 0.9999. The optimal a human would intuitively choose would be to put a tower on both sites, but instead the the UD-MIS would reject it as the two sites are formally intersecting. A new way of reformulating the problem would be to maximize the area covered while minimizing the overlap. In order to do that, the edges of the graph corresponding to the problem could be weighted by the overlap surface. In fact if we take the exact formula of the overlap between two circle (normalised to 1 being the surface of unit circle) where **dij** is the disance between the **i**th and **j**th centers.

**wij = 2 pi ( arcos(d) - d \sqrt(1-dij)^2}**

It turns out that the value : sum of activated tower - sum of the weights over the edges is exactly equal to the surface covered by at least one tower. In that new framework this is the quantity to maximize, for a given number of towers, that becomes the cost.

By brute force we plot where all solutions stand in the space total overlap vs cost. The red line shows the optimal solution for each number of towers :
![Task 3: Result](./img/Task3_overlap_cost.png)

And below we display the optimal solution for each number of tower, the overlap value can be seen in the title
![Task 3: Result](./img/Task3_compromise.png)



## Further Challenges:

* Solving the problem with real quantum hardware.

### Implementation on Dwave
associated [notebook](./Dwave.ipynb)

**TODO Alice**

### Implementation on IonQ

**TODO Victor**

### mapping the Nurse Scheduling Problem to UD-MIS
Demonstrating how other problems can be mapped to UD-MIS and solving said problems.

**TODO Victor**

### benchmarking the Nurse Scheduling Problem

**TODO Felipe**
Comparing the methods used to solve the UD-MIS problem.
Benchmarking other quantum and classical optimization methods to solve your UD-MIS problems.


## Business Application
For more details refer to the [Business Application found here](./Business_Application.md)
