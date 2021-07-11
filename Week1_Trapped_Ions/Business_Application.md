![CDL 2020 Cohort Project](../figures/Slot_machine.png)
# Quantum Cohort Project Week 1 Business Application. Simulating quantum advantage with trapped ions

## Summary of the technical problems solved in the exercise

The goal of this project is to replicate Google's supremacy experiment on Trapped Ions based quantum computers and study the results with a business focus. The random circuit simulation is carried out with a Matrix Product State code and explored the output distribution by plotting them as speckle patterns across different circuit widths and depths. We then studied the effect of errors in 1-qubit gates. Next, we investigate the convergence of a perfect quantum random-circuit to a Porter-Thomas distribution and deviations from these distributions as the 2-qubit gate errors increase.  
To tackle the technical challenge, we followed Google's original experiment in detail along with relevant theoretical methods to understand the quantum advantage hypothesis laid out in their experiment. In particular, we have studied the cross-entropy benchmark (XEB) used to measure the fidelity of the random circuits and how their outputs over a large sample of outcomes converge to Porter-Thomas distribution. We have taken these learnings and applied them to the Julia based Matrix Product State simulator to generate random circuits and extract samples for experiments relevant to different tasks.


## Examples of real-world business applications built around sampling-based quantum computing with random circuits

**- Applied metrology for the slot machines**

Slot machines are the most popular gambling option in casinos. Their simplicity and the appeal of a game of fair chances attract customers resulting in between 65% and 80% of the average casino income in the US [[1]][id1]. And even in 2021, after the infamous events happening these years, the market opportunity for slot machines is still prominent and promises to grow [[2]][id2]. 
In 2018, the global Slot Machines market faced a valuation of $3.23B and the number is projected to reach $4.99B by 2025 [[3]][id3].

In this field, where the chances drive the revenue of the gambling market, the stakeholders have to make sure the machines are providing consistently random outputs.  
We are offering a tool on how to test the machines in a fast and accurate manner by using cutting-edge techniques. The method works as follows: for each outcome of the slot machines, the probability distribution is constructed and samples are randomly collected from multiple machines in real-time. The system then compares the output distribution of the collected samples to the ultimate "perfect" distribution (the Potter-Thomas distribution). If the calculated so-called "randomness factor" deviates from the recommended value, the system reports a case for investigation. This automated service is proven to protect slot machine providers from malfunctions, errors and frauds and will guarantee trustworthy, compliant and profitable operations.  

## Potential customers in these areas

**- Casinos**

* MGM Resorts International ($5.16B in revenues in 2020 and $12.9B in 2019)
* Las Vegas Sands ($3.61B in revenues in 2020 and $13.74B in 2019)
* Wynn Resorts ($2.1B in revenues in 2020)
* Caesars Entertainment ($3.47B in revenues in 2020)
and others

**- Slot machines manufacturers**

The manufacturers market is highly saturated. Key slot machine manufacturers include:
* Scientific Games ($2.72B in revenues in 2020)
* IGT ($2.64B in revenues 2020)
* Aristocrat Leisure ($4.1B in revenues in 2020)
* Novomatic (€0.67B in revenues in 2020)
* Konami Gaming (total revenue for the fiscal year ending on March 31, 2021 is $2.48B)

**- Gaming Control Boards**

For the US, each state is governed by different regulations. As a result, agencies respective to each state in particular are operating within the borders, i.e. Nevada Gaming Commission and Control Board, New York State Gaming Commission, New Jersey Casino Control Commission and Division of Gaming Enforcement etc.

## Presentation of the value proposition of our innovation to the potential customer

[![IMAGE ALT TEXT](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=CEDotbqWZpM "CDL Cohort 2021 Week 1 Group 4")


[id1]: https://www.forbes.com/sites/davidschwartz/2018/06/04/how-casinos-use-math-to-make-money-when-you-play-the-slots/?sh=ecd88ae94d09
[id2]: https://marketbusinessnews.com/the-slot-machine-market-is-going-higher-and-higher/256115/
[id3]: https://www.marketwatch.com/press-release/global-slot-machines-market-2021-2025-with-top-countries-data-industry-size-share-business-growth-revenue-trends-market-demand-penetration-and-forecast-2021-04-14

