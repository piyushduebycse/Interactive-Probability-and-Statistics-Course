# Module 2: Random Variables and Distributions

## Learning Objectives
By the end of this module, you will be able to:
- Distinguish between discrete and continuous random variables
- Calculate and interpret probability mass functions and probability density functions
- Compute expected values, variances, and standard deviations
- Identify and apply common probability distributions
- Understand the relationships between different distributions
- Apply distribution concepts to solve real-world problems

## 2.1 Introduction to Random Variables

### What is a Random Variable?

A random variable is a function that assigns a real number to each outcome in the sample space of a random experiment. It provides a way to quantify and work with random outcomes mathematically.

For example, if we roll a die, we could define a random variable X as the number that appears on the top face. In this case, X can take values 1, 2, 3, 4, 5, or 6, each with probability 1/6.

Random variables allow us to move from qualitative descriptions of outcomes to quantitative measures that we can analyze mathematically.

### Types of Random Variables

Random variables are classified into two main types:

1. **Discrete Random Variables**: Can take on only a countable number of distinct values.
   - Example: Number of heads in 10 coin flips (possible values: 0, 1, 2, ..., 10)
   - Example: Number of customers entering a store in an hour (possible values: 0, 1, 2, ...)
   - Example: Number of defective items in a batch of 100 products

2. **Continuous Random Variables**: Can take on any value in a continuous range.
   - Example: Height of a randomly selected person
   - Example: Time until a radioactive particle decays
   - Example: Temperature at a specific location

The distinction between discrete and continuous random variables affects how we calculate probabilities and work with their distributions.

## 2.2 Discrete Random Variables

### Probability Mass Function (PMF)

For a discrete random variable X, the probability mass function (PMF) gives the probability that X takes on a specific value x:

P(X = x) = P_X(x)

Properties of a valid PMF:
1. P_X(x) ≥ 0 for all x (probabilities are non-negative)
2. ∑P_X(x) = 1, where the sum is over all possible values of X (probabilities sum to 1)

Example: If X represents the number of heads in 3 coin flips, the PMF is:
- P(X = 0) = 1/8
- P(X = 1) = 3/8
- P(X = 2) = 3/8
- P(X = 3) = 1/8

### Cumulative Distribution Function (CDF)

The cumulative distribution function (CDF) of a discrete random variable X gives the probability that X is less than or equal to a specific value x:

F_X(x) = P(X ≤ x) = ∑P_X(t), where the sum is over all t ≤ x

Properties of a CDF:
1. 0 ≤ F_X(x) ≤ 1 for all x
2. F_X(x) is non-decreasing (if a < b, then F_X(a) ≤ F_X(b))
3. lim(x→-∞) F_X(x) = 0 and lim(x→∞) F_X(x) = 1

Example: For the number of heads in 3 coin flips:
- F_X(0) = P(X ≤ 0) = P(X = 0) = 1/8
- F_X(1) = P(X ≤ 1) = P(X = 0) + P(X = 1) = 1/8 + 3/8 = 4/8 = 1/2
- F_X(2) = P(X ≤ 2) = P(X = 0) + P(X = 1) + P(X = 2) = 1/8 + 3/8 + 3/8 = 7/8
- F_X(3) = P(X ≤ 3) = P(X = 0) + P(X = 1) + P(X = 2) + P(X = 3) = 1/8 + 3/8 + 3/8 + 1/8 = 8/8 = 1

## 2.3 Continuous Random Variables

### Probability Density Function (PDF)

For a continuous random variable X, the probability density function (PDF) f_X(x) is such that the probability of X falling in a small interval [x, x+dx] is approximately f_X(x)dx.

The probability that X falls in an interval [a, b] is:
P(a ≤ X ≤ b) = ∫[a to b] f_X(x) dx

Properties of a valid PDF:
1. f_X(x) ≥ 0 for all x (density is non-negative)
2. ∫[-∞ to ∞] f_X(x) dx = 1 (total probability is 1)

Note: For a continuous random variable, the probability of any single point is zero:
P(X = a) = 0 for any value a

Example: If X has a uniform distribution on [0, 1], then:
- f_X(x) = 1 for 0 ≤ x ≤ 1, and f_X(x) = 0 otherwise
- P(0.25 ≤ X ≤ 0.75) = ∫[0.25 to 0.75] 1 dx = 0.75 - 0.25 = 0.5

### Cumulative Distribution Function (CDF)

The CDF of a continuous random variable X is:
F_X(x) = P(X ≤ x) = ∫[-∞ to x] f_X(t) dt

Properties of a CDF are the same as for discrete random variables.

The relationship between PDF and CDF:
- f_X(x) = d/dx F_X(x) (the PDF is the derivative of the CDF)
- F_X(x) = ∫[-∞ to x] f_X(t) dt (the CDF is the integral of the PDF)

Example: For a uniform distribution on [0, 1]:
- F_X(x) = 0 for x < 0
- F_X(x) = x for 0 ≤ x ≤ 1
- F_X(x) = 1 for x > 1

## 2.4 Expected Value and Variance

### Expected Value (Mean)

The expected value (or mean) of a random variable X, denoted E(X) or μ_X, is a measure of the central tendency of the distribution.

For a discrete random variable:
E(X) = ∑x·P_X(x), where the sum is over all possible values of X

For a continuous random variable:
E(X) = ∫[-∞ to ∞] x·f_X(x) dx

The expected value can be interpreted as the long-run average value of the random variable over many repetitions of the experiment.

Example: For the number of heads in 3 coin flips:
E(X) = 0·(1/8) + 1·(3/8) + 2·(3/8) + 3·(1/8) = 0 + 3/8 + 6/8 + 3/8 = 12/8 = 1.5

### Properties of Expected Value

1. E(a) = a for any constant a
2. E(aX) = a·E(X) for any constant a
3. E(X + Y) = E(X) + E(Y) for any random variables X and Y
4. E(X - Y) = E(X) - E(Y)
5. If X and Y are independent, then E(X·Y) = E(X)·E(Y)

### Variance and Standard Deviation

The variance of a random variable X, denoted Var(X) or σ²_X, measures the spread or dispersion of the distribution around the mean.

Var(X) = E[(X - μ_X)²] = E(X²) - [E(X)]²

For a discrete random variable:
Var(X) = ∑(x - μ_X)²·P_X(x) = ∑x²·P_X(x) - [∑x·P_X(x)]²

For a continuous random variable:
Var(X) = ∫[-∞ to ∞] (x - μ_X)²·f_X(x) dx = ∫[-∞ to ∞] x²·f_X(x) dx - [∫[-∞ to ∞] x·f_X(x) dx]²

The standard deviation, denoted σ_X, is the square root of the variance:
σ_X = √Var(X)

The standard deviation has the same units as the random variable, making it easier to interpret than the variance.

Example: For the number of heads in 3 coin flips:
E(X²) = 0²·(1/8) + 1²·(3/8) + 2²·(3/8) + 3²·(1/8) = 0 + 3/8 + 12/8 + 9/8 = 24/8 = 3
Var(X) = E(X²) - [E(X)]² = 3 - 1.5² = 3 - 2.25 = 0.75
σ_X = √0.75 ≈ 0.866

### Properties of Variance

1. Var(a) = 0 for any constant a
2. Var(aX) = a²·Var(X) for any constant a
3. Var(X + a) = Var(X) for any constant a
4. If X and Y are independent, then Var(X + Y) = Var(X) + Var(Y)

## 2.5 Common Discrete Distributions

### Bernoulli Distribution

The Bernoulli distribution models a single trial with two possible outcomes: success (1) or failure (0).

PMF: P(X = x) = p^x · (1-p)^(1-x) for x ∈ {0, 1}
- P(X = 1) = p (probability of success)
- P(X = 0) = 1-p (probability of failure)

Mean: E(X) = p
Variance: Var(X) = p(1-p)

Example: A single coin flip with probability p of heads follows a Bernoulli distribution.

### Binomial Distribution

The binomial distribution models the number of successes in n independent Bernoulli trials, each with probability p of success.

PMF: P(X = k) = (n choose k) · p^k · (1-p)^(n-k) for k = 0, 1, 2, ..., n

Where (n choose k) = n! / [k! · (n-k)!] is the binomial coefficient.

Mean: E(X) = np
Variance: Var(X) = np(1-p)

Example: The number of heads in 10 coin flips follows a binomial distribution with n = 10 and p = 0.5.

### Geometric Distribution

The geometric distribution models the number of trials until the first success in a sequence of independent Bernoulli trials.

PMF: P(X = k) = (1-p)^(k-1) · p for k = 1, 2, 3, ...

Mean: E(X) = 1/p
Variance: Var(X) = (1-p)/p²

Example: The number of times you need to roll a die until you get a 6 follows a geometric distribution with p = 1/6.

### Poisson Distribution

The Poisson distribution models the number of events occurring in a fixed interval of time or space, assuming events occur independently and at a constant average rate.

PMF: P(X = k) = (λ^k · e^(-λ)) / k! for k = 0, 1, 2, ...

Where λ (lambda) is the average number of events in the interval.

Mean: E(X) = λ
Variance: Var(X) = λ

Example: The number of calls arriving at a call center in a 10-minute interval might follow a Poisson distribution with λ = 5 (average of 5 calls per 10 minutes).

### Negative Binomial Distribution

The negative binomial distribution models the number of trials needed to achieve r successes in a sequence of independent Bernoulli trials.

PMF: P(X = k) = (k-1 choose r-1) · p^r · (1-p)^(k-r) for k = r, r+1, r+2, ...

Mean: E(X) = r/p
Variance: Var(X) = r(1-p)/p²

Example: The number of times you need to roll a die to get three 6's follows a negative binomial distribution with r = 3 and p = 1/6.

### Hypergeometric Distribution

The hypergeometric distribution models the number of successes in n draws without replacement from a finite population containing N items, of which K are successes.

PMF: P(X = k) = [(K choose k) · (N-K choose n-k)] / (N choose n) for max(0, n+K-N) ≤ k ≤ min(n, K)

Mean: E(X) = n·(K/N)
Variance: Var(X) = n·(K/N)·(1-K/N)·(N-n)/(N-1)

Example: If you draw 5 cards from a standard deck, the number of hearts follows a hypergeometric distribution with N = 52, K = 13, and n = 5.

## 2.6 Common Continuous Distributions

### Uniform Distribution

The uniform distribution models a random variable that is equally likely to take any value in a given interval [a, b].

PDF: f(x) = 1/(b-a) for a ≤ x ≤ b, and f(x) = 0 otherwise

Mean: E(X) = (a+b)/2
Variance: Var(X) = (b-a)²/12

Example: The position of a randomly placed point on a line segment from 0 to 1 follows a uniform distribution on [0, 1].

### Normal (Gaussian) Distribution

The normal distribution is a bell-shaped distribution that is symmetric about its mean. It is one of the most important distributions in statistics due to the Central Limit Theorem.

PDF: f(x) = (1/(σ√(2π))) · e^(-(x-μ)²/(2σ²)) for -∞ < x < ∞

Where μ is the mean and σ is the standard deviation.

Mean: E(X) = μ
Variance: Var(X) = σ²

The standard normal distribution has μ = 0 and σ = 1, and is denoted Z ~ N(0, 1).

Properties of the normal distribution:
- Symmetric about the mean
- The mean, median, and mode are all equal
- 68% of the data falls within 1 standard deviation of the mean
- 95% of the data falls within 2 standard deviations of the mean
- 99.7% of the data falls within 3 standard deviations of the mean (the 68-95-99.7 rule)

Example: Heights of adult males in a population often follow a normal distribution.

### Exponential Distribution

The exponential distribution models the time between events in a Poisson process, or the time until the first event occurs.

PDF: f(x) = λe^(-λx) for x ≥ 0, and f(x) = 0 for x < 0

Where λ is the rate parameter.

Mean: E(X) = 1/λ
Variance: Var(X) = 1/λ²

The exponential distribution has the "memoryless property": P(X > s+t | X > s) = P(X > t)

Example: The time until the next earthquake in a region might follow an exponential distribution.

### Gamma Distribution

The gamma distribution is a flexible distribution that generalizes the exponential distribution to model the time until the kth event in a Poisson process.

PDF: f(x) = (λ^α · x^(α-1) · e^(-λx)) / Γ(α) for x > 0, and f(x) = 0 for x ≤ 0

Where α (alpha) is the shape parameter, λ is the rate parameter, and Γ(α) is the gamma function.

Mean: E(X) = α/λ
Variance: Var(X) = α/λ²

Example: The total time to complete α tasks, where each task takes an exponentially distributed amount of time with rate λ.

### Beta Distribution

The beta distribution is a flexible distribution defined on the interval [0, 1], often used to model proportions or probabilities.

PDF: f(x) = (x^(α-1) · (1-x)^(β-1)) / B(α, β) for 0 ≤ x ≤ 1, and f(x) = 0 otherwise

Where α and β are shape parameters, and B(α, β) is the beta function.

Mean: E(X) = α/(α+β)
Variance: Var(X) = (α·β)/((α+β)²·(α+β+1))

Example: The proportion of voters who will vote for a particular candidate might be modeled using a beta distribution.

### Chi-Square Distribution

The chi-square distribution with k degrees of freedom is the distribution of the sum of squares of k independent standard normal random variables.

PDF: f(x) = (x^(k/2-1) · e^(-x/2)) / (2^(k/2) · Γ(k/2)) for x > 0, and f(x) = 0 for x ≤ 0

Mean: E(X) = k
Variance: Var(X) = 2k

Example: The chi-square distribution is used in hypothesis testing and constructing confidence intervals for population variance.

### Student's t-Distribution

The t-distribution with v degrees of freedom is the distribution of the ratio of a standard normal random variable to the square root of a chi-square random variable with v degrees of freedom divided by v.

PDF: Complex formula involving the gamma function

Mean: E(X) = 0 for v > 1, undefined otherwise
Variance: Var(X) = v/(v-2) for v > 2, undefined for v ≤ 2

Properties of the t-distribution:
- Symmetric about 0
- Bell-shaped, but with heavier tails than the normal distribution
- As v increases, the t-distribution approaches the standard normal distribution

Example: The t-distribution is used in hypothesis testing and constructing confidence intervals for population means when the population standard deviation is unknown.

## 2.7 Relationships Between Distributions

Many probability distributions are related to each other in various ways:

1. **Binomial and Bernoulli**: A binomial distribution with n = 1 is a Bernoulli distribution.

2. **Binomial and Poisson**: For large n and small p, with np = λ, the binomial distribution B(n, p) approximates the Poisson distribution with parameter λ.

3. **Binomial and Normal**: For large n, the binomial distribution B(n, p) can be approximated by the normal distribution N(np, np(1-p)).

4. **Poisson and Exponential**: If events occur according to a Poisson process with rate λ, then the time between events follows an exponential distribution with parameter λ.

5. **Exponential and Gamma**: The sum of n independent exponential random variables with parameter λ follows a gamma distribution with shape parameter n and rate parameter λ.

6. **Normal and Chi-Square**: If Z₁, Z₂, ..., Zₙ are independent standard normal random variables, then the sum of their squares follows a chi-square distribution with n degrees of freedom.

7. **Normal and t-Distribution**: If Z is a standard normal random variable and V is a chi-square random variable with v degrees of freedom, independent of Z, then Z/√(V/v) follows a t-distribution with v degrees of freedom.

## 2.8 Applications of Distributions

### Quality Control

Binomial and Poisson distributions are used in quality control to model the number of defects in a batch of products. Control charts and acceptance sampling plans are based on these distributions.

Example: A manufacturer inspects a sample of 100 items from a large batch. If the acceptable defect rate is 2%, they might use a binomial distribution to determine the probability of finding more than 5 defects in the sample.

### Reliability Engineering

Exponential and Weibull distributions are commonly used to model the lifetime of components and systems in reliability engineering.

Example: If the lifetime of a light bulb follows an exponential distribution with a mean of 1000 hours, the probability that it lasts more than 1500 hours is e^(-1500/1000) ≈ 0.223 or about 22.3%.

### Finance

Normal, log-normal, and other distributions are used to model stock returns, option pricing, and risk management in finance.

Example: The Black-Scholes model for option pricing assumes that stock prices follow a log-normal distribution.

### Queuing Theory

Poisson and exponential distributions are fundamental in queuing theory, which models waiting lines in service systems.

Example: If customers arrive at a bank according to a Poisson process with rate λ = 10 per hour, and service times follow an exponential distribution with mean 5 minutes, queuing theory can predict the average waiting time and queue length.

### Insurance

Gamma, Pareto, and other heavy-tailed distributions are used in insurance to model claim sizes and frequencies.

Example: An insurance company mig
(Content truncated due to size limit. Use line ranges to read in chunks)