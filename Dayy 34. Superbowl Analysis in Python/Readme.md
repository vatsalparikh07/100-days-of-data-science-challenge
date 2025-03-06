# Day 34. 100 Days of Data Science Challenge - 03/06/2025

# 🏈 Super Bowl LVII Running Game Analysis  

## 🚀 Project Overview  

Every year, millions of fans watch the Super Bowl, but the true game-changing plays aren't always the flashy passes—they're often the gritty, hard-earned rushing yards. In this project, I took a deep dive into the rushing performances of the Philadelphia Eagles and Kansas City Chiefs during **Super Bowl LVII**.  

Using **real NFL play-by-play data**, I built statistical models to evaluate player performance and developed a custom metric, **Rushing Yards Over Expected (RYOE)**, to highlight which players truly made an impact.  

---

## 🧠 What I Learned  

### 💡 **Data Science Techniques**  
- **Data Wrangling:** Cleaned and prepped large NFL datasets using `pandas` and `numpy`.  
- **Exploratory Data Analysis (EDA):** Visualized rushing performance with `seaborn` and `matplotlib`.  
- **Predictive Modeling:** Applied both **simple** and **multiple linear regression** using `statsmodels`.  
- **Feature Engineering:** Created the RYOE metric to compare actual vs. expected rushing performance.  

### 🏈 **Football Insights**  
- The rushing game often holds hidden value in a team's success.  
- Situational variables like `down`, `yards to go`, and `field position` play crucial roles in rushing success.  
- Data-driven analysis can offer unique perspectives beyond traditional football stats.  

---

## 🔍 Project Highlights  

### 1. **Data Collection & Preparation**  

I used the `nfl_data_py` package to pull in play-by-play data for the **2022 NFL season**. The dataset included everything from play types to rushing yards and player IDs. After filtering out non-rushing plays and cleaning missing values, I had a dataset ready for analysis.  

### 2. **Exploratory Data Analysis (EDA)**  

Before jumping into models, I explored the data:  
- **Top Rushers Identified:** *Miles Sanders* (Eagles) and *Isiah Pacheco* (Chiefs) emerged as key players.  
- **Underperformers:** Players like *Clyde Edwards-Helaire* struggled, with negative RYOE.  
- **Visual Insights:** Box plots showed the distribution of RYOE, making it easy to see who exceeded expectations.  

### 3. **Modeling Rushing Yards Over Expected (RYOE)**  

To quantify rushing performance, I built two models:  

- 🟢 **Simple Linear Regression:** Predicted rushing yards based solely on `ydstogo` (yards to go).  
- 🔵 **Multiple Regression:** Added more variables like `down`, `yardline_100`, `run_location`, `score_differential`, and `game_seconds_remaining`.  

The **multiple regression model** provided deeper insights by showing how different game scenarios influenced rushing outcomes.  

### 4. **RYOE Metric: The Secret Sauce**  

By comparing actual rushing yards with model predictions, I created the **RYOE** metric. This metric became a key indicator of whether a player was over- or under-performing relative to expectations.  

---

## 🏆 Key Results  

| **Player**             | **Team**        | **Total Yards** | **Average RYOE** |  
|------------------------|-----------------|-----------------|------------------|  
| *Miles Sanders*        | Eagles          | 1401            | +0.44            |  
| *Isiah Pacheco*        | Chiefs          | 951             | +0.50            |  
| *Clyde Edwards-Helaire*| Chiefs          | 302             | -0.13            |  
| *Jerick McKinnon*      | Chiefs          | 317             | -0.83            |  

### ✨ **Insights:**  
- **Sanders & Pacheco** were highly efficient, showing strong positive RYOE.  
- **McKinnon & Edwards-Helaire** struggled, suggesting inefficiency in rushing attempts.  
- Situational factors like **short-yardage situations** had a significant impact on rushing success.  

---

## 📊 Visualization  

A key visualization was the **RYOE box plot**, comparing players' efficiency:  

- **Positive RYOE:** Showed players outperforming expectations.  
- **Negative RYOE:** Highlighted areas where improvements were needed.  

This visual storytelling approach helped transform raw data into clear insights, bridging the gap between **data science** and **football analysis**.  

---

## 🚧 Challenges Faced  

1. **Data Quality:** Managing missing values and ensuring data integrity.  
2. **Model Complexity:** Balancing a simple model's clarity with a multiple regression's depth.  
3. **Football Context:** Translating raw data into meaningful football insights.  

---

## 💡 What’s Next?  

- **Broader Analysis:** Include passing and defensive metrics for a 360° game analysis.  
- **Advanced Modeling:** Test machine learning techniques to enhance predictive accuracy.  
- **Real-Time Analytics:** Develop an interactive dashboard for live NFL game analysis.  

---

## 📝 Conclusion  

This project was more than just a data exercise—it was an exploration of how numbers can tell stories. By blending **statistical analysis** with **football strategy**, I provided a fresh perspective on the Super Bowl's rushing performances. This experience sharpened my technical skills and deepened my appreciation for data's role in sports analytics.  

---

Thanks for checking out my project! If you’re into **data science**, **sports analytics**, or just love football, let’s connect! 😊  
