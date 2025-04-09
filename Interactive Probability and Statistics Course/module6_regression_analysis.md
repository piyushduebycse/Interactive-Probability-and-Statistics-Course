# Module 6: Regression Analysis

## Introduction to Regression Analysis

Regression analysis is a statistical method used to examine the relationship between one dependent variable and one or more independent variables. It helps us understand how the dependent variable changes when any of the independent variables change.

### Key Concepts:

1. **Dependent Variable (Y)**: The outcome variable we're trying to predict or explain.
2. **Independent Variable(s) (X)**: The predictor variable(s) used to predict or explain the dependent variable.
3. **Regression Equation**: A mathematical formula that defines the relationship between variables.
4. **Regression Coefficient**: A value that indicates the magnitude and direction of the relationship between variables.
5. **Residual**: The difference between the observed value and the predicted value.

## Simple Linear Regression

Simple linear regression models the relationship between two variables using a straight line.

### Model:
Y = β₀ + β₁X + ε

Where:
- Y is the dependent variable
- X is the independent variable
- β₀ is the y-intercept (value of Y when X = 0)
- β₁ is the slope (change in Y for a one-unit change in X)
- ε is the error term (residual)

### Assumptions:
1. **Linearity**: The relationship between X and Y is linear.
2. **Independence**: Observations are independent of each other.
3. **Homoscedasticity**: The variance of residuals is constant across all levels of X.
4. **Normality**: The residuals are normally distributed.

### Estimation Method:
Ordinary Least Squares (OLS) minimizes the sum of squared residuals:
- Minimize ∑(Yᵢ - Ŷᵢ)² = ∑(Yᵢ - (β₀ + β₁Xᵢ))²

### Formulas for Estimators:
- β₁ = ∑((Xᵢ - X̄)(Yᵢ - Ȳ)) / ∑(Xᵢ - X̄)² = Cov(X,Y) / Var(X)
- β₀ = Ȳ - β₁X̄

### Measures of Fit:

1. **Coefficient of Determination (R²)**:
   - Proportion of variance in Y explained by X
   - R² = 1 - (SSE / SST) = 1 - ∑(Yᵢ - Ŷᵢ)² / ∑(Yᵢ - Ȳ)²
   - Range: 0 ≤ R² ≤ 1
   - Higher values indicate better fit

2. **Standard Error of the Estimate (SEE)**:
   - SEE = √(SSE / (n - 2))
   - Measures the average distance between observed values and the regression line

### Inference in Simple Linear Regression:

1. **Testing Significance of Slope (β₁)**:
   - H₀: β₁ = 0 (no linear relationship)
   - H₁: β₁ ≠ 0 (linear relationship exists)
   - Test statistic: t = β₁ / SE(β₁) with n-2 degrees of freedom

2. **Confidence Interval for β₁**:
   - β₁ ± t(α/2, n-2) × SE(β₁)

3. **Prediction Interval for Individual Y**:
   - Ŷ ± t(α/2, n-2) × SEP
   - Where SEP = SEE × √(1 + 1/n + (X₀ - X̄)²/∑(Xᵢ - X̄)²)

4. **Confidence Interval for Mean Y at X₀**:
   - Ŷ ± t(α/2, n-2) × SEM
   - Where SEM = SEE × √(1/n + (X₀ - X̄)²/∑(Xᵢ - X̄)²)

## Multiple Linear Regression

Multiple linear regression extends simple linear regression to include two or more independent variables.

### Model:
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε

Where:
- Y is the dependent variable
- X₁, X₂, ..., Xₚ are p independent variables
- β₀, β₁, β₂, ..., βₚ are the regression coefficients
- ε is the error term

### Assumptions:
Same as simple linear regression, plus:
- No multicollinearity (independent variables are not highly correlated with each other)

### Estimation:
- OLS is used to estimate the coefficients
- Matrix notation: β = (X'X)⁻¹X'Y

### Measures of Fit:

1. **Multiple R²**:
   - Proportion of variance in Y explained by all X variables
   - Increases with additional variables, even if they don't improve the model

2. **Adjusted R²**:
   - Adjusts R² for the number of predictors
   - R²ₐ = 1 - [(1 - R²)(n - 1) / (n - p - 1)]
   - Penalizes for adding variables that don't improve the model

3. **F-statistic**:
   - Tests the overall significance of the model
   - H₀: All βᵢ = 0 (i = 1, 2, ..., p)
   - H₁: At least one βᵢ ≠ 0
   - F = (R² / p) / ((1 - R²) / (n - p - 1))

### Interpretation of Coefficients:
- βᵢ represents the change in Y for a one-unit change in Xᵢ, holding all other variables constant

### Variable Selection Methods:

1. **Forward Selection**:
   - Start with no variables and add one at a time based on significance

2. **Backward Elimination**:
   - Start with all variables and remove one at a time based on lack of significance

3. **Stepwise Regression**:
   - Combination of forward and backward approaches
   - Variables can be added or removed at each step

4. **Best Subset Selection**:
   - Evaluate all possible combinations of variables
   - Select the model with the best criterion (e.g., adjusted R², AIC, BIC)

## Polynomial Regression

Polynomial regression models nonlinear relationships by including polynomial terms.

### Model:
Y = β₀ + β₁X + β₂X² + ... + βₚXᵖ + ε

### Implementation:
- Create new variables for the polynomial terms
- Fit using standard multiple regression techniques

## Logistic Regression

Logistic regression models the probability of a binary outcome.

### Model:
log(p/(1-p)) = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ

Where:
- p is the probability of the event occurring
- log(p/(1-p)) is the log-odds (logit)

### Estimation:
- Maximum Likelihood Estimation (MLE) instead of OLS

### Interpretation:
- eᵝⁱ is the odds ratio for a one-unit change in Xᵢ

### Measures of Fit:
- Pseudo R² (e.g., McFadden's R², Cox & Snell R², Nagelkerke R²)
- Classification accuracy, sensitivity, specificity
- ROC curve and AUC

## Correlation Analysis

Correlation measures the strength and direction of the linear relationship between two variables.

### Pearson Correlation Coefficient:
- r = ∑((Xᵢ - X̄)(Yᵢ - Ȳ)) / √(∑(Xᵢ - X̄)² × ∑(Yᵢ - Ȳ)²)
- Range: -1 ≤ r ≤ 1
- r = 1: Perfect positive correlation
- r = -1: Perfect negative correlation
- r = 0: No linear correlation

### Spearman Rank Correlation:
- Nonparametric measure based on ranks
- Useful for ordinal data or when the relationship is monotonic but not linear

### Testing Significance of Correlation:
- H₀: ρ = 0 (no correlation)
- H₁: ρ ≠ 0 (correlation exists)
- Test statistic: t = r × √(n - 2) / √(1 - r²) with n-2 degrees of freedom

## Regression Diagnostics

Diagnostic tools help assess model assumptions and identify influential observations.

### Residual Analysis:
- Residual plots (residuals vs. fitted values, residuals vs. predictors)
- Normal probability plot of residuals
- Standardized residuals

### Influence Measures:
- Leverage (hat values)
- Cook's distance
- DFBETAS, DFFITS

### Multicollinearity Diagnostics:
- Variance Inflation Factor (VIF)
- Condition number
- Correlation matrix of predictors

## Applications of Regression Analysis:

1. **Economics**: Modeling relationships between economic variables (e.g., GDP and unemployment)
2. **Finance**: Predicting stock returns, risk assessment
3. **Marketing**: Analyzing factors affecting sales
4. **Healthcare**: Identifying risk factors for diseases
5. **Social Sciences**: Studying relationships between social variables

## Interactive Examples for Module 6:

1. Regression analyzer with customizable datasets
2. Coefficient interpretation tool
3. Residual analysis visualization
4. Model comparison calculator
5. Prediction interval simulator
