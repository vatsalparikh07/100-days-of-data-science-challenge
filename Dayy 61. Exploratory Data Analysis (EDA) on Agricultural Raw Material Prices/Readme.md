# Day 61. 100 Days of Data Science Challenge - 04/02/2025

# 🌱 US Agricultural Raw Material Price Analysis (1990-2020)

## 📊 Project Overview
This analysis examines 30 years of price fluctuations for 9 key agricultural commodities in the United States. Using advanced time series analysis and correlation studies, we uncover hidden relationships between different commodity markets and identify significant price trends that shaped American agriculture over three decades.

![image](https://github.com/user-attachments/assets/72af97ca-e3cd-452a-82c0-0e05b2365a66)

## 🛠️ Technologies Used
- **Python 3.8+**
- **Pandas** for data manipulation
- **Seaborn/Matplotlib** for visualization
- **Jupyter Notebook** for interactive analysis
- **NumPy** for numerical operations

## 📁 Dataset Description
**Source:** [Kaggle - Agricultural Raw Material Prices](https://www.kaggle.com/datasets/kianwee/agricultural-raw-material-prices-19902020)  
**Time Frame:** April 1990 - June 2020  
**Commodities Tracked:**
1. Cotton
2. Hard Logs
3. Hard Sawnwood
4. Hides
5. Plywood
6. Rubber
7. Soft Logs
8. Soft Sawnwood
9. Wood Pulp

**Original Features:**
- Monthly price data
- Percentage price changes
- 361 monthly records (cleaned to 327 complete records)

## 🔧 Data Preparation
### Key Cleaning Steps:
1. Removed 34 incomplete records containing null values
2. Standardized price formats across decades
3. Converted percentage change metrics to absolute values
4. Focused analysis on 9 core commodities:

```
cleaned_columns = [
"Cotton Price", "Hard log Price", "Hard sawnwood Price",
"Hide Price", "Plywood Price", "Rubber Price",
"Softlog Price", "Soft sawnwood Price", "Wood pulp Price"
]
```


## 📈 Key Analysis

### 1. Decadal Price Trends
**Notable Patterns:**
- **Rubber** showed the most volatility (σ=$1.07)
- **Wood Pulp** had the steadiest growth (+216% since 1990)
- **Cotton** exhibited 3 distinct boom-bust cycles (1995, 2008, 2011)

### 2. Correlation Matrix Insights


**Strong Relationships:**
- Rubber ⇄ Cotton (r=0.74)
- Hard Logs ⇄ Plywood (r=0.83)
- Wood Pulp ⇄ Cotton (r=0.56)

**Unexpected Finding:**  
Soft Sawnwood prices showed inverse relationship with Hide prices (r=-0.11)

### 3. Price Distribution Analysis
**Commodity** | **Average Price** | **Max Price** | **Min Price**
---|---|---|---
Cotton | $1.62/lb | $5.06 (2011) | $0.82 (2001)
Hard Logs | $248.98/ton | $520.81 (1993) | $133.28 (1998)
Wood Pulp | $678.67/ton | $966.49 (2010) | $384.00 (1998)

## 📌 Key Insights
1. **Rubber-Cotton Link:** Strong positive correlation suggests shared market forces
2. **2008 Crisis Impact:** All commodities except wood pulp dropped 18-42%
3. **Sustainability Shift:** Hardwood prices stabilized post-2010 (+1.2% annual vs 4.8% pre-2010)
4. **COVID-19 Early Impact:** March 2020 showed 7-15% price drops across soft commodities

## 🔮 Future Analysis Directions
- Predict prices using ARIMA models
- Incorporate climate change data
- Analyze geopolitical impacts on agricultural markets
- Compare with global commodity prices

