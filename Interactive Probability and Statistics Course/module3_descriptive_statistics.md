# Module 3: Descriptive Statistics

## Introduction to Descriptive Statistics

Descriptive statistics involves methods for organizing, summarizing, and presenting data in a meaningful way. These techniques help us understand the main features of a dataset without necessarily making inferences beyond the data we have.

### Types of Data:

1. **Qualitative (Categorical) Data**: Non-numerical data that can be classified into categories.
   - **Nominal**: Categories with no natural ordering (e.g., gender, blood type)
   - **Ordinal**: Categories with a natural ordering (e.g., education level, satisfaction ratings)

2. **Quantitative (Numerical) Data**: Numerical measurements or counts.
   - **Discrete**: Countable values, often integers (e.g., number of children, count of errors)
   - **Continuous**: Can take any value within a range (e.g., height, weight, time)

## Measures of Central Tendency

These statistics describe the center or typical value of a dataset.

1. **Mean (Arithmetic Average)**:
   - Formula: μ = (∑x) / n (population) or x̄ = (∑x) / n (sample)
   - Properties:
     - Affected by extreme values (outliers)
     - Uses all data points
     - Appropriate for symmetric distributions

2. **Median**:
   - The middle value when data is arranged in order
   - For odd n: middle value
   - For even n: average of two middle values
   - Properties:
     - Resistant to outliers
     - Appropriate for skewed distributions or when outliers are present

3. **Mode**:
   - The most frequently occurring value(s)
   - A dataset can have no mode, one mode (unimodal), or multiple modes (multimodal)
   - The only measure of central tendency applicable to categorical data

4. **Geometric Mean**:
   - Formula: (∏x)^(1/n) or (x₁ × x₂ × ... × xₙ)^(1/n)
   - Used for growth rates, returns, and ratios

5. **Harmonic Mean**:
   - Formula: n / (∑(1/x))
   - Used for averaging rates and ratios

## Measures of Dispersion

These statistics describe the spread or variability in a dataset.

1. **Range**:
   - Formula: Maximum value - Minimum value
   - Simple but affected by outliers

2. **Interquartile Range (IQR)**:
   - Formula: Q₃ - Q₁ (75th percentile - 25th percentile)
   - Robust to outliers
   - Contains middle 50% of the data

3. **Variance**:
   - Population: σ² = ∑(x - μ)² / N
   - Sample: s² = ∑(x - x̄)² / (n-1)
   - Measures average squared deviation from the mean
   - Units are squared (e.g., meters²)

4. **Standard Deviation**:
   - Population: σ = √σ²
   - Sample: s = √s²
   - Same units as original data
   - Interpretation with normal distribution:
     - Approximately 68% of data within 1 standard deviation of mean
     - Approximately 95% of data within 2 standard deviations of mean
     - Approximately 99.7% of data within 3 standard deviations of mean

5. **Coefficient of Variation**:
   - Formula: (s / x̄) × 100%
   - Unitless measure of relative variability
   - Useful for comparing variability between datasets with different units or scales

## Measures of Position

These statistics describe the relative position of data points.

1. **Percentiles**:
   - The pth percentile is a value such that p% of the data falls below it
   - Quartiles: Q₁ (25th percentile), Q₂ (50th percentile = median), Q₃ (75th percentile)
   - Deciles: Divide data into 10 equal parts
   - Quintiles: Divide data into 5 equal parts

2. **Z-scores (Standard scores)**:
   - Formula: z = (x - x̄) / s
   - Measures how many standard deviations a data point is from the mean
   - Useful for comparing values from different distributions

## Measures of Shape

These statistics describe the form of the distribution.

1. **Skewness**:
   - Measures asymmetry of the distribution
   - Positive skew: Right tail is longer (mean > median)
   - Negative skew: Left tail is longer (mean < median)
   - Zero skew: Symmetric distribution (mean = median)

2. **Kurtosis**:
   - Measures the "tailedness" of the distribution
   - Leptokurtic: Heavy tails, more outlier-prone than normal distribution
   - Mesokurtic: Similar to normal distribution
   - Platykurtic: Light tails, less outlier-prone than normal distribution

## Data Visualization Techniques

1. **For Categorical Data**:
   - Bar charts
   - Pie charts
   - Pareto charts
   - Contingency tables

2. **For Numerical Data**:
   - Histograms
   - Stem-and-leaf plots
   - Box plots (Box-and-whisker plots)
   - Scatter plots
   - Line graphs
   - Frequency polygons

3. **For Bivariate Data**:
   - Scatter plots
   - Heat maps
   - Bubble charts

## Exploratory Data Analysis (EDA)

EDA is an approach to analyzing datasets to summarize their main characteristics, often with visual methods.

1. **Key Steps in EDA**:
   - Data cleaning and preprocessing
   - Univariate analysis (examining one variable at a time)
   - Bivariate analysis (examining relationships between pairs of variables)
   - Multivariate analysis (examining relationships between multiple variables)

2. **Common EDA Techniques**:
   - Summary statistics
   - Visualization
   - Correlation analysis
   - Outlier detection

## Interactive Examples for Module 3:

1. Data visualization tool with real datasets (GDP, population, education, health indicators)
2. Interactive histogram generator with adjustable bin sizes
3. Box plot creator with outlier identification
4. Measures of central tendency and dispersion calculator
5. Distribution shape analyzer (skewness and kurtosis)
