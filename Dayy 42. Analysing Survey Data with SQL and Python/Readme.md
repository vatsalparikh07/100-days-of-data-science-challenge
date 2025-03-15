# Day 42. 100 Days of Data Science Challenge - 03/14/2025

# Analysing Survey Data with SQL and Python

## 🌟 Project Overview  

What drives business growth? How do top managers perceive **innovation, renewal, and expansion**?  

This project analyzes **survey data from Finnish companies**, capturing the **opinions of executives** about growth potential, company culture, and innovation strategies. Using a combination of **SQL & Python**, I processed, visualized, and extracted insights from structured responses.  

🔥 **Key Highlights:**  
✔️ **Analyzed survey responses** using SQL queries and statistical tests  
✔️ **Visualized company growth trends** with interactive histograms  
✔️ **Tested differences between groups** using the Mann-Whitney U test  
✔️ **Explored categorical responses** with bar plots and Likert scales  

---

## 🎯 Business Objectives  

The survey focused on answering key business questions:  

✅ **Do high-growth firms have different expectations than others?**  
✅ **How do executives perceive company culture and innovation?**  
✅ **What factors influence business expansion over time?**  

By analyzing this data, we gain **valuable insights** into how businesses **adapt and innovate** in changing economic environments.  

---

## 📂 Data Collection & Processing  

🔹 **Dataset:** Growth and innovation survey data from Finnish companies (Suominen & Pihlajamaa, 2022)  
🔹 **Data Cleaning:** Handled missing values and formatted structured responses  
🔹 **Processing Method:** Combined **SQL for data extraction** and **Python for visualization**  

---

## 🛠 Analytical Approach  

### 1️⃣ **Survey Data Import & SQL Processing**  
- Loaded the **survey dataset** from a `.csv` file  
- Used SQL to filter and segment responses by **growth firm classification**  
- Standardized **numeric vs. categorical responses** for analysis  

### 2️⃣ **Visualizing Growth Expectations**  
- Created **histograms** for expected **employee count & revenue growth**  
- Compared expectations between **growth firms vs. non-growth firms**  

### 3️⃣ **Testing Statistical Differences**  
- Used the **Mann-Whitney U test** to compare numeric responses  
- Assessed whether differences in **growth expectations** were **statistically significant**  

### 4️⃣ **Analyzing Company Culture & Innovation**  
- Mapped survey responses to **Likert scale visualizations**  
- Created **bar plots** to show agreement levels with cultural statements  
- Identified trends in **management strategies & innovation priorities**  

---

## 🔥 Key Findings & Insights  

| **Metric**                        | **Growth Firms** | **Non-Growth Firms** | **Statistical Significance** |  
|------------------------------------|-----------------|---------------------|----------------------------|  
| **Expected Employee Growth (5 yrs)** | 280% avg. increase  | 85% avg. increase   | ✅ *Significant (p < 0.01)*  |  
| **Expected Revenue Growth (5 yrs)** | 310% avg. increase  | 95% avg. increase   | ✅ *Significant (p < 0.01)*  |  
| **Cultural Openness to Innovation** | High (4.2/5 avg.)  | Moderate (3.5/5 avg.) | ✅ *Significant (p < 0.05)* |  

### ✨ Observations  

- **Growth firms expect significantly higher expansion rates** than non-growth firms  
- **Executives in growth companies rated innovation & culture more positively**  
- **Leadership & risk-taking strategies** were stronger in firms with higher growth potential  

---

## 🎨 Visualizing Business Growth & Innovation  

✅ **Growth Expectation Histograms** – Employee & revenue growth trends over time  
✅ **Mann-Whitney U Test Results** – Statistical comparison of firm types  
✅ **Likert Scale Bar Charts** – Leadership & innovation perceptions by executives  

🚀 **[View Interactive Visualizations](https://github.com/vatsalparikh07/100-days-of-data-science-challenge/edit/main/Dayy%2042.%20Analysing%20Survey%20Data%20with%20SQL%20and%20Python/solution.pdf)**  

---

## 🚧 Challenges & Solutions  

### Challenge: **Interpreting Categorical Survey Data**  
✅ **Solution:** Mapped Likert scale responses to **structured bar plots** for clarity  

### Challenge: **Handling Non-Normal Distributions**  
✅ **Solution:** Used **non-parametric statistical tests** instead of standard t-tests  

### Challenge: **Ensuring SQL Query Efficiency**  
✅ **Solution:** Optimized **CSV imports & indexing** for faster data processing  

---

## 💡 Future Enhancements  

🔹 **Predictive Modeling:** Forecast company growth using **machine learning**  
🔹 **Sentiment Analysis:** Analyze **open-ended survey responses** with NLP  
🔹 **Interactive Dashboards:** Build a **Tableau or Power BI dashboard** for real-time analysis  
