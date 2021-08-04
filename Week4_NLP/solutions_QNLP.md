![CDL 2021 Cohort Project](../figures/CDL_logo.jpg)
# Project 4: QNLP pipeline solution

**Reference Code** can be foun in [this notebook](./QNLP_notebook.ipynb)

## The Problem and the Data
The problem we are going to solve is to build a model to classify sentences into "True" or "False" on a limited semantic space. Namely we are going to fight the flat earth theory. We have a set of sentences some are true and some are False, some examples are shown below.

**FALSE** Flat earth theory:
* Earth is flat
* Arctic is in the center
* Sun revolves around Earth

**TRUE** Reality :
* Earth is round
* Arctic is the North Pole
* Earth revolves around the Sun

<center>
<table>
        <tr>
            <td><img src="imgs/10_histogram.png"></td>
        </tr>
</table>
</center>

Our initial Idea was to work on the above dataset but the complexity of the task lead us to reduce it to a simpler problem with 7 nouns ('Earth', 'Antartic', 'Artic', 'north', 'south', 'flat', 'round') and one verb ('is'). We created a tool to easily label training data manually and store it, with two options : brute force or random. We use the Brute Force one for the Training.=, which means we have all the combination of word x word = 7 x 7 = 49.

## From Diagrams to Quantum Circuits

We define an ansatz for 

* **Nouns** with three real parameters reprenting the three Euler rotations Rx(p0) >> Rz(p1) >> Rx(p2). An example with random parameters is shown for the Noun "Earth", with the diagram on the left and the quantum circuit on the right.
<center>
<table>
        <tr>
            <td><img src="imgs/22_earth.png"></td>
            <td><img src="imgs/21_earth.png"></td>
        </tr>
</table>
</center>

* **Verbs** more specifically the only transitive verb in our semantic space "is". We define a generic U4 unitary as an ansatz with six real parameters. The verb is is shown below, with the diagram on the left and the quantum circuit on the right.
<center>
<table>
        <tr>
            <td><img src="imgs/31_is.png"></td>
            <td><img src="imgs/32_is.png"></td>
        </tr>
</table>
</center>

A **sentence** is done composing a Noun with a Verb with a Noun, an example is shown below, with the diagram on the top and the quantum circuit on the bottom.
<center>
<table>
        <tr>
            <td><img src="imgs/41_sentence.png"></td>
        </tr>
        <tr>
            <td><img src="imgs/42_sentence.png"></td>
        </tr>
</table>
</center>

## Training Process

There is a class imbalance between the True sentences (13) and the False sentences (36). We take 9 samples (~75%) of each class as training data. We therefore have 18 samples for training and 31 for testing. Training data examples :
- Earth is round :  1
- round is Earth :  1
- Antartic is Antartic :  1
- north is north :  1
- flat is flat :  1
- Antartic is south :  1
- south is Antartic :  1
- round is round :  1
- north is Artic :  1
- Artic is Antartic :  0
- Earth is Antartic :  0
- flat is round :  0
- south is round :  0
- north is Earth :  0
- south is north :  0
- Earth is flat :  0
- Antartic is flat :  0
- flat is Artic :  0

We define the loss function to optimise as the Binary Cross Entropy, which is very common for binary classification task. Essentially for data point we add the logarithm of the probability of guessing the label right. It yields the following formula, where yt are the true labels and yp are the predicted label :

C = - ( yt * log(yp) + (1 - yp) * log ( 1- yp ) )

An additional metric we monitor is the accuracy, which is essentially  the percentage of correctly guessed labels.

On the below graph we show how this metrics progress as iterations go by, for the training set on the left and the testing set on the right

<center>
<table>
        <tr>
            <td><img src="imgs/51_train.png"></td>
            <td><img src="imgs/52_test.png"></td>
        </tr>
</table>
</center>

Even though the testing test shows overall a lower accuracy, there is no obvious overfitting, and the optimisation algorithm shows a reasonable convergence.

## Results Display and Analysis

As a result of the training process we have learned rotation parameters for each word. In particular each Noun is encoded into a generic 1-qubit state, in the form psi = a |0> + b |1>. We can display any qubit into the bloch sphere (on the left in the figure below). We evaluate the diagram for each Noun and map the resulting qubit encoding to the bloch coordinates for each noun. The results are plotted it in the diagram below, in a projection chosen by hand that shows the best information
<center>
<table>
        <tr>
            <td><img src="imgs/61_bloch.png"></td>
            <td><img src="imgs/60_word_circle.png"></td>
        </tr>
</table>
</center>

. What we can observe as general rules of thumb is that :
1. similar concept are close together (e.g. "earth" is close to "round", "Artic" is close to "North")
2. opposite concepts are on the oposite side of the circle (e.g. "north" is away from "south", "round" is away from "flat"
3. unrelated concepts are orthogonal (e.g. "earth "and "north", "antartic" and "flat")

We also display the similarity between all words in the heatmap below
<center>
<table>
        <tr>
            <td><img src="imgs/70_matrix.png"></td>
        </tr>
</table>
</center>

## Discussion
degrees of freedom.
not complex grammar structures










