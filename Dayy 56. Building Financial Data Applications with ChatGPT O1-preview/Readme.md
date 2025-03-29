# Day 56. 100 Days of Data Science Challenge - 03/28/2025  

# 📈 Building Financial Data Applications with Sentiment Analysis [(Colab Link)](https://colab.research.google.com/drive/1PN-HiKjzoIH20KlxoLtqqSPnMEFzMtv0?usp=sharing)

**Status:** ![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  
**Tools Used:** Python, Yahoo Finance API, Finnhub API, Matplotlib, Seaborn, Pandas, NLTK, ChatGPT O1

---

## 🌟 Project Overview  

This project focuses on building a comprehensive **Financial Data Analysis Tool** that combines **interactive stock price visualizations** with **financial news sentiment analysis**. The tool enables users to explore stock trends over various time horizons and analyze market sentiment using real-time financial news headlines.  

The project is divided into three key components:  
1. **Stock Price Visualization Tool**: Interactive plots for stock prices with options to add technical indicators like SMA, EMA, and Bollinger Bands.  
2. **Customizable Date Range Selection**: Enhanced interactivity with date pickers for flexible time-based analysis.  
3. **Financial News Sentiment Analysis**: Extracts headlines from the Finnhub API and performs sentiment analysis using NLTK's VADER model.

---

## ✨ Key Features  

### **1. Stock Price Visualization Tool**  
- **Interactive Dropdowns**: Select stocks (e.g., AAPL, GOOGL, TSLA) and time horizons (e.g., 1M, 3M, 6M).  
- **Technical Indicators**:
  - *Simple Moving Average (SMA)*: Smooths out price data to identify trends.  
  - *Exponential Moving Average (EMA)*: Reacts quickly to recent price changes for trend detection.  
  - *Bollinger Bands*: Measures market volatility with upper/lower bands around a moving average.  
- **Custom Date Pickers**: Analyze stock performance over user-defined date ranges.

### Visualization Example  
#### Tesla (TSLA) Closing Prices with Bollinger Bands  
![TSLA Bollinger Bands](https://cdn.mathpix.com/cropped/2025_03_29_8167e291321bfea7c045g-5.jpg?height=840&width=1757&top_left_y=1322&top_left_x=201)  

---

### **2. Financial News Sentiment Analysis**  
- **Sentiment Scoring**:
  - Headlines are scored as *Positive*, *Negative*, or *Neutral* based on compound polarity scores from NLTK's VADER model.  
- **DataFrame Output**:
  - Columns include Stock Symbol, Date, Headline Title, and Sentiment.
- **Insights from Sentiment Distribution**:
  - AAPL shows the highest number of positive articles (73), while MSFT has the most neutral coverage (94).  

### Sentiment Analysis Example  
#### Sample Sentiment Distribution for AAPL, GOOGL, MSFT  
| Stock | Sentiment | Count |  
|-------|-----------|-------|  
| AAPL  | Positive  | 73    |  
| AAPL  | Neutral   | 69    |  
| AAPL  | Negative  | 38    |  
| GOOGL | Positive  | 76    |  
| GOOGL | Neutral   | 81    |  
| GOOGL | Negative  | 26    |  

#### Example Headlines for AAPL Sentiment Analysis  
| Stock | Date                | Title                                              | Sentiment |  
|-------|---------------------|----------------------------------------------------|-----------|  
| GOOGL | 2025-03-22 08:15:33 | VUG: Mag 7 Now The Lag 7, Better Valuation, We...	 | Negative  |  
| AAPL  | 2025-03-28 15:59:53 | TBLD: Profit From The Market's Shift Towards E... | Positive  |  
| AAPL  | 2025-03-28 15:35:48 | Why Mag 7 is a 'boy band' that needs to 'breakup'| Neutral   |

---

## 🛠️ Technical Highlights  

### **Stock Price Visualization Architecture**
1. **Data Source**: Yahoo Finance API for fetching historical stock prices.
2. **Interactive Widgets**:
   - Dropdowns for stock selection and time horizons.
   - Custom date pickers for flexible range selection.
3. **Indicators Implementation**:
   - SMA and EMA calculated using rolling averages and exponential smoothing.
   - Bollinger Bands computed as SMA ± (2 × standard deviation).

### **Sentiment Analysis Workflow**
1. **Data Source**: Finnhub API for fetching financial news headlines.
2. **Sentiment Scoring**:
   - Performed using NLTK's VADER model.
   - Compound polarity scores determine sentiment classification.
3. **Output Format**:
   - Results stored in a DataFrame with columns for Stock Symbol, Date, Title, and Sentiment.

---

## 🔍 Key Insights  

### Stock Price Trends
- Tesla's closing prices over the past year show significant volatility captured by Bollinger Bands.
- SMA and EMA provide smoother trendlines for identifying upward/downward movements.

### Market Sentiment
- Positive sentiment dominates across most stocks analyzed (AAPL, GOOGL, MSFT).
- Neutral articles often reflect balanced reporting or market uncertainty.

---

## 🖼️ Visual Insights  

### Stock Price Trends
![Stock Trends](https://cdn.mathpix.com/cropped/2025_03_29_8167e291321bfea7c045g-3.jpg?height=1031&width=1817&top_left_y=107&top_left_x=137)  

### 
---

## 🚀 Future Directions  

1. **Expand Indicator Library**:
   - Add RSI (Relative Strength Index) and MACD (Moving Average Convergence Divergence).  
2. **Enhance Sentiment Analysis**:
   - Incorporate additional APIs like Alpha Vantage or NewsAPI for broader coverage.
3. **Integrate Predictive Models**:
   - Use ARIMA or LSTM models to forecast stock prices based on historical data.

---

## 💡 Takeaways  

This project demonstrates how to combine interactive visualizations with sentiment analysis to gain actionable insights into financial markets. By integrating technical indicators and real-time news analysis, this tool empowers users to make informed investment decisions.

Made with ❤️ during Day 56 of my Data Science Challenge! 🚀
