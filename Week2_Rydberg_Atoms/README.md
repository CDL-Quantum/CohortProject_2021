![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 2: Optimization problems \& Rydberg atom arrays
Team 1: 

This project will guide you through using the foundations of quantum hardware to demonstrate a quantum advantage in real-world problems.

Open up [instructions.pdf](https://github.com/CDL-Quantum/CohortProject_2021/tree/main/Week2_Rydberg_Atoms/instructions.pdf) to begin learning about your tasks for this week!

## Solutions ##
### Task 1

Convergence to solution varies depending on temperature step. Faster cooling risks leading to a suboptimal solution. Slow cooling helps to get to global minimum. Biggest sensitivity to cooling schedule is achieved when

E ~ KT

where Eis the excitation energy. Outside of that region, the temperature step can be large and it won’t affect the end result much. But inside the region cooling must proceed adiabatically to avoid bringing the system to a local energy minimum. 

Based on the underlying physics, here are the steps to work out the annealing schedule that can lead to faster results without compromising much of the accuracy:

1. Determine the excitation energy (it’s the energy fluctuation size)
2. Start with T>>dE, for exampleT=20 dE so that all nodes get a chance to try excited and ground states. Larger temperature will add no value.
3. Cool adiabatically in steps with dT<<dE
4. Interrupt procedure once T<<dEfor example at T=0.1 dE

Annealing dynamics that follows the schedule worked out this way is shown in figure below. Then it takes 150 steps instead of 4000.

Generally, optimal schedule can be worked out by formulated the problem as a Q-learning problem [1].
![Annealing dynamics at 4000 steps](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Convergence%20in%204000%20steps.png)
![Annealing dynamics at 150 steps](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Convergence%20in%20150%20steps.png)

### Task 2
The solution for the task 2 can be found [here](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/run_quantum_annealing_zq.ipynb)                                   
                                    
### Task 3
![alt text](https://upload.wikimedia.org/wikipedia/en/c/c6/Bat-signal_1989_film.jpg)

Batman receiving the Bat Signal.
                                    
1. The Gotham City problem is a problem of optimal resource allocation. Revenue from the towers is proportional to their covered area. That area forms from the number of towers (first term in Eq. (3) ) with the exception of the overlap areas (second term). Optimal tower configuration is determined by maximizing the utility function, which is equivalent to the energy minimization problem of the Rydberg chain. 

                                    
2. There are multiple [solutions](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Benchmarking_UDMIS_Algorithms.ipynb) to this problem. The exact algorithm produces 8 possible solutions: [(0, 1, 4, 6, 7), (0, 1, 4, 6, 8), (0, 1, 4, 6, 10), (0, 1, 4, 6, 11), (0, 1, 4, 9, 10), (0, 1, 4, 9, 11), (0, 3, 4, 9, 10), (0, 3, 4, 9, 11)]
                                    
![alt text](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Images/3.1.png)

![alt text](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Images/3.2.png)

![alt text](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Images/3.3.png)                                   

3. If the problem is stated as in the document: “should Bruce pay for more towers to make sure that more of the City is covered” then the answer is yes, since there are uncovered areas, but it has nothing to do with economic considerations.
If, however, the problem was formulated as “Is it economically beneficial for Bruce to put up more towers”, the answer is no. Economic benefit is decided by maximization of the utility function, which will increase if there is economic benefit. In the Rydberg chain formulation this translates to the possibility of further energy decrease: if adding another tower within the City limits helps decrease the energy of the corresponding Rydberg chain, it is beneficial to pay for an extra tower. 

We solved the problem for economic benefit using a classical annealing algorithm. First, as an example, we look at the case when an extra tower is added at a distant location, as shown in figure below, so that we already know there is a clear benefit. Indeed, this resulted in energy decrease from -5 to -6.

![alt text](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Images/3.4.png)
                                    
Then, we started adding an extra tower at 200 random locations in addition to already existing ones (since that’s what Bruce is looking for). These locations are shown as blue dots in Figure (). We then reoptimized using the brief annealing schedule that we found in Task 1, and took energy measurements. 
Only a subset of locations produced a lower energy: -6 instead of -5. They are shown in Figure (). All these suggestions fall outside the Gotham City limits in the water area, so unless the sea coverage is in play, adding an extra tower is not feasible. 
                                
![alt text](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Images/3.5.png)
                                    
![alt text](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Images/3.6.png)

## Benchmarking

[QAOA](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/QAOA%20challenge.ipynb)

[Benchmarking various algorithm](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Benchmarking%20Various%20Algorithms.md)



## Business Application
Optimization using Rydberg atom is a resource allocation solution. Any business problem where economic benefit comes from scaling with the exception of overlap activities can be formulated and solved using Rydberg chains.

Examples of business applications are shown [here](https://github.com/ziweiqiu/CohortProject_2021/blob/Week2-Team1/Week2_Rydberg_Atoms/Business_Application.md)

### References                                  
[1] I.Halperin, M.Dixon, P.Bilokon, “Machine Learning in Finance: From Theory to Practice 1st ed. 2020 Edition” https://arxiv.org/abs/2006.11190



