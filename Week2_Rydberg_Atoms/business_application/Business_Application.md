![CDL 2020 Cohort Project](../../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application

## Step 1: Explain the technical problem you solved in this exercise

In this project we have studied how the Unit-Disk Maximum Independent Set (UD-MIS) can be solved using Rydberg atom arrays. 
We used 2 different approaches to solve a simple toy problem:
- Classical simulated annealing using a simple Monte Carlo approach
- Classical simulation of Quantum annealing (sounds the same but is very different)

We also developed a third approach, which required expressing the problem Hamiltonian as an MPO, which we used DMRG to 
find the ground-state. The motivation here is that the solution need not be a product state (although that is what we
assume the solution to be) which would give us the ability to assess the annealing approach in the 
presence of unitary noise, for example. However, it did not improve upon the other classical approach
but was only a first-pass MVP implementation. Further development could yield interesting results and
there are many efficiencies that could be drawn upon.

Lastly, we solve a real-world problem by optimising the cell network in Gotham for an esteemed client: Bruce
Wayne. We delivered what he wanted but we have warned the client that there will likely be some disgruntled residents of Gotham.

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

The UDMIS problem is extremely generalised and many problems can be embedded into it's definition:

- Traffic analysis and optimisation
- Social network analysis 
- Water and Power infrastructure optimisation and planning

In fact most networking problems could be cast as UDMIS problems or a variant of it.

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

In our business application we have identified a less obviouse vertical: conservation efforts, whether they are also not-for-profits,
government bodies or local councils. Others include

- Government bodies (Traffic, Water, Power, Infrastructure)

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Meet **Ghost in the Shell** initiative, a not-for-profit using quantum computing to save a species from extinction.
Our proof of concept was performed in partnership with a local conservation department in New Zealand to 
save the Kokako from extinction.

https://youtu.be/aGysWK3fbew