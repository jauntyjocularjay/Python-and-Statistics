# 3.0 Probability

- is a measure associated with how certain we are of outcomes of a particular activity
- the long-term relative frequences of an outcome
- between [0,1] inclusive
- equal probability, equally likely, means each outcome is equally likely to occur

## 3.1 Terminology

### outcome

the result of an activity

### sample space

the set of possible outcomes

- as list
- a tree diagram
- a Venn diagram

### event

- is any combination of outcomes
- upper case letters represent events
- expressed as a probability function ex. $P(x) = 3/4  \rightarrow 0.75$

### calculating probability

1. count the number of outcomes for an event
1. divide by the total number of outcomes in the sample space

#### ex. flipping heads or tails

- the sample space of a fair coin is {HH,TH,HT,TT} where H = heads, T = tails
- The two outcomes are {HT, TH}
- $P(A) = 2/4 \rightarrow 1/2 \rightarrow 0.5$

### Law of Large Numbers

as the number of repetitions increase, the relative frequency tends to approach the theoretical probability

### biased (unfair) outcomes

when the observed probability does not approach the the theoretical probability

### Union, 'OR', ∪ event

- An outcome is in the event A OR B if the outcome is in A or is B or is in both A and B.
- A OR B is also written as A (union) B: 𝐴∪𝐵
    1. ex. A = {1, 2, 3, 4} and B = {3, 4, 5, 6} 𝐴∪𝐵 = {1, 2, 3, 4, 5, 6}
    2. 𝐴∪𝐵 is a **set** with no repeating outcomes.

### Intersection, 'AND', ∩ event

- An outcome is in the event A AND B if the outcome is both A and B at the same time. 
- A AND B is written as A intersection B: 𝐴 ∩ 𝐵
    1. ex. A = {1, 2, 3, 4} and B = {3, 4, 5, 6} 𝐴∩𝐵 = {3, 4}
    2. 𝐴∪𝐵 is a **set** with no repeating outcomes.

### Conditional Probability

- the probability event A will occur given that B has already occured
- written as *P(A|B)*, *P*robability of *A given B*

### Complementary Event

- The complement of *P(A)* is *P(A')* or every event that is not *P(A)*
- ex if *P(D) where D=6* of rolling a six sided dice on the number six, *P(D) = 1/6* and *P(D') = 5/6*
- *P(A)* + *P(A')* = 1

### conditional probability

- *P(A|B)* 'the probability of A given B'
- meaning *A* will occur if *B* has already occurred.
- a conditional reduces the sample space
- The conditional probability of $P(A \mid B)$ is:

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

where:

- $P(A \mid B)$ is the probability of event $A$ occurring given that $B$ has occurred,
- $P(A \cap B)$ is the probability that both $A$ and $B$ occur,
- $P(B)$ is the probability that $B$ occurs.

## 3.2 Independent *v* Dependent Events

- Two events are independent if the following are true:
    1. $P(A \mid B) = P(A)$, and
    1. $P(A \mid B) = P(B)$, and
    1. $P(A \land B) = P(A)P(B)$
- meaning the knowledge of one do not affect the chance the other occurs.
- ex. the roll of two fair die does not change the probability for the outcome of the other.

### Sampling

#### With Replacement

if each member of a population is replaced after it is picked, then that member has the possibility of being chosen more than once. Sampling done with replacement have independent events meaning the result of the first pick will not change the probabilities for the second pick. This is **independent** because the available pool of picks does not shrink with each pick.

#### Without Replacement

When sampling without replacement, each member of a population may only represent once. In this case, the probabilities of the second pick are affected by the result of the first pick. These event are *dependent* as the available pool of picks shrinks.

#### When in out, assume dependence

- If $P(A)$ and $P(B)$ may be either dependent or independent.
- *When in doubt, assume they are dependent unless you can show otherwise.*

### Mutually Exclusive Events

- *A* and *B* are **mutually exclusive** events if they cannot occur at the same time. This means that *A* and *B* do not share outcomes.
- $P(A \land B) = 0$ indicates a relationship is mutually exclusive.
- When in doubt, *assume events are mutually exclusive unless you can show otherwise*.

#### ex. Mutually *vs* Not Mutually Exclusive

Let:

- $S = \{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 \} $
- $A = \{ 1, 2, 3, 4, 5 \}$
- $B = \{ 4, 5, 6, 7, 8 \}$
- $C = \{ 7, 9 \}$
- $P(A \land B) = {4, 5}$
- The probability of both $P(A)$ and $P(B)$ occurring is:
- $ P(A \cap B) = \frac{|A \cap B|}{|S|} = \frac{2}{10} ; \therefore$ (therefore) **not** mutually exclusive
- $ P(A \cap C) = \varnothing ; \therefore$ (therefore) mutually exclusive

## 3.3 Two Basic Rules of Probability

### Multiplication Rule

- if A and B are two events defined on a **sample space**, then:
- $P(A \cap B) = P(B) * P(A|B) \Rightarrow P(A|B) = \frac{ P(A \cap B) }{ P(B) } $

### Addition Rule

- if A and B are defined on a sample space, then: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ and,
- if A and B are *mutually exclusive* ⇒ $P(A \cap B) = 0 ⇒ P(A \cup B) = P(A) + P(B)$

## 3.4 Contingency Tables

- Portrays data to facilitate probability calculations
- sample values are displayed in relationship to variables

ex.shows a random sample of 100 hikers and the areas of hiking they prefer.

| Sex    | The Coastline | Near Lakes and Streams| On Mountain Peaks | Total |
|--------|:-------------:|:---------------------:|:-----------------:|:-----:|
| Women  |      18       |          16           |                   |  45   |
| Men    |               |                       |        14         |  55   |
| Total  |               |          41           |                   |       |

### a. fill out the missing areas 

| Sex    | The Coastline | Near Lakes and Streams| On Mountain Peaks | Total |
|--------|:-------------:|:---------------------:|:-----------------:|:-----:|
| Women  |      18       |          16           |        11         |  45   |
| Men    |      16       |          25           |        14         |  55   |
| Total  |      34       |          41           |        25         | 100   |

### b. Problem

Are the events "being a woman" and "preferring the coastline" independent events?

Let F = being a woman and let C = preferring the coastline.

1. Find P(F AND C).
1. Find P(F)P(C)

Are these two numbers the same? If they are, then F and C are independent. If they are not, then F and C are not independent.

### c. Problem

Find the probability that a person is a man given that the person prefers hiking near lakes and streams. Let M = being a man, and let L = prefers hiking near lakes and streams.

1. What word tells you this is a conditional?
1. Fill in the blanks and calculate the probability: P(___|___) = ___.
1. Is the sample space for this problem all 100 hikers? If not, what is it?

### d. Problem

Find the probability that a person is a woman or prefers hiking on mountain peaks.
- Let F = being a woman, and 
- let P = prefers mountain peaks.

1. Find P(F) = 45/100
1. Find P(P) = 25/100
1. Find P(F AND P) = 11/100
1. Find P(F OR P) = (45+25-11)/100 $ \rightarrow $ 59/100


