#### The baseline

Our baseline will be the proposed anneling schedule

![equation](https://latex.codecogs.com/svg.image?T&space;=&space;T_i&space;*&space;(\frac{T_f}{T_i})^{(\frac{t}{N})})

To benchmark the annealing schedule we can check the value of the energy at the end of each iteration and see how many iterations we have to reach the ground state energy, in the baseline we have

<table><tr>
    <td><img src="./figs task 1/Baseline_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the proposed annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/Baseline_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the proposed annealing schedule </figcaption></td>
    </tr>
</table>

It takes a bit of iterations but eventually around the iteration 70 it got to the ground state. We can also see how the occupations change throughout the iterations, we sample 4 different iterations to plot the graphs with the occupation states (right figure).

#### Frange cycle

The range cycle dynamically change the proposed values for the temperature in a way that resembles a saw tooth, we got the following results from this schedule:

<table><tr>
    <td><img src="./figs task 1/FrangeCycle_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the frange cycle annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/FrangeCycle_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the frange cycle annealing schedule </figcaption></td>
    </tr>
</table>

Although the frange cycle can be interesting it does not reach the ground state in the desirable timeframe. 

#### LAMBDA annealing

In this annealing scheme we have:

![equation](https://bit.ly/2Up3d2e)

with k runing over the number of iterations and Lambda as the decay constant.

We got the following results from this schedule:

<table><tr>
    <td><img src="./figs task 1/Lambda_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the LAMBDA annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/lambda_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the LAMBDA annealing schedule </figcaption></td>
    </tr>
</table>

Quite good, we reach the ground state around iteration 17, can we do better?

#### Multiplicative annealing

We can use Multiplicative annealing:

![equation](https://bit.ly/3iirkYp)

with k runing over the number of iterations and Gamma as the decay constant.

with the following results:

<table><tr>
    <td><img src="./figs task 1/Multiplicative_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the Multiplicative annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/Multiplicative_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the Multiplicative annealing schedule </figcaption></td>
    </tr>
</table>

Thats quite fast!!!, we reach the ground state at iteration 3.

#### Step annealing

This schedule decays the temperature by gamma every step_size iteration. 


we got the following results from this schedule:

<table><tr>
    <td><img src="./figs task 1/Step_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the Step annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/Step_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the Step annealing schedule </figcaption></td>
    </tr>
</table>

#### MultiStep annealing

This schedule is similar to the Step annealing, however the temperature decays everytime when the iteration reach some milestone


and we have:

<table><tr>
    <td><img src="./figs task 1/MultiStep_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the MultiStep annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/MultiStep_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the MultiStep annealing schedule </figcaption></td>
    </tr>
</table>

that aint a good one, lets check another schedule

#### Exponential annealing

In this schedule the temperature decays by a factor (gamma) every iteration (k). 

![equation](https://bit.ly/3zb4tom)

and we have:

<table><tr>
    <td><img src="./figs task 1/Exponential_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the Exponential annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/Exponential_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the Exponential annealing schedule </figcaption></td>
    </tr>
</table>

thats really fast, however I think this must be because the temperature decays too fast.

#### CosineAnnealing

This schedule works by setin the temperatures using a cosine annealing, where $T_{max}$ is set to the initial temperature and $T_{cur}$ is the number of iterations since the last restart.

![equation](https://bit.ly/3evH9Kq)


we got:

<table><tr>
    <td><img src="./figs task 1/CosineAnnealing_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the Exponential annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/CosineAnnealing_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the Exponential annealing schedule </figcaption></td>
    </tr>
</table>

Quite unstable, lets move on to the next schedule.

#### Cyclic annealing

In this schedule the temperatures are set according to cyclical learning rate policy (CLR). The policy cycles the tempearture rate between two boundaries with a constant frequency, as detailed in the paper [Cyclical Learning Rates for Training Neural Networks](https://arxiv.org/abs/1506.01186). The distance between the two boundaries can be scaled on a per-iteration or per-cycle basis.

##### "triangular": A basic triangular cycle without amplitude scaling.
<table><tr>
    <td><img src="./figs task 1/CyclicTriangula_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the Cyclic triangular annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/CyclicTriangula_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the Cyclic triangular annealing schedule </figcaption></td>
    </tr>
</table>

##### "triangular 2": A basic triangular cycle that scales initial amplitude by half each cycle.
<table><tr>
    <td><img src="./figs task 1/CyclicTriangula2_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the Cyclic triangular 2 annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/CyclicTriangula2_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the Cyclic triangular 2 annealing schedule </figcaption></td>
    </tr>
</table>


##### "exp_range": A cycle that scales initial amplitude by $\text{gamma}^{\text{cycle iterations}}$ iterations at each cycle iteration.
<table><tr>
    <td><img src="./figs task 1/CyclicExp_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the Cyclic exp_range annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/CyclicExp_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the Cyclic exp_range annealing schedule </figcaption></td>
    </tr>
</table>

The best out from the three displayed is the Cyclic exp_range, although is not quite as good the previous contenders.

#### OneCycle 

This schedule sets the temperature according to the 1cycle policy. The 1cycle policy anneals the temperature from an initial value to some maximum temperature and then from that maximum temperature to some minimum value much lower than the initial temperature. This policy was initially described in the paper [Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates](https://arxiv.org/abs/1708.07120).

##### "OneCycle - cos"
<table><tr>
    <td><img src="./figs task 1/OneCycle_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the OneCycle annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/OneCycle_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the OneCycle annealing schedule </figcaption></td>
    </tr>
</table>

##### "OneCycle - linear"
<table><tr>
    <td><img src="./figs task 1/OneCycleLinear_annealing.png" style="width: 350px;"><figcaption> <font size="3">Energy history using the OneCycle linear annealing schedule </figcaption></td> 
    <td><img src="./figs task 1/OneCycleLinear_occupations.png" style="width: 250px;"><figcaption> <font size="3">Occupation states history using the OneCycle linear annealing schedule </figcaption></td>
    </tr>
</table>

Interesting effects but not quite good as we want.
