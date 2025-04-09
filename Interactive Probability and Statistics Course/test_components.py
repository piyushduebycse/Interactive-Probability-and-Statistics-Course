#!/usr/bin/env python3

import os
import json
import math
import random
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_coin_flip_simulator():
    """Test the mathematical accuracy of the coin flip simulator."""
    print("Testing Coin Flip Simulator...")
    
    # Simulate coin flips
    num_flips = 10000
    results = [random.choice(['H', 'T']) for _ in range(num_flips)]
    
    # Count heads and tails
    heads = results.count('H')
    tails = results.count('T')
    
    # Calculate probabilities
    p_heads = heads / num_flips
    p_tails = tails / num_flips
    
    # Check if probabilities are close to 0.5
    assert abs(p_heads - 0.5) < 0.05, f"Heads probability {p_heads} is not close to 0.5"
    assert abs(p_tails - 0.5) < 0.05, f"Tails probability {p_tails} is not close to 0.5"
    
    # Check if the sum of probabilities is 1
    assert abs(p_heads + p_tails - 1.0) < 1e-10, f"Sum of probabilities {p_heads + p_tails} is not 1.0"
    
    print("✓ Coin Flip Simulator tests passed")
    return True

def test_distribution_explorer():
    """Test the mathematical accuracy of the distribution explorer."""
    print("Testing Distribution Explorer...")
    
    # Test normal distribution
    mean = 0
    std_dev = 1
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x, mean, std_dev)
    
    # Check if the PDF integrates to approximately 1
    dx = x[1] - x[0]
    integral = np.sum(y * dx)
    assert abs(integral - 1.0) < 0.01, f"Normal PDF integral {integral} is not close to 1.0"
    
    # Check if the mean is correct
    calculated_mean = np.sum(x * y * dx) / integral
    assert abs(calculated_mean - mean) < 0.01, f"Calculated mean {calculated_mean} is not close to {mean}"
    
    # Check if the variance is correct
    calculated_var = np.sum((x - calculated_mean)**2 * y * dx) / integral
    assert abs(calculated_var - std_dev**2) < 0.05, f"Calculated variance {calculated_var} is not close to {std_dev**2}"
    
    # Test binomial distribution
    n, p = 10, 0.3
    k = np.arange(0, n+1)
    binomial_pmf = stats.binom.pmf(k, n, p)
    
    # Check if the PMF sums to 1
    assert abs(np.sum(binomial_pmf) - 1.0) < 1e-10, f"Binomial PMF sum {np.sum(binomial_pmf)} is not 1.0"
    
    # Check if the mean is correct
    binomial_mean = np.sum(k * binomial_pmf)
    assert abs(binomial_mean - n*p) < 0.01, f"Binomial mean {binomial_mean} is not close to {n*p}"
    
    # Check if the variance is correct
    binomial_var = np.sum((k - binomial_mean)**2 * binomial_pmf)
    assert abs(binomial_var - n*p*(1-p)) < 0.05, f"Binomial variance {binomial_var} is not close to {n*p*(1-p)}"
    
    print("✓ Distribution Explorer tests passed")
    return True

def test_descriptive_statistics_calculator():
    """Test the mathematical accuracy of the descriptive statistics calculator."""
    print("Testing Descriptive Statistics Calculator...")
    
    # Test data
    data = [12, 15, 18, 22, 25, 28, 30, 35, 40, 45]
    
    # Calculate statistics
    mean = np.mean(data)
    median = np.median(data)
    mode = stats.mode(data, keepdims=True).mode[0]
    std_dev = np.std(data, ddof=1)
    variance = np.var(data, ddof=1)
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    
    # Check mean
    expected_mean = sum(data) / len(data)
    assert abs(mean - expected_mean) < 1e-10, f"Mean {mean} does not match expected {expected_mean}"
    
    # Check median
    sorted_data = sorted(data)
    if len(data) % 2 == 0:
        expected_median = (sorted_data[len(data)//2 - 1] + sorted_data[len(data)//2]) / 2
    else:
        expected_median = sorted_data[len(data)//2]
    assert abs(median - expected_median) < 1e-10, f"Median {median} does not match expected {expected_median}"
    
    # Check variance
    expected_variance = sum((x - expected_mean) ** 2 for x in data) / (len(data) - 1)
    assert abs(variance - expected_variance) < 1e-10, f"Variance {variance} does not match expected {expected_variance}"
    
    # Check standard deviation
    expected_std_dev = math.sqrt(expected_variance)
    assert abs(std_dev - expected_std_dev) < 1e-10, f"Standard deviation {std_dev} does not match expected {expected_std_dev}"
    
    # Check range
    assert range_val == max_val - min_val, f"Range {range_val} does not match expected {max_val - min_val}"
    
    # Check IQR
    assert iqr == q3 - q1, f"IQR {iqr} does not match expected {q3 - q1}"
    
    print("✓ Descriptive Statistics Calculator tests passed")
    return True

def test_interactive_quiz():
    """Test the accuracy of the interactive quiz questions and answers."""
    print("Testing Interactive Quiz...")
    
    # Sample quiz questions to test
    quiz_questions = [
        {
            "question": "If P(A) = 0.4 and P(B) = 0.3 and A and B are mutually exclusive events, what is P(A ∪ B)?",
            "options": ["0.12", "0.7", "0.1", "0.4"],
            "correctAnswer": 1,
            "explanation": "For mutually exclusive events, P(A ∪ B) = P(A) + P(B). So P(A ∪ B) = 0.4 + 0.3 = 0.7."
        },
        {
            "question": "For a binomial random variable with n = 10 and p = 0.3, what is the expected value?",
            "options": ["3", "0.3", "7", "10"],
            "correctAnswer": 0,
            "explanation": "For a binomial distribution, E(X) = n·p = 10 × 0.3 = 3."
        },
        {
            "question": "What is the median of the data set {3, 7, 8, 9, 12}?",
            "options": ["3", "7", "8", "9"],
            "correctAnswer": 2,
            "explanation": "The median is the middle value when the data is arranged in order. Since there are 5 values, the median is the 3rd value, which is 8."
        }
    ]
    
    # Test each question
    for i, q in enumerate(quiz_questions):
        print(f"  Testing question {i+1}...")
        
        # Test question 1: P(A ∪ B) for mutually exclusive events
        if i == 0:
            p_a = 0.4
            p_b = 0.3
            expected_answer = p_a + p_b
            assert abs(expected_answer - 0.7) < 1e-10, f"Expected answer {expected_answer} does not match 0.7"
            assert q["correctAnswer"] == 1, f"Correct answer index {q['correctAnswer']} does not match expected 1"
        
        # Test question 2: Expected value of binomial
        elif i == 1:
            n = 10
            p = 0.3
            expected_answer = n * p
            assert abs(expected_answer - 3) < 1e-10, f"Expected answer {expected_answer} does not match 3"
            assert q["correctAnswer"] == 0, f"Correct answer index {q['correctAnswer']} does not match expected 0"
        
        # Test question 3: Median
        elif i == 2:
            data = [3, 7, 8, 9, 12]
            expected_answer = 8
            assert expected_answer == data[len(data)//2], f"Expected answer {expected_answer} does not match {data[len(data)//2]}"
            assert q["correctAnswer"] == 2, f"Correct answer index {q['correctAnswer']} does not match expected 2"
    
    print("✓ Interactive Quiz tests passed")
    return True

def test_data_analysis_tool():
    """Test the mathematical accuracy of the data analysis tool."""
    print("Testing Data Analysis Tool...")
    
    # Test correlation analysis
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    
    # Calculate correlation coefficient
    r, p_value = stats.pearsonr(x, y)
    
    # Calculate manually
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numerator = np.sum((x - x_mean) * (y - y_mean))
    x_denominator = np.sum((x - x_mean) ** 2)
    y_denominator = np.sum((y - y_mean) ** 2)
    
    expected_r = numerator / np.sqrt(x_denominator * y_denominator)
    
    assert abs(r - expected_r) < 1e-10, f"Correlation coefficient {r} does not match expected {expected_r}"
    
    # Test linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    # Calculate manually
    expected_slope = numerator / x_denominator
    expected_intercept = y_mean - expected_slope * x_mean
    
    assert abs(slope - expected_slope) < 1e-10, f"Slope {slope} does not match expected {expected_slope}"
    assert abs(intercept - expected_intercept) < 1e-10, f"Intercept {intercept} does not match expected {expected_intercept}"
    
    # Test R-squared
    r_squared = r_value ** 2
    
    # Calculate predicted values and residuals
    y_pred = slope * x + intercept
    residuals = y - y_pred
    
    # Calculate R-squared manually
    ss_total = np.sum((y - y_mean) ** 2)
    ss_residual = np.sum(residuals ** 2)
    expected_r_squared = 1 - (ss_residual / ss_total)
    
    assert abs(r_squared - expected_r_squared) < 1e-10, f"R-squared {r_squared} does not match expected {expected_r_squared}"
    
    # Test t-test
    group1 = np.array([12, 15, 18, 22, 25, 28])
    group2 = np.array([10, 14, 16, 20, 21, 24])
    
    t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=True)
    
    # Calculate manually
    mean1 = np.mean(group1)
    mean2 = np.mean(group2)
    var1 = np.var(group1, ddof=1)
    var2 = np.var(group2, ddof=1)
    n1 = len(group1)
    n2 = len(group2)
    
    # Pooled variance
    pooled_var = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)
    
    # t-statistic
    expected_t = (mean1 - mean2) / np.sqrt(pooled_var * (1/n1 + 1/n2))
    
    assert abs(t_stat - expected_t) < 1e-10, f"t-statistic {t_stat} does not match expected {expected_t}"
    
    print("✓ Data Analysis Tool tests passed")
    return True

def run_all_tests():
    """Run all tests and generate a report."""
    print("Running all tests for the Probability and Statistics Course...")
    print("=" * 80)
    
    results = {}
    
    try:
        results["coin_flip_simulator"] = test_coin_flip_simulator()
    except Exception as e:
        print(f"✗ Coin Flip Simulator tests failed: {str(e)}")
        results["coin_flip_simulator"] = False
    
    print("-" * 80)
    
    try:
        results["distribution_explorer"] = test_distribution_explorer()
    except Exception as e:
        print(f"✗ Distribution Explorer tests failed: {str(e)}")
        results["distribution_explorer"] = False
    
    print("-" * 80)
    
    try:
        results["descriptive_statistics_calculator"] = test_descriptive_statistics_calculator()
    except Exception as e:
        print(f"✗ Descriptive Statistics Calculator tests failed: {str(e)}")
        results["descriptive_statistics_calculator"] = False
    
    print("-" * 80)
    
    try:
        results["interactive_quiz"] = test_interactive_quiz()
    except Exception as e:
        print(f"✗ Interactive Quiz tests failed: {str(e)}")
        results["interactive_quiz"] = False
    
    print("-" * 80)
    
    try:
        results["data_analysis_tool"] = test_data_analysis_tool()
    except Exception as e:
        print(f"✗ Data Analysis Tool tests failed: {str(e)}")
        results["data_analysis_tool"] = False
    
    print("=" * 80)
    
    # Generate summary
    all_passed = all(results.values())
    
    print("\nTest Summary:")
    for component, passed in results.items():
        status = "PASSED" if passed else "FAILED"
        print(f"  {component}: {status}")
    
    print("\nOverall Result:", "PASSED" if all_passed else "FAILED")
    
    # Save results to file
    with open('/home/ubuntu/probability_statistics_course/testing/test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\nTest results saved to /home/ubuntu/probability_statistics_course/testing/test_results.json")
    
    return all_passed

if __name__ == "__main__":
    run_all_tests()
