# Module 5: Hypothesis Testing

## Learning Objectives
By the end of this module, you will be able to:
- Understand the fundamental concepts and logic of hypothesis testing
- Formulate appropriate null and alternative hypotheses
- Calculate and interpret test statistics and p-values
- Make decisions based on statistical significance
- Recognize and interpret Type I and Type II errors
- Apply various hypothesis tests for different scenarios
- Understand the concept of statistical power and its implications

## 5.1 Introduction to Hypothesis Testing

### The Logic of Hypothesis Testing

Hypothesis testing is a method of statistical inference that uses data from a sample to draw conclusions about a population parameter or a population probability distribution. It is a systematic way to test claims or ideas about a group or population.

The basic logic of hypothesis testing follows these steps:
1. Make an initial assumption (the null hypothesis)
2. Collect data
3. Assess whether the data are consistent or inconsistent with the initial assumption
4. Based on this assessment, either reject or fail to reject the null hypothesis

### The Null and Alternative Hypotheses

The **null hypothesis (H₀)** is a statement of no effect, no difference, or no relationship. It represents the status quo or the claim to be tested. The null hypothesis is assumed to be true until evidence suggests otherwise.

The **alternative hypothesis (H₁ or Hₐ)** is a statement that contradicts the null hypothesis. It represents what we're trying to establish evidence for.

Examples of null and alternative hypotheses:
- H₀: μ = 100 (The population mean equals 100)
  H₁: μ ≠ 100 (The population mean does not equal 100)

- H₀: μ ≤ 100 (The population mean is at most 100)
  H₁: μ > 100 (The population mean is greater than 100)

- H₀: p = 0.5 (The population proportion equals 0.5)
  H₁: p < 0.5 (The population proportion is less than 0.5)

- H₀: μ₁ = μ₂ (The means of two populations are equal)
  H₁: μ₁ ≠ μ₂ (The means of two populations are not equal)

### Types of Hypothesis Tests

Hypothesis tests can be classified based on the form of the alternative hypothesis:

1. **Two-tailed test**: Tests whether the parameter is different from the specified value (≠)
   - H₀: parameter = value
   - H₁: parameter ≠ value

2. **Left-tailed test**: Tests whether the parameter is less than the specified value (<)
   - H₀: parameter ≥ value
   - H₁: parameter < value

3. **Right-tailed test**: Tests whether the parameter is greater than the specified value (>)
   - H₀: parameter ≤ value
   - H₁: parameter > value

The choice of which test to use depends on the research question and what we're trying to establish.

## 5.2 Steps in Hypothesis Testing

The hypothesis testing procedure follows a systematic approach:

### Step 1: State the Hypotheses

Clearly state the null hypothesis (H₀) and the alternative hypothesis (H₁) in terms of population parameters.

Example:
- H₀: μ = 100 (The population mean equals 100)
- H₁: μ > 100 (The population mean is greater than 100)

### Step 2: Specify the Significance Level (α)

The significance level (α) is the threshold value for the p-value below which we reject the null hypothesis. Common values are 0.05, 0.01, and 0.10.

The significance level represents the probability of rejecting the null hypothesis when it is actually true (Type I error).

### Step 3: Select the Appropriate Test Statistic

The test statistic is a value calculated from sample data that is used to make a decision about the null hypothesis. The choice of test statistic depends on:
- The parameter being tested (mean, proportion, etc.)
- The assumptions about the population (normal, non-normal, etc.)
- The sample size

Common test statistics include:
- Z-statistic (for large samples or known population standard deviation)
- t-statistic (for small samples with unknown population standard deviation)
- Chi-square statistic (for categorical data)
- F-statistic (for comparing variances or in ANOVA)

### Step 4: Calculate the Test Statistic and p-value

Using the sample data, calculate the test statistic and determine the corresponding p-value.

The **p-value** is the probability of obtaining a test statistic at least as extreme as the one observed, assuming the null hypothesis is true. It quantifies the strength of evidence against the null hypothesis.

### Step 5: Make a Decision

Compare the p-value to the significance level (α):
- If p-value ≤ α: Reject H₀
- If p-value > α: Fail to reject H₀

Alternatively, you can use the critical value approach:
- Calculate the critical value(s) based on α
- Compare the test statistic to the critical value(s)
- Make a decision based on whether the test statistic falls in the rejection region

### Step 6: Interpret the Result

Interpret the decision in the context of the original problem. This should include:
- A clear statement about rejecting or failing to reject the null hypothesis
- An explanation of what this means in practical terms
- Any limitations or assumptions of the test

## 5.3 Types of Errors and Power

### Type I and Type II Errors

In hypothesis testing, two types of errors can occur:

1. **Type I Error (False Positive)**: Rejecting a true null hypothesis.
   - Probability = α (significance level)
   - Example: Concluding that a treatment is effective when it actually isn't

2. **Type II Error (False Negative)**: Failing to reject a false null hypothesis.
   - Probability = β
   - Example: Concluding that a treatment is not effective when it actually is

The relationship between these errors involves a trade-off: decreasing the probability of one type of error typically increases the probability of the other type.

### Statistical Power

The **power** of a hypothesis test is the probability of correctly rejecting a false null hypothesis. It is calculated as:

Power = 1 - β

Factors affecting statistical power:
1. **Sample size**: Larger samples increase power
2. **Effect size**: Larger effects are easier to detect
3. **Significance level (α)**: Higher α increases power but also increases Type I error rate
4. **Variability**: Less variability in the data increases power

### Power Analysis

Power analysis is used to determine the sample size needed to detect an effect of a specified size with a certain level of confidence.

Steps in power analysis:
1. Specify the significance level (α)
2. Specify the desired power (typically 0.80 or higher)
3. Specify the effect size (small, medium, large, or a specific value)
4. Calculate the required sample size

Example: To detect a medium effect size (d = 0.5) with 80% power at α = 0.05 in a two-sample t-test, each group would need approximately 64 subjects.

## 5.4 Z-Test for a Population Mean

The Z-test is used to test hypotheses about a population mean when the population standard deviation is known or when the sample size is large (n ≥ 30).

### Assumptions:
- The population is normally distributed or the sample size is large (n ≥ 30)
- The population standard deviation (σ) is known
- The sample is random and representative of the population

### Test Statistic:
Z = (x̄ - μ₀) / (σ / √n)

Where:
- x̄ is the sample mean
- μ₀ is the hypothesized population mean
- σ is the population standard deviation
- n is the sample size

### Decision Rule:
- Two-tailed test (H₁: μ ≠ μ₀):
  Reject H₀ if |Z| > Z(α/2) or if p-value < α

- Left-tailed test (H₁: μ < μ₀):
  Reject H₀ if Z < -Z(α) or if p-value < α

- Right-tailed test (H₁: μ > μ₀):
  Reject H₀ if Z > Z(α) or if p-value < α

### Example:
A manufacturer claims that the mean lifetime of their light bulbs is at least 1,000 hours. A random sample of 100 bulbs has a mean lifetime of 980 hours with a known population standard deviation of 120 hours. Test the claim at α = 0.05.

H₀: μ ≥ 1,000 hours
H₁: μ < 1,000 hours (left-tailed test)

Z = (980 - 1,000) / (120 / √100) = -20 / 12 = -1.67

For α = 0.05 in a left-tailed test, the critical value is -Z(0.05) = -1.645.
Since Z = -1.67 < -1.645, we reject H₀.

p-value = P(Z < -1.67) = 0.0475

Since p-value = 0.0475 < α = 0.05, we reject H₀.

Conclusion: There is sufficient evidence to conclude that the mean lifetime of the light bulbs is less than 1,000 hours.

## 5.5 T-Test for a Population Mean

The t-test is used to test hypotheses about a population mean when the population standard deviation is unknown and the sample size is small (n < 30).

### One-Sample T-Test

#### Assumptions:
- The population is normally distributed
- The population standard deviation (σ) is unknown
- The sample is random and representative of the population

#### Test Statistic:
t = (x̄ - μ₀) / (s / √n)

Where:
- x̄ is the sample mean
- μ₀ is the hypothesized population mean
- s is the sample standard deviation
- n is the sample size

The test statistic follows a t-distribution with n-1 degrees of freedom.

#### Decision Rule:
- Two-tailed test (H₁: μ ≠ μ₀):
  Reject H₀ if |t| > t(α/2, n-1) or if p-value < α

- Left-tailed test (H₁: μ < μ₀):
  Reject H₀ if t < -t(α, n-1) or if p-value < α

- Right-tailed test (H₁: μ > μ₀):
  Reject H₀ if t > t(α, n-1) or if p-value < α

#### Example:
A researcher claims that the mean cholesterol level in a certain population is 200 mg/dL. A random sample of 25 individuals has a mean cholesterol level of 210 mg/dL with a sample standard deviation of 20 mg/dL. Test the claim at α = 0.05.

H₀: μ = 200 mg/dL
H₁: μ ≠ 200 mg/dL (two-tailed test)

t = (210 - 200) / (20 / √25) = 10 / 4 = 2.5

For α = 0.05 in a two-tailed test with df = 24, the critical values are ±t(0.025, 24) = ±2.064.
Since t = 2.5 > 2.064, we reject H₀.

p-value = 2 × P(t > 2.5) with df = 24 ≈ 0.02

Since p-value = 0.02 < α = 0.05, we reject H₀.

Conclusion: There is sufficient evidence to conclude that the mean cholesterol level in the population is not 200 mg/dL.

### Two-Sample T-Test (Independent Samples)

The two-sample t-test is used to compare the means of two independent populations.

#### Assumptions:
- Both populations are normally distributed
- The samples are independent
- The samples are random and representative of their respective populations

#### Equal Variances (Pooled Variance):

If we can assume that the population variances are equal, we use the pooled variance estimate:

t = (x̄₁ - x̄₂) / (sp√(1/n₁ + 1/n₂))

Where:
- x̄₁ and x̄₂ are the sample means
- n₁ and n₂ are the sample sizes
- sp² = [(n₁-1)s₁² + (n₂-1)s₂²] / (n₁ + n₂ - 2) is the pooled variance
- s₁² and s₂² are the sample variances

The test statistic follows a t-distribution with n₁ + n₂ - 2 degrees of freedom.

#### Unequal Variances (Welch's T-Test):

If we cannot assume that the population variances are equal, we use Welch's t-test:

t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)

The degrees of freedom are calculated using the Welch-Satterthwaite equation, which is complex but is handled by statistical software.

#### Example:
A researcher wants to compare the effectiveness of two different teaching methods. Method A is used with 30 students, resulting in a mean score of 85 with a standard deviation of 8. Method B is used with 25 students, resulting in a mean score of 80 with a standard deviation of 10. Test whether there is a significant difference between the two methods at α = 0.05.

H₀: μ₁ = μ₂ (or μ₁ - μ₂ = 0)
H₁: μ₁ ≠ μ₂ (or μ₁ - μ₂ ≠ 0) (two-tailed test)

Assuming equal variances:
sp² = [(30-1)8² + (25-1)10²] / (30 + 25 - 2) = [1856 + 2400] / 53 = 4256 / 53 = 80.3
sp = √80.3 = 8.96

t = (85 - 80) / (8.96√(1/30 + 1/25)) = 5 / (8.96 × 0.283) = 5 / 2.54 = 1.97

For α = 0.05 in a two-tailed test with df = 53, the critical values are approximately ±t(0.025, 53) = ±2.006.
Since |t| = 1.97 < 2.006, we fail to reject H₀.

p-value ≈ 0.054 > α = 0.05, so we fail to reject H₀.

Conclusion: There is not sufficient evidence to conclude that there is a difference in the effectiveness of the two teaching methods.

### Paired T-Test

The paired t-test is used when the samples are dependent, such as in before-after studies or matched pairs designs.

#### Assumptions:
- The differences between pairs are normally distributed
- The pairs are dependent
- The sample is random and representative of the population

#### Test Statistic:
t = d̄ / (sd / √n)

Where:
- d̄ is the mean of the differences
- sd is the standard deviation of the differences
- n is the number of pairs

The test statistic follows a t-distribution with n-1 degrees of freedom.

#### Example:
A weight-loss program claims to be effective. To test this claim, the weights of 15 participants are measured before and after the program. The mean weight loss is 5 kg with a standard deviation of 3 kg. Test whether the program is effective at α = 0.05.

H₀: μd ≤ 0 (The program is not effective)
H₁: μd > 0 (The program is effective) (right-tailed test)

t = 5 / (3 / √15) = 5 / 0.775 = 6.45

For α = 0.05 in a right-tailed test with df = 14, the critical value is t(0.05, 14) = 1.761.
Since t = 6.45 > 1.761, we reject H₀.

p-value = P(t > 6.45) with df = 14 < 0.001

Since p-value < α = 0.05, we reject H₀.

Conclusion: There is sufficient evidence to conclude that the weight-loss program is effective.

## 5.6 Z-Test for a Population Proportion

The Z-test for a population proportion is used to test hypotheses about a population proportion.

### Assumptions:
- The sample is random and representative of the population
- The sample size is large enough that both np₀ ≥ 5 and n(1-p₀) ≥ 5, where p₀ is the hypothesized proportion

### Test Statistic:
Z = (p̂ - p₀) / √[p₀(1-p₀)/n]

Where:
- p̂ is the sample proportion
- p₀ is the hypothesized population proportion
- n is the sample size

### Decision Rule:
- Two-tailed test (H₁: p ≠ p₀):
  Reject H₀ if |Z| > Z(α/2) or if p-value < α

- Left-tailed test (H₁: p < p₀):
  Reject H₀ if Z < -Z(α) or if p-value < α

- Right-tailed test (H₁: p > p₀):
  Reject H₀ if Z > Z(α) or if p-value < α

### Example:
A candidate claims that more than 50% of voters support them. In a random sample of 400 voters, 220 express support for the candidate. Test the claim at α = 0.05.

H₀: p ≤ 0.5
H₁: p > 0.5 (right-tailed test)

p̂ = 220/400 = 0.55

Z = (0.55 - 0.5) / √[0.5(1-0.5)/400] = 0.05 / √(0.25/400) = 0.05 / 0.025 = 2

For α = 0.05 in a right-tailed test, the critical value is Z(0.05) = 1.645.
Since Z = 2 > 1.645, we reject H₀.

p-value = P(Z > 2) = 0.0228

Since p-value = 0.0228 < α = 0.05, we reject H₀.

Conclusion: There is sufficient evidence to support the candidate's claim that more than 50% of voters support them.

## 5.7 Chi-Square Tests

Chi-square tests are used for categorical data to determine whether there is a significant association between variables or whether a sample comes from a population with a specific distribution.

### Chi-Square Goodness-of-Fit Test

The chi-square goodness-of-fit test is used to determine whether a sample comes from a population with a specific distribution.

#### Assumptions:
- The sample is random and representative of the population
- The expected frequency for each category is at least 5
- The observations are independent

#### Test Statistic:
χ² = ∑[(O - E)² / E]

Where:
- O is the observed frequency
- E is the expected frequency
- The sum is over all categories

The test statistic follows a chi-square distribution with k - 1 - m degrees of freedom, where k is the number of categories and m is the number of parameters estimated from the data.

#### Example:
A die is rolled 120 times with the following results: 1 (25 times), 2 (18 times), 3 (16 times), 4 (22 times), 5 (19 times), 6 (20 times). Test whether the die is fair at α = 0.05.

H₀: The die is fair (all outcomes are equally likely)
H₁: The die is not fair (at least one outcome has a different probability)

If the die is fair, the expected frequency for each outcome is E = 120/6 = 20.

χ² = (25-20)²/20 + (18-20)²/20 + (16-20)²/20 + (22-20)²/20 + (19-20)²/20 + (20-20)²/20
   = 25/20 + 4/20 + 16/20 + 4/20 + 1/20 + 0/20
   = 50/20 = 2.5

For α = 0.05 with df = 6 -
(Content truncated due to size limit. Use line ranges to read in chunks)