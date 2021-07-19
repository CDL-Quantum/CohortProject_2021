![drones](https://github.com/aidaah/CohortProject_2021/blob/main/Week2_Rydberg_Atoms/334.PNG)
# Quantum Cohort Project 2 Business Application

We are considering two business applications, both undoubtedly interesting, one with higher impact on environment. We briefly introduce one and elaborate furhter on the second application in the step 2, below.


## Step 1: The technical problem we solved in this exercise

For this week's Cohort project we investigated the Unit-Disk Maximal Independent Set (UD-MIS) problem. MIS is NP-hard to solve and also NP to approximate, but UD/MIS can actually be approximated efficiently. The classical approach to solve this problem is to use Monte-Carlo techniques to solve the problem at high temperatures and then cool it down with a particular scheme to find the solution of minimal energy (simulated annealing, see task 1). But the UD-MIS can also be solved by using the building blocks of neutral-atom quantum computers, namely Rydberg atoms. The quantum version of simulated annealing is to evolve the system using a Hamiltonian that depends on parameters that can be tuned such that as we approach the state of minimal energy (ground state) the Hamiltonian approaches the UD-MIS Hamiltonian. In order to find the solution in the quantum version, one measures the final state a large number of times (sampling) and chooses the ground state to be the bit-string with the highest frequency of appearance. In the quantum version, the connectivity of the graph (which vertices are independent and which not) is given not by the occupations as in the classical case but by the state of each Ryberg atom, which can be either in the ground state or in the excited state. UD-MIS problems are a well-known class of mathematical problems that can describe a range of common scientific and industrial challenges: for instance, how to map the resources or centres in a cost-efficient way such that it offers the best coverage with the lowest overlap.

## Step 2: Two examples of the types of real-world problems this solution can solve

1. **distribution of greenhouse gas sensors**

Another application that we considered is the distribution of greenhouse gases emission sensors. These sensors are key to implement carbon taxes, a policy already effective in the EU countries, Canada, Mexico, Chile among others and which is supposed to become effective in Washington State USA this year. 
For example, several national laws in European countries set requirements for continuous monitoring of flue gas emissions at waste incinerators, power plants, cement plants, and other industrial plants. The demand for emission measurements has only increased and the limit values tightened in recent years, and the trend will undoubtedly continue. 
We believe the UD-MIS problems are well suited to find solutions for the geographical distribution of these measurements since it is key that the coverage of the sensors does not overlap in order to be able to discern which plant is the emission coming from.

2. **Last-mile drone delivery service**

In our today's world, when e-commerce solutions have become the prevalent way of shopping in many countries, smooth and fast deliveries has become not just a pleasant final touch but the required customer expectations [1](https://www.businessinsider.com/last-mile-delivery-shipping-explained). Some studies report that almost half (46%) of shoppers think that convenience and personalisation of delivery service are the key factors in their online buying decisions [2](https://internetretailing.net/themes/themes/customers-want-more-convenient-delivery-options-study-15924). 
Unfortunately enough, the last-mile delivery service also often happens to be the most expensive and time-consuming leg of the good's journey, not to mention that, nowadays, the customers mostly expect low-cost or completely free-of-charge shipment. 
The number of deliveries that occur every day is astonishing in some cities (1.5 million in a day in New York back in 2019 [3](https://www.nytimes.com/2019/10/27/nyregion/nyc-amazon-delivery.html)). And, to think of it, "with every click of that enticingly convenient 'Buy' icon, we create a truck trip each time" [4](https://time.com/5481981/online-shopping-amazon-free-shipping-traffic-jams/), making the gridlocks even worse (hence, increased delivery times), not to mention the effect in the greenhouse gas emissions.
It does not come as a surprise that the vast majority of e-commerce companies state current attempts to try to reduce last-mile delivery costs.

In 2019, domestic parcel traffic increased to over 21 billion units with an average price of around 6.4 USD per parcel [5](https://www.statista.com/statistics/737418/parcel-traffic-worldwide-by-sector/). See figure below.

![image1](https://github.com/aidaah/CohortProject_2021/blob/main/Week2_Rydberg_Atoms/Slide2.JPG)

The current e-commerce market size is astonishing. The global retail e-commerce sales amounted to 4.28 T USD sales worldwide in 2020 and it project to grow by 22%  by 2024 [6](https://www.statista.com/statistics/379046/worldwide-retail-e-commerce-sales/). See figure below.

![image2](https://github.com/aidaah/CohortProject_2021/blob/main/Week2_Rydberg_Atoms/Slide3.JPG)

![image2](https://github.com/aidaah/CohortProject_2021/blob/main/Week2_Rydberg_Atoms/Slide4.JPG)


We suggest creating an alternative service for last-mile deliveries working on drones. Real estate prices have only increased in major customer centres. By using the UD-MIS formulation to optimally place drone delivery centres within major cities, we would allow for short delivery times. Every drone will fly “as the crow flies”, which follows the unit disks. It is worth mentioning, we do not actually need perfect coverage over a city here (unlike cell coverage we investigated in the tasks). Shipment companies would be able to service the rest of the uncovered parts of the city with the same vehicle deliveries.
By introducing this option, we would be able to:
- reduce trucking costs by 80 %;
- cut the delivery times (due to the traffic jams in the rush hours);
- move to electric services for decarbonization;
- provide a service completely free of interaction with the delivery person (which could be useful in times of global pandemic);
- improve the overall customer experience.


## Step 3: Potential customers for this solution

1.   Last-mile deliverers, i.e. local couriers
In NYC:
  - Premier Courier Services Inc. (\$3.6 million in sales)
  - Accurate Courier LLC (\$1.6 million in sales)
  - Unites States express (\$3 million in sales)

  and many others;
  
2.   Big delivery companies
  - DHL (generated 66.8 billion euros in 2020)
  - FedEx (\$69.22 billion in 2020 in revenues)

  and others;
  
3.   Food delivery platforms
In NYC:
  - Grubhub (\$1.8 billion in 2020 in revenues)
  - Uber Eats (\$4.8 billion in 2020 in revenues)
  - DoorDash (\$2.9 billion in 2020 in revenues)

  and others;
  
4.   E-commerce platforms
  - Amazon (\$108.52 billion in 2020 in revenues)
  - Alibaba Group Holding Limited (around \$109 billion  for the fiscal year ending on March 31, 2020)
  - eBay Inc.  (around \$10 billion  for the fiscal year ending on March 31, 2021)

  and others.


## Step 4: A 90 second video explaining the value proposition of our innovation to this potential customer in non-technical language

[![IMAGE ALT TEXT](http://img.youtube.com/vi/mY33muTBi9E/0.jpg)](https://www.youtube.com/watch?v=mY33muTBi9E "Video Title")

