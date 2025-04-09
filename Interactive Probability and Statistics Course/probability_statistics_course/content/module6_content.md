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
   - Cp = (SSEp / MSE) - (n - 2p)
   - Where SSEp is the sum of squared errors for a model with p parameters
   - Models with Cp ≈ p are preferred

### Handling Categorical Predictors

Categorical variables must be properly encoded for regression:

1. **Dummy Variables**:
   - For a categorical variable with k levels, create k-1 dummy variables
   - Each dummy variable represents one level (1 if present, 0 if not)
   - The omitted level becomes the reference category

2. **Effect Coding**:
   - Similar to dummy coding, but uses 1, 0, and -1
   - The reference category is coded as -1 on all variables

3. **Interaction Terms**:
   - Interaction between categorical and continuous: Create separate slopes for each category
   - Interaction between two categorical: Create dummy variables for each combination

### Example:

A researcher wants to predict salary based on years of experience, education level (high school, bachelor's, master's, doctorate), and gender. Education level is categorical with 4 levels, so 3 dummy variables are created:

Ŷ = β₀ + β₁(Years) + β₂(Bachelor's) + β₃(Master's) + β₄(Doctorate) + β₅(Gender)

Where:
- Bachelor's = 1 if education is bachelor's, 0 otherwise
- Master's = 1 if education is master's, 0 otherwise
- Doctorate = 1 if education is doctorate, 0 otherwise
- High school is the reference category
- Gender = 1 if male, 0 if female

## 6.6 Polynomial Regression

Polynomial regression extends linear regression to model curvilinear relationships by including polynomial terms.

### The Polynomial Regression Model

For a single predictor, a polynomial regression of degree p has the form:

Y = β₀ + β₁X + β₂X² + ... + βₚXᵖ + ε

This is still a linear model in terms of the parameters (β's), but nonlinear in terms of the predictor variable X.

### Implementation

To fit a polynomial regression:
1. Create new variables for the polynomial terms (X², X³, etc.)
2. Fit a multiple linear regression model using these terms
3. Assess the fit and significance of the polynomial terms

### Example:

A researcher studying the relationship between fertilizer amount (X) and crop yield (Y) finds that the relationship is not linear. A quadratic model might be appropriate:

Y = β₀ + β₁X + β₂X² + ε

If the estimated equation is:
Ŷ = 10 + 5X - 0.5X²

Interpretation:
- The positive linear term (5X) indicates that yield initially increases with fertilizer
- The negative quadratic term (-0.5X²) indicates that the rate of increase diminishes and eventually turns negative
- The maximum yield occurs at X = 5 (found by taking the derivative and setting it to zero)

### Choosing the Degree of the Polynomial

1. **Statistical Significance**:
   - Test whether adding higher-order terms significantly improves the model
   - Compare nested models using F-tests or information criteria

2. **Visual Inspection**:
   - Plot the data and fitted curves
   - Look for systematic patterns in residuals

3. **Domain Knowledge**:
   - Some relationships have known functional forms
   - Higher-order polynomials may fit the data better but can lead to overfitting

### Limitations of Polynomial Regression

1. **Extrapolation**:
   - Polynomial models can behave erratically outside the range of observed data
   - High-degree polynomials are particularly problematic

2. **Multicollinearity**:
   - Polynomial terms are often highly correlated
   - Consider centering the predictor (X - X̄) before creating polynomial terms

3. **Interpretability**:
   - Higher-order terms can be difficult to interpret
   - Consider alternative nonlinear models if appropriate

## 6.7 Logistic Regression

Logistic regression is used when the dependent variable is binary (e.g., success/failure, yes/no).

### The Logistic Regression Model

The model predicts the probability of the dependent variable being 1 (success):

log(p/(1-p)) = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ

Where:
- p is the probability of success
- log(p/(1-p)) is the log-odds or logit
- β's are the regression coefficients

Solving for p:
p = 1 / (1 + e^(-(β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ)))

### Estimation

Unlike linear regression, logistic regression uses Maximum Likelihood Estimation (MLE) instead of OLS:
1. Start with initial values for the β's
2. Calculate the likelihood of observing the data given these values
3. Adjust the β's to maximize the likelihood
4. Repeat until convergence

### Interpreting Logistic Regression Coefficients

1. **Log-Odds Interpretation**:
   - βᵢ represents the change in log-odds for a one-unit increase in Xᵢ, holding other variables constant

2. **Odds Ratio Interpretation**:
   - e^βᵢ is the odds ratio for a one-unit increase in Xᵢ
   - If e^βᵢ > 1, the odds increase
   - If e^βᵢ < 1, the odds decrease

3. **Probability Interpretation**:
   - The effect on probability depends on the current probability
   - The relationship is S-shaped (sigmoid)

### Example:

A researcher wants to predict whether a student will pass an exam (1 = pass, 0 = fail) based on study time (hours) and attendance (percentage). The estimated logistic regression equation is:

log(p/(1-p)) = -5 + 0.8(Study Time) + 0.05(Attendance)

Interpretation:
- For each additional hour of study time, the log-odds of passing increase by 0.8, or the odds multiply by e^0.8 ≈ 2.23
- For each additional percentage point of attendance, the log-odds of passing increase by 0.05, or the odds multiply by e^0.05 ≈ 1.05

### Assessing Model Fit

1. **Likelihood Ratio Test**:
   - Compares the fitted model to a null model
   - χ² = -2ln(L₀/L₁) = -2(ln(L₀) - ln(L₁))
   - Where L₀ is the likelihood of the null model and L₁ is the likelihood of the fitted model

2. **Pseudo R²**:
   - McFadden's R² = 1 - ln(L₁)/ln(L₀)
   - Cox & Snell R² = 1 - (L₀/L₁)^(2/n)
   - Nagelkerke R² (adjusted Cox & Snell to range from 0 to 1)

3. **Classification Metrics**:
   - Accuracy: Proportion of correct predictions
   - Sensitivity: Proportion of actual positives correctly identified
   - Specificity: Proportion of actual negatives correctly identified
   - ROC curve and AUC: Plot of sensitivity vs. (1 - specificity) at various thresholds

### Assumptions of Logistic Regression

1. **Binary Dependent Variable**:
   - The dependent variable must be binary
   - For multinomial outcomes, use multinomial logistic regression

2. **Independence**:
   - Observations should be independent

3. **No Multicollinearity**:
   - Independent variables should not be highly correlated

4. **Linearity in the Logit**:
   - The log-odds should be linearly related to the independent variables
   - Can be checked by including interaction terms with the log of the variable

5. **Sample Size**:
   - Requires a larger sample size than linear regression
   - Rule of thumb: At least 10 events per predictor variable

## 6.8 Correlation Analysis

Correlation measures the strength and direction of the linear relationship between two variables.

### Pearson Correlation Coefficient

The Pearson correlation coefficient (r) is calculated as:

r = ∑((Xᵢ - X̄)(Yᵢ - Ȳ)) / √(∑(Xᵢ - X̄)² × ∑(Yᵢ - Ȳ)²) = Cov(X,Y) / (σₓ × σᵧ)

Properties:
- Range: -1 ≤ r ≤ 1
- r = 1: Perfect positive correlation
- r = -1: Perfect negative correlation
- r = 0: No linear correlation

Interpretation:
- |r| < 0.3: Weak correlation
- 0.3 ≤ |r| < 0.7: Moderate correlation
- |r| ≥ 0.7: Strong correlation

### Testing Significance of Correlation

To test whether a correlation is significantly different from zero:
- H₀: ρ = 0 (no correlation)
- H₁: ρ ≠ 0 (correlation exists)
- Test statistic: t = r × √(n - 2) / √(1 - r²) with n-2 degrees of freedom
- If p-value < α, reject H₀ and conclude that the correlation is significant

### Spearman Rank Correlation

The Spearman correlation (rₛ) is a non-parametric measure based on the ranks of the data:
- Convert X and Y to ranks
- Calculate the Pearson correlation of the ranks

Properties:
- Robust to outliers
- Detects monotonic relationships, not just linear ones
- Does not require normality

### Correlation Matrix

For multiple variables, a correlation matrix shows all pairwise correlations:
- Diagonal elements are always 1 (correlation of a variable with itself)
- Off-diagonal elements show correlations between pairs of variables
- The matrix is symmetric

### Limitations of Correlation

1. **Correlation ≠ Causation**:
   - Correlation does not imply a causal relationship
   - Third variables may explain the observed correlation

2. **Linearity Assumption**:
   - Pearson correlation only measures linear relationships
   - Variables may have a strong nonlinear relationship but low Pearson correlation

3. **Sensitivity to Outliers**:
   - Pearson correlation can be heavily influenced by outliers
   - Consider robust correlation measures

4. **Restricted Range**:
   - Correlation can be attenuated if the range of either variable is restricted

## 6.9 Time Series Regression

Time series regression deals with data collected over time, where observations may not be independent.

### Autocorrelation

Autocorrelation is the correlation of a variable with itself at different time lags:
- Positive autocorrelation: Values tend to be followed by similar values
- Negative autocorrelation: Values tend to be followed by dissimilar values

Detection:
- Durbin-Watson test
- Autocorrelation Function (ACF) plot
- Partial Autocorrelation Function (PACF) plot

### Time Series Regression Models

1. **Autoregressive (AR) Models**:
   - Current value depends on previous values
   - AR(p): Yₜ = c + φ₁Yₜ₋₁ + φ₂Yₜ₋₂ + ... + φₚYₜ₋ₚ + εₜ

2. **Moving Average (MA) Models**:
   - Current value depends on current and previous error terms
   - MA(q): Yₜ = c + εₜ + θ₁εₜ₋₁ + θ₂εₜ₋₂ + ... + θₚεₜ₋ₚ

3. **Autoregressive Moving Average (ARMA) Models**:
   - Combination of AR and MA models
   - ARMA(p,q): Yₜ = c + φ₁Yₜ₋₁ + ... + φₚYₜ₋ₚ + εₜ + θ₁εₜ₋₁ + ... + θₚεₜ₋ₚ

4. **Autoregressive Integrated Moving Average (ARIMA) Models**:
   - For non-stationary time series
   - Includes differencing to achieve stationarity
   - ARIMA(p,d,q): p = AR order, d = differencing order, q = MA order

### Handling Time Series Data in Regression

1. **Trend Variables**:
   - Include time as a predictor
   - Use polynomial terms for nonlinear trends

2. **Seasonal Dummy Variables**:
   - Create dummy variables for seasons, months, days of week, etc.

3. **Lagged Variables**:
   - Include lagged values of the dependent variable
   - Include lagged values of independent variables

4. **Differencing**:
   - First difference: ΔYₜ = Yₜ - Yₜ₋₁
   - Removes linear trends
   - Higher-order differencing for more complex trends

5. **Handling Autocorrelation**:
   - Generalized Least Squares (GLS)
   - Newey-West standard errors
   - ARIMA modeling

## 6.10 Advanced Regression Topics

### Ridge Regression

Ridge regression addresses multicollinearity by adding a penalty term to the OLS objective function:

Minimize: ∑(Yᵢ - (β₀ + β₁X₁ᵢ + ... + βₚXₚᵢ))² + λ∑β²ⱼ

Where λ is the regularization parameter that controls the strength of the penalty.

Properties:
- Shrinks coefficients toward zero
- Does not set any coefficients exactly to zero
- Reduces variance at the expense of some bias
- Particularly useful when predictors are highly correlated

### Lasso Regression

Lasso (Least Absolute Shrinkage and Selection Operator) uses a different penalty term:

Minimize: ∑(Yᵢ - (β₀ + β₁X₁ᵢ + ... + βₚXₚᵢ))² + λ∑|βⱼ|

Properties:
- Can set some coefficients exactly to zero
- Performs variable selection
- Useful for high-dimensional data

### Elastic Net

Elastic Net combines the penalties of Ridge and Lasso:

Minimize: ∑(Yᵢ - (β₀ + β₁X₁ᵢ + ... + βₚXₚᵢ))² + λ₁∑β²ⱼ + λ₂∑|βⱼ|

Properties:
- Combines the benefits of Ridge and Lasso
- Can handle groups of correlated variables better than Lasso

### Quantile Regression

Quantile regression models the relationship at different quantiles of the dependent variable:
- Median regression (50th percentile) minimizes the sum of absolute deviations
- Can model the entire conditional distribution, not just the mean
- Robust to outliers
- Useful when the effect of predictors varies across the distribution

### Nonlinear Regression

Nonlinear regression models relationships that cannot be expressed as a linear combination of parameters:
- Y = f(X, β) + ε
- Examples: Exponential growth, logistic growth, asymptotic models
- Requires iterative estimation methods
- Starting values are often critical

## Interactive Learning Activities

Throughout this module, you'll engage with several interactive tools to reinforce your understanding of regression analysis:

1. **Regression Analyzer**: Build and analyze regression models with real-world datasets.

2. **Correlation Explorer**: Visualize and interpret correlations between variables.

3. **Model Diagnostics Tool**: Assess regression assumptions and identify potential problems.

4. **Variable Selection Simulator**: Practice different methods of variable selection.

5. **Prediction Calculator**: Make predictions with confidence and prediction intervals.

## Summary

In this module, we've covered the fundamental concepts of regression analysis:

- Simple linear regression for modeling relationships between two variables
- Multiple linear regression for incorporating multiple predictors
- Model diagnostics and validation techniques
- Variable selection and model building strategies
- Polynomial regression for curvilinear relationships
- Logistic regression for binary outcomes
- Correlation analysis for measuring relationships
- Time series regression for temporal data
- Advanced regression techniques for special situations

These concepts provide powerful tools for analyzing relationships between variables, making predictions, and understanding complex systems.

## Practice Exercises

1. A real estate agent collects data on house prices (in thousands of dollars) and house size (in square feet) for 30 houses. The regression equation is Ŷ = 50 + 0.1X, with R² = 0.75.
   a) Interpret the slope and intercept.
   b) Predict the price of a 2,000 square foot house.
   c) Interpret the R² value.

2. A researcher wants to predict student performance on a final exam based on hours studied, attendance percentage, and previous GPA. The regression equation is Ŷ = 40 + 3(Hours) + 0.2(Attendance) + 10(GPA), with R² = 0.65.
   a) Interpret each coefficient.
   b) Which predictor has the strongest effect? (Hint: Consider standardized coefficients)
   c) Predict the final exam score for a student who studied 10 hours, had 80% attendance, and has a GPA of 3.5.

3. A marketing manager collects data on sales (Y), advertising expenditure (X₁), price (X₂), and competitor's price (X₃). The correlation matrix is:

   |       | Sales | Advertising | Price | Competitor's Price |
   |-------|-------|-------------|-------|-------------------|
   | Sales | 1.00  | 0.75        | -0.60 | 0.40              |
   | Advertising | 0.75 | 1.00   | -0.30 | 0.20              |
   | Price | -0.60 | -0.30       | 1.00  | 0.50              |
   | Competitor's Price | 0.40 | 0.20 | 0.50 | 1.00          |

   a) Interpret the correlations between sales and each predictor.
   b) Is there evidence of multicollinearity? Explain.
   c) Which predictors would you expect to be significant in a multiple regression model?

4. A health researcher wants to predict whether a patient will develop a certain disease (1 = yes, 0 = no) based on age, BMI, and smoking status (1 = smoker, 0 = non-smoker). The logistic regression equation is:
   log(p/(1-p)) = -5 + 0.05(Age) + 0.1(BMI) + 1.2(Smoking)
   
   a) Interpret each coefficient in terms of odds ratios.
   b) Calculate the probability of disease for a 50-year-old smoker with a BMI of 30.
   c) How does the probability change if the person is a non-smoker?

5. A researcher suspects that the relationship between study time and exam score is not linear. The data for 20 students shows:

   | Study Time (hours) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
   |-------------------|---|---|---|---|---|---|---|---|---|----|
   | Exam Score        |60 |68 |74 |78 |82 |84 |85 |85 |84 |82  |

   a) Fit a quadratic regression model to this data.
   b) Interpret the coefficients.
   c) At what study time is the exam score maximized?
   d) Why might a quadratic model be more appropriate than a linear model in this case?

## References and Further Reading

- Kutner, M. H., Nachtsheim, C. J., Neter, J., & Li, W. (2004). *Applied Linear Statistical Models* (5th ed.). McGraw-Hill/Irwin.
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning with Applications in R*. Springer.
- Fox, J. (2015). *Applied Regression Analysis and Generalized Linear Models* (3rd ed.). SAGE Publications.
- Hosmer, D. W., Lemeshow, S., & Sturdivant, R. X. (2013). *Applied Logistic Regression* (3rd ed.). Wiley.
- Hyndman, R. J., & Athanasopoulos, G. (2018). *Forecasting: Principles and Practice* (2nd ed.). OTexts.
- UCLA Statistical Consulting: Regression Analysis. https://stats.oarc.ucla.edu/other/mult-pkg/introduction-to-regression/
- Penn State STAT 501: Regression Methods. https://online.stat.psu.edu/stat501/
