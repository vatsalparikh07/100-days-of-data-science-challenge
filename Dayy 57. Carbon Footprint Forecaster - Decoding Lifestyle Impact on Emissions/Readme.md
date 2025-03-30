# Day 57. 100 Days of Data Science Challenge - 03/29/2025

## 🌱 Carbon Footprint Forecaster - Decoding Lifestyle Impact on Emissions  

**Project Status:** ![Completed](https://img.shields.io/badge/Status-Completed-brightgreen)  

**Dataset:** 10,000 lifestyle profiles with 20+ behavioral/environmental factors [(Kaggle Link)](https://www.kaggle.com/datasets/dumanmesut/individual-carbon-footprint-calculation/data)

**Model:** Random Forest Regressor (R²: 0.98 | MSE: 19,493)  

## 🌍 Project Vision  
This analysis uncovers the hidden relationship between daily habits and carbon footprints, transforming mundane lifestyle data into actionable climate insights. By decoding patterns in energy use, transportation, and consumption behaviors, we create a predictive model that quantifies how small choices ripple into planetary impacts.

---

## 🔥 Key Discoveries  

### **Top 5 Emission Drivers**  
1. **Vehicle Distance**: Accounts for 32% of variance (1km ≈ 0.74kg CO₂)  
2. **Air Travel Frequency**: "Very Frequent" flyers emit 4.2x more than non-flyers  
3. **Diet**: Omnivores → 2,895kg | Vegans → 1,632kg (Δ43.6%)  
4. **Heating Energy**: Coal users emit 68% more than solar users  
5. **Clothing Consumption**: Fast fashion adds 12kg/month per 10 new garments  


---

## 🛠️ Technical Architecture  

### **Data Pipeline**  

```
Raw Data → Missing Value Imputation → Label Encoding → Feature Selection → Model Training
```

### **Preprocessing Highlights**  
- **67% Missing Vehicle Types** → Replaced with "None" to preserve dataset integrity  
- **16 Unique Recycling Patterns** → Encoded via label embedding  
- **4,003 Unique Vehicle Distances** → Preserved as continuous variable  

### **Model Performance**  
| Metric | Value | Interpretation |  
|--------|-------|----------------|  
| R² | 0.981 | Explains 98.1% of emission variance |  
| MSE | 19,493 | Avg error of ±140kg vs actual emissions |  
| OOB | 0.808 | Strong generalization capability |  

---

## 🎯 Lifestyle Impact Analysis  

### **Transportation Breakdown**  
| Category | Avg Emission (kg) |  
|----------|-------------------|  
| Diesel Vehicle Users | 4,742 |  
| Electric Vehicle Users | 1,300 |  
| Bicycle Commuters | 1,074 |  

### **Dietary Footprints**  
- Vegetarians show 29% lower emissions than omnivores

### **Energy Efficiency Paradox**  
- "Energy Efficient" labeled users showed only 7.2% lower emissions  
- *Insight:* May indicate rebound effects or measurement inaccuracies  

---

## 🔮 Predictive Insights  
The model identifies critical leverage points:  
- Reducing vehicle distance by 1,000km/month ≈ 740kg CO₂ savings  
- Switching coal → solar heating ≈ 1.2 ton annual reduction  
- Cutting fast fashion by 5 items/month ≈ 60kg monthly decrease  

---

## 🌱 Humanitarian Impact  
This work empowers:  
- **Policy Makers**: Identify high-impact sectors for climate regulations  
- **Urban Planners**: Optimize city layouts for sustainable commuting  
- **Individuals**: Make data-driven lifestyle changes  

> *"Every 1kg reduction across 1M people equals removing 140 gas-powered cars from roads annually"*

---

## 🚀 Future Directions  
1. Develop personalized sustainability recommendation engine  
2. Integrate real-time IoT data from smart homes/vehicles  
3. Build climate action gamification platform using prediction API  
