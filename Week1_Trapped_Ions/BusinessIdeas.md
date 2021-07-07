### Business ideas 
In the following, a couple of ideas for the application of random circuits to practical business cases. 
The main idea behind all of them is that the random circuit provides a true source of randomness generation.

![CDL 2020 Cohort Project](../Week1_Trapped_Ions/img/machine-rng.jpg)
[source](https://www.insidescience.org/news/randomness-machine)

#### Nestle (food industry)
Nestle is the largest food producer in the world. (Total Sales: $93 bln in 2019)
Goal: implement a random testing and auditing framework to protect against food fraud.

For large food chain organisations, the reduction of costs is often connected to an overly complex supply chains, 
extending back to suppliers and producers around the world and resulting in distribution to international markets. 
In this case, businesses have to rely on due diligence and trust as the supply chain cannot be as tightly controlled. 
Large organisations often have their own supplier management programmes in place to monitor and control each of their suppliers. 
Here, frequent testing takes place, along with regular audits, in order to ensure the safety of ingredients and the end product.

However, this system is often affected by fraudulent activities which aim at an economic gain at the expense of the organization.
Such fraudulent activities are generally associated to the understanding of when and where testing takes place and often connected.

We propose a quantum based framework to perform true random testing across the geographically distributed suppliers of Nestle.   
https://www.intertek.com/blog/2015-09-01-sample-testing/

#### Amazon (logistics) 
Amazon’s warehouses are not organized hierarchically by product categories. Instead, goods are stored anywhere there is space, and their location recorded in an internal system.
This essentially random method may seem unnecessarily chaotic, but over time it distributes inventory evenly across the warehouse, so Amazon’s workers rarely have to travel long distances to fulfill an order. It also lessens the overall size of the distribution center by requiring less empty shelf space.
https://medium.com/@Jake_Color/the-purpose-of-randomness-d3298ae18e17

#### Pixar or any Gaming company  
Random generation of environments

#### Amsterdam Schiphol airport (logistics)
Random selection for airport passenger check at customs control
Extension to cargo check
https://www.maa.org/external_archive/devlin/devlin_05_02.html

#### General Electric (simulation and testing)
Random Topology Power Grids for testing: Produce power grids with scalable size and randomly generated topologies. These ensembles of networks can then be used as a statistical tool to study the scale of communication needs and the performance of the combined electric power control and communication networks. The topological and system features of the randomly generated power grids are compared with those of standard power system test models as a “sanity check” on the method. 
https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.7615&rep=rep1&type=pdf
(likely widespread catastrophic failures of electric power grids)
($33.96bn)

#### Lockheed Martin (simulation and testing)
Aircraft dynamic modelling application: random number generators are used to produce Gaussian white noise sequences to assess their suitability in aircraft dynamic modeling applications. A set of sequences of random numbers can be produced and analyzed in terms of the mean, variance, normality, autocorrelation, and power spectral density. These sequences can then applied to two problems in aircraft dynamic modeling, namely estimating stability and control derivatives from simulated onboard sensor data, and simulating flight in atmospheric turbulence. 
 https://www.researchgate.net/publication/329385173_A_Comparison_of_Three_Random_Number_Generators_for_Aircraft_Dynamic_Modeling_Applications 
(Lockheed Martin	$53,800 million)

#### Ethereum (blockchain)
Ethereum: Those familiar with random number generation (RNG) problem know that all of the software-based random algorithms are generating pseudo-randomness (PRNG) as opposed to true-randomness (TRNG). In short, it means that computers generate random numbers based on a variable called a seed. Consequently, if a malicious user uncovered the value of such a seed or took control over it, it would compromise the validity and security of a PRNG. In most cases PRNG is still good enough as it’s executed server-side, protected from the evil of this world by infrastructure.
Due to the transparent nature of blockchain and isolation of respective blocks, this challenge is only magnified in the blockchain environment. Smart contracts can’t access data from the outside world, so in order to provide seed for on-chain PRNG, we would need to use some data that is also available to a miner.
https://medium.com/gardeneroracle/random-number-generation-in-gardener-1660e5c25e00

#### Online poker companies: a bit obvious

#### Government applications: random sampling of jurors (US), random sampling of participant for polls, loteries...
