# Day 65. 100 Days of Data Science Challenge - 04/06/2025

# 🧠 Banking Behavior Analyzer  
> **Extracting customer insights through feature engineering and visual intelligence**

---

## 💡 Project Overview

This project explores **data enrichment** and **group-wise analytics** on customer banking data. By engineering meaningful features—such as average age, maximum account balances, campaign interactions—we aim to provide a foundational layer for downstream modeling, segmentation, or visual storytelling.

Whether you're visualizing marketing outreach effectiveness or profiling financial demographics, this toolkit offers **modular, tested, and extensible components**.

---

## 🔍 What’s Inside?

### 🎯 Core Functions (`production_code.py`)

| Function | Description |
|---------|-------------|
| `max_customer_account_balance` | Adds the max balance of all customers to each row |
| `customers_mean_age` | Adds mean age as a new feature |
| `gb_max_customer_account_balance` | Gets max balance within a group |
| `gb_customers_mean_age` | Gets mean age within a group |
| `marital_status_groups` | Group-wise summarization by marital status |
| `creating_features_banking_data` | Pipelines key feature transformations |

---

### 🧪 Testing Suite

Located in `test_productions_code.py`, this ensures robustness of core logic using **Pytest**:

- ✅ Feature values are computed correctly
- ✅ Group aggregations respect labels
- ✅ All expected columns exist post-transformation

---

### 🧬 Data Context

The dataset (`train.csv`) includes fields like:

- `balance` – customer account balance
- `age` – customer age
- `duration` – duration of last contact
- `campaign` – number of contacts performed during this campaign
- `marital` – marital status of the customer

Sample enhancements from `sample_code.py`:
- 🧮 `annual_duration`: Flattened nested durations  
- 🔁 `campaign_limit`: Tuple encoding for campaign reach  
- 📊 GroupBy summaries across `marital` segments

---

## ⚙️ Pre-Commit Automation

`pre-commit-config.yaml` includes hooks for:

- **`ruff`**: Linting Python files lightning-fast  
- **`ruff-format`**: Auto-formatting according to project standards

### Style Conventions (`pyproject.toml`)
- **Quote Style**: Double `" "`  
- **Indentation**: 4 spaces  
- **Lint Rules**: Based on `flake8`, `pyflakes`, `bugbear`  
- **Line Width**: 88 characters

---

## 🧠 Highlights

- 🏗️ **Composable data pipeline** using `.pipe()`
- 🧪 **Test-driven** approach to data transformations
- 🧼 **Clean code standards** using Ruff & TOML configs
- 🔍 **Insightful summaries** by marital groups
- 🧰 **Flexible structure** for experimentation

---

## 🚀 Example Output

Here’s what a grouped summary looks like (simplified):

| Marital | Balance Max | Age Mean |
|---------|-------------|----------|
| M       | 1500        | 45.6     |
| S       | 1200        | 38.2     |
| W       | 950         | 58.4     |
