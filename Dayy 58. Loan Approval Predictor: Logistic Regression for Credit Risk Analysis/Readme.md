# Day 58. 100 Days of Data Science Challenge - 03/30/2025

## 🔍 Loan Approval Predictor: Logistic Regression for Credit Risk Analysis  

**Model:** Logistic Regression  
**Final Accuracy:** 79%  

---

## Project Overview

This project aims to predict the approval of loan applications using a supervised classification approach. By integrating a robust feature engineering pipeline into our traditional logistic regression model, we were able to improve the baseline accuracy significantly—from an initial 70% to 79%. The model utilizes a blend of financial, demographic, and property-related features extracted from a dataset of 553 loan applications.

---

## Data Dictionary

| Column Name            | Description                                                            |
|------------------------|------------------------------------------------------------------------|
| **loan_id**            | Unique identifier for each loan                                      |
| **gender**             | Applicant's gender (`Male` / `Female`)                                 |
| **married**            | Marital status (`Yes` / `No`)                                          |
| **dependents**         | Number of dependents                                                   |
| **education**          | Education level (`Graduate` / `Not Graduate`)                          |
| **self_employed**      | Self-employment status (`Yes` / `No`)                                  |
| **applicant_income**   | Applicant's income                                                     |
| **coapplicant_income** | Coapplicant's income                                                   |
| **loan_amount**        | Loan amount in thousands                                               |
| **loan_amount_term**   | Term of loan in months                                                 |
| **credit_history**     | Whether credit history meets guidelines (`1` = Yes, `0` = No)          |
| **property_area**      | Area of the property (`Urban` / `Semi Urban` / `Rural`)                |
| **loan_status**        | Loan approval outcome (target variable: `1` = Approved, `0` = Rejected)  |

---

## Exploratory Data Analysis (EDA)

Our initial analysis focused on data quality, distribution, and inter-variable relationships:
- **Cleanliness:** Checked data types, non-null counts, and removed the `loan_id` column to prevent data leakage.
- **Distributions & Relationships:**  
  - **Pairplots:** Visualized how numerical features such as `applicant_income`, `loan_amount`, and `credit_history` vary with the target variable.
    
    ![image](https://github.com/user-attachments/assets/214cb413-d447-4979-a820-4231987014bd)
    
  - **Correlation Heatmap:** Analyzed correlations between numerical features to identify potential multicollinearity.
    
    ![image](https://github.com/user-attachments/assets/d381577d-f398-413b-9c7e-87f40c2b8a57)
    
- **Class Imbalance:** The target distribution was examined to understand the approval versus rejection rates (~70% approved).

---

## Feature Engineering

A critical phase of this project was the development of an advanced feature engineering pipeline, which contributed to a significant performance gain:

- **Handling Skewed Distributions:**  
  - Applied log transformations on income features (both `applicant_income` and `coapplicant_income`) to reduce skewness.
  
- **Scaling & Normalization:**  
  - Scaled continuous variables such as `loan_amount` and `loan_amount_term` to standardize the range of values.
  
- **Categorical Encoding:**  
  - Performed one-hot encoding on categorical variables (`gender`, `married`, `education`, `self_employed`, `property_area`) to convert them into numeric features.
  
- **Outlier Detection & Removal:**  
  - Identified and handled outliers in financial features to stabilize model training.

These feature transformations not only improved model interpretability but also boosted our prediction accuracy to 79%.

---

## Modeling

The final model is built using logistic regression with the following workflow:
1. **Data Splitting:** The dataset was split into training (70%) and testing (30%) sets with stratification based on `loan_status`.
2. **Model Training:** A logistic regression classifier was trained using our engineered feature set.
3. **Evaluation:** Model performance was evaluated using accuracy, a confusion matrix, and other relevant metrics.


### Confusion Matrix

The confusion matrix below shows how well the model distinguishes between approved and rejected loans:
  
![image](https://github.com/user-attachments/assets/5b146f5b-5102-4369-9f6a-93cec2cb2a5c)

---

## Feature Importance

A simple bar plot of the trained model's coefficients revealed that **credit_history** and financial indicators (such as **loan_amount** and **applicant_income**) are the most significant predictors for loan approval.

![image](https://github.com/user-attachments/assets/6d739da1-b662-4f82-b683-25862c6479e3)

---

## Future Work

To further enhance model performance, potential next steps include:
- **Additional Feature Engineering:** Incorporating derived ratios (e.g., income-to-loan amount) and interaction features.
- **Model Selection:** Testing ensemble methods such as Random Forests or Gradient Boosting.
- **Hyperparameter Tuning:** Optimizing regularization and solver parameters for logistic regression.
- **Robust Validation Techniques:** Implementing cross-validation and more comprehensive error analysis.

---

## Resources

- **Dataset:** [loans.csv](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/30330689/f0cbde62-9fdb-4930-a7b2-f54d6bb312b6/loans.csv)
- **Solution Notebook:** [solution.ipynb](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/30330689/2ecb2471-2358-4308-b0b4-4dee0011a26c/solution.ipynb)
