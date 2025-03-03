# Day 30. 100 Days of Data Science Challenge - 03/02/2025

# Explaining Black-Box Machine Learning Models 
[![SHAP](https://img.shields.io/badge/SHAP-Explainability-ff69b4)](https://github.com/slundberg/shap) 
[![EBM](https://img.shields.io/badge/EBM-Interpretable-blue)](https://interpret.ml/)

## 🔍 Project Objective  
Develop an ML system predicting employment status (`Working`/`Not Working`) using North Carolina's 2017 Census data, while prioritizing **model transparency** and **fairness analysis**.

---

## 📦 Core Components  

### 📊 Dataset  
- **83,517 records** from [Folktables ACS 2017](https://github.com/zykls/folktables)
- **16 Features**:  
```
['Age', 'Schooling', 'Marital Status', 'Disability', 'Citizen Status',
'Sex', 'Race', 'Cognitive Difficulty', 'Military Service', ...]
```
- **Target**: Binary classification (`ESR` column)  
- **Class Balance**: 45.6% "Not Working" (handled via class weighting)

### 🧠 Model Zoo  
| Model Type       | Algorithms                          | Explanation Strategy     |
|------------------|-------------------------------------|--------------------------|
| **White-Box**    | Logistic Regression, EBM, FIGS     | Built-in coefficients    |
| **Black-Box**    | CatBoost, MLP                       | SHAP, Partial Dependence |

---

## 🏆 Performance & Fairness  

### 📈 Top Model Metrics  
| Model       | Accuracy | F1-Score | ROC-AUC | Runtime |
|-------------|----------|----------|---------|---------|
| **CatBoost**| 79.4%    | 77.2%    | 86.8%   | 38s     |
| **EBM**     | 79.3%    | 76.3%    | 86.7%   | 2m19s   |

### ⚖️ Demographic Disparities  
- **Gender**:  
- Male accuracy: 82.3% vs Female: 76.7% (CatBoost)  
- +4.5% false negatives for females  
- **Race**:  
- White individuals: 77% accuracy vs Asian: 69% (Decision Tree)  

---

## 💡 Technical Highlights  

### 1️⃣ Global Feature Impacts (SHAP)  
![SHAP Summary](https://cdn.mathpix.com/cropped/2025_03_03_e0774a5cb5c783fe601bg-18.jpg?height=1455&width=1729)  
- **Age** showed U-shaped risk pattern:  
```
shap.plots.partial_dependence("Age", cb_mdl.predict, X_test) # Critical under 21/over 64
```
- **Disability** doubled prediction risk (SHAP value +0.44)  
- Counterintuitive **gender effect**: Male → +8% employment probability  

### 2️⃣ Model-Specific Insights  
**EBM Feature Interactions**  
```
ebm_imp_df.sort_values('importance', ascending=False)[:3]
```
| Feature          | Importance |  
|------------------|------------|  
| Age              | 1.14       |  
| Age × Disability | 0.18       |  
| Sex × Race       | 0.05       |  

**Decision Tree Logic**  
```
|--- Age <= 62.50
|--- Disability <= 0.50 → Working
|--- Disability > 0.50 → Not Working
```

### 3️⃣ Local Explanations  
**Case Study**: 87-year-old with disability  
```shap.plots.waterfall(shap_values)```

# Key drivers:
- Age: +43% SHAP impact  
- Disability: +21%  
- Schooling: -7% (protective factor)  

---

## 🛠️ Technical Workflow  
1. **Data Engineering**  
   - Encoded 16 census categories → binary/ordinal features  
   - Stratified 75-25 split with class weighting  

2. **Model Development**  
   - Trained 6 models with fixed hyperparameters  
   - Evaluated precision-recall tradeoffs and ROC curves  

3. **Interpretation Layer**  
   - White-box: Coefficient analysis, tree visualization  
   - Black-box: SHAP beeswarm/decision plots  

---

## 🧠 Key Learnings  
1. **Interpretability Tradeoffs**:  
   - CatBoost (86.8% AUC) required post-hoc SHAP analysis  
   - EBM achieved 86.7% AUC with native explainability  

2. **Fairness Challenges**:  
   - All models showed gender/race accuracy gaps despite class weighting  

3. **Domain Validation**:  
   - Extreme age ranges and disability status aligned with real-world employment patterns  


