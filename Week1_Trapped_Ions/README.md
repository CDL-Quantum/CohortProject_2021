![CDL 2020 Cohort Project](../figures/CDL_logo.jpg)
## Project 1: Quantum Advantage with Trapped Ions 

## Technical Tasks 
* Simulating a random circuit with a Matrix Product State code, and producing a speckle pattern.
* Adding a single bit-flip error and exploring the change in the speckle pattern.
* Exploring convergence of the Porter-Thomas Distribution.
* Exploring the effect of 2-qubit gate errors.
[https://github.com/stared/CohortProject_2021/blob/main/Week1_Trapped_Ions/Project_week1_Team9.ipynb] (https://github.com/stared/CohortProject_2021/blob/main/Week1_Trapped_Ions/Project_week1_Team9.ipynb)

## Business Task
Describe a business that could be build around random circuits.

The underlying objective of the project relates to quantum advantage. Random number generation is routinely done classically, and when computational costs trump the true randomness of the algo, then pseudo-random number generators suffice. If you rely on true RNG however, for cryptography for instance, than a true RNG should never produce a given random bit string in a deterministic manner, either by manipulating it’s input, or by waiting a given amount of time before the RNG cycles back and repeats itself. This is why if a given RNG is flawed and not producing true RNs, then you can predict the crypto keys that were generated and then break into the records they were meant to protect (i.e they are not future proof). 

So where does this project come into play ? It’s in trusting that the RNs come from the right machine. Here is a way to generate RNs drawn for a distribution that is exponentially harder to mimic by a classical computer as the number of qubits N is increased. When N is large enough (> 70 according to S. Aaronson), then it becomes classically intractable to produce the RNs required in a limited amount of time, indirectly proving that the obtained RNs are certifiably more random than what you could be able to do classically under the same circumstances. You can check that the RNs belong to the right distribution if you gather enough of them over time and compute the distribution statistics. If you don’t achieve this a certain threshold after M trials, the more likely it is that the RNs you are receiving are not the good ones and should not be trusted.

The underlying problem is trust in the RNG. So real-world applications will relate to those with trust issues and where trust is paramount. We can think of: 
* polling machines for elections;
* Notarized documents;
* Crypto-currencies;
* Lotteries & casinos;
* CGI image processing : textures and visual effects (ex: blur)
In this case, good RNG allows you to have a random pattern on a very large scale, ie high resolution images or for very large scenery. If the RNG is bad, you’ll see obvious repetitions or structure. In a 4K frame, you have 8M+ pixels so obviously you’ll need to draw a lot of RN to generate a realistic texture even if it only covers a small part of the frame. 

## Business Case

Online gambling is expected to grow to a $US100 billion market by 2025 [https://www.globenewswire.com/en/news-release/2021/04/19/2212384/28124/en/Global-97-69-Billion-Online-Gambling-Market-to-2025-Increasing-Investment-in-Software-and-Technology-and-the-Use-of-Cryptocurrencies.html](GlobeNewsWire). In a land where transaction security and anonimity is prime, cryptographic currencies and security measures are put into place to make gamblers feel more safe while playing. While the gamer can easily trust the banking transactions, how can he trust that the online casino is fair play ? Dishonest online casinos are legion on the interwebs [https://www.casino.org/blacklisted/](Casino.org) and making a bad reputation on industry. 

Our business proposal is to provide a truted fair play experience to online gambling sites and casinos using certifyable quantum random number generation. This is done by using a NISQ ion trap quantum computer connected to the online server and deliver true random numbers used to virtually roll dices, shuffle cards or crank a slot machine. Because the random numbers used are too hard to produce by a classical computer, the random numbers from the ion trap QC can be authenticated and certified by a third party. This technology enables a trusted online gambling experience where the player is confident in how the odds are drawn. This technology has a farreaching market potential like: reaching untapped demographics, state lotteries or even loot boxes in video games. This last segment alone is expected to grow to $US20 billion by 2025.
