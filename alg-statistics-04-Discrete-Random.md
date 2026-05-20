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

#### Example 4.18

A safety engineer feels that 35% of all industrial accidents in the plant are caused by failure of employees to follow instructions. They decide to look at the accident reports (selected randomly and replaced in the pile after reading) until they find one that shows an accident caused by failure of employees to follow instructions. On average, how many reports would the safety engineer expect to look at until they find a report showing an accident caused by employee failure to follow instructions? What is the probability that the safety engineer will have to examine at least three reports until they find a report showing an accident caused by employee failure to follow instructions?

Let X = the number of accidents the safety engineer must examine until they find a report showing an accident caused by employee failure to follow instructions. X takes on the values 1, 2, 3, .... The first question asks you to find the expected value or the mean. The second question asks you to find P(x ≥ 3). ("At least" translates to a "greater than or equal to" symbol).

- p = 35/100
- q = 65/100

$ μ = (p)^{-1} \rightarrow (35/100)^{-1} \rightarrow (100/3.5) ≈ 2.8 $

#### Example 4.19

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

d. The probability question is P(_5/100_)

### Geometric Distribution Function Notation

$ x $ ~ $ G(p) $

- x: the value x
- ~: is a random variable
- G(): with a geometric distribution
- p: where p is the probability of success

#### Case 1: Random Variable x is event of first success

Equation: $ p(x)=(1-p)^{x-1} p $

Standard Deviation: $ σ = \sqrt{ \frac {p}{(1-p)^2}} $

#### Case 2: Random Variable x is number of failures before success

Equation: $ P(x) = (1-p)^{x} p $

Mean: $ μ = \frac{1-p}{p} $

Standard Deviation: $σ = \sqrt{ \frac{1-p}{p} } \Rightarrow \sqrt{μ_{case 2}} $

#### Example 4.20

Assume that the probability of a defective computer component is 0.02. Components are randomly selected. Find the probability that the first defect is caused by the seventh component tested. How many components do you expect to test until one is found to be defective?

Let X = the number of computer components tested until the first defect is found.

X takes on the values 1, 2, 3, ... where p = 0.02.

Find P(x = 7). P(x = 7) = 0.0177

- p = 0.02
- $ (1 - p) = 0.98 $
- $ P(x) = p^1 \cdot (1-p)^{x-1} \rightarrow (0.02) * (0.98)^6 \rightarrow 0.0177 $

#### Example 4.21

The lifetime risk of developing cancer is about one in 67 (1.5%). Let X = the number of people you ask until one says they have cancer. Then X is a discrete random variable with a geometric distribution:

X ~ 𝐺⁡( $ \frac{1}{67} $ ) or X ~ $ 𝐺⁡(0.015) $

- What is the probability of that you ask ten people before one says they have cancer?
  - p = $ \frac{1}{67} $, q = $ \frac{66}{67} $
  - G(x) = $ q^{x-1} \cdot p $
  - G(x) = $ (\frac{66}{67})^{9} \frac{1}{67} $
- What is the probability that you must ask 20 people?
  - G(x) = $ (\frac{66}{67})^{19} \frac{1}{67} $
- Find the (i) mean and (ii) standard deviation of X

## 4.5 Hypergeometric Distribution

1. take samples from two groups  
2. concerned with the first group, the "group of interest"  
3. sample _without_ replacement from the combined groups  
4. each pick is _dependent_ (sampling without replacement)  
5. not dealing w/ Bernoulli trials

---

### Example 4.22 Problem

A candy dish contains 100 jelly beans and 80 gumdrops. Fifty candies are picked at random. What is the probability that 35 of the 50 are gumdrops? The two groups are jelly beans and gumdrops. Since the probability question asks for the probability of picking gumdrops, the group of interest (first group) is gumdrops. The size of the group of interest (first group) is 80. The size of the second group is 100. The size of the sample is 50 (jelly beans or gumdrops). Let X = the number of gumdrops in the sample of 50. X takes on the values x = 0, 1, 2, ..., 50. What is the probability statement written mathematically?

- Probability statement is: P(x=35)

---

### Example 4.24

You are president of an on-campus special events organization. You need a committee of seven students to plan a special birthday party for the president of the college. Your organization consists of 18 women and 15 men. You are interested in the number of men on your committee. If the members of the committee are randomly selected, what is the probability that your committee has more than four men?

This is a hypergeometric problem because you are choosing your committee from two groups (men and women).
Problem

- a. Are you choosing with or without replacement?
  - _without replacement_
- b. What is the group of interest?
  - _Men_
- c. How many are in the group of interest?
  - _15/33_
- d. How many are in the other group?
  - _18/33_
- e. Let X = _________ on the committee. What values does X take on?
  - _x=4_
- f. The probability question is P(_______).
  - _P(x > 4)_

---

## 4.6 Poisson Distribution

1. The Poisson probability distribution gives the probability of a number of events occurring in a fixed interval of time or space if these events happen with a known average rate and independently of the time since the last event.
1. The Poisson distribution may be used to approximate the binomial if the probability of success is "small" (such as 0.01) and the number of trials is "large" (such as 1,000). You will verify the relationship in the homework exercises. n is the number of trials, and p is the probability of a "success."

### Example 4.26

The average number of loaves of bread put on a shelf in a bakery in a half-hour period is 12. Of interest is the number of loaves of bread put on the shelf in five minutes. The time interval of interest is five minutes. What is the probability that the number of loaves, selected randomly, put on the shelf in five minutes is three?

Let X = the number of loaves of bread put on the shelf in five minutes. If the average number of loaves put on the shelf in 30 minutes (half-hour) is 12, then the average number of loaves put on the shelf in five minutes is (5/30)(12) = 2 loaves of bread.

The probability question asks you to find P(x = 3).

### Example 4.27 Problem

A bank expects to receive six bad checks per day, on average. What is the probability of the bank getting fewer than five bad checks on any given day? Of interest is the number of checks the bank receives in one day, so the time interval of interest is one day. Let X = the number of bad checks the bank receives in one day. If the bank expects to receive six bad checks per day then the average is six checks per day. Write a mathematical statement for the probability question.

$$
P(X < 5)
$$

### Poisson Distribution

Poisson Distribution tells you how likely it is to observe exactly (x) events, given an average rate $(\mu)$.

$$
P(X) = pois(X, \mu),\quad x=0,1,2,\dots
$$

#### Poisson point probability formula

$$
pois(x) = \frac { \mu^x \cdot e^{-\mu} } { x! }
$$

#### Special Tail-Probability (complement) case

Use the Special Tail-Probability (complement) case when it is easier to calculate the complement of a tail event.

$$
P(X_m) = 1 - [\frac { \mu^0 \cdot e^{-\mu} } { 1 } + \frac { \mu^x{_m} \cdot e^{-\mu} } { X_m! }]
$$

### Example 4.29

Leah receives about six telephone calls between 8 a.m. and 10 a.m. What is the probability that Leah receives more than one call in the next 15 minutes?

Let X = the number of calls Leah receives in 15 minutes. (The interval of interest is 15 minutes or 1/4 hour.)

$$
P(x > 1) \mu = \frac{6}{2} * \frac{1}{4} \Rightarrow 3 * \frac{1}{4} \Rightarrow \frac{3}{4} \Rightarrow 0.75
$$

$$
P(x > 1) \Rightarrow 1 - [P(0)+P(1)] \Rightarrow
$$

$$
1 - [\frac{(0.75^0) \cdot e^{-0.75}}{1} + \frac{(0.75^1) \cdot e^{-0.75}}{1} ] \approx 1−[0.4724+0.3543] \approx 0.1733
$$
