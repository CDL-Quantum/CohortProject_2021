![CDL 2020 Cohort Project](img/threesome.png)

# Quantum Cohort Project Business Application

## Step 1: Explain the technical problem you solved in this exercise

Variational Quantum Eigensolver: Constructing Potential Energy Surfaces for Small Molecules

The Variational Quantum Eigensolver (VQE) is a quantum/classical hybrid algorithm that is used to obtain an approximate solution for the lowest energy state of a molecule. A model of the molecule’s Hamiltonian is stored on the quantum computer. This Hamiltonian depends on a set of adjustable parameters, and its expected value serves as a cost function. At each step of the optimization, the cost function is evaluated, and the parameters are then adjusted using the classical computer. When the optimization is complete, the energy should approximate that of the molecule’s ground state.


## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

It might seem that calculating the ground state of a simple molecule is an academic exercise, but in fact there are a number of potential business applications in areas including drug discovery, spectroscopy, materials design, and finance.

The method can be applied to a wide variety of optimization problems, including quadratic unconstrained binary optimization (QUBO) problems. These are of the form:

minimise: cTx+qxTQx
subject to: x0,1n
with q∈R, cRn and QRn×n

An example is the portfolio optimization problem in finance. The aim here is to select a portfolio from a set of assets which optimises a weighted combination of expected returns and volatility. In the QUBO formulation, the vector x indicates whether a particular asset is in the portfolio or not. The matrix Q specifies the covariances between the assets, and the scalar q represents the investor’s risk appetite. For this problem, there is an additional budget constraint for the sum of the securities; this can be addressed by adding a penalty term to the cost function.

While portfolio optimization is considered to be a key application of VQEs in finance, it should be noted that portfolio selection cannot be reduced to a straightforward optimization problem in this way. The reason is that the returns and covariances are not well-defined or stable quantities, but depend on the time period over which they are measured; and of course their future values are unknown. However the quantum approach will still be attractive to some financial organisations who currently use classical portfolio optimization techniques, and could serve as a stepping stone to the adoption of non-classical algorithms in finance.

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved
Our business model is applying quantum models to small-molecule drug development. In their quest to identify promising new drug candidates, pharmaceutical firms usually have to screen hundreds of thousands of compounds to select for desired properties. They would like to accelerate this process by designing and testing drugs on the computer, but even small molecules test the limits of conventional devices. Which is where quantum comes in.

We have chosen this application for three main reasons: the relevance of quantum approaches, the size of the market, and the ability to scale and develop the use of quantum algorithms in related areas of drug discovery.

First, quantum approaches are particularly relevant to small-molecule drug design for the simple reason that the compounds are best seen as quantum systems. As Richard Feynman remarked, “Nature isn’t classical, dammit, and if you want to make a simulation of nature, you’d better make it quantum mechanical.” Methods such as the Variational Quantum Eigensolver do exactly this, and can be used to accurately predict key properties such as how the compound will interact with target proteins.

Second, in terms of market size, pharma spends some 15 percent of its sales on research and development, and in fact accounts for about a fifth of global R&D spend. The industry is already heavily computational, and was an early adopter of methods such as systems biology and machine learning. Quantum computing is the logical next step – and will be required for extending the technique to larger molecules such as biologics.

Finally, the drug development process isn’t just expensive, it is also unreliable. Just as most movies or plays don’t turn out to be box-office hits, so most of those very expensive drugs fail at some stage of the development process – in fact, only four percent make it through. Quantum models will help to improve the odds – not just by modelling the drugs themselves, but by using methods such as quantum machine learning to better understand their interaction with the human body at every level. With quantum drug development, small molecules are just the start.


## Step 4: Video Pitch

Research and development in the pharmaceutical industry is dominated by the big multinationals. The following companies earned revenues of over $40 billion in 2020: 
Johnson & Johnson – $56.1bn
Pfizer – $51.75bn
Roche – $49.23bn
Novartis – $47.45bn
Merck & Co. – $46.84bn
GlaxoSmithKline – $44.27bn
Sanofi – $40.46bn

But there is also an ecosystem of small and medium-sized companies involved at various stages in the drug development pipeline. One advantage of in silico quantum modelling is that it will allow these smaller firms to accelerate their programs and compete with the industry behemoths.

[Link to Video](https://drive.google.com/file/d/1-mDDw-R9x9uqQf6TwLwufyW-TbXYnKDj/view?usp=sharing)

![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
