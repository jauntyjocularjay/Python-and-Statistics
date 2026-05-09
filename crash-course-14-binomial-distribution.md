# 15 Binomial Distribution

∵ the random variable X counts successes

1. fixed `n` number of trials before the experiment begins
1. `two outcomes`: success and failure (p + q = 1)
1. the probability of success `p` across all trials is constant
1. trials are independent (the outcome of one trial does not change the probabilty of any other trial)

## ex. Illustrating the outcomes

| day |  Mon  |  Tue  |  Wed  |  Thu  |  Fri  |product|
|-----|-------|-------|-------|-------|-------|-------|
|  1  |  0.2  |  0.8  |  0.8  |  0.8  |  0.8  | 0.082 |
|  2  |  0.8  |  0.2  |  0.8  |  0.8  |  0.8  | 0.082 |
|  3  |  0.8  |  0.8  |  0.2  |  0.8  |  0.8  | 0.082 |
|  4  |  0.8  |  0.8  |  0.8  |  0.2  |  0.8  | 0.082 |
|  5  |  0.8  |  0.8  |  0.8  |  0.8  |  0.2  | 0.082 |

Multiply across, add down

$ 5 \times 0.2^1 \times 0.8^4 $

## Binomial Formula

### Coefficient

the binomial coefficient formula is read as: 'N choose K'

∵ n = number of trials, k = successful outcomes

∴ $ nCk = \frac{n!}{k! \cdot (n-k)!} $

### Probability of Success and Failure

$ p^k \cdot (1-p)^{n-k} $

### Together

binom(n,k) = $ \binom{n=20}{k=0} \cdot p^k \cdot (1-p)^{n-k} $

binom(n,k) = $ \frac{n!}{k! (n-k)!} \cdot p^k \cdot (1-p)^{n-k} $

### Example: Flat Tires

- p: is the probability of getting a flat tire in one year.
- n: is the range of years observed (number of trials)
- k: is the number years with a flat tire

given:

- ∵ p = 0.05
- ∵ n = 20
- ∵ k = 1

therefore:

- ∴ binom(20, 1)
- ∴ $ 1 \cdot (0.05)^1 \cdot (0.95)^{20} $
- ∴ $ \approx 0.358 $
