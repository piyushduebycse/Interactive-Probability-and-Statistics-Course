# Module 5: Hypothesis Testing

## Introduction to Hypothesis Testing

Hypothesis testing is a method of statistical inference used to decide whether experimental data supports a particular claim about a population parameter.

### Key Components:

1. **Null Hypothesis (H₀)**: A statement of no effect, no difference, or no relationship. It represents the status quo or the claim to be tested.

2. **Alternative Hypothesis (H₁ or Hₐ)**: A statement that contradicts the null hypothesis. It represents what we're trying to establish evidence for.

3. **Test Statistic**: A value calculated from sample data that is used to make a decision about the null hypothesis.

4. **p-value**: The probability of obtaining a test statistic at least as extreme as the one observed, assuming the null hypothesis is true.

5. **Significance Level (α)**: The threshold value for the p-value below which we reject the null hypothesis. Common values are 0.05, 0.01, and 0.10.

## Steps in Hypothesis Testing

1. **State the hypotheses**:
   - Null hypothesis (H₀)
   - Alternative hypothesis (H₁)

2. **Specify the significance level (α)**

3. **Select the appropriate test statistic**

4. **Determine the critical region or calculate the p-value**

5. **Make a decision**:
   - If p-value ≤ α: Reject H₀
   - If p-value > α: Fail to reject H₀

6. **Interpret the result in the context of the problem**

## Types of Errors

1. **Type I Error (False Positive)**: Rejecting a true null hypothesis.
   - Probability = α (significance level)

2. **Type II Error (False Negative)**: Failing to reject a false null hypothesis.
   - Probability = β
   - Power of the test = 1 - β (probability of correctly rejecting a false null hypothesis)

## Common Hypothesis Tests

### 1. Z-Test for a Population Mean (σ known)

- **Assumptions**:
  - Population is normally distributed or n ≥ 30
  - Population standard deviation (σ) is known

- **Test Statistic**: Z = (x̄ - μ₀) / (σ / √n)

- **Hypotheses**:
  - Two-tailed: H₀: μ = μ₀ vs. H₁: μ ≠ μ₀
  - Left-tailed: H₀: μ ≥ μ₀ vs. H₁: μ < μ₀
  - Right-tailed: H₀: μ ≤ μ₀ vs. H₁: μ > μ₀

### 2. T-Test for a Population Mean (σ unknown)

- **Assumptions**:
  - Population is normally distributed or n ≥ 30
  - Population standard deviation (σ) is unknown

- **Test Statistic**: t = (x̄ - μ₀) / (s / √n) with n-1 degrees of freedom

- **Hypotheses**: Same as Z-test

### 3. Z-Test for a Population Proportion

- **Assumptions**:
  - np₀ ≥ 5 and n(1-p₀) ≥ 5

- **Test Statistic**: Z = (p̂ - p₀) / √[p₀(1-p₀)/n]

- **Hypotheses**:
  - Two-tailed: H₀: p = p₀ vs. H₁: p ≠ p₀
  - Left-tailed: H₀: p ≥ p₀ vs. H₁: p < p₀
  - Right-tailed: H₀: p ≤ p₀ vs. H₁: p > p₀

### 4. Two-Sample Z-Test for Comparing Means (σ₁ and σ₂ known)

- **Test Statistic**: Z = (x̄₁ - x̄₂ - (μ₁ - μ₂)₀) / √(σ₁²/n₁ + σ₂²/n₂)

- **Hypotheses**:
  - Two-tailed: H₀: μ₁ - μ₂ = 0 vs. H₁: μ₁ - μ₂ ≠ 0
  - Left-tailed: H₀: μ₁ - μ₂ ≥ 0 vs. H₁: μ₁ - μ₂ < 0
  - Right-tailed: H₀: μ₁ - μ₂ ≤ 0 vs. H₁: μ₁ - μ₂ > 0

### 5. Two-Sample T-Test for Comparing Means (σ₁ and σ₂ unknown)

- **Independent Samples (Equal Variances)**:
  - Test Statistic: t = (x̄₁ - x̄₂) / (sp√(1/n₁ + 1/n₂))
  - Where sp² = [(n₁-1)s₁² + (n₂-1)s₂²] / (n₁ + n₂ - 2)
  - Degrees of freedom: n₁ + n₂ - 2

- **Independent Samples (Unequal Variances) - Welch's T-Test**:
  - Test Statistic: t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)
  - Degrees of freedom: Calculated using Welch-Satterthwaite equation

- **Paired Samples**:
  - Test Statistic: t = d̄ / (sd / √n)
  - Where d̄ is the mean of the differences
  - Degrees of freedom: n - 1

### 6. Chi-Square Test for Independence

- **Purpose**: Determine if there is a significant association between two categorical variables

- **Test Statistic**: χ² = ∑[(O - E)² / E]
  - O = observed frequency
  - E = expected frequency = (row total × column total) / grand total

- **Degrees of freedom**: (r - 1) × (c - 1), where r = number of rows, c = number of columns

### 7. Chi-Square Goodness-of-Fit Test

- **Purpose**: Determine if a sample comes from a population with a specific distribution

- **Test Statistic**: χ² = ∑[(O - E)² / E]

- **Degrees of freedom**: k - 1 - m, where k = number of categories, m = number of parameters estimated

### 8. ANOVA (Analysis of Variance)

- **Purpose**: Compare means of three or more independent groups

- **Test Statistic**: F = MSB / MSW
  - MSB = Mean Square Between groups
  - MSW = Mean Square Within groups

- **Degrees of freedom**: numerator = k - 1, denominator = N - k
  - k = number of groups
  - N = total sample size

## P-Values vs. Critical Values Approach

### P-Value Approach:
1. Calculate the test statistic
2. Find the p-value
3. Compare p-value to α
4. Make a decision

### Critical Value Approach:
1. Calculate the test statistic
2. Find the critical value(s) based on α
3. Compare test statistic to critical value(s)
4. Make a decision

## Effect Size

Effect size measures the magnitude of a phenomenon, providing information about the practical significance of a result.

### Common Effect Size Measures:
1. **Cohen's d**: For comparing means
   - d = (μ₁ - μ₂) / σ
   - Small: d = 0.2, Medium: d = 0.5, Large: d = 0.8

2. **Correlation Coefficient (r)**: For measuring association
   - Small: r = 0.1, Medium: r = 0.3, Large: r = 0.5

3. **Phi (φ) and Cramer's V**: For categorical data
   - Small: 0.1, Medium: 0.3, Large: 0.5

## Interactive Examples for Module 5:

1. Hypothesis testing simulator with step-by-step guidance
2. Type I and Type II error visualization
3. Interactive p-value calculator for different test statistics
4. Power analysis tool
5. Real-world hypothesis testing scenarios with economic and social indicators
