# Probability

## Empirical probability

probability derived from real-world samples

## theoretical probability

the probability derived mathematically

## addition rule

- The probability of A $\cup$ (||) B occuring is equal to the sum of probabilities of A $\cap$ (&&) B minus the probability of both occuring
- $ P(A \cup B) = P(A) + P(B) - P(A \cap B) $
- $ P(A \cap B) = P(A) + P(B) - P(A \cup B) $
- $ P(A + B) = P(A \cap B) + P(A \cup B) $
- given flipping a coin for TAILS and rolling 1d6 for s6
     - $P(TAILS \cup s6) = P(TAILS) + P(s6) - P(TAILS \cap s6)$
     - because the outcome of flipping tails and s6 gets counted twice we need to subtract off when both happen.

## multiplication rule

- if A and B are two events defined on a **sample space**, then:
- $P(A \cap B) = P(B) * P(A|B) \Rightarrow P(A|B) = \frac{ P(A \cap B) }{ P(B) } $
- $P(A|B) =  \frac{ P(A \cap B) }{ P(B) }$
- Example: 1d6 and 1d20 Dice
    - Event A: Roll a 1 on the 1d6.
    - Event B: Roll a 1 on the 1d20.
    - Step 1: Find $P(A), P(B)$
    - a. Probability of rolling a 1 on 1d6 $\Rightarrow P(A) = 1/6$
    - b. Probability of rolling a 1 on 1d20 $\Rightarrow P(B) = 1/20$ 
    - Step 2: Find $𝑃(𝐴 ∩ 𝐵)$, Assuming the dice are independent:
        - $P(A ∩ B) \Rightarrow 𝑃(𝐴)×𝑃(𝐵) = 1 / (6 * 20)  \Rightarrow 1 / 120$
    - Step 3: Calculate $P(A∣B)$ using the multiplication rule:
        - $P(A∣B) = \frac{ P(A∩B) }{ P(B)} \Rightarrow \frac{ 1/120 }{ 1/20 } \Rightarrow \frac {20} {120} \Rightarrow \frac{1}{6} $​
    - Verbal Interpretation: 
        1. Since the dice are independent
        1. $P(A∣B)$ is the probability of rolling s1 on the 1d6, given that you rolled a s1 on 1d20.
