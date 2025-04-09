# Module 1: Introduction to Probability

## Learning Objectives
By the end of this module, you will be able to:
- Define fundamental probability concepts and terminology
- Calculate probabilities using various rules and formulas
- Apply probability concepts to solve real-world problems
- Understand conditional probability and Bayes' theorem
- Recognize independence and mutually exclusive events

## 1.1 Basic Probability Concepts

### What is Probability?

Probability is a branch of mathematics that deals with calculating the likelihood of a given event's occurrence. It is a measure of the certainty that an event will occur, expressed as a number between 0 and 1.

- A probability of 0 indicates impossibility (the event will not occur)
- A probability of 1 indicates certainty (the event will occur)
- A probability between 0 and 1 indicates the degree of likelihood of the event occurring

Probability theory provides a framework for modeling random phenomena and making predictions about events when we cannot be certain about the outcome.

### Historical Context

The formal study of probability began in the 17th century with mathematicians Blaise Pascal and Pierre de Fermat, who analyzed games of chance. Their correspondence about gambling problems laid the foundation for probability theory. Later, mathematicians like Jacob Bernoulli, Abraham de Moivre, Pierre-Simon Laplace, and Andrey Kolmogorov further developed the field into the mathematical discipline we know today.

### Sample Space and Events

To analyze probability problems, we need to understand several key concepts:

**Sample Space (Ω)**: The set of all possible outcomes of a random experiment.

Example 1: When flipping a coin, the sample space is Ω = {Heads, Tails}
Example 2: When rolling a six-sided die, the sample space is Ω = {1, 2, 3, 4, 5, 6}
Example 3: When drawing a card from a standard deck, the sample space consists of all 52 cards

**Event**: A subset of the sample space, representing a collection of outcomes.

Example 1: The event of getting a head when flipping a coin is E = {Heads}
Example 2: The event of rolling an even number on a die is E = {2, 4, 6}
Example 3: The event of drawing a heart from a deck is the set of all 13 heart cards

### Probability Axioms

Modern probability theory is based on three axioms proposed by Andrey Kolmogorov:

1. **Non-negativity**: The probability of an event is a non-negative real number.
   P(E) ≥ 0 for any event E

2. **Normalization**: The probability of the entire sample space is 1.
   P(Ω) = 1

3. **Additivity**: For mutually exclusive events E and F (events that cannot occur simultaneously), the probability of either event occurring is the sum of their individual probabilities.
   If E ∩ F = ∅, then P(E ∪ F) = P(E) + P(F)

These axioms form the foundation of probability theory and allow us to derive various probability rules and formulas.

### Approaches to Probability

There are three main approaches to defining and interpreting probability:

1. **Classical (Theoretical) Probability**: Based on equally likely outcomes.
   P(E) = Number of favorable outcomes / Total number of possible outcomes

   Example: The probability of rolling a 3 on a fair die is 1/6 because there is 1 favorable outcome (rolling a 3) out of 6 possible outcomes.

2. **Relative Frequency (Empirical) Probability**: Based on the frequency of occurrence in repeated experiments.
   P(E) = Number of times E occurs / Total number of trials

   Example: If we flip a coin 100 times and get 53 heads, the empirical probability of heads is 53/100 = 0.53.

3. **Subjective Probability**: Based on personal belief or judgment about the likelihood of an event.
   
   Example: A doctor might estimate a 70% chance of recovery for a patient based on experience and medical knowledge.

## 1.2 Probability Rules and Formulas

### Complement Rule

The complement of an event E, denoted E' or E^c, consists of all outcomes in the sample space that are not in E. The probability of the complement is:

P(E') = 1 - P(E)

Example: If the probability of rain tomorrow is 0.3, then the probability it will not rain is 1 - 0.3 = 0.7.

### Addition Rule

For any two events E and F, the probability of either E or F occurring (or both) is:

P(E ∪ F) = P(E) + P(F) - P(E ∩ F)

Where P(E ∩ F) is the probability that both events occur.

For mutually exclusive events (E ∩ F = ∅), this simplifies to:

P(E ∪ F) = P(E) + P(F)

Example: In a standard deck of cards, what is the probability of drawing either a king or a heart?
- P(King) = 4/52 = 1/13
- P(Heart) = 13/52 = 1/4
- P(King ∩ Heart) = 1/52 (the king of hearts)
- P(King ∪ Heart) = 1/13 + 1/4 - 1/52 = 4/52 + 13/52 - 1/52 = 16/52 = 4/13

### Multiplication Rule

For any two events E and F, the probability of both E and F occurring is:

P(E ∩ F) = P(E) × P(F|E) = P(F) × P(E|F)

Where P(F|E) is the conditional probability of F given that E has occurred.

For independent events, this simplifies to:

P(E ∩ F) = P(E) × P(F)

Example: If we roll two dice, what is the probability of getting a 6 on both dice?
- P(First die shows 6) = 1/6
- P(Second die shows 6) = 1/6
- Since the dice rolls are independent: P(Both show 6) = 1/6 × 1/6 = 1/36

## 1.3 Conditional Probability

Conditional probability is the probability of an event occurring given that another event has already occurred.

For events E and F, the conditional probability of E given F is:

P(E|F) = P(E ∩ F) / P(F), where P(F) > 0

Example: In a class of 30 students, 15 are female and 10 students (including 6 females) take statistics. What is the probability that a randomly selected student is female given that the student takes statistics?

- P(Female ∩ Statistics) = 6/30 = 1/5
- P(Statistics) = 10/30 = 1/3
- P(Female | Statistics) = P(Female ∩ Statistics) / P(Statistics) = (1/5) / (1/3) = 3/5 = 0.6

### Independence

Two events E and F are independent if the occurrence of one does not affect the probability of the other. Mathematically, E and F are independent if and only if:

P(E ∩ F) = P(E) × P(F)

Equivalently, E and F are independent if:

P(E|F) = P(E) or P(F|E) = P(F)

Example: Drawing cards with replacement from a deck. The probability of drawing a heart on the second draw is independent of what was drawn on the first draw (assuming the first card is returned and the deck is shuffled).

### Mutually Exclusive vs. Independent Events

It's important to distinguish between mutually exclusive events and independent events:

- **Mutually Exclusive Events**: Cannot occur simultaneously. If E and F are mutually exclusive, then P(E ∩ F) = 0.
- **Independent Events**: The occurrence of one does not affect the probability of the other.

Note: If two events have non-zero probabilities and are mutually exclusive, they cannot be independent. This is because if E and F are mutually exclusive, then P(E|F) = 0, which is not equal to P(E) unless P(E) = 0.

## 1.4 Bayes' Theorem

Bayes' theorem provides a way to revise existing predictions or theories given new or additional evidence. It is expressed as:

P(A|B) = [P(B|A) × P(A)] / P(B)

Where:
- P(A|B) is the posterior probability of A given B
- P(B|A) is the likelihood of B given A
- P(A) is the prior probability of A
- P(B) is the prior probability of B

Bayes' theorem is particularly useful when we have information about P(B|A) but want to find P(A|B).

### Law of Total Probability

The law of total probability is often used in conjunction with Bayes' theorem. If events A₁, A₂, ..., Aₙ form a partition of the sample space (they are mutually exclusive and their union is the entire sample space), then for any event B:

P(B) = P(B|A₁)P(A₁) + P(B|A₂)P(A₂) + ... + P(B|Aₙ)P(Aₙ)

This allows us to calculate P(B) for use in Bayes' theorem.

### Example: Medical Testing

A classic application of Bayes' theorem is in medical testing. Consider a test for a disease that affects 1% of the population. The test has a sensitivity of 95% (P(Positive|Disease) = 0.95) and a specificity of 90% (P(Negative|No Disease) = 0.90).

If a person tests positive, what is the probability they have the disease?

We want to find P(Disease|Positive).

Using Bayes' theorem:
P(Disease|Positive) = [P(Positive|Disease) × P(Disease)] / P(Positive)

We know:
- P(Positive|Disease) = 0.95 (sensitivity)
- P(Disease) = 0.01 (prevalence)
- P(Positive) = P(Positive|Disease)P(Disease) + P(Positive|No Disease)P(No Disease)
  = 0.95 × 0.01 + 0.10 × 0.99 = 0.0095 + 0.099 = 0.1085

Therefore:
P(Disease|Positive) = (0.95 × 0.01) / 0.1085 ≈ 0.088 or about 8.8%

This example illustrates the "base rate fallacy" - even with a positive test result, the probability of having the disease is relatively low because the disease is rare in the population.

## 1.5 Counting Principles

Counting principles are essential tools for calculating probabilities, especially when dealing with large sample spaces.

### Multiplication Principle

If a task can be performed in n₁ ways, and for each of these ways, a second task can be performed in n₂ ways, then the two tasks can be performed in sequence in n₁ × n₂ ways.

Example: If you have 5 shirts and 3 pairs of pants, you can create 5 × 3 = 15 different outfits.

### Permutations

A permutation is an arrangement of objects in a specific order. The number of permutations of n distinct objects is:

P(n,n) = n! = n × (n-1) × (n-2) × ... × 2 × 1

The number of permutations of k objects selected from n distinct objects is:

P(n,k) = n! / (n-k)!

Example: How many ways can 3 runners finish in first, second, and third place in a race with 8 runners?
P(8,3) = 8! / (8-3)! = 8! / 5! = 8 × 7 × 6 = 336

### Combinations

A combination is a selection of objects without regard to order. The number of combinations of k objects selected from n distinct objects is:

C(n,k) = n! / [k! × (n-k)!]

This is often denoted as (n choose k) or ₍ₙₖ₎.

Example: How many different 5-card hands can be dealt from a standard 52-card deck?
C(52,5) = 52! / [5! × (52-5)!] = 52! / [5! × 47!] = 2,598,960

## 1.6 Real-World Applications

### Risk Assessment and Insurance

Insurance companies use probability to assess risk and set premiums. They analyze historical data to estimate the probability of various events (accidents, natural disasters, etc.) and calculate expected losses.

Example: An auto insurance company might determine that drivers in a certain age group have a 0.05 probability of filing a claim in a given year, with an average claim amount of $3,000. The expected cost per policyholder would be 0.05 × $3,000 = $150, which helps determine the premium (plus administrative costs and profit margin).

### Games of Chance

Probability theory originated from analyzing games of chance, and it remains fundamental to understanding gambling.

Example: In roulette, a European wheel has 37 slots (numbers 0-36). The probability of winning by betting on a single number is 1/37 ≈ 0.027 or about 2.7%. The payout is 35:1, meaning the expected value of a $1 bet is (35 × 1/37) - (36 × 1/37) = -1/37 ≈ -$0.027, giving the house a 2.7% edge.

### Weather Forecasting

Meteorologists use probability to express uncertainty in weather predictions. A "30% chance of rain" means that, based on current data and historical patterns, similar conditions have resulted in rain 30% of the time.

### Quality Control

Manufacturers use probability in sampling plans to inspect product quality. Rather than testing every item (which may be destructive or time-consuming), they test a sample and make inferences about the entire batch.

Example: A manufacturer might inspect 50 items from a batch of 1,000. If the acceptable quality level is 1% defective, and 2 or more defective items are found in the sample, the entire batch is rejected.

### Finance and Investment

Probability is central to modern finance, from portfolio theory to option pricing.

Example: The Black-Scholes model for option pricing uses probability theory to determine the fair price of options based on the probability distribution of future stock prices.

## Interactive Learning Activities

Throughout this module, you'll engage with several interactive tools to reinforce your understanding of probability concepts:

1. **Coin Flip Simulator**: Experiment with flipping coins to see how experimental probability approaches theoretical probability as the number of trials increases.

2. **Dice Rolling Experiment**: Explore sample spaces and probability distributions by simulating dice rolls with various configurations.

3. **Conditional Probability Explorer**: Visualize conditional probabilities using Venn diagrams and contingency tables, with real-time calculations.

4. **Bayes' Theorem Calculator**: Work through examples of Bayesian reasoning with step-by-step explanations.

5. **Probability Practice Problems**: Test your understanding with interactive problems that provide immediate feedback.

## Summary

In this module, we've covered the fundamental concepts of probability theory:

- Basic definitions and axioms of probability
- Different approaches to probability (classical, empirical, subjective)
- Probability rules (complement, addition, multiplication)
- Conditional probability and independence
- Bayes' theorem and the law of total probability
- Counting principles (permutations and combinations)
- Real-world applications of probability

These concepts form the foundation for the more advanced topics we'll explore in subsequent modules, including random variables, probability distributions, and statistical inference.

## Practice Exercises

1. A card is drawn at random from a standard deck. Find the probability of drawing:
   a) A heart
   b) A face card (jack, queen, or king)
   c) A red face card

2. A bag contains 5 red marbles, 3 blue marbles, and 2 green marbles. If two marbles are drawn without replacement, find the probability that:
   a) Both marbles are red
   b) The first marble is red and the second is blue
   c) One marble is red and one is blue (in any order)

3. In a certain city, the probability of rain on any given day is 0.3. Assuming that weather conditions are independent from day to day, find the probability that:
   a) It rains on exactly 2 of the next 5 days
   b) It rains on at least 1 of the next 3 days

4. A manufacturing process produces items with a 5% defect rate. If 10 items are randomly selected, what is the probability that:
   a) None are defective
   b) Exactly 1 is defective
   c) At least 1 is defective

5. A medical test for a disease has a sensitivity of 90% (P(Positive|Disease) = 0.9) and a specificity of 80% (P(Negative|No Disease) = 0.8). If the prevalence of the disease in the population is 2%, what is the probability that a person who tests positive actually has the disease?

## References and Further Reading

- Blitzstein, J. K., & Hwang, J. (2019). *Introduction to Probability* (2nd ed.). CRC Press.
- Ross, S. M. (2019). *A First Course in Probability* (10th ed.). Pearson.
- Wasserman, L. (2004). *All of Statistics: A Concise Course in Statistical Inference*. Springer.
- Khan Academy: Probability and Statistics. https://www.khanacademy.org/math/statistics-probability
- Harvard University's Statistics 110: Probability. https://projects.iq.harvard.edu/stat110
