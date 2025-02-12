# Day 12. 100 Days of Data Science Challenge - 02/12/2025
# 🌿 Liver Disease Prediction System

**Classifying liver health using biochemical markers and patient data**  
*A binary classification project leveraging ensemble methods and data visualization*

---

## 🌟 Project Highlights
- Achieved **74.3% accuracy** using a voting ensemble of Logistic Regression, SVM, and Random Forest
- Handled **missing values** with median imputation
- Visualized data distribution for each feature (histograms, boxplots)
- Addressed data imbalance using SMOTE oversampling

---

## 📊 Dataset Overview
| Feature | Description | Transformation |
|---------|-------------|-----------------|
| Age | Patient age (years) | StandardScaler |
| Gender | Male/Female | LabelEncoder |
| Total Bilirubin | TB level (mg/dL) | StandardScaler |
| ... | ... | ... |
| Dataset | Liver disease (1) or not (2) | Binary Label |

**Key Insight**:  Imbalanced dataset (diseased: 416, non-diseased: 167)

---

## 🛠️ Implementation Highlights
1. **Data Cleaning**: Imputation for missing 'Albumin\_and\_Globulin\_Ratio' using median
2. **Feature Scaling**: StandardScaler applied to numerical features
3. **Model Training**:
   - Logistic Regression
   - SVM (RBF kernel)
   - Random Forest
4. **Performance Evaluation**: Accuracy, Precision, Recall, F1-score, Confusion Matrix

---

## 🚀 Key Findings
1. **Feature Importance**: Total Bilirubin and Alkaline Phosphotase are important predictors
2. **Missing Data**:  Imputing 'Albumin\_and\_Globulin\_Ratio' improved model stability
3. **SMOTE Impact**: Oversampling enhanced the detection of non-diseased cases

---

## ⚙️ Model Performance
| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Voting Classifier | 74.3% | 75.6% | 89.7% | 82.0% |
| Logistic Regression | 71.8% | 73.2% | 88.1% | 79.9% |
| SVM | 70.5% | 72.1% | 87.4% | 79.1% |
| Random Forest | 72.4% | 74.0% | 87.7% | 80.3% |

---

## 🌐 Future Enhancements
- Implement cross-validation for robust evaluation
- Explore more advanced ensemble techniques (e.g., stacking)
- Integrate SHAP values for explainable AI

---

🔗 **Dataset Source**: [Indian Liver Patient Records](https://www.kaggle.com/datasets/uciml/indian-liver-patient-records)  
📌 **Key Technique**: VotingClassifier with diverse base models  
💡 **Pro Tip**: Use `GridSearchCV` to optimize VotingClassifier weights
