![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application of Unit-Disk Maximum Independent Set for Protein Folding

Unit-Disk Maximum Independent Set (UD-MIS) is an NP-hard problem represented as a graph optimization problem. The graph has a constraint that the distance between two vertices should be greater than a unit distance—this constraint models multiple real-world issues ranging from atomic physics to the communication industry. As the UD-MIS problem is NP-hard, many real-world problems with the domain constraint can be mapped into this simple model: wildlife distribution and packing, for example. Rydberg atoms naturally carry the model Hamiltonian of UD-MIS that can simulate the corresponding optimization problem. In this report, we propose applying the UD-MIS-Rydberg-Atom simulator to protein folding optimization processes.                    

## Step 1: Explain the technical problem you solved in this exercise

By mapping the optimal cell phone tower problem to a quantum annealing problem of a spin Hamiltonian via the UD-MIS representation, we were able to find the optimal cell phone tower configuration.  

## Step 2: Explain or provide examples of the types of real-world problems this solution can solve

Example: protein folding, wildlife distribution, packing problem (e.g., wood- glass- paper- industries), optimal CCTV locations, optimal distribution of franchise stores or warehouses, etc.

"Protein folding is a process by which a polypeptide (amino acids) chain folds to become a biologically active protein in its native 3D structure. 
The amino acids in the chain eventually interact with each other to form a well-defined, folded protein. The amino acid sequence of a protein determines its 3D structure." (https://www.news-medical.net/life-sciences/Protein-Folding.aspx)
![Protein structure folding stages - LadyofHats, commons wikimedia org _thumb](https://user-images.githubusercontent.com/87050306/125888404-5037f379-4c7e-444f-8fd6-24b67a677821.png)

"Protein folding is in relation to the protein biological function. At the coarsest level, folding involves first the establish- ment of secondary structures, particularly alpha helices and beta sheets, and only afterwards tertiary structure. Actually, the greatest open problem in Structural Bioinformatics is the 3D protein structure prediction from its primary structure. Since the protein folding problem is still unsolved, a typical alternative approach is to identify a set of sub-problems, such as the prediction of protein secondary structures, solvent accessibility and/or prediction of residue contacts and try to search specific solutions. Among different possibilities, the prediction of contact maps of proteins starting from the protein chain is particularly promising, since a partial solution of it can significantly help the prediction of the protein structure. 
Having at hand a contact map a reliable and fast re-construction procedure of the 3D structure is needed. The problem is equivalent to unit disk graph realization which has been proved to be NP-hard." (https://link.springer.com/chapter/10.1007/978-3-540-72031-7_53#citeas)

So far, lattice protein folding models have been tested by a quantum annealing device. This report proposes constructing a protein folding model, which combines the lattice and the contact map-unit-disk-graph models, for the quantum annealing optimization simulation. (https://www.nature.com/articles/srep00571)   

## Step 3: Identify at least one potential customer for this solution - ie: a business who has this problem and would consider paying to have this problem solved

Examples: 
- pharmaceutical company
- government
- franchise company
- wood- glass- paper- industries

## Step 4: Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language

[Business Application video can be found here](./week2_businessapplication_small.mov)
