# Cohort Project Week 4 (Team 8)
![logo](./images/logo.png)

# Table of contents
1. [Introduction](#introduction)
2. [Tensors as boxes](#paragraph2)
3. [Drawing Quantum Circuits](#paragraph3)
4. [Drawing Grammatical Structure](#paragraph4)
5. [Putting it all together: QNLP](#paragraph5)


## Introduction <a name="introduction"></a>

In this Cohort project, we implement quantum natural machine learning with [`discopy`](https://github.com/oxford-quantum-group/discopy) and [`pytket`](https://github.com/CQCL/pytket). We solve all the exercies in the `qnlp-tutorial` [notebook](https://github.com/oxford-quantum-group/discopy/blob/main/docs/notebooks/qnlp-tutorial.ipynb).

Solution Notebooks:

Tasks 1 to 4: [`qnlp_tutorial_solution_Tasks_1_to_4.ipynb`](./qnlp_tutorial_solution_Tasks_1_to_4.ipynb)

Task 5-1: [`qnlp_tutorial_solution_Task5-1.ipynb`](./qnlp_tutorial_solution_Task5-1.ipynb)

Task 5-2: [`qnlp_tutorial_solution_Task5-2_SWAP_test.ipynb`](./qnlp_tutorial_solution_Task5-2_SWAP_test.ipynb)

## Installation Guide

To run the notebooks in this project, create a new conda environment to install the essential packages.

```
conda create -n env_name
conda activate env_name
```
Then install the following packages by

```
conda install python
pip install discopy
pip install pytket
pip install pytket-qiskit
pip install tensornetwork
```
<a name="paragraph1"></a>

![task4](./images/exercise1.png)

----Add images if needed (put the images in ./images/)---

**Exercise 1-1:** Draw your favorite cooking recipe as a diagram. You'll want to keep your ingredients in order if you want to avoid swapping them too much.

- We create a four eggs omelette recipe with vegetables/bacon and cheese options.

![img1-1-1](./images/img1-1-1.png)

**Exercise 1-2:** Define a function that takes a number `n` and returns the recipe of a tiramisu with `n` layers of crema di mascarpone and savoiardi.

- add description

![img1-2-1](./images/img1-2-1.png)


**Exercise 1-3 (harder):** Define a function that takes a number `n` and returns the recipe for cracking `n` eggs.

- add description

![img1-3-1](./images/img1-3-1.png)

**Exercise 1-4:** Define a functor that translate your favorite language to English, try composing it with `english2french`.

- add description

![img1-4-1](./images/img1-4-1.png)


**Exercise 1-5:** Define a `french2english` functor, check that it's the inverse of `english2french` on a small example.

- add description


![img1-5-1](./images/img1-5-1.png)
![img1-5-2](./images/img1-5-2.png)

<a name="paragraph2"></a>

![task2](./images/exercise2.png)

**Exercise 2-1:** Check out the [diagram rewriting](https://discopy.readthedocs.io/en/main/notebooks/rewriting-diagrams.html) notebook to learn how to remove snakes from a diagram. This can greatly speed up the evaluation of tensor diagrams!

- add description

![img2-1-1](./images/img2-1-1.gif)
![img2-1-2](./images/img2-1-2.gif)
![img2-1-3](./images/img2-1-3.gif)


**Exercise 2-2:** Define a function that takes a number `n` and returns the diagram for a [matrix product state](https://en.wikipedia.org/wiki/Matrix_product_state) (MPS) with `n` particles and random entries. Check how the evaluation time scales with the size of the diagram. 

**Exercise 2-3:** Pip install the [tensornetwork](https://pypi.org/project/tensornetwork/) library and use it to contract the MPS diagrams more efficiently. This is done with the syntax `diagram.eval(contractor=tn.contractor.auto)`, see the [docs](https://discopy.readthedocs.io/en/main/_autosummary/discopy.tensor.Diagram.html#discopy.tensor.Diagram.eval).

![img2-2-1](./images/img2-2-1.png)

- For Exercies 2-2 and 2-3, we define a function returning the diagram for a matrix product state with a size `n`. The diagram for `n` = 5 is shown above. We also compare the evaluation time between `DisCoPy` and `tensornetwork` with respective to the size of the diagram. As shown below, the evaluation time for the discopy significantly increases as `n` > 8. However, `tensornetwork` performs much efficiently at higher diagram size.

![img2-2-2](./images/img2-2-2.png)

<a name="paragraph3"></a>

![task3](./images/exercise3.png)

**Exercise 3-1:** Run your own Bell experiment on quantum hardware! You can use IBMQ machines for free, if you're ready to wait.
**Exercise 3-2:** Draw a circuit that evaluates to the GHZ state 
$\frac{1}{\sqrt{2}} (|000\rangle + |111\rangle)$.
**Exercise 3-3 (harder):** Define a function that takes a number `n` and returns a circuit for the  state $\frac{1}{\sqrt{2}} (|0...0\rangle + |1...1\rangle)$.

- In this exercise we use `pytket` to convert the `discopy` circuit diagram for the Bell state (see below) and access the IBMQ backend `bogota` to measure the Bell state. 
![img3-1-1](./images/img3-1-1.png)

The result shows that $|00\rangle$ and $|11\rangle$ states have nearly equal probabilities.

![img3-1-2](./images/img3-1-2.png)

-In

![img3-2-1](./images/img3-2-1.png)
![img3-2-2](./images/img3-2-2.png)

![img3-3-1](./images/img3-3-1.png)
![img3-3-2](./images/img3-3-2.png)

<a name="paragraph4"></a>

![task4](./images/exercise4.png)

In task4 we were charged with drawing the grammatical structure of sentences using diagrams. There we several exercises which tested this ability. For example, in one task we drew the diagrm to the sentence "Alice loves Bob" in japanese (where the sentence structure is not subject-verb-noun).

![4.1](./images/4.4.png)

We implemeted the same sentence in arabic, where the sentence is read right to left.

![4.2](./images/4.3.png)

We were also tasked with implementing a sentence from Lambek's classic paper. We chose the sentence, "cannibals prefer men to pork".

![4.3](./images/4.2.png)

These tasks were more focused on practicing the drawing of the diagrams. The next three tasks enabled us to see how we could pry the grammatical structure from the diagrams. For example, we first had to draw our favourite sentence and evaluate it as a tensor. We chose the sentence 'Batman is serious' (as a parody of the famous line from the Joker- why so serious). So we evaluated the sentence: who is serious?- and we obtained the correct response of Batman.

![4.5](./images/4.5.png)

next, we created a 4 noun wordspace with 4/5 of our group members. We added further difficulty by enabling interactions between multiple members of the noun space. For example, Eli and Yuval like eachother, but Eli and Ming are not so friendly:

![4.6](./images/4.6.png)

![4.7](./images/4.7.png)

The final exercise for task4 had us evaluating the question 'Does Alice love Bob'. Here is a diagram of the question; it's a normalized diagram, since the word 'does' isn't contributing any grammatical structure to the sentence.

![4.7](./images/4.8.png)

By looking in the notebbok you can confirm we obtain the correct response of 'yes' for this task.

<a name="paragraph5"></a>

![task5](./images/exercise5.png)

Our first exercise for task5 was to train a QNLP model using circuits to answer the types of questions (such as 'Does Alice love Bob') seen in task4. We were able to efficiently create the diagrams and circuits in this task. To supplement this task, we also included a classical NLP model, which can be seen in [this notebook](Classical_NLP.ipynb). Implementations of exercise 1 from Task 5 are found here and also in [this notebook](task5_implement2.ipynb)


In our second exercise for task5 we were required to create a SWAP circuit to answer the question, 'Does Alice love Bob'. This is implemented in....


For more details refer to the [Business Application found here](./Business_Application.md)
 
![joke](./images/nlp.png)
 
   
   
 
  
  
