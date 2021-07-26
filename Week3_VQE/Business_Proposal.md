![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Using Vibrational Excitations to Separate Molecules

<p align="center">
  <img height=250 width=300 src="https://lh3.googleusercontent.com/proxy/VR-QHyYQf8z2JKChe0SMfZuBj0BZBRDEQh1sOK8vPVJqGLBBKLVM0GIzGSHTvcvshWPO0chq3Jx1jABJ_LxownQAnJ7a6C-8QrSS">
 </p> 


## Introduction

Q is specializing in using quantum technology for modelling vibrational excitations in the molecules. Our technology can have tremendous effect on variety of fields such as optics, ecology and drug design. For the purposes of this presentation we will focus on how knowing molecular vibrations is going to help separate  molecule of methane CH<sub>4</sub> molecule into methyl radical CH<sub>3</sub>. We use classical methods to find the energy minimum of the ground state of a molecule and Variational Quantum Eigensolver to find the energy of an excited state at the ground state minimum. The difference between these variables is proportional to the amount of light required to separate single hydrogen molecule from the remaining CH<sub>3</sub> molecule. 

## Technical Description

We will be using classical computer to find out the lowest energy level of the ground state of the methane molecule. We are then going to use a quantum computer find the lowest energy level of the excited state of the methane molecule. Crucially, coordiantes of the 3 hydrogen molecules and one carbon molecule will be fixed, while we perform energy measurements of the molecule at different bond lengths of the "top" hydrogen molecule. 

Our idea starts by putting the CH<sub>4</sub> molecule in the fixed and symmetric position, that puts the hydrogen molecule on the Z-axis. This will enable us to continuosly pull it across one axis until we find the lowest energy level. We have used Hartree-Fock, CCSD, CISD and FCI methods to plot the energy levels at different bond lengths to identify that minimum, which occurs at the bond length of roughly `1.09`.

<img src = "./business_proposal/ch4_dissociation.png"> </img>

In principle, our methods can be applied to any molecule, but we are limited by the number of qubits for some systems. In the case of a CH<sub>4</sub> molecule, we have run the following code using that produces the Hamiltonian of the molecule and the amount of qubits required for the VQE.

```py
symbols = ["C", "H", "H", "H", "H"]
coordinates = np.array([0.0, 0.0, 0.0, 
                        0.0, 0.0, 1.089, # the Z coordinate for the top hydrogen molecule determined from classical methods
                        1.026719, 0, -0.363, 
                        -0.51336, -0.889165, -0.363, 
                        -0.51336, 0.889165, -0.363])

H, qubits = qchem.molecular_hamiltonian(symbols, coordinates) 
print(f"Number of qubits = {qubits}\n")
print(f"H = {H}")
```

Unfortunately, we do not have access to the Quantum Computer with 18 qubits, however if we had an access to some commercial backends such as `ibmq_montreal` we would be able to run the eigensolver and get the energy level of the excited state. Once we found the energy level of the excited state we can also compute other important components such as: Normal modes of the ground electronic state/excited electronic state, Atomic coordinates of the ground electronic state/excited electronic state, and Vibrational frequencies of the ground electronic state/excited electronic state. We can do it by finding out a Hessian of the Hamiltonian.

@Rodrgio: add stuff about Hessians

However, we can also utilize a faster approach. We can use VQE to calculate the lowest energy level of the excited electronic state of the CH<sub>4</sub> molecule and simply subtract it from the lowest energy level of it's ground electronic state. The difference will be proportional to the amount of light that needs to be applied to break the bond between the top hydrogen molecule and the rest of the CH<sub>4</sub> molecular structure.

## Business Pitch

We have found a revolutionary way of severing chemical bonds in the methane molecule. For example, our innovative idea enables us to transform a gasous methane molecule into the radical CH<sub>3</sub> molecule. 

