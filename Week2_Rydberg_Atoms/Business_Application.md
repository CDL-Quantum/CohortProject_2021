![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application

For each weekly project, your team is asked to complete the below business application exercise.
To complement the technical tasks, please consdier the four questions below.
You are free to format your response to these four questions as you wish (with the final question done as a short recorded video), and to include
the content (or links to the content) on your forked repository.

A brief example for each question is included for the 
[Traveling Salesman Problem.](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

## Step 1: Explain the technical problem you solved in this exercise

Example: Finding a global minimum in settings where a classical approach may not be able to find a global minimum.

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

A number of industrial applications have been identified for optimization using the quantum approach outlined here. A broad class of problems is the design of wireless sensor networks (WSNs). These can be used to monitor atmospheric conditions such as temperature, humidity, and wind; environmental conditions such as water quality or levels of noise or pollution; events such as forest fires, landslides, and floods; or the movement of people or animals (for example to detect intruders in a controlled area). As with cell phone tower placement, the optimization problem is to achieve the best coverage with the least number of sensors.

Another important application will be resource allocation for computations on cloud servers (e.g. AWS, IBM, NVIDIA). Since computing resources are limited, and there are many users competing to use them, the problem is how to optimally allocate resources to users based on their requirements. Revenues scale proportionaly to the number of clients, but performance drops if their use overlaps. The utility function is the same as the Rydberg array energy with a minus sign, and therefore it’s the same problem.

The particular application that we have chosen to focus on is the smart-charging of electric vehicles. The high level of power needed to charge the vehicles, especially with fast-load stations, means that the electricity useage must be carefully handled and optimized. The importance of this issue will only grow as electric vehicle useage is set to explode in coming years, putting electricity systems under increasing stress. This type of scheduling problem is highly complex and difficult to calculate using classical algorithms; however it can be translated into a UD-MIS problem as shown in [(Dalyac et al., 2021)](https://doi.org/10.1140/epjqt/s40507-021-00100-3)

![alt text](https://github.com/ziweiqiu/CohortProject_2021/blob/main/Week2_Rydberg_Atoms/ChargingStation.jpg "EV Charging Station")

Photo: An electric vehicle charging station in Paris, France. Source: [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/belib-reseau-parisien-de-bornes-de-recharges-accelerees-22-kw-ac-dc-pour-vehicules-electriques/)

A set of load tasks is represented as intervals on a timeline. Each task belongs to a certain group, which might represent a company’s vehicle fleet. The aim is to find the subset of these loads which maximizes the number of non-overlapping tasks, while ensuring that at most one load in each group is completed. The first condition means that the competion time is minimized, while the second condition means that no single group is over-represented in the schedule. 

In contrast to the cell-phone tower or WSN problems, which involve finding an optimal spatial arrangement, the optimization problem now involves scheduling in time. A loading event is therefore described by the start and end times, instead of two spatial coordinates. Overlap occurs if two events from the same group share an edge. The Maximal Independent Set then describes a solution which minimizes the completion time while avoiding any overlap.

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Examples: 
- Federal Express
- Canada Post

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Example: By travelling to all destinations via the shortest route, a courier can generate the same revenue that it would have generated following any other route, but will minimize travel costs (e.g., fuel costs). By minimizing travel costs, the courier will be more profitable than it would have been had it travelled through any other route.

**Please store your video externally to the repo, and provide a link e.g. to Google Drive**
