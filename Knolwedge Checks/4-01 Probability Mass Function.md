# Worksheet: 4.1 Probability Mass Function (PMF) for a Discrete Random Variable

## Instructions

- Show all work for computational questions.
- Use exact values when possible; round final decimals to **4 places** unless told otherwise.
- Write short, complete explanations for conceptual questions.

---

## Scenario

A quality-control machine classifies each item as defective or non-defective.  
Let X = number of defective items in a randomly selected sample of 4 items.

The PMF of X is:

|     x    |   0  |   1  |   2  |   3  |   4  |
| -------- | ---- | ---- | ---- | ---- | ---- |
| $P(X=x)$ | 0.10 | 0.25 | 0.35 | 0.20 | 0.10 |

---

## Part A: PMF Foundations

### 1. PMF validity

- a. Verify that the table defines a valid PMF.  
- b. State the two PMF conditions in words.

---

### 2. Reading probabilities directly

- a. $P(X=2)=$ __________  
- b. $P(X=4)=$ __________  
- c. $P(X=5)=$ __________

---

## Part B: Event Probabilities

### 3. Compute each probability

- a. $P(X \le 1)$
- b. $P(X \ge 3)$
- c. $P(1 < X \le 3)$
- d. $P(X \text{ is even})$
- e. $P(X \text{ is odd})$

---

### 4. Complement check

- a. Compute $P(X<3)$ directly from PMF.  
- b. Compute $P(X<3)$ using a complement.  
- c. Do the results match? Explain briefly.

---

## Part C: CDF and Interpretation

### 5. Build the CDF

Let $F(x)=P(X\le x)$.

- a. Fill in the values:

| $x$ | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| $F(x)$ | ____ | ____ | ____ | ____ | ____ |

- b. $F(2.5)=$ __________  
- c. $F(4)=$ __________  
- d. Why is the CDF of a discrete variable a step function?

---

## Part D: Moments and Spread

### 6. Expected value

- a. Compute $E[X]$.  
- b. Interpret $E[X]$ in context.

---

### 7. Variance and standard deviation

- a. Compute $E[X^2]$.  
- b. Compute $\mathrm{Var}(X)=E[X^2]-(E[X])^2$.  
- c. Compute $\sigma_X=\sqrt{\mathrm{Var}(X)}$.  
- d. Interpret the standard deviation in context.

---

## Part E: Shape and Transformations

### 8. Most likely outcome and shape

- a. Find the mode of $X$.  
- b. Is the distribution unimodal or multimodal?  
- c. Is it symmetric, left-skewed, right-skewed, or neither? Briefly justify.

---

### 9. Transformation

Let $Y=2X+1$.

- a. List all possible values of $Y$.  
- b. Write the PMF of $Y$.  
- c. Compute $E[Y]$ from your PMF of $Y$.  
- d. Verify with $E[Y]=2E[X]+1$.

---

## Part F: Conditional Probability

### 10. Conditional probabilities

- a. $P(X=2\mid X\ge2)$  
- b. $P(X\le1\mid X\text{ is odd})$  
- c. In one sentence: how does conditioning change the sample space?

---

## Part G: Critical Thinking

### 11. Model critique

- a. If someone changes $P(X=2)$ from 0.35 to 0.50, what must happen to keep a valid PMF?  
- b. Give one realistic reason why $P(X=0)$ might increase over time in this process.

---

### 12. Concept reflection (short response)

- a. Difference between a PMF value and a CDF value.  
- b. Why is $P(X=2.7)=0$ for this variable?  
- c. Give one real-world example where a discrete PMF is appropriate.

---

## Challenge (Optional)

Create your own PMF for a discrete variable with values $0,1,2,3$.  

- Ensure it is valid.
- Compute $E[X]$ and $\mathrm{Var}(X)$.  
- Write one sentence interpreting each.
