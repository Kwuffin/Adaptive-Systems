# Adaptive Systems / Inleveropgave 1
In deze directory zullen alle opdrachten van de eerste inleveropgave zitten, ook de theoretische opdrachten.

## Theoretische opdrachten:
### 1.1 Markov Chain:
Created states and policies.

![1.1](https://github.com/Kwuffin/Adaptive-Systems/blob/main/Inleveropgave%201/1.1%20Markov%20Chain.png "Opdracht 1.1")

### 1.2 Markov Reward Process:
Added rewards.

![1.2](https://github.com/Kwuffin/Adaptive-Systems/blob/main/Inleveropgave%201/1.2%20Markov%20Reward%20Process.png "Opdracht 1.2")

### 1.3 Sampling. Een voorbereiding voor Monte-Carlo Policy Evaluation:
Added samples.

![1.3](https://github.com/Kwuffin/Adaptive-Systems/blob/main/Inleveropgave%201/1.3%20Sampling.png "Opdracht 1.3")

### 1.4 De value-function bepalen:
Calculated values of nodes for the first two iterations.

![1.4](https://github.com/Kwuffin/Adaptive-Systems/blob/main/Inleveropgave%201/1.4%20De%20value-function%20bepalen.png "Opdracht 1.4")

### 1.5 Zelf-onderzoek
 In werkelijkheid zien we vrijwel nooit een discount factor van 1. Een discount factor van 0.9 is wel veel voorkomend. Noem twee problemen die je mogelijk hebt met γ=1

##### Probleem 1:
Een discount rate van 1 zorgt ervoor dat de rewards in de toekomst evenveel meetellen als een reward die een agent gelijk krijgt.


"A reward received k time steps in the future is worth only γk-1 times what it would be worth if it were
received immediately." 
(Page 55, Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning, second edition. Amsterdam University Press.)

##### Probleem 2:
Een discount rate dat kleiner is dan 1 is een wiskundig trucje om een oneindige som eindig te maken.
Dit helpt met het convergeren van het algoritme als het niet zeker is wanneer het programma eindigt.

### 2. Control met Value Iteration
Bepaal de utility van elke state (value function) van onderstaande MDP, je mag zelf kiezen wanneer je stopt met itereren maar beargumenteer waarom. Te vroeg stoppen is niet goed. Neem een discount factor van γ=1

De value voor alle states worden geinitialiseerd op 0. De waardes boven de pijlen zijn de rewards die je krijgt voor het gaan naar de state.

![2.](https://github.com/Kwuffin/Adaptive-Systems/blob/main/Inleveropgave%201/2.0%20Control%20met%20Value%20Iteration.png "Opdracht 2.")