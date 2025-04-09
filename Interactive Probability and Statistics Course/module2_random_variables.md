# Module 2: Random Variables and Distributions

## Random Variables

A random variable is a function that assigns a real number to each outcome in the sample space of a random experiment.

### Types of Random Variables:

1. **Discrete Random Variables**: Take on a countable number of distinct values.
   - Example: Number of heads in 10 coin flips (possible values: 0, 1, 2, ..., 10)
   - Example: Number of customers entering a store in an hour

2. **Continuous Random Variables**: Can take on any value in a continuous range.
   - Example: Height of a randomly selected person
   - Example: Time until a radioactive particle decays

### Probability Distributions:

#### For Discrete Random Variables:
- **Probability Mass Function (PMF)**: P(X = x) gives the probability that the random variable X takes on the value x.
  - Properties:
    - P(X = x) ≥ 0 for all x
    - ∑P(X = x) = 1, where the sum is over all possible values of X

- **Cumulative Distribution Function (CDF)**: F(x) = P(X ≤ x) gives the probability that X takes on a value less than or equal to x.

#### For Continuous Random Variables:
- **Probability Density Function (PDF)**: f(x) such that P(a ≤ X ≤ b) = ∫[a to b] f(x) dx
  - Properties:
    - f(x) ≥ 0 for all x
    - ∫[-∞ to ∞] f(x) dx = 1

- **Cumulative Distribution Function (CDF)**: F(x) = P(X ≤ x) = ∫[-∞ to x] f(t) dt

### Expected Value and Variance:

- **Expected Value (Mean)**: E(X) = μ
  - For discrete RV: E(X) = ∑x·P(X = x)
  - For continuous RV: E(X) = ∫x·f(x) dx

- **Variance**: Var(X) = σ² = E[(X - μ)²]
  - For discrete RV: Var(X) = ∑(x - μ)²·P(X = x)
  - For continuous RV: Var(X) = ∫(x - μ)²·f(x) dx
  - Alternative formula: Var(X) = E(X²) - [E(X)]²

- **Standard Deviation**: σ = √Var(X)

## Common Probability Distributions:

### Discrete Distributions:

1. **Bernoulli Distribution**:
   - Models a single trial with two possible outcomes (success/failure)
   - PMF: P(X = x) = p^x · (1-p)^(1-x) for x ∈ {0, 1}
   - Mean: E(X) = p
   - Variance: Var(X) = p(1-p)

2. **Binomial Distribution**:
   - Models the number of successes in n independent Bernoulli trials
   - PMF: P(X = k) = (n choose k) · p^k · (1-p)^(n-k) for k = 0, 1, 2, ..., n
   - Mean: E(X) = np
   - Variance: Var(X) = np(1-p)

3. **Poisson Distribution**:
   - Models the number of events occurring in a fixed interval
   - PMF: P(X = k) = (λ^k · e^(-λ)) / k! for k = 0, 1, 2, ...
   - Mean: E(X) = λ
   - Variance: Var(X) = λ

4. **Geometric Distribution**:
   - Models the number of trials until the first success
   - PMF: P(X = k) = (1-p)^(k-1) · p for k = 1, 2, 3, ...
   - Mean: E(X) = 1/p
   - Variance: Var(X) = (1-p)/p²

### Continuous Distributions:

1. **Uniform Distribution**:
   - All values in an interval [a, b] are equally likely
   - PDF: f(x) = 1/(b-a) for a ≤ x ≤ b
   - Mean: E(X) = (a+b)/2
   - Variance: Var(X) = (b-a)²/12

2. **Normal (Gaussian) Distribution**:
   - Bell-shaped curve defined by mean μ and standard deviation σ
   - PDF: f(x) = (1/(σ√(2π))) · e^(-(x-μ)²/(2σ²))
   - Standard Normal: Z ~ N(0, 1)
   - Properties:
     - Symmetric about the mean
     - 68-95-99.7 rule: 68% of data within 1σ, 95% within 2σ, 99.7% within 3σ

3. **Exponential Distribution**:
   - Models the time between events in a Poisson process
   - PDF: f(x) = λe^(-λx) for x ≥ 0
   - Mean: E(X) = 1/λ
   - Variance: Var(X) = 1/λ²
   - Memoryless property: P(X > s+t | X > s) = P(X > t)

## Applications of Distributions:

1. **Binomial**: Quality control (number of defective items), election polling
2. **Poisson**: Call center arrivals, website traffic, radioactive decay
3. **Normal**: Heights, weights, measurement errors, stock returns
4. **Exponential**: Equipment failure times, customer service times

## Interactive Examples for Module 2:

1. Distribution explorer with adjustable parameters
2. Probability calculator for various distributions
3. Visual comparison of different distributions
4. Central Limit Theorem demonstration
5. Random variable simulation with histogram generation
