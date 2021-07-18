![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Business Application: Sprinkler and social distancing go Quantum


## Summary of the technical problem solved in this exercise

In this exercise we solved the UD-MIS problem on a graph G of V vertices and E edges by finding the ground state of the Hamiltonian of a system of V Rydberg atoms placed in the vertices of G.

We used two different approaches to solve this problem:
1) Classical annealing
>We simulated the associated Hamiltonian at low temperature using classical Monte Carlo simulations. At a low enough temperature, we can achieve its ground state, i.e. the solution of our original problem. In our simulations, we tried different annealing schedules to achieve the desired solution.

2) Quantum annealing
>Starting in an easy-to-prepare ground state of a Hamiltonian H(0), we evolved this state with a time-dependent Hamiltonian H(t) in such a way that the ground state of the final Hamiltonian H(t*) is the one we were looking for. We accomplished this by forcing H(t*) to be the UD-MIS Hamiltonian.

In non-technical language, we found the maximum number of occupied locations under certain constraints using classical and quantum techniques to compute the solutions.

Finally, we mapped the UD-MIS problem to a real-life one. We applied these techniques to choose in which places to install a set of cell phone towers in Gotham City since a set of possible locations is given.

## Examples of real-world problems related to our solutions

#### Movie theaters
Due to COVID-19 pandemic, most movie theater chains had to temporarily close all theater sites for public safety concerns. While vaccination campaigns are quite advanced, theaters still need to take into account social distancing to reopen. A slightly-modified version of our solution allows them to have the largest audience possible, with each person sitting 2 meters -or 6 feet- apart from each other, according to the health recommendations when indoors.

#### Agricultural industry
Over one billion people worldwide work in agriculture, representing more than 27% of the world population in 2018 and generating $2.4 trillion for the global economy [1,2]. Choosing where to put watering systems is an everyday challenge for small to medium croplands. Our solution can determine the best location for water sprinklers in their fields in order to irrigate most of your crops with the lowest cost.

## Potential customers for this solution

Some of the largest movie theatre chains from around the globe:

- AMC (US): 11,041 screens, US$1.2424 billion revenue in 2020
- Cineworld (UK): 9,500 screens, £852.3 million (~ US$ 1.174 bill) revenue in 2020
- CGV (South Korea): 3,459 screens, US$522.77 million revenue in 2020.
- Cineplex (Canada): 1676 screens, CAD$ 1.665 billion (~ US$ 1.32 bill) revenue in 2019


To conclude, we made [a short video](https://drive.google.com/file/d/1YFC5P-q3sqXwucukQ61pdF_tsplOgkNx/view?usp=sharing) for a potential customer.


## References

https://croplife.org/news/agriculture-a-2-4-trillion-industry-worth-protecting/

[Employment in agriculture](https://data.worldbank.org/indicator/SL.AGR.EMPL.ZS?end=2018&most_recent_year_desc=true&start=1991&type=shaded&view=chart) (Data retrieved on January 29, 2021)
