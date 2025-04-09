# Module 3: Descriptive Statistics

## Learning Objectives
By the end of this module, you will be able to:
- Distinguish between different types of data and measurement scales
- Calculate and interpret measures of central tendency
- Compute and analyze measures of dispersion
- Describe the shape of distributions using skewness and kurtosis
- Create and interpret various data visualizations
- Apply exploratory data analysis techniques to real datasets

## 3.1 Introduction to Descriptive Statistics

### What are Descriptive Statistics?

Descriptive statistics involve methods for organizing, summarizing, and presenting data in a meaningful way. While inferential statistics (covered in later modules) aim to draw conclusions beyond the data at hand, descriptive statistics focus on describing the main features of the collected data.

Descriptive statistics serve several important purposes:
- Summarizing large datasets into simpler, more digestible information
- Identifying patterns, trends, and relationships in the data
- Detecting outliers and unusual observations
- Providing the foundation for further statistical analysis
- Communicating data findings effectively

### Types of Data

Before applying statistical methods, it's important to understand the type of data you're working with:

1. **Qualitative (Categorical) Data**: Non-numerical data that can be classified into categories.
   - **Nominal**: Categories with no natural ordering
     - Examples: Gender, blood type, country of origin, product type
     - Operations: Equality/inequality, frequency counts, mode
   
   - **Ordinal**: Categories with a natural ordering
     - Examples: Education level (high school, bachelor's, master's, doctorate), satisfaction ratings (poor, fair, good, excellent), socioeconomic status
     - Operations: All nominal operations plus greater than/less than, median, percentiles

2. **Quantitative (Numerical) Data**: Numerical measurements or counts.
   - **Discrete**: Countable values, often integers
     - Examples: Number of children, count of errors, number of customers
     - Operations: Arithmetic operations, all summary statistics
   
   - **Continuous**: Can take any value within a range
     - Examples: Height, weight, time, temperature, distance
     - Operations: Arithmetic operations, all summary statistics

### Measurement Scales

Another way to classify data is by measurement scale:

1. **Nominal Scale**: Categories with no meaningful order
   - Example: Colors (red, blue, green)
   - Permissible statistics: Frequency, mode, chi-square

2. **Ordinal Scale**: Categories with a meaningful order but no consistent interval between values
   - Example: Likert scale (strongly disagree, disagree, neutral, agree, strongly agree)
   - Permissible statistics: Median, percentiles, rank correlation

3. **Interval Scale**: Numerical scale with consistent intervals but no meaningful zero point
   - Example: Temperature in Celsius (0°C does not mean "no temperature")
   - Permissible statistics: Mean, standard deviation, Pearson correlation

4. **Ratio Scale**: Numerical scale with consistent intervals and a meaningful zero point
   - Example: Height, weight, time (0 means "none")
   - Permissible statistics: All statistical measures, including geometric mean and coefficient of variation

Understanding the type and scale of your data is crucial for selecting appropriate descriptive statistics and visualization methods.

## 3.2 Measures of Central Tendency

Measures of central tendency describe the "typical" or "central" value of a dataset. The three most common measures are the mean, median, and mode.

### Mean (Arithmetic Average)

The mean is the sum of all values divided by the number of values.

For a population:
μ = (∑x) / N

For a sample:
x̄ = (∑x) / n

Properties of the mean:
- Uses all data points in the calculation
- Sensitive to extreme values (outliers)
- Appropriate for interval and ratio data
- Minimizes the sum of squared deviations from the center

Example: For the dataset {2, 5, 7, 9, 12}, the mean is (2 + 5 + 7 + 9 + 12) / 5 = 35 / 5 = 7

### Median

The median is the middle value when the data is arranged in order.

For an odd number of observations:
Median = value at position (n + 1) / 2

For an even number of observations:
Median = average of values at positions n / 2 and (n / 2) + 1

Properties of the median:
- Not affected by extreme values (outliers)
- Appropriate for ordinal, interval, and ratio data
- Minimizes the sum of absolute deviations from the center
- Useful for skewed distributions

Example: For the dataset {2, 5, 7, 9, 12}, the median is 7 (the middle value)
Example: For the dataset {2, 5, 7, 9, 12, 20}, the median is (7 + 9) / 2 = 8

### Mode

The mode is the most frequently occurring value in the dataset.

Properties of the mode:
- Can be used with any type of data, including nominal
- A dataset can have no mode, one mode (unimodal), or multiple modes (multimodal)
- Not affected by extreme values
- May not be unique

Example: For the dataset {2, 5, 5, 7, 9, 12, 12}, the modes are 5 and 12 (bimodal)

### Other Measures of Central Tendency

#### Geometric Mean

The geometric mean is the nth root of the product of n values.

Geometric Mean = (∏x)^(1/n) = (x₁ × x₂ × ... × xₙ)^(1/n)

Properties:
- Appropriate for ratio data
- Used for growth rates, returns, and ratios
- Less sensitive to extreme values than the arithmetic mean
- All values must be positive

Example: For the dataset {2, 4, 8}, the geometric mean is (2 × 4 × 8)^(1/3) = 64^(1/3) ≈ 4

#### Harmonic Mean

The harmonic mean is the reciprocal of the arithmetic mean of the reciprocals.

Harmonic Mean = n / (∑(1/x)) = n / (1/x₁ + 1/x₂ + ... + 1/xₙ)

Properties:
- Appropriate for ratio data
- Used for averaging rates and ratios
- All values must be positive
- Gives more weight to smaller values

Example: For the dataset {2, 4, 8}, the harmonic mean is 3 / (1/2 + 1/4 + 1/8) = 3 / (4/8 + 2/8 + 1/8) = 3 / (7/8) = 24/7 ≈ 3.43

### Choosing the Appropriate Measure of Central Tendency

The choice of which measure to use depends on:
- The type and scale of the data
- The shape of the distribution
- The presence of outliers
- The specific question being addressed

General guidelines:
- For nominal data: Use the mode
- For ordinal data: Use the median
- For interval/ratio data with a symmetric distribution: Use the mean
- For interval/ratio data with a skewed distribution: Use the median
- For growth rates or ratios: Consider the geometric mean
- For rates (e.g., speeds): Consider the harmonic mean

## 3.3 Measures of Dispersion

Measures of dispersion describe the spread or variability in a dataset. They indicate how much the data points differ from each other and from the center of the distribution.

### Range

The range is the difference between the maximum and minimum values in the dataset.

Range = Maximum value - Minimum value

Properties:
- Simple to calculate and understand
- Uses only two data points (ignores all others)
- Highly sensitive to outliers
- Increases with sample size

Example: For the dataset {2, 5, 7, 9, 12}, the range is 12 - 2 = 10

### Interquartile Range (IQR)

The IQR is the difference between the third quartile (Q₃) and the first quartile (Q₁).

IQR = Q₃ - Q₁

Where:
- Q₁ is the 25th percentile (the median of the lower half of the data)
- Q₃ is the 75th percentile (the median of the upper half of the data)

Properties:
- Robust to outliers
- Contains the middle 50% of the data
- Used to identify outliers (values below Q₁ - 1.5 × IQR or above Q₃ + 1.5 × IQR)
- Useful for skewed distributions

Example: For the dataset {2, 5, 7, 9, 12}, Q₁ = 3.5, Q₃ = 10.5, so IQR = 10.5 - 3.5 = 7

### Variance

The variance measures the average squared deviation from the mean.

For a population:
σ² = ∑(x - μ)² / N

For a sample:
s² = ∑(x - x̄)² / (n - 1)

Note: The sample variance uses n - 1 in the denominator (instead of n) to provide an unbiased estimate of the population variance.

Properties:
- Uses all data points
- Sensitive to outliers
- Always non-negative
- Units are squared (e.g., meters²)
- Minimized when calculated around the mean

Example: For the dataset {2, 5, 7, 9, 12} with mean 7:
s² = [(2-7)² + (5-7)² + (7-7)² + (9-7)² + (12-7)²] / 4
   = [25 + 4 + 0 + 4 + 25] / 4
   = 58 / 4
   = 14.5

### Standard Deviation

The standard deviation is the square root of the variance.

For a population:
σ = √σ²

For a sample:
s = √s²

Properties:
- Same units as the original data
- Sensitive to outliers
- Always non-negative
- Useful for comparing variability across datasets with different units
- For normal distributions:
  - Approximately 68% of data falls within 1 standard deviation of the mean
  - Approximately 95% of data falls within 2 standard deviations of the mean
  - Approximately 99.7% of data falls within 3 standard deviations of the mean

Example: For the dataset {2, 5, 7, 9, 12} with variance 14.5, the standard deviation is √14.5 ≈ 3.81

### Coefficient of Variation (CV)

The coefficient of variation is the ratio of the standard deviation to the mean, often expressed as a percentage.

CV = (s / x̄) × 100%

Properties:
- Unitless measure
- Useful for comparing variability between datasets with different units or scales
- Only meaningful for ratio data with a positive mean
- Not appropriate for data with a mean near zero

Example: For the dataset {2, 5, 7, 9, 12} with mean 7 and standard deviation 3.81:
CV = (3.81 / 7) × 100% ≈ 54.4%

### Mean Absolute Deviation (MAD)

The MAD is the average of the absolute deviations from the mean.

MAD = ∑|x - x̄| / n

Properties:
- Uses all data points
- Less sensitive to outliers than variance
- Same units as the original data
- Easier to interpret than variance

Example: For the dataset {2, 5, 7, 9, 12} with mean 7:
MAD = [|2-7| + |5-7| + |7-7| + |9-7| + |12-7|] / 5
    = [5 + 2 + 0 + 2 + 5] / 5
    = 14 / 5
    = 2.8

### Choosing the Appropriate Measure of Dispersion

The choice of which measure to use depends on:
- The type and scale of the data
- The presence of outliers
- The specific question being addressed
- The measure of central tendency being used

General guidelines:
- For a comprehensive analysis: Calculate multiple measures
- When outliers are present: Consider IQR or MAD
- For comparing datasets: Consider standard deviation or CV
- When using the mean: Pair with variance or standard deviation
- When using the median: Pair with IQR

## 3.4 Measures of Position

Measures of position describe the relative standing of values within a dataset.

### Percentiles

The pth percentile is a value such that p% of the data falls below it.

Common percentiles:
- 25th percentile (Q₁): First quartile
- 50th percentile (Q₂): Median
- 75th percentile (Q₃): Third quartile

Properties:
- Useful for understanding the distribution of data
- Robust to outliers
- Appropriate for ordinal, interval, and ratio data

Example: In a dataset of test scores, the 90th percentile represents the score below which 90% of the scores fall.

### Quartiles

Quartiles divide the data into four equal parts:
- Q₁ (25th percentile): First quartile
- Q₂ (50th percentile): Median
- Q₃ (75th percentile): Third quartile

Properties:
- Q₁, Q₂, and Q₃ together provide a five-number summary when combined with the minimum and maximum values
- Used to create box plots
- Robust to outliers

### Deciles and Quintiles

- Deciles divide the data into 10 equal parts (10th, 20th, ..., 90th percentiles)
- Quintiles divide the data into 5 equal parts (20th, 40th, 60th, 80th percentiles)

### Z-scores (Standard Scores)

The z-score indicates how many standard deviations a data point is from the mean.

z = (x - x̄) / s

Properties:
- Unitless measure
- Allows comparison of values from different distributions
- For normal distributions:
  - z-scores between -1 and 1 contain approximately 68% of the data
  - z-scores between -2 and 2 contain approximately 95% of the data
  - z-scores between -3 and 3 contain approximately 99.7% of the data

Example: If a student scores 85 on a test with mean 75 and standard deviation 5, their z-score is (85 - 75) / 5 = 2, indicating they scored 2 standard deviations above the mean.

## 3.5 Measures of Shape

Measures of shape describe the form of the distribution.

### Skewness

Skewness measures the asymmetry of the distribution.

- **Positive Skew (Right Skew)**: Tail extends to the right
  - Mean > Median
  - Most values are concentrated on the left
  - Examples: Income distributions, house prices

- **Negative Skew (Left Skew)**: Tail extends to the left
  - Mean < Median
  - Most values are concentrated on the right
  - Examples: Age at death, exam scores in an easy test

- **Zero Skew (Symmetric)**: Balanced on both sides
  - Mean = Median
  - Examples: Normal distribution, uniform distribution

Pearson's coefficient of skewness:
Skewness = 3(Mean - Median) / Standard Deviation

More formal calculation (sample skewness):
Skewness = [n / ((n-1)(n-2))] × ∑[(x - x̄)³ / s³]

Interpretation:
- Skewness > 0: Positively skewed
- Skewness < 0: Negatively skewed
- Skewness = 0: Symmetric
- |Skewness| < 0.5: Approximately symmetric
- 0.5 < |Skewness| < 1: Moderately skewed
- |Skewness| > 1: Highly skewed

### Kurtosis

Kurtosis measures the "tailedness" of the distribution, or how much of the data is in the tails compared to a normal distribution.

- **Leptokurtic (High Kurtosis)**: Heavy tails, more outlier-prone than normal distribution
  - Peaked distribution
  - Examples: Student's t-distribution with few degrees of freedom

- **Mesokurtic (Medium Kurtosis)**: Similar to normal distribution
  - Example: Normal distribution (kurtosis = 3)

- **Platykurtic (Low Kurtosis)**: Light tails, less outlier-prone than normal distribution
  - Flat distribution
  - Examples: Uniform distribution, beta distribution with α = β = 2

Excess kurtosis (sample):
Excess Kurtosis = [n(n+1) / ((n-1)(n-2)(n-3))] × ∑[(x - x̄)⁴ / s⁴] - [3(n-1)² / ((n-2)(n-3))]

Interpretation:
- Excess Kurtosis > 0: Leptokurtic (heavier tails than normal)
- Excess Kurtosis = 0: Mesokurtic (similar to normal)
- Excess Kurtosis < 0: Platykurtic (lighter tails than normal)

Note: Some statistical software reports excess kurtosis (kurtosis - 3), while others report the raw kurtosis.

## 3.6 Data Visualization Techniques

Data visualization is a powerful way to explore and communicate patterns in data.

### Visualizing Categorical Data

#### Bar Charts

Bar charts display the frequency or proportion of each category using rectangular bars.

- **Simple Bar Chart**: Shows frequencies for a single categorical variable
- **Grouped Bar Chart**: Compares frequencies across multiple groups
- **Stacked Bar Chart**: Shows both total frequencies and the breakdown by subgroups

Best practices:
- Order bars logically (e.g., by frequency, alphabetically, or by natural ordering)
- Use consistent colors
- Include clear labels and a title
- Start the y-axis at zero

#### Pie Charts

Pie charts show the proportion of each category as a slice of a circle.

Best practices:
- Limit to a small number of categories (ideally ≤ 7)
- Order slices logically
- Label each slice with category and percentage
- Use when the focus is on part-to-whole relationships
- Consider a bar chart instead if precise comparisons are needed

#### Pareto Charts

Pareto charts combine a bar chart (ordered by frequency) with a cumulative line graph.

Best practices:
- Use to identify the "vital few" categories that account for most of the effect
- Order bars from highest to lowest frequency
- Include both frequency and cumulative percentage scales

#### Contingency Tables

Contingency tables (cross-tabulations) show the relationship between two categorical variables.

Best practices:
- Include row and column totals
- Consider converting to percentages for easier interpretation
- Use color or shading to highlight patterns

### Visualizing Numerical Data

#### Histograms

Histograms display the distribution of a continuous variable by dividing it into bins and showing the frequency of each bin.

Best practices:
- Choose an appropriate number of bins (too few or too many can obscure patterns)
- Use equal bin widths when possible
- Label axes clearly
- Include a title that describes the distribution

#### Stem-and-Leaf Plots

Stem-and-leaf plots show both the distribution shape and the actual data values.

Best practices:
- Use for small to moderate-sized datasets
- Include a key explaining the scale
- Order stems and leaves

#### Box Plots (Box-and-Whisker Plots)

Box plots show the five-number summary (minimum, Q₁, median, Q₃, maximum) and potential outliers.

Best practices:
- Use consistent outlier definition (typically 1.5 × IQR)
- Include a clear scale
- Consider notched box plots to show confidence intervals for the median
- Use side-by-side box plots to compare distributions

#### Scatter Plots

Scatter plots show the relationship between two continuous variables by plotting points.

Best practices:
- Include clear axis labels with units
- Consider adding a trend line or smoothing curve
- Use color or shape to indicate a third variable if relevant
- Include a title that describes the relationship

#### Line Graphs

Line graphs show trends over time or another ordered variable.

Best practices:
- Use for time series or other ordered data
- Include clear axis labels with units
- Consider multiple lines to compare trends across groups
- Avoid connecting points if there are missing values

#### Frequency Polygons

Frequency polygons show the distribution of a continuous variable by connecting the midpoints of histogram bins.

Best practices:
- Use when comparing multiple distributions
- Include clear axis labels
- Use different line styles or colors for each distribution

### Visualizing Bivariate Data

#### Heat Maps

Heat maps use color to represent the values in a two-way table.

Best practices:
- Use a color scale that intuitively represents the data
- Include a color legend
- Consider reordering rows and columns to reveal patterns

#### Bubble Charts

Bubble charts extend scatter plots by using bubble size to represent a third variable.

Best practices:
- Scale bubble area (not radius) proportionally to the data
- Include a legend explaining the bubble sizes
- Avoid overlapping bubbles when possible

#### Mosaic Plots

Mosaic plots show the relationship between two or more categorical variables using rectangular tiles.

Best practices:
- Order categories logically
- Use color to highlight patterns
- Include clear labels

## 3.7 Exploratory Data Analysis (EDA)

Exploratory Data Analysis is an approach to analyzing datasets to summarize their main characteristics, often with visual methods.

### Key Steps in EDA

1. **Data Cleaning and Preprocessing**
   - Handling missing values
   - Identifying and addressing outliers
   - Correcting data entry errors
   - Transforming variables if necessary

2. **Univariate Analysis** (examining one variable at a time)
   - Calculating summary statistics
   - Creating visualizations (histograms, box plots, etc.)
   - Identifying the distribution shape

3. **Bivariate Analysis** (examining relationships between pairs of variables)
   - Creating scatter plots, contingency tables, etc.
   - Calculating correlation coefficients
   - Identifying potential relationships

4. **Multivariate Analysis** (examining relationships between multiple variables)
   - Creating multiple scatter plots, 3D plots, etc.
   - Using dimension reduction techniques
   - Identifying complex patterns

### Common EDA Techniques

#### Summary Statistics

Calculate appropriate summary statistics for each variable:
- For categorical variables: Frequencies, proportions, mode
- For numerical variables: Mean, median, standard deviation, range, percentiles

#### Visualization

Create appropriate visualizations for each variable and relationships between variables.

#### Correlation Analysis

For numerical variables, calculate correlation coefficients:
- Pearson correlation (linear relationships)
- Spearman correlation (monotonic relationships)
- Point-biserial correlation (numerical and binary variables)

#### Outlier Detection

Identify potential outliers using:
- Z-scores (|z| > 3 for potential outliers)
- IQR method (values below Q₁ - 1.5 × IQR or above Q₃ + 1.5 × IQR)
- Visual inspection (box plots, scatter plots)

#### Data Transformation

Consider transformations to address skewness or non-linearity:
- Logarithmic transformation (for positive skew)
- Square root transformation (for moderate positive skew)
- Inverse transformation (for severe positive skew)
- Square transformation (for negative skew)

### The EDA Process

1. **Ask questions about the data**
   - What are the variables and their types?
   - What is the structure of the data?
   - What are the key questions to answer?

2. **Examine the data**
   - Look at the first few rows
   - Check for missing values
   - Verify data types

3. **Clean the data**
   - Handle missing values
   - Address outliers
   - Correct errors

4. **Create summaries**
   - Calculate appropriate statistics
   - Create tables and visualizations

5. **Explore relationships**
   - Look for patterns and correlations
   - Identify potential confounding variables

6. **Refine questions and repeat**
   - Based on initial findings, refine questions
   - Conduct additional analyses as needed

## 3.8 Working with Real Data

### Case Study: Analyzing Economic Indicators

Let's apply descriptive statistics to analyze economic indicators from the World Bank's DataBank.

#### Data Description

The dataset includes various economic indicators for different countries:
- GDP per capita
- Unemployment rate
- Inflation rate
- Trade as percentage of GDP
- Foreign direct investment

#### Analysis Steps

1. **Data Cleaning**
   - Check for missing values
   - Identify outliers
   - Verify data consistency

2. **Summary Statistics**
   - Calculate mean, median, standard deviation, etc. for each indicator
   - Compare statistics across regions or income groups

3. **Visualization**
   - Create histograms to show the distribution of each indicator
   - Use box plots to compare indicators across regions
   - Create scatter plots to explore relationships between indicators

4. **Interpretation**
   - Identify patterns and trends
   - Compare different countries or regions
   - Draw preliminary conclusions

#### Example Findings

- GDP per capita shows a highly skewed distribution, with a few wealthy countries and many lower-income countries
- There is a negative correlation between unemployment and GDP per capita
- Countries with higher trade percentages tend to have higher foreign direct investment

### Best Practices for Data Analysis

1. **Start with clear questions**
   - Define what you want to learn from the data
   - Identify the key variables of interest

2. **Understand the data collection process**
   - How was the data collected?
   - What are the potential sources of bias or error?

3. **Use multiple approaches**
   - Calculate different statistics
   - Create various visualizations
   - Look at the data from different angles

4. **Be cautious about interpretation**
   - Correlation does not imply causation
   - Consider confounding variables
   - Acknowledge limitations of the data

5. **Document your process**
   - Keep track of data cleaning steps
   - Note any assumptions made
   - Make your analysis reproducible

## Interactive Learning Activities

Throughout this module, you'll engage with several interactive tools to reinforce your understanding of descriptive statistics:

1. **Data Visualization Tool**: Create various charts and graphs to visualize different types of data.

2. **Measures of Central Tendency Explorer**: Interactively explore how different measures of central tendency behave with various datasets.

3. **Dispersion and Shape Analyzer**: Calculate and visualize measures of dispersion and shape for different distributions.

4. **Exploratory Data Analysis Simulator**: Practice the EDA process with real-world datasets.

5. **Statistical Summary Generator**: Generate comprehensive statistical summaries for your own data.

## Summary

In this module, we've covered the fundamental concepts of descriptive statistics:

- Types of data and measurement scales
- Measures of central tendency (mean, median, mode, etc.)
- Measures of dispersion (range, variance, standard deviation, etc.)
- Measures of position (percentiles, z-scores)
- Measures of shape (skewness, kurtosis)
- Data visualization techniques for different types of data
- Exploratory Data Analysis (EDA) process and techniques
- Application of descriptive statistics to real-world data

These concepts provide the foundation for understanding and communicating data patterns, which is essential for the inferential statistics we'll explore in subsequent modules.

## Practice Exercises

1. For the dataset {15, 22, 18, 24, 17, 25, 26, 19, 21, 18}, calculate:
   a) Mean, median, and mode
   b) Range, variance, and standard deviation
   c) First and third quartiles, and the interquartile range
   d) Z-scores for each value

2. A company collects data on employee salaries (in thousands of dollars): {45, 48, 52, 55, 56, 57, 58, 60, 62, 65, 70, 72, 75, 80, 120}. Calculate appropriate measures of central tendency and dispersion. Is the mean or median a better representation of the "typical" salary? Explain your reasoning.

3. Create a histogram and box plot for the following exam scores: {65, 70, 72, 75, 78, 80, 82, 85, 85, 88, 90, 92, 95, 98}. Describe the shape of the distribution.

4. A survey asks respondents to rate their satisfaction with a product on a scale of 1 to 5 (1 = very dissatisfied, 5 = very satisfied). The results are: 1 (15 respondents), 2 (25 respondents), 3 (40 respondents), 4 (35 respondents), 5 (20 respondents). Create an appropriate visualization and calculate relevant summary statistics.

5. Using the World Bank data on GDP per capita for different countries, create a box plot comparing the distributions across continents. Identify any outliers and discuss what they represent.

## References and Further Reading

- Moore, D. S., Notz, W. I., & Fligner, M. A. (2018). *The Basic Practice of Statistics* (8th ed.). W. H. Freeman.
- Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
- Few, S. (2009). *Now You See It: Simple Visualization Techniques for Quantitative Analysis*. Analytics Press.
- Wickham, H., & Grolemund, G. (2017). *R for Data Science*. O'Reilly Media.
- Khan Academy: Statistics and Probability. https://www.khanacademy.org/math/statistics-probability
- DataCamp: Introduction to Data Visualization. https://www.datacamp.com/courses/introduction-to-data-visualization
