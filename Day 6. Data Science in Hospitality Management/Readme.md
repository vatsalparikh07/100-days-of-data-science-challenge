# Day 6. 100 Days of Data Science Challenge - 02/06/2025

# Data Science in Hospitality Management 🏨

**Predict guest room preferences using booking data**  
*A multi-class classification project to optimize hotel inventory management and guest experiences.*

---

## 🔍 Project Overview  
This project predicts the room type guests are likely to reserve (`room_type_reserved`) using hotel booking data. 

Key objectives include:  
- Identifying patterns in guest preferences  
- Optimizing dynamic pricing and marketing strategies  
- Reducing operational inefficiencies through demand forecasting  

**Tools Used**: Python, Pandas, Scikit-learn, Matplotlib, Seaborn  

---

## 📂 Dataset Features  
- **Demographics**: Adults/children count  
- **Stay Details**: Weekend/weeknight nights, lead time, arrival dates  
- **Guest History**: Repeat guests, cancellations, special requests  
- **Economic Factors**: Average room price, market segment  

---

## 🛠️ Steps  
1. **EDA & Preprocessing**  
   - Analyzed feature distributions and correlations  
   - Encoded categorical variables (`type_of_meal_plan`, `market_segment_type`)  
   - Scaled numerical features (StandardScaler)  

2. **Model Building**  
   - Tested **Random Forest**, **Decision Tree**, and **KNN** classifiers  
   - Optimized hyperparameters via grid search  

3. **Evaluation**  
   - **Top Model**: Random Forest (Accuracy: 92%, F1-score: 0.91)  
   - Feature importance analysis revealed **lead time** and **avg_price_per_room** as key predictors
  
---

## 🌟 Future Enhancements  
- Implement neural networks for complex pattern detection  
- Build a real-time booking recommendation system  
- Add SHAP values for interpretability  

---

## 👨💻 Behind the Code  
*"Day 6 taught me the power of ensemble methods in handling imbalanced class distributions. The Random Forest’s ability to capture non-linear relationships in guest behavior was a game-changer!"*  


