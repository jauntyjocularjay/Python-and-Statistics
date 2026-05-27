# Section 4.2 — Mean, Expected Value, and Standard Deviation (Knowledge Check)

Instructions: This worksheet focuses only on Section 4.2. Answer concisely and show work for calculations.

---

1. State the definition of the expected value (mean) for a discrete random variable and write its formula.

2. State the formula for the population standard deviation of a discrete random variable in terms of the PMF.

3. Given the PMF below, verify it sums to 1 and compute the expected value $\mu=E[X]$. Show steps.

| x | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| P(X=x) | 2/50 | 4/50 | 23/50 | 9/50 | 4/50 | 1/50 |

4. Using your result from Q3, compute $E[X^2]$ and then the variance $\sigma^2$. Show steps.

5. Compute the population standard deviation $\sigma$ (numeric) from Q4. Round to three decimal places.

6. Explain briefly why $E[X^2]-[E[X]]^2$ equals the variance.

7. If every outcome above were equally likely (i.e., uniform across x=0..5), how would the formula for $E[X]$ simplify? Compute the uniform mean for x=0..5.

8. Short conceptual: When interpreting the standard deviation of a discrete distribution, what does a larger $\sigma$ tell you about the distribution's outcomes? (one sentence)

9. True/False: "If two discrete distributions have the same mean, they must have the same variance." Briefly justify your answer.

---

## Answer Key (brief)

1. $E[X]=\sum_x xP(x)$.

2. $\sigma=\sqrt{\sum_x (x-\mu)^2P(x)}$, where $\mu=E[X]$.

3. Sum: $\frac{2+4+23+9+4+1}{50}=1$. $E[X]=\sum xP(x)=\frac{0\cdot2+1\cdot4+2\cdot23+3\cdot9+4\cdot4+5\cdot1}{50}=\frac{98}{50}=1.96$.

4. $E[X^2]=\sum x^2P(x)=\frac{0+4+92+81+64+25}{50}=\frac{266}{50}=5.32$. Var $=5.32-1.96^2=1.4784$.

5. $\sigma=\sqrt{1.4784}\approx1.216$.

6. Because $E[(X-\mu)^2]=E[X^2]-2\mu E[X]+\mu^2=E[X^2]-\mu^2$.

7. Uniform mean: $E[X]=(0+1+2+3+4+5)/6=15/6=2.5$.

8. A larger $\sigma$ indicates outcomes are more spread out from the mean.

9. False. Different distributions can share the same mean but have different spreads; variance depends on how values are dispersed around the mean.

---

If you want this as a printable PDF or with answers hidden (separate file), tell me and I'll generate it.
