![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application
## 

## Example of real-world problems:
A number of industrial applications have been identified for optimization using the quantum approach outlined here. A broad class of problems is the design of wireless sensor networks (WSNs). These can be used to monitor atmospheric conditions such as temperature, humidity, and wind; environmental conditions such as water quality or levels of noise or pollution; events such as forest fires, landslides, and floods; or the movement of people or animals (for example to detect intruders in a controlled area). As with cell phone tower placement, the optimization problem is to achieve the best coverage with the least number of sensors.

The particular application that we have chosen to focus on is the smart-charging of electric vehicles. The high level of power needed to charge the vehicles, especially with fast-load stations, means that the electricity useage must be carefully handled and optimized. This type of scheduling problem is highly complex and difficult to calculate using classical algorithms; however it can be translated into a UD-MIS problem as shown in [Dalyac et al., 2021](https://doi.org/10.1140/epjqt/s40507-021-00100-3)

![alt text](https://github.com/ziweiqiu/CohortProject_2021/blob/main/Week2_Rydberg_Atoms/ChargingStation.jpg "EV Charging Station")
Photo: An electric vehicle charging station in Paris, France. Source: [data.gov.fr](https://www.data.gouv.fr/fr/datasets/belib-reseau-parisien-de-bornes-de-recharges-accelerees-22-kw-ac-dc-pour-vehicules-electriques/)

A set of load tasks is represented as intervals on a timeline. Each task belongs to a certain group, which might represent a company’s vehicle fleet. The aim is to find the subset of these loads which maximizes the number of non-overlapping tasks, while ensuring that at most one load in each group is completed. The first condition means that the competion time is minimized, while the second condition means that no single group is over-represented in the schedule.

In contrast to the cell-phone tower or WSN problems, which involve finding an optimal spatial arrangement, the optimization problem now involves scheduling in time. A loading event is therefore described by the start and end times, instead of two spatial coordinates. Overlap occurs if two events from the same group share an edge. The Maximal Independent Set then describes a solution which minimizes the completion time while avoiding any overlap.

##  Smart-charging of Electric vehicle
Smart-charging appears to be a mandatory condition to allow electric mobility expansion. The high level of power required to load electrical vehicles, especially on fast load stations, require optimal modulation of this load demand in time. Further, the use of vehicle batteries as energy storage devices and power sources could significantly improve the flexibility of the electrical system, reduce high-peak of electricity demand and thus generate significant energy savings, while offering customers with various services providing earning money and saving costs opportunities. 


