# Module 4: Inferential Statistics

## Introduction to Inferential Statistics

Inferential statistics uses sample data to make inferences about a larger population. While descriptive statistics summarize what's in a dataset, inferential statistics help us draw conclusions that extend beyond the immediate data.

### Key Concepts:

1. **Population**: The entire group of individuals or objects about which we want to draw conclusions.
2. **Sample**: A subset of the population that is actually studied.
3. **Parameter**: A numerical characteristic of a population (usually unknown).
4. **Statistic**: A numerical characteristic of a sample (used to estimate parameters).
5. **Sampling Error**: The difference between a sample statistic and the corresponding population parameter.

## Sampling Methods

1. **Simple Random Sampling**:
   - Each member of the population has an equal probability of being selected.
   - Minimizes bias but can be difficult to implement for large populations.

2. **Stratified Sampling**:
   - Population is divided into distinct subgroups (strata), then samples are taken from each stratum.
   - Ensures representation of all subgroups.
   - More precise than simple random sampling when strata are homogeneous.

3. **Cluster Sampling**:
   - Population is divided into clusters, then entire clusters are randomly selected.
   - More economical but typically less precise than simple random sampling.

4. **Systematic Sampling**:
   - Select every kth element from the population after a random start.
   - Simple to implement but can introduce bias if there's a pattern in the population.

5. **Convenience Sampling**:
   - Samples are selected based on availability.
   - Prone to bias and not generally recommended for inferential statistics.

## Sampling Distributions

A sampling distribution is the probability distribution of a statistic obtained from a large number of samples drawn from a specific population.

### Properties of the Sampling Distribution of the Mean:

1. **Shape**:
   - For large samples (n ≥ 30) or normally distributed populations, the sampling distribution is approximately normal (Central Limit Theorem).

2. **Center**:
   - The mean of the sampling distribution equals the population mean: μx̄ = μ

3. **Spread**:
   - The standard deviation of the sampling distribution (standard error) is: σx̄ = σ/√n
   - As sample size increases, the standard error decreases.

### Central Limit Theorem (CLT):

The CLT states that the sampling distribution of the mean approaches a normal distribution as the sample size increases, regardless of the shape of the population distribution.

- For n ≥ 30, the sampling distribution is approximately normal.
- The approximation improves as n increases.
- This theorem is fundamental to many inferential procedures.

## Point Estimation

A point estimate is a single value used to estimate a population parameter.

### Common Point Estimators:

1. **Sample Mean (x̄)**: Estimates the population mean (μ)
2. **Sample Proportion (p̂)**: Estimates the population proportion (p)
3. **Sample Variance (s²)**: Estimates the population variance (σ²)
4. **Sample Standard Deviation (s)**: Estimates the population standard deviation (σ)

### Properties of Good Estimators:

1. **Unbiased**: The expected value of the estimator equals the parameter being estimated.
2. **Consistent**: The estimator converges to the parameter as sample size increases.
3. **Efficient**: The estimator has the smallest variance among all unbiased estimators.
4. **Sufficient**: The estimator uses all relevant information in the sample.

## Confidence Intervals

A confidence interval provides a range of values that likely contains the population parameter.

### Confidence Interval for Population Mean (μ):

1. **When σ is known**:
   - CI: x̄ ± z(α/2) × (σ/√n)
   - z(α/2) is the critical value from the standard normal distribution

2. **When σ is unknown and n ≥ 30**:
   - CI: x̄ ± z(α/2) × (s/√n)

3. **When σ is unknown and n < 30**:
   - CI: x̄ ± t(α/2, n-1) × (s/√n)
   - t(α/2, n-1) is the critical value from the t-distribution with n-1 degrees of freedom

### Confidence Interval for Population Proportion (p):

- CI: p̂ ± z(α/2) × √[p̂(1-p̂)/n]
- Valid when np̂ ≥ 5 and n(1-p̂) ≥ 5

### Interpretation of Confidence Level:

- A 95% confidence level means that if we were to take many samples and construct a confidence interval from each sample, about 95% of these intervals would contain the true population parameter.
- It does NOT mean there's a 95% probability that the parameter falls within a specific interval.

### Factors Affecting Confidence Interval Width:

1. **Confidence Level**: Higher confidence level → wider interval
2. **Sample Size**: Larger sample size → narrower interval
3. **Population Variability**: Greater variability → wider interval

## Margin of Error

The margin of error (ME) is half the width of a confidence interval.

- For means: ME = z(α/2) × (σ/√n) or ME = t(α/2, n-1) × (s/√n)
- For proportions: ME = z(α/2) × √[p̂(1-p̂)/n]

### Sample Size Determination:

To achieve a desired margin of error (E) at a given confidence level:

- For means: n = (z(α/2) × σ/E)²
- For proportions: n = (z(α/2))² × p̂(1-p̂)/E²

## Interactive Examples for Module 4:

1. Sampling distribution simulator with adjustable parameters
2. Central Limit Theorem visualization tool
3. Confidence interval calculator with interpretation
4. Sample size calculator for different scenarios
5. Interactive demonstration of different sampling methods
