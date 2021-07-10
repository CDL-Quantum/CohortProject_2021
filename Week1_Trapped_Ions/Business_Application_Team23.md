![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Week1: Quantum Cohort Project Business Application of Random Circuit Sampling

As with other quantum sampling problems like [boson sampling](https://en.wikipedia.org/wiki/Boson_sampling) and [instantaneous quantum polynomial](https://strawberryfields.ai/photonics/demos/run_iqp.html) (IQP), the random circuit sampling (RCS) problem has no apparent practical application. The main focus of these quantum sampling experiments is the advancement of knowledge. Nevertheless, scientists suggested a couple of applications of the quantum sampling problems. For example, the Gaussian version of boson sampling can be used to simulate molecular spectroscopy and protein docking problems because the distribution is a function of hafnians (multivariate gaussian moments). The IQP is connected to the partition function that it might have an application in statistical mechanics. However, the qubit distribution out of RCS cannot be defined with well-known matrix functions like permanent, hafnian, and determinant. It is even more challenging to find a potential usage of the random quantum circuit. This cohort project report proposes applying the RCS machine to [quantum key distribution](https://en.wikipedia.org/wiki/Quantum_key_distribution) (QKD), a secure quantum communication protocol.    


## Step 1: Explain the technical problem you solved in this exercise

Problem: Alice (the message sender) wants to send a secret key (binary numbers) to Bob (the message receiver) without being eavesdropped on by Eve (the eavesdropper).  
<img width="1018" alt="Screen Shot 2021-07-08 at 8 38 32 PM" src="https://user-images.githubusercontent.com/87050306/125159514-d8a43300-e1b2-11eb-8507-13aa8448e3f0.png">
<img width="1024" alt="Screen Shot 2021-07-08 at 8 38 20 PM" src="https://user-images.githubusercontent.com/87050306/125159519-df32aa80-e1b2-11eb-89e6-eccfbfa62a86.png">


## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

Example: A courier has to deliver parcels to several locations and is looking to minimize its travel time. (e.g., “the travelling salesman problem”).

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Examples: 
- Federal Express
- Canada Post

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

Example: By travelling to all destinations via the shortest route, a courier can generate the same revenue that it would have generated following any other route, but will minimize travel costs (e.g., fuel costs). By minimizing travel costs, the courier will be more profitable than it would have been had it travelled through any other route. [Business Application found here](./week1_businessapplication_small.mov)

