# 4 Discrete Random Variable

## 4.1 Probability Distribution Function (PDF) for a Discrete Random Variable

a discrete probability function (PDF) has

1. each probability is between [Zero, one] inclusive
2. The sum of the probabilities is one


|   P(x)       |     x     |
|--------------|-----------|
| $ P(x_0) $   |  2/50     |
| $ P(x_1) $   |  4/50     |
| $ P(x_2) $   | 23/50     |
| $ P(x_3) $   |  9/50     |
| $ P(x_4) $   |  4/50     |
| $ P(x_5) $   |  1/50     |
| $ \sum P(x)$ | 50/50 = 1 |


## 4.2 Mean Expected Value and Standard Deviation

**expected value** or **long term average or mean**: Over the long term running an experiment, expect the long term mean  

mean = $ μ = \sum [x·P(x)] $

standard deviation = $ \sigma = \sqrt{ \sum [(x − μ)²·P(x)]} $

When the outcomes of a probability distribution are equally likely, these formulas coincide with the mean and std. deviation of the set of possible outcomes.

## 4.3 Binomial Distribution

1. Fixed number of trials where n = # of trials
2. Two possible outcomes: success, failure
    - p indicates success
    - q indicates failure
    - p + q = 1
3. n trials are independent & repeat using identical condition

outcomes of a binomial experiment fit a binomial probability distribution. The variable x = the number of successes obtained in the n independent trials.

μ = the mean 
σ² = variance

for a binomial probability distribution
- μ = np (trials • successes)
- σ² = npq
- standard deviation = σ = √npq

Binomial trial has characteristics 2, 3 and where n = 1
binomial experiment takes place when the number of successes is counted in one or more Bernoulli trials

## 4.4 Geometric Distribution

1. a trial is repeated until a success  

2. Repeated trials are independent  

3. probability of success (p), failure (q) remain the same for each trial  

4. random variable x is the number of trials in which the first success occurs  

5. random variable is discrete  

6. Probability of success & failure are constant  

7. "memory loss" - all prior attempts do not affect the outcome

### The Mean (μ)

The mean (experiments to expect the first success) is $ μ = (p)^{-1} $

### Example 4.18

A safety engineer feels that 35% of all industrial accidents in the plant are caused by failure of employees to follow instructions. They decide to look at the accident reports (selected randomly and replaced in the pile after reading) until they find one that shows an accident caused by failure of employees to follow instructions. On average, how many reports would the safety engineer expect to look at until they find a report showing an accident caused by employee failure to follow instructions? What is the probability that the safety engineer will have to examine at least three reports until they find a report showing an accident caused by employee failure to follow instructions?

Let X = the number of accidents the safety engineer must examine until they find a report showing an accident caused by employee failure to follow instructions. X takes on the values 1, 2, 3, .... The first question asks you to find the expected value or the mean. The second question asks you to find P(x ≥ 3). ("At least" translates to a "greater than or equal to" symbol).

- p = 35/100
- q = 65/100

$ μ = (p)^{-1} \rightarrow (35/100)^{-1} \rightarrow (100/3.5) ≈ 2.8 $



### Example 4.19

Suppose that you are looking for a student at your college who lives within five miles of you. You know that 55% of the 25,000 students do live within five miles of you. You randomly contact students from the college until one says they live within five miles of you. What is the probability that you need to contact four people?

This is a geometric problem because you may have a number of failures before you have the one success you desire. Also, the probability of a success stays the same each time you ask a student if they live within five miles of you. There is no definite number of trials (number of times you ask a student).

 Problem

a. Let X = the number of _students_ you must ask _before_ one says yes.

b. What values does X take on?
- The total number of attempts made.

c. What are p and q?

- $ p = 0.55 $
- $ q = 0.45 $
- μ (the mean) = $ p^{-1} \rightarrow $ (100/55) $ => $ 1.82 contacts before reaching somebody as intended.

d. The probability question is P(_5/100_).