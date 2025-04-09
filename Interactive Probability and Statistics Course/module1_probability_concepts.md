# Module 1: Introduction to Probability

## Basic Probability Concepts

Probability theory provides a mathematical framework for modeling and analyzing random phenomena. It quantifies the likelihood of events occurring in a random experiment.

### Key Concepts:

1. **Sample Space (Ω)**: The set of all possible outcomes of a random experiment.
   - Example: When rolling a six-sided die, Ω = {1, 2, 3, 4, 5, 6}
   - Example: When flipping a coin, Ω = {Heads, Tails}

2. **Event**: A subset of the sample space.
   - Example: The event of rolling an even number = {2, 4, 6}
   - Example: The event of drawing a face card from a standard deck

3. **Probability Function (P)**: A function that assigns a real number P(A) to an event A, representing the likelihood of A occurring.

### Probability Axioms:

1. Non-negativity: P(A) ≥ 0 for any event A
2. Normalization: P(Ω) = 1
3. Additivity: For mutually exclusive events A and B, P(A ∪ B) = P(A) + P(B)

### Probability Rules:

1. **Complement Rule**: P(A') = 1 - P(A)
   - Example: If P(rolling a 6) = 1/6, then P(not rolling a 6) = 1 - 1/6 = 5/6

2. **Addition Rule**: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
   - For mutually exclusive events: P(A ∪ B) = P(A) + P(B)

3. **Conditional Probability**: P(A|B) = P(A ∩ B) / P(B), where P(B) > 0
   - Represents the probability of event A occurring given that event B has occurred

4. **Multiplication Rule**: P(A ∩ B) = P(A) × P(B|A) = P(B) × P(A|B)

5. **Law of Total Probability**: If events B₁, B₂, ..., Bₙ form a partition of the sample space, then:
   P(A) = P(A|B₁)P(B₁) + P(A|B₂)P(B₂) + ... + P(A|Bₙ)P(Bₙ)

### Independence:

Two events A and B are independent if P(A ∩ B) = P(A) × P(B), or equivalently, if P(A|B) = P(A) or P(B|A) = P(B).

### Bayes' Theorem:

P(A|B) = [P(B|A) × P(A)] / P(B)

This theorem allows us to update probabilities based on new evidence.

## Real-World Applications:

1. **Risk Assessment**: Insurance companies use probability to determine premiums based on the likelihood of various events.

2. **Medical Diagnosis**: Doctors use conditional probabilities to interpret test results and make diagnoses.

3. **Weather Forecasting**: Meteorologists use probability models to predict weather patterns.

4. **Quality Control**: Manufacturers use probability to design sampling plans for inspecting products.

5. **Games of Chance**: Casinos and lottery systems are designed based on probability principles.

## Interactive Examples for Module 1:

1. Coin flip simulator with probability tracking
2. Dice rolling experiments with frequency analysis
3. Card drawing simulations for calculating probabilities
4. Venn diagram interactive tool for visualizing set operations
5. Conditional probability calculator with visual representations
