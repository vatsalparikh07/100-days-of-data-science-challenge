# Day 36. 100 Days of Data Science Challenge - 03/08/2025
# 📈 Time Series Analysis: Forecasting GameStop's Stock Price 🚀  

## 🌟 Project Overview  

On Day 36, I explored the world of **Time Series Analysis** using **Python** to analyze and predict the stock price of **GameStop (GME)**. With data spanning from **2020 to 2023**, this project focused on understanding historical trends, visualizing price movements, and using **ARIMA** models to forecast future prices.  

---

## 🚀 Key Highlights  

- **Historical Analysis:** Visualized GameStop's legendary stock price movements with interactive charts.  
- **Autocorrelation Insight:** Detected patterns in the data using **ACF and PACF** plots.  
- **Predictive Modeling:** Built and evaluated **ARIMA models** to generate stock price forecasts.  
- **Market Context:** Compared GameStop’s performance with the **S&P 500** to provide a benchmark.  

---

## 🧠 What I Learned  

### 💡 **Technical Skills Mastered**  

- **Time Series Methods:** Implemented rolling averages, **autocorrelation analysis**, and **ARIMA** modeling.  
- **Visualization Excellence:** Created dynamic visualizations using **Plotly** for deeper insights.  
- **Model Selection:** Evaluated different **ARIMA configurations** using **AIC/BIC** criteria.  
- **Forecasting:** Generated **7-day price predictions** with confidence intervals.  

### 📈 **Financial Insights**  

- GameStop's price exhibited **strong autocorrelation**, indicating momentum-driven behavior.  
- Major market events, such as the **Reddit-fueled surge** and **Robinhood trading restrictions**, had visible impacts on price trends.  
- The **AR(1) model** suggested a high dependency of prices on their previous values, showcasing the "meme stock" effect.  

---

## 📊 Methodology  

### 1. **Data Collection & Preparation**  

- Imported historical stock data for **GameStop (GME)** using **yfinance**.  
- Standardized the data for accurate comparison with the **S&P 500** index.  
- Managed missing values and ensured the time series data was continuous.  

### 2. **Exploratory Data Analysis (EDA)**  

- **Visualization:** Line and candlestick charts provided a clear picture of GameStop’s volatility.  
- **Statistical Analysis:** Analyzed the **stationarity** of the series using the **Dickey-Fuller test**.  
- **Autocorrelation Insights:** **ACF/PACF plots** revealed the optimal parameters for the **ARIMA** model.  

### 3. **Modeling Approach**  

- Evaluated multiple **ARIMA(p,d,q)** models to identify the best fit for forecasting.  
- Selected the **AR(1) model** based on the **BIC (Bayesian Information Criterion)**.  
- Forecasted the stock price with **95% confidence intervals**, offering a realistic price range.  

---

## 🏆 Key Results  

| **Metric**              | **Value**               |  
|-------------------------|-------------------------|  
| **Best Model**          | AR(1) with **BIC = 110.45**   |  
| **Forecasted Price**    | $19.76 (Feb 20, 2023)       |  
| **Price Range (95% CI)** | **$15.82** to **$23.70**       |  

### ✨ **Insights:**  

- **Strong Autocorrelation:** The **AR(1) model** showed a coefficient of **0.82**, indicating momentum in price movements.  
- **Market Events Impact:** Highlighted how specific events, like the **Robinhood halt**, disrupted the price trend.  
- **Comparison with S&P 500:** GameStop's price showed extreme volatility compared to the broader market index.  

---

## 🎨 Visualization Highlights  

1. **Interactive Price Chart:**  
   - Line and candlestick charts provided detailed views of GameStop’s stock performance.  
   - Annotated key events like the **r/wallstreetbets surge** for context.  

2. **Prediction Plot:**  
   - Displayed **7-day forecasted prices** with shaded confidence intervals, offering clear insights into expected volatility.  

---

## 🚧 Challenges & Solutions  

- **Volatile Data:** Managed price spikes by applying **rolling averages** for smoother trend visualization.  
- **Model Selection:** Compared **ARIMA models** using **AIC/BIC scores** to ensure the best fit.  
- **Handling Missing Data:** Utilized **re-indexing** to maintain a consistent time series format.  

---

## 📝 Conclusion  

This project was a fantastic opportunity to merge **data science** with **financial analysis**, showcasing how historical data can drive meaningful predictions. By combining robust **time series techniques** with **financial insights**, I developed a powerful tool for understanding stock price behaviors, especially in the context of **meme stocks** like GameStop.  

---

Thanks for following along! If you're into **data science**, **finance**, or just love a good stock market story, let’s connect! 😊  
