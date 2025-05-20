## SQL-Powered Price Optimization: Maximizing Revenue with Linear Regression 📈

[![SQL](https://img.shields.io/badge/Language-SQL_(DuckDB_Flavor)-blue?style=flat-square&logo=sqlite)](https://duckdb.org/) <!-- Assuming DuckDB due to REGR_ functions -->
[![Data Analysis](https://img.shields.io/badge/Technique-Price_Optimization-yellowgreen?style=flat-square)](https://en.wikipedia.org/wiki/Price_optimization)
[![Concept](https://img.shields.io/badge/Core_Concept-Demand_Curve_Analysis-orange?style=flat-square)](https://en.wikipedia.org/wiki/Demand_curve)
[![Dataset](https://img.shields.io/badge/Data-Custom_Sales_Data-lightgrey?style=flat-square)](./demand_curve_data.csv)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_3-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Finding the Optimal Price to Maximize Revenue using SQL

Welcome to Day 3 of my #100DaysOfDataScience challenge! Businesses constantly grapple with pricing: too low, and you leave money on the table; too high, and you lose sales. This project demonstrates a powerful analytical technique to **determine the price point that maximizes total revenue**, using only **SQL** (specifically with functions available in systems like DuckDB) and fundamental calculus concepts.

We analyze a dataset (`demand_curve_data.csv`) containing `price` and `quantity_sold` to:
1.  **Model Demand:** Perform a linear regression in SQL to describe `quantity_sold` as a function of `price`, including a log transformation to better capture the non-linear relationship.
2.  **Formulate Revenue Function:** Derive an equation for `revenue` (price * quantity_sold) based on the demand model.
3.  **Optimize with Calculus:** Use calculus (finding the derivative of the revenue function and setting it to zero) to mathematically identify the price that maximizes revenue.
4.  **Report Results:** Present the optimal price and the expected maximum revenue.

This project highlights how SQL, often seen as just a data retrieval language, can be a powerful tool for statistical modeling and business optimization, directly impacting a company's bottom line.

---

## ✨ Key Features & Concepts Mastered

*   **SQL for Regression:**
    *   Calculated components of linear regression (slope, intercept) using standard SQL aggregate functions (`STDDEV`, `AVG`, `CORR`) and the fundamental regression formulas.
    *   Utilized specialized SQL functions (`REGR_SLOPE`, `REGR_INTERCEPT`) available in databases like DuckDB for direct calculation of regression parameters.
*   **Logarithmic Transformation for Demand Modeling:**
    *   Applied a natural logarithm (`LN()`) transformation to `quantity_sold` to better model the non-linear relationship between price and demand, resulting in an equation of the form `log(quantity_sold) = b₀ + b₁ * price`.
    *   Understood the implication of this transformation for the revenue function: `revenue = price * EXP(b₀ + b₁ * price)`.
*   **Calculus for Optimization:**
    *   Conceptually derived the revenue function based on the log-linear demand model.
    *   Applied the **product rule** of differentiation to find the derivative of the revenue function with respect to price.
    *   Solved for the price where the derivative equals zero, yielding the revenue-maximizing price formula: **Optimal Price = -1 / b₁** (where b₁ is the slope from the log-linear regression).
    *   Derived the formula for maximum revenue at this optimal price: **Max Revenue = (-1 / b₁) * EXP(b₀ - 1)**.
*   **SQL for Implementation:**
    *   Used **Common Table Expressions (CTEs)** with the `WITH` clause to structure complex queries, calculate intermediate regression statistics, and then compute the optimal price and maximum revenue.
    *   Leveraged SQL aggregate functions (`AVG`, `STDDEV`, `CORR`) and specialized regression functions (`REGR_SLOPE`, `REGR_INTERCEPT`).
    *   Utilized mathematical functions in SQL (`LN`, `EXP`).
*   **Exploratory Data Analysis (EDA) in SQL:**
    *   Initial visualization (conceptual scatter plot in the DataLab environment) of `price` vs. `quantity_sold` to understand the underlying relationship.
    *   Comparison of model-derived optimal revenue vs. naively selecting the highest observed revenue from the dataset.

---

## 🛠️ Tech Stack & Core SQL Functions

*   **Primary Tool:** SQL (syntax compatible with DuckDB or similar systems supporting advanced analytical functions).
*   **Data Source:** `demand_curve_data.csv` (a custom dataset with 200 rows of price and quantity sold data).
*   **Key SQL Functions & Clauses Used:**
    *   `SELECT`, `FROM`, `WITH ... AS` (CTEs)
    *   **Aggregate Functions:** `COUNT(*)`, `SUM()`, `AVG()`, `STDDEV()`, `CORR(y, x)`
    *   **Specialized Regression Functions:** `REGR_SLOPE(y, x)`, `REGR_INTERCEPT(y, x)`
    *   **Mathematical Functions:** `LN()` (natural log), `EXP()` (exponential)
    *   `ORDER BY`, `LIMIT` (for naive best price check)
*   **Mathematical Concepts:** Simple Linear Regression, Logarithmic Transformation, Differential Calculus (Product Rule, Optimization by finding where the derivative is zero).
*   **Environment:** DataLab SQL Notebook.

---

## 🗺️ The Optimization Workflow: A SQL-Driven Approach

The project follows a three-part structure to find the revenue-maximizing price:

### Part 1: Linear Regression in SQL (Modeling Demand)

*   **Objective:** Model the relationship `quantity_sold = b₀ + b₁ * price`.
*   **Steps:**
    1.  **EDA:** Initial `SELECT price, quantity_sold` and conceptual scatter plot visualization (in DataLab) to observe the inverse, potentially non-linear relationship.
    2.  **Calculate Regression Statistics:**
        *   Used a CTE (`regression_data`) to compute `STDDEV(price)`, `STDDEV(quantity_sold)`, `AVG(price)`, `AVG(quantity_sold)`, and `CORR(price, quantity_sold)`.
        *   Calculated `slope (b₁)` as `correlation * (sd_quantity_sold / sd_price)`.
        *   Calculated `intercept (b₀)` as `mean_quantity_sold - slope * mean_price`.
    3.  **Alternative using DuckDB Functions:** Demonstrated using `REGR_SLOPE(quantity_sold, price)` and `REGR_INTERCEPT(quantity_sold, price)` for direct calculation.

### Part 2: Modeling Revenue with Log Transformation

*   **Objective:** Derive a revenue function `revenue = f(price)` that better captures the observed curvature.
*   **Transformation:** Applied a natural log transformation to `quantity_sold`, modeling `LN(quantity_sold) = b₀ + b₁ * price`.
*   **Revenue Equation:** This leads to `revenue = price * EXP(b₀_log + b₁_log * price)`.
*   **SQL Implementation:** Used nested `SELECT` statements (subqueries) within the `EXP()` function to calculate `b₀_log` (intercept of LN(quantity_sold) vs price) and `b₁_log` (slope of LN(quantity_sold) vs price) and then compute the `revenue_function` for each price point.

### Part 3: Finding the Price That Maximizes Revenue (Calculus & SQL)

*   **Theoretical Basis:**
    *   The derivative of the revenue function `revenue = price * EXP(b₀_log + b₁_log * price)` was found using the product rule.
    *   Setting this derivative to zero and solving for `price` yields: **Optimal Price = -1 / b₁_log** (where b₁_log is the slope from the regression of `LN(quantity_sold)` on `price`).
    *   The **Maximum Revenue** at this price is: `(-1 / b₁_log) * EXP(b₀_log - 1)`.
*   **SQL Implementation:**
    *   Used a CTE (`regression_data`) to calculate the `slope` (b₁_log) and `intercept` (b₀_log) from the `LN(quantity_sold)` vs. `price` regression.
    *   Selected `(-1 / slope) AS optimal_price` and `(-1 / slope) * EXP(intercept - 1) AS max_revenue` from this CTE.

```
WITH regression_data AS (
SELECT
REGR_INTERCEPT(LN(quantity_sold), price) AS intercept,
REGR_SLOPE(LN(quantity_sold), price) AS slope
FROM "demand_curve_data.csv"
)
SELECT
(-1 / slope) AS optimal_price,
(-1 / slope) * EXP(intercept - 1) AS max_revenue
FROM regression_data;
```
---

## 💰 Results: The Optimal Price & Maximum Revenue

| Metric         | Value         |
| :------------- | :------------ |
| Optimal Price  | $20,106.44    |
| Max Revenue    | $733,106.95   |

**Comparison with Naive Approach:**
The notebook also shows a naive approach of finding the price that yielded the highest actual revenue in the dataset (`SELECT price, price * quantity_sold AS revenue FROM "demand_curve_data.csv" ORDER BY revenue DESC LIMIT 1`). This yielded a price of $24,020.10 and revenue of $840,703.52.

*   **Important Note:** The model-derived optimal price ($20,106) and max revenue ($733,107) are based on the *log-linear demand model*. The notebook's naive approach actually yielded a higher *observed* revenue at a different price point ($24,020 leading to $840,703). This discrepancy highlights that the log-linear model, while capturing curvature, might not perfectly fit the data or other demand models might be more appropriate. The project's goal was to demonstrate the *methodology* of using SQL for this type of optimization based on a chosen model.

---

*Day 3 of #100DaysOfDataScience shows how SQL, combined with fundamental economic and calculus principles, can be a powerful tool for solving complex business optimization problems like price setting. A fascinating blend of theory and practical SQL! - Vatsal Parikh*
