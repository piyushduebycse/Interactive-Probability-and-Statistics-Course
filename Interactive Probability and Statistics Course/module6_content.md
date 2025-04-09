# Module 6: Regression Analysis

## Learning Objectives
By the end of this module, you will be able to:
- Understand the fundamental concepts of regression analysis
- Develop and interpret simple linear regression models
- Extend to multiple linear regression with multiple predictors
- Assess model fit and validate regression assumptions
- Perform model selection and address multicollinearity
- Apply polynomial and logistic regression for non-linear relationships
- Interpret regression results in the context of real-world problems

## 6.1 Introduction to Regression Analysis

### What is Regression Analysis?

Regression analysis is a statistical method used to examine the relationship between one dependent variable and one or more independent variables. It helps us understand how the dependent variable changes when any of the independent variables change, while other independent variables are held fixed.

Regression analysis serves several important purposes:
- Describing the relationship between variables
- Predicting values of the dependent variable
- Identifying which independent variables have the strongest relationship with the dependent variable
- Modeling complex systems and processes

### Types of Regression Models

There are various types of regression models, each suited to different types of data and relationships:

1. **Simple Linear Regression**: One dependent variable and one independent variable, with a linear relationship.

2. **Multiple Linear Regression**: One dependent variable and multiple independent variables, with linear relationships.

3. **Polynomial Regression**: Used when the relationship between variables is curvilinear.

4. **Logistic Regression**: Used when the dependent variable is binary (e.g., yes/no, success/failure).

5. **Other Advanced Models**:
   - Ridge Regression: Addresses multicollinearity through regularization
   - Lasso Regression: Performs variable selection and regularization
   - Quantile Regression: Models the relationship at different quantiles of the dependent variable
   - Nonlinear Regression: Models complex nonlinear relationships

### Applications of Regression Analysis

Regression analysis is widely used across various fields:

1. **Economics and Finance**:
   - Forecasting economic indicators
   - Analyzing factors affecting stock prices
   - Modeling consumer behavior

2. **Healthcare**:
   - Identifying risk factors for diseases
   - Predicting patient outcomes
   - Analyzing the effectiveness of treatments

3. **Marketing**:
   - Determining factors that influence sales
   - Optimizing pricing strategies
   - Analyzing customer behavior

4. **Social Sciences**:
   - Studying relationships between social variables
   - Analyzing educational outcomes
   - Investigating demographic trends

5. **Environmental Science**:
   - Modeling climate patterns
   - Analyzing pollution factors
   - Predicting natural resource usage

## 6.2 Simple Linear Regression

Simple linear regression models the relationship between two variables using a straight line.

### The Simple Linear Regression Model

The model is expressed as:

Y = β₀ + β₁X + ε

Where:
- Y is the dependent variable (response variable)
- X is the independent variable (predictor variable)
- β₀ is the y-intercept (value of Y when X = 0)
- β₁ is the slope (change in Y for a one-unit change in X)
- ε is the error term (residual)

### Assumptions of Simple Linear Regression

For valid inference, simple linear regression relies on several assumptions:

1. **Linearity**: The relationship between X and Y is linear.
2. **Independence**: The observations are independent of each other.
3. **Homoscedasticity**: The variance of residuals is constant across all levels of X.
4. **Normality**: The residuals are normally distributed.

### Estimating the Regression Coefficients

The most common method for estimating the regression coefficients is Ordinary Least Squares (OLS), which minimizes the sum of squared residuals:

Minimize ∑(Yᵢ - Ŷᵢ)² = ∑(Yᵢ - (β₀ + β₁Xᵢ))²

The formulas for the OLS estimators are:

β₁ = ∑((Xᵢ - X̄)(Yᵢ - Ȳ)) / ∑(Xᵢ - X̄)² = Cov(X,Y) / Var(X)

β₀ = Ȳ - β₁X̄

Where:
- X̄ is the mean of X
- Ȳ is the mean of Y
- Cov(X,Y) is the covariance between X and Y
- Var(X) is the variance of X

### Interpreting the Regression Coefficients

- **Intercept (β₀)**: The predicted value of Y when X = 0. This may not always have a meaningful interpretation, especially if X = 0 is outside the range of observed data.

- **Slope (β₁)**: The change in Y for a one-unit increase in X. If β₁ is positive, Y increases as X increases; if β₁ is negative, Y decreases as X increases.

### Example:

A researcher collects data on study time (hours) and exam scores (out of 100) for 20 students:

| Student | Study Time (X) | Exam Score (Y) |
|---------|---------------|----------------|
| 1       | 2             | 65             |
| 2       | 3             | 70             |
| ...     | ...           | ...            |
| 20      | 8             | 95             |

Using OLS, the estimated regression equation is:
Ŷ = 50 + 5X

Interpretation:
- The intercept (50) suggests that a student who doesn't study at all (X = 0) would be expected to score 50 on the exam.
- The slope (5) indicates that each additional hour of studying is associated with a 5-point increase in the exam score, on average.

### Measures of Fit

Several statistics help assess how well the regression model fits the data:

1. **Coefficient of Determination (R²)**:
   - Proportion of variance in Y explained by X
   - R² = 1 - (SSE / SST) = 1 - ∑(Yᵢ - Ŷᵢ)² / ∑(Yᵢ - Ȳ)²
   - Range: 0 ≤ R² ≤ 1
   - Higher values indicate better fit

2. **Standard Error of the Estimate (SEE)**:
   - SEE = √(SSE / (n - 2))
   - Measures the average distance between observed values and the regression line
   - Same units as Y

3. **Residual Analysis**:
   - Residuals = Observed values - Predicted values = Yᵢ - Ŷᵢ
   - Plotting residuals helps assess model assumptions

### Inference in Simple Linear Regression

1. **Testing Significance of Slope (β₁)**:
   - H₀: β₁ = 0 (no linear relationship)
   - H₁: β₁ ≠ 0 (linear relationship exists)
   - Test statistic: t = β₁ / SE(β₁) with n-2 degrees of freedom
   - If p-value < α, reject H₀ and conclude there is a significant linear relationship

2. **Confidence Interval for β₁**:
   - β₁ ± t(α/2, n-2) × SE(β₁)
   - Provides a range of plausible values for the true slope

3. **Prediction**:
   - Point prediction for Y at X = X₀: Ŷ = β₀ + β₁X₀
   - Prediction interval for individual Y: Ŷ ± t(α/2, n-2) × SEP
     - Where SEP = SEE × √(1 + 1/n + (X₀ - X̄)²/∑(Xᵢ - X̄)²)
   - Confidence interval for mean Y at X₀: Ŷ ± t(α/2, n-2) × SEM
     - Where SEM = SEE × √(1/n + (X₀ - X̄)²/∑(Xᵢ - X̄)²)

## 6.3 Multiple Linear Regression

Multiple linear regression extends simple linear regression to include two or more independent variables.

### The Multiple Linear Regression Model

The model is expressed as:

Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε

Where:
- Y is the dependent variable
- X₁, X₂, ..., Xₚ are p independent variables
- β₀, β₁, β₂, ..., βₚ are the regression coefficients
- ε is the error term

### Assumptions of Multiple Linear Regression

The assumptions are similar to those for simple linear regression:
1. **Linearity**: The relationship between each independent variable and the dependent variable is linear.
2. **Independence**: The observations are independent of each other.
3. **Homoscedasticity**: The variance of residuals is constant across all levels of the independent variables.
4. **Normality**: The residuals are normally distributed.
5. **No multicollinearity**: The independent variables are not highly correlated with each other.

### Estimating the Regression Coefficients

OLS is used to estimate the coefficients by minimizing the sum of squared residuals. In matrix notation:

β = (X'X)⁻¹X'Y

Where:
- β is the vector of regression coefficients
- X is the design matrix of independent variables
- Y is the vector of dependent variable values

### Interpreting the Regression Coefficients

In multiple regression, each coefficient represents the change in Y for a one-unit increase in the corresponding X, holding all other independent variables constant.

For example, if:
Ŷ = 10 + 5X₁ + 3X₂ - 2X₃

Interpretation:
- β₀ = 10: The predicted value of Y when all X's are zero
- β₁ = 5: A one-unit increase in X₁ is associated with a 5-unit increase in Y, holding X₂ and X₃ constant
- β₂ = 3: A one-unit increase in X₂ is associated with a 3-unit increase in Y, holding X₁ and X₃ constant
- β₃ = -2: A one-unit increase in X₃ is associated with a 2-unit decrease in Y, holding X₁ and X₂ constant

### Measures of Fit

1. **Multiple R²**:
   - Proportion of variance in Y explained by all X variables
   - Range: 0 ≤ R² ≤ 1
   - Increases with additional variables, even if they don't improve the model

2. **Adjusted R²**:
   - Adjusts R² for the number of predictors
   - R²ₐ = 1 - [(1 - R²)(n - 1) / (n - p - 1)]
   - Penalizes for adding variables that don't improve the model
   - Useful for comparing models with different numbers of predictors

3. **Standard Error of the Estimate**:
   - SEE = √(SSE / (n - p - 1))
   - Measures the average distance between observed values and the regression surface

### Inference in Multiple Regression

1. **Overall F-test**:
   - Tests the overall significance of the model
   - H₀: All βᵢ = 0 (i = 1, 2, ..., p)
   - H₁: At least one βᵢ ≠ 0
   - F = (R² / p) / ((1 - R²) / (n - p - 1))
   - If p-value < α, reject H₀ and conclude that the model is significant

2. **t-tests for Individual Coefficients**:
   - H₀: βᵢ = 0
   - H₁: βᵢ ≠ 0
   - t = βᵢ / SE(βᵢ) with n-p-1 degrees of freedom
   - If p-value < α, reject H₀ and conclude that the variable is significant

3. **Confidence Intervals for Coefficients**:
   - βᵢ ± t(α/2, n-p-1) × SE(βᵢ)

4. **Prediction**:
   - Similar to simple linear regression, but accounting for multiple predictors

### Example:

A researcher wants to predict house prices based on square footage (X₁), number of bedrooms (X₂), and age of the house (X₃). The estimated regression equation is:

Ŷ = 50,000 + 100X₁ + 15,000X₂ - 1,000X₃

Interpretation:
- For each additional square foot, the predicted house price increases by $100, holding other variables constant.
- For each additional bedroom, the predicted house price increases by $15,000, holding other variables constant.
- For each additional year of age, the predicted house price decreases by $1,000, holding other variables constant.

## 6.4 Model Diagnostics and Validation

Model diagnostics help assess whether the assumptions of regression are met and identify potential problems.

### Residual Analysis

Residuals (e = Y - Ŷ) provide valuable information about model fit:

1. **Residual Plot** (residuals vs. fitted values):
   - Should show random scatter around zero
   - Patterns may indicate non-linearity or heteroscedasticity

2. **Normal Probability Plot of Residuals**:
   - Points should approximately follow a straight line
   - Deviations suggest non-normality

3. **Standardized Residuals**:
   - Residuals divided by their standard deviation
   - Values beyond ±3 may indicate outliers

### Detecting Influential Observations

1. **Leverage** (hat values):
   - Measures the potential influence of an observation on the fitted values
   - High leverage points have unusual X values

2. **Cook's Distance**:
   - Measures the overall influence of an observation
   - Combines leverage and residual information
   - Values > 1 are often considered influential

3. **DFBETAS**:
   - Measures the influence of an observation on each regression coefficient
   - Large values indicate influential points for specific coefficients

### Checking Assumptions

1. **Linearity**:
   - Residual plots should show no systematic patterns
   - Partial regression plots can help assess linearity for individual predictors

2. **Independence**:
   - Durbin-Watson test for autocorrelation
   - Plot residuals against time or order of collection

3. **Homoscedasticity**:
   - Breusch-Pagan test or White test
   - Residual plot should show constant variance

4. **Normality**:
   - Shapiro-Wilk test or Kolmogorov-Smirnov test
   - Q-Q plot of residuals

5. **Multicollinearity**:
   - Variance Inflation Factor (VIF) = 1/(1-R²ⱼ)
     - Where R²ⱼ is the R² from regressing the jth predictor on all other predictors
   - VIF > 10 suggests problematic multicollinearity
   - Correlation matrix of predictors

### Addressing Violations of Assumptions

1. **Non-linearity**:
   - Transform variables (e.g., log, square root)
   - Add polynomial terms
   - Use non-linear regression models

2. **Heteroscedasticity**:
   - Transform the dependent variable
   - Use weighted least squares
   - Use robust standard errors

3. **Non-normality**:
   - Transform the dependent variable
   - Use non-parametric regression
   - For large samples, rely on the Central Limit Theorem

4. **Multicollinearity**:
   - Remove one of the correlated predictors
   - Use principal component analysis
   - Apply ridge regression

5. **Outliers and Influential Points**:
   - Investigate for data errors
   - Consider robust regression methods
   - Analyze with and without the influential points

### Cross-Validation

Cross-validation helps assess how well the model will generalize to new data:

1. **Holdout Method**:
   - Split data into training and testing sets
   - Fit model on training data
   - Evaluate performance on testing data

2. **k-fold Cross-Validation**:
   - Divide data into k subsets
   - For each subset, train on the other k-1 subsets and test on the current subset
   - Average the performance metrics

3. **Leave-One-Out Cross-Validation**:
   - Special case of k-fold where k = n
   - Each observation serves as a test set once

## 6.5 Variable Selection and Model Building

In multiple regression, selecting the right variables is crucial for building an effective model.

### Criteria for Variable Selection

1. **Statistical Significance**:
   - Include variables with significant t-tests (p < α)
   - Consider the overall F-test

2. **Contribution to R²**:
   - Variables should meaningfully increase R² or adjusted R²

3. **Theoretical Relevance**:
   - Variables should have a logical connection to the dependent variable
   - Prior research may guide selection

4. **Parsimony**:
   - Simpler models are generally preferred
   - Avoid overfitting

5. **Prediction Accuracy**:
   - Models should perform well on new data
   - Cross-validation can help assess this

### Variable Selection Methods

1. **Forward Selection**:
   - Start with no variables
   - Add one variable at a time, selecting the one that improves the model the most
   - Continue until no remaining variable significantly improves the model

2. **Backward Elimination**:
   - Start with all variables
   - Remove one variable at a time, selecting the one whose removal least degrades the model
   - Continue until removing any variable would significantly worsen the model

3. **Stepwise Regression**:
   - Combination of forward and backward approaches
   - Variables can be added or removed at each step
   - Continues until no variable can be added or removed based on specified criteria

4. **Best Subset Selection**:
   - Evaluate all possible combinations of variables
   - Select the model with the best criterion (e.g., adjusted R², AIC, BIC)
   - Computationally intensive for many variables

### Information Criteria

Information criteria balance model fit and complexity:

1. **Akaike Information Criterion (AIC)**:
   - AIC = 2k - 2ln(L)
   - Where k is the number of parameters and L is the likelihood
   - Lower values indicate better models

2. **Bayesian Information Criterion (BIC)**:
   - BIC = k·ln(n) - 2ln(L)
   - Penalizes complexity more heavily than AIC
   - Lower values indicate better models

3. **Mallows' Cp**:
   - Cp = (SSEp / MSE) - (n - 2
(Content truncated due to size limit. Use line ranges to read in chunks)