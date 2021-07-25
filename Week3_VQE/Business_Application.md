![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)

# VQE Basics

We first explain the basics of the VQE method for someone that does not have familiarity with quantum chemistry.

At the quantum level behavior of particles can be described by the Schrodinger's equation. 

![fig1](./resources/fig1.png)

This equation describes the evolution of a quantum state. 
One can think of this as energy functions we are familiar with that include kinetic energy and potential energy.

We are familiar with the dynamics at the macro level of a pendulum through laws of motion. However, the pendulum can also be represented as an energy function with Kinetic and Potential energy terms ensuring conservation of energy.

![fig2](./resources/fig2.png)

A particle can be represented as bounded in a well. This particle according to Schrodinger's equations will have solutions that represent the probabilities of where the particle is found. There are solutions which are also the eigenvalues are shown below.

![fig3](./resources/fig3.png)

In order to solve the Hamiltonian H that has components H1,H2 that do not commute (i.e. a x b != b x a), we take incremental steps based on the Lie formula. This process called Trotterization is used later. 

![fig4](./resources/fig4.png)

Charged particles create potential energy based on Coulomb's law.

![fig5](./resources/fig5.png)

The same is the case for particles where the proton is positively charged and the electron is negatively charged.

![fig6](./resources/fig6.png)
![source](https://www.southampton.ac.uk/assets/centresresearch/documents/compchem/DFT_L2.pdf)

Below is a simple representation of the Hamiltonian of the Helium atom which has an atomic number of 2. The kinetic and potential terms are shown. Various approximations may be made (for example the Born-Oppenheimer approximation that the nucleus is stationary relative to the electrons). 

![fig7](./resources/fig7.png)

We will see that this energy equation is then converted into Pauli rotations for quantum gates in Step #2 using Jordan-Wigner (jw) or Bravyi-Kitaev (bk) methods.

![fig8](./resources/fig8.png)
![source](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.6.031007)

Further simplifications based on Hamiltonian symmetries are used to produce even simpler set of gates that can be implemented on our NISQ hardware.

We next look at the actual implementation of Unitaries on quantum computers. in Step #3. The figure below shows a high level of steps from classical preparation to solving functions on both annealing and gate quantum computers. Annealing requires conversion to a Binary Quadratic Model (BQM), while gate computers require the use of an initial starting energy function or Ansatz along with hybrid classical-quantum algorithms called Phase Estimation Algorithm (PEA) or Variational Quantum EigenSolver (VQE).

![fig9](./resources/fig9.png)
![source](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.6.031007)

In VQE we start with a set of parameters (values of angles) that we will first calculate in Step #3. Then we will prepare the initial state and measure the expectation value of the Hamiltonian in the desired basis (for example stog3) in step #4. 

![fig10](./resources/fig10.png)

The figure below shows a summary of the steps taken in VQE 

![fig11](./resources/fig11.png)

![source](https://arxiv.org/abs/1512.06860)

![additional reference](https://iopscience.iop.org/article/10.1088/1367-2630/18/2/023023/meta)

Below we will use this basic concepts to show actual run of H2 and LiH using the Tequila library

# Technical Problems Solved



# Type of real-world problems that can be solved


# Quantum Cohort Project Business Application

## Introduction

We are LightQ. We build beautiful and efficient, organic light-emitting diodes (OLED) accross North America. Our secret-sauce is the use of the variational quantum eigensolvers to determine the ground and excited energy states of industrially relavent molecules such as Tris(8-hydroxyquinolinato)aluminium[[1]](https://en.wikipedia.org/wiki/OLED). This allows us to create thermally activated delayed fluorescence (TADF) emitters suitable for OLED application with potentially 100% quantum efficiency [[2]](https://www.nature.com/articles/s41524-021-00540-6).

![logo](./resources/logo.png)

## OLED Industry Overview

OLED technology is used to create digital displays in all kinds of devices. These devices range from television screens, computer monitors, smartphones and even handheld game consoles [[1]](https://en.wikipedia.org/wiki/OLED). Since more people are working from home than ever, this industry is absolutely booming [[3]](https://www.oled-info.com/dscc-increases-its-oled-market-forecasts-it-sees-increased-adoption-phones). According to Display Supply Chain Consultants (DSCC), the expected 2021 revenue for the OLED market is at $42.5 billion dollars but is growing fast to $60.6 billion in 2025  [[3]](https://www.oled-info.com/dscc-increases-its-oled-market-forecasts-it-sees-increased-adoption-phones).

![logo](./resources/tech-stuff.jpeg)


<p align="center">
  <a href="https://www.velocitas.com/industry-news/dominating-the-lead-gen-game-landing-pages_new/" target="_blank">Source</a>
</p> 

The laptop market is absolutely huge, and is something that LightQ will tap into. Since we build leading OLED displays, deals with huge venders like Apple, Lenovo, HP and Dell are currently underway. DSCC has already seen 5 million OLED laptop displays shipped in 2021 [[3]](https://www.oled-info.com/dscc-increases-its-oled-market-forecasts-it-sees-increased-adoption-phones). Furthermore, the anticipate serious growth in the upcomming years, predicting 8 million in 2022, and over 11 million in 2025. Total revenues will reach over $1 billion in 2023 [[3]](https://www.oled-info.com/dscc-increases-its-oled-market-forecasts-it-sees-increased-adoption-phones). We summarize these results in the following table.

| Year | Laptop OLED Displays in Production|
| :--------------: | :---------: 
| 2021 | 5 million |
| 2022 | 8 million |
| 2025 | 11 million |


DSCC is also anticipating that Apple will introduce their first OLED tablet in 2023. This year alone, DSCC has seen 4.5 million tablet OLED displays in production. They are forcasting that this unmber will grow to 16 million in 2025. This mean that tablet OLED shipment growth will be approximately 37% CAGR. Additionally, they estimate that revenues will grow at 34% CACR [[3]](https://www.oled-info.com/dscc-increases-its-oled-market-forecasts-it-sees-increased-adoption-phones). These amazing results are summarized in the table below.

| Year | Tablet OLED Displays in Production|
| :--------------: | :---------: 
| 2021 | 4.5 million |
| 2022 | 5.7 million |
| 2024 | 14 million |
| 2025 | 15 million |

As a leading manufacturer in OLED, LightQ is starting early talks with Apple and other leading tablet and laptop manufacturers to produce the best displays for the growing tablet market. 

<p align="left">
  <img src="./resources/DSCC-oled-market.jpeg" width=500/>
  <a href="https://www.oled-info.com/dscc-increases-its-oled-market-forecasts-it-sees-increased-adoption-phones" target="_blank">Source</a>
</p> 

## Real World Problems a Quantum Variational Eigensolver can Solve

We outline a few real world problems the quantum variational eigensolver can potentially solve that are not strictly related to LightQ's business pitch.

- Producer of efficient organic light-emitting diodes (OLED). OLEDs are used to create digital displays in devices such as televisions, smartphones, computer monitors etc. We use the methods outlined in this repository (VQEs etc) to determine ground and excited state energies of industrially relevant molecules. This allows the thermally activated delayed fluorescence (TADF) emitters suitable for OLED application to potentially perform with 100% quantum efficiency [[4]](https://www.nature.com/articles/s41524-021-00540-6).

- Efficient producer of fertilizer. We model the biological nitrogen fixation by the enzyme nitrogenase which we can use to create fertilizer. This method is much preffered over the traditional Harber-Bosch method because the latter requires high temperature and pressure and is therefore very energy-intensive [[5]](https://www.pnas.org/content/114/29/7555). We use the methods in this repository to elucidate the reaction mechanism of biological nitrogen fixation in notrogenase [[5]](https://www.pnas.org/content/114/29/7555) which is crucial in using it to create fertilizer. 

- Creating next-generation lithium-sulfur batteries. We are able to simulate the next-generation of battery technology using the techniques in this repository. Lithium-sulfu batteries are theoretically much stronger and more efficient than traditional batteries, however, the reaction mechanism for the sulfur reduction in the battery environment is in much debate in the scientific field [[6]](https://arxiv.org/pdf/2001.01120.pdf). We use the the methods outlined in this repository to model the electon-cloud density distribution of molecules and in particular their dipole moment (which are very important to understand the feasibility of these batteries)[[6]](https://arxiv.org/pdf/2001.01120.pdf) to eventually create the next generation of batteries!

## Potential Customers

We have done an in depth analysis of some potential customers for LightQ's OLED technology. They are summarized in the below table.

|Company name|Country|R&D budget-2020↑|Profit-2020|
|----|----|----|----|
| Apple Inc. | USA | $18.75 billion | $59.7 billion |
| Dell | USA | $4.4 billion | $92.15 billion |
| Lenovo | China | $1.43 billion | $50 billion |
| HP | USA | $1.48 billion | $56.6 billion |

## Business Pitch

[![Video](./resources/video-cover.png)](https://drive.google.com/file/d/1EHxNry_KGci-1Ssjv0kMTpVQdF3DyLml/view?usp=sharing "Business Pitch")

If the above video does not work, find it in [google drive](https://drive.google.com/file/d/1EHxNry_KGci-1Ssjv0kMTpVQdF3DyLml/view?usp=sharing).



## References

1. https://en.wikipedia.org/wiki/OLED
2. https://www.nature.com/articles/s41524-021-00540-6
3. https://www.oled-info.com/dscc-increases-its-oled-market-forecasts-it-sees-increased-adoption-phones
4. https://www.nature.com/articles/s41524-021-00540-6
5. https://www.pnas.org/content/114/29/7555
6. https://arxiv.org/pdf/2001.01120.pdf