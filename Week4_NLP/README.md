![CDL 2021 Cohort Project](../figures/CDL_logo.jpg)
## Project 4: NLP: Natural Language Processing on a Quantum Computer 

For more details refer to the [Business Application found here](./Business_Application.md)

## Technical Assignment

#working on it

## E1
Our task was trying to generate Chocolate Mousse [Ref](https://www.recipetineats.com/chocolate-mousse/). 

<p align="center"><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f1.png"width=1000/></p>

By swapping the white and yolk, we were able to get foam and choc cream. By combining two choc cream and foam, we were able to generate choc mousse. By far as we understand, this is the first generation of choc mousse in discopy environment. Previous research [link](https://graphicallinearalgebra.net/2015/05/06/crema-di-mascarpone-rules-of-the-game-part-2-and-diagrammatic-reasoning/) already showed generation of Crema di Mascarpone, but the challenge was obtaining Mascarpone in grocery store. Therefore, our work enhanced previous studies by utilizing more accessible product to create choc mousse in discopy environment. 


As we are preparing the choc mouse, we also replicate previous research on tiramisu generation, and successfully recreate multi-layer tiramisu with simple for-loop method. 
<p align="center"><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f2.png"width=1000/></p>
This diagram represents multi-layer structure of tiramisu, which can be easily replicate in average household. One of the main challenge of this work was that often requires large amount of eggs. This challenges was also integrated into our solution where we can easily scable the operation with N number of egg. 


<p align="center"><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f3.png"width=1000/></p>

Our cascade and scalable egg york generation should resolve the challenges with large-egg process, and provide simple and compact solution for future multi-layer tiramisu generation. 

Another challenges for tiramisu generation was language barriers. Many of recipes are based on English, and there is alot of interest in building tiramisu in other platform in different language. As part of the localization project, we have developed our unique French to English translation where we can translate the recipe into French. 

<p align="center"><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f4.png"width=1000/></p>

<p align="center"><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f5.png"width=1000/></p>

Our research is funded by international tiramisu & choc mousse Association (ITCMA). 

## E2



<table align="center">
    <tr>
        <td><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f2o-4.png" width="500"></td>
        <td><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f2o-5.png" width="500"></td>
     </tr>
 </table>
 
As we increase the tensor size, we can see exponetial increase of the time (left). On the right, we have used tensornetwork contractor to reduce the cost of time. From the green trace, we can see significant decrease of the time compare to the normal evaluation method shown in red.

### E3

For this excerise, we accomplish three different generation, bell state, GHZ state, and N-GHZ state. 

<table align="center">
    <tr>
        <td><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/bell-1.png" width="500"></td>
        <td><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/GHZ1.png" width="500"></td>
        <td><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/GHZ2.png" width="500"></td>
     </tr>
 </table>
 
With help by Real IBMQ machine, we were able to generate the probability distribution of those states. From quick calculation, we picked first |00...0> value to calculate the accuracy of the state.

| STate | Accuracy  |
| :---: |  :---: |
| Bell |  81% |
| GHZ |  72% |
| 4-GHZ | 66% |

As we increase the parity, the entangelment decohere. 

## E4

<p align="center"><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f4-1.png"width=1000/></p>

First, we take a look at the japense, we write the sentence Hanako ga tegami o kaita, which means Hanako has wrote a letter, [link](https://aclanthology.org/Y07-1009.pdf).

<p align="center"><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f4-2.png"width=1000/></p>

ġadara ahmad al-madinah, which means ahmad left the city [link](https://www.researchgate.net/publication/326268380_Parsing_Arabic_Verb_Phrases_Using_Pregroup_Grammars).

<p align="center"><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f4-3.png"width=1000/></p>

Then we implement "I see you saw her"

<p align="center"><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f4-4.png"width=1000/></p>

We now want to confirm that our sentense can be used as tensor and verify the truth statement. 

<p align="center"><img src="https://github.com/alice4space/CohortProject_2021/blob/week4/Week4_NLP/figures/f4-5.png"width=1000/></p>


Using the tensor, we further look at the statement including Charlie and Diane. We can evaluate the statement and check the truth statement. 




## E5

## Reference Code

[Tutorial-Part1](qnlp-tutorial-Part1.ipynb)

[Tutorial-Part2](qnlp-tutorial-Part2.ipynb)

[Tutorial-Part3](qnlp-tutorial-Part3.ipynb)

[Tutorial-Part4](qnlp-tutorial-Part4.ipynb)

[Tutorial-Part5](qnlp-tutorial-Part5.ipynb)
