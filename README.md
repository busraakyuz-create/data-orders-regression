# What Drives Customer Review Scores? Multivariate Regression on Olist Orders

Using **OLS regression (statsmodels)** on ~96,000 orders from the **Olist** Brazilian e-commerce dataset to measure how delivery and order features affect customer `review_score`, holding the other factors constant.

## Questions
- Is the review score driven by the total **wait time** or by the **delay versus the promised date**? The two are strongly correlated.
- Which other order features matter once we control for delivery?

## Approach
1. **Simple regressions:** `review_score ~ wait_time` and `review_score ~ delay_vs_expected`
2. **Multivariate regression** with both variables, to separate their effects (partial coefficients)
3. **Extended model** with order features: number of items, number of sellers, price, freight value, seller–customer distance
4. Checked coefficient significance and plotted the residuals

## Key findings

| Model | R² |
|---|---|
| `wait_time` only | 0.112 |
| `delay_vs_expected` only | 0.074 |
| `wait_time` + `delay_vs_expected` | 0.114 |
| Full model (7 features, 95,872 orders) | **0.145** |

- **Wait time is the main delivery driver.** Each extra day of waiting lowers the score by ~0.045 points. Once wait time is controlled for, the effect of delay drops from -0.075 to -0.021 per day.
- **Each additional seller in an order** lowers the score by about **1 point** (coef. -1.06), and each extra item lowers it by ~0.24 points.
- **Price and freight value are not significant** (p = 0.49 and p = 0.39).
- With R² ≈ 0.15, delivery and order features explain only part of customer satisfaction. Most of the variance comes from other factors, such as the product itself and the review text.

## Tech
Python · statsmodels · pandas · NumPy · seaborn · Matplotlib

## Files
- `orders_regression.ipynb` – full analysis
- `regression_analysis.py` – standalone script for the three base models
- `residual_analysis.png` – residual plot
- `olist/` – reusable data-cleaning package

Built during the Workintech Data Science & Machine Learning program.
