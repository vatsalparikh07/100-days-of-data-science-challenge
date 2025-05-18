## 📈 Stock Market Performance Analysis with Python & yfinance

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-yellowgreen?style=flat-square&logo=pandas)](https://pandas.pydata.org/)
[![yfinance](https://img.shields.io/badge/yfinance-Yahoo_Finance_API-orange?style=flat-square)](https://pypi.org/project/yfinance/)
[![Plotly Express](https://img.shields.io/badge/Plotly_Express-Interactive_Viz-blueviolet?style=flat-square)](https://plotly.com/python/plotly-express/)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_94-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Unveiling Market Insights from Historical Stock Data

Welcome to Day 94 of my #100DaysOfDataScience challenge! This project dives into **Stock Market Performance Analysis**, using Python to fetch, process, and visualize historical data for major tech companies: **Apple (AAPL), Microsoft (MSFT), Netflix (NFLX), and Google (GOOG)**. The goal is to apply common financial analysis techniques to understand price movements, trends, volatility, and correlations between these stocks.

By leveraging the **`yfinance` API** to access Yahoo Finance data and **Pandas** for data manipulation, coupled with **Plotly Express** for interactive visualizations, we aim to:
*   Retrieve and structure historical stock data (OHLCV - Open, High, Low, Close, Volume).
*   Visualize overall stock performance and compare trends across companies.
*   Calculate and analyze **Moving Averages (MA10, MA20)** to identify potential buy/sell signals.
*   Measure and visualize stock **Volatility**.
*   Examine the **Correlation** between stock prices of different companies (e.g., Apple vs. Microsoft).

This project demonstrates a practical workflow for financial data analysis, providing insights that could inform investment decisions.

---

## ✨ Key Features & Concepts Mastered

*   **Data Acquisition via API:** Utilized the `yfinance` library to download historical stock data (OHLCV) for multiple tickers over a specified period (last 3 months).
*   **Pandas for Time-Series Data:**
    *   Concatenated data for multiple tickers into a single DataFrame with a MultiIndex (`Ticker`, `Date`).
    *   Reshaped data (`.reset_index()`) for easier plotting.
    *   Calculated **Moving Averages (10-day and 20-day)** on the 'Close' price, grouped by 'Ticker' (`.groupby('Ticker')['Close'].rolling(window=...).mean()`).
    *   Calculated **Volatility** as the rolling standard deviation of daily percentage changes (`.groupby('Ticker')['Close'].pct_change().rolling(window=10).std()`).
    *   Filtered and merged DataFrames to prepare for correlation analysis.
*   **Interactive Data Visualization (Plotly Express):**
    *   **Line Charts:** For overall stock performance (`px.line(df, x='Date', y='Close', color='Ticker')`) and for visualizing Moving Averages alongside closing prices for each stock.
    *   **Area Charts (Faceted):** To easily compare the performance trends of different companies side-by-side (`px.area(..., facet_col='Ticker')`).
    *   **Scatter Plots with Trendlines:** To visualize the correlation between two stock prices (e.g., AAPL vs. MSFT) using `px.scatter(..., trendline='ols')`.
*   **Financial Metrics & Interpretation:**
    *   Understanding Moving Average crossovers (MA10 vs. MA20) as bullish/bearish signals.
    *   Interpreting Volatility as a measure of price fluctuation and risk.
    *   Analyzing Correlation to understand how different stocks move in relation to each other.

---

## 🛠️ Tech Stack: The Financial Analyst's Python Toolkit

*   **Core Language:** Python 3.8+
*   **Data Acquisition:** `yfinance` library
*   **Data Manipulation & Analysis:** Pandas
*   **Date/Time Handling:** `datetime` module, `pandas.DateOffset`
*   **Interactive Visualization:** Plotly Express (`plotly.express`)
*   **Environment:** Jupyter Notebook (`solution.ipynb`)

---

## 🗺️ The Analytical Workflow: From Tickers to Trends

This project follows a structured approach to stock market analysis:

1.  **Setup & Data Retrieval:**
    *   Installed `yfinance` (`!pip install yfinance`).
    *   Imported necessary libraries (`pandas`, `yfinance`, `datetime`, `plotly.express`).
    *   Defined a list of `tickers` (AAPL, MSFT, NFLX, GOOG) and a date range (last 3 months).
    *   Used a loop with `yf.download(ticker, start=start_date, end=end_date)` to fetch data for each ticker.
    *   Concatenated the individual DataFrames into a single master DataFrame `df` using `pd.concat`, with 'Ticker' and 'Date' as a MultiIndex.
    *   Reset the index to make 'Ticker' and 'Date' regular columns.

2.  **Overall Performance Visualization:**
    *   Created a **line chart** showing the 'Close' price over 'Date' for all tickers, colored by 'Ticker', to visualize general performance.
    *   Generated a **faceted area chart** to compare individual stock price movements more clearly, with each ticker in its own subplot.

![image](https://github.com/user-attachments/assets/9dd5d195-db00-47be-8d8b-2a906dca64d1)

*Fig 1: Plotly line chart showing closing prices for AAPL, MSFT, NFLX, GOOG over the last 3 months.*

![image](https://github.com/user-attachments/assets/341cbdb2-65db-4503-ab31-feed2edad78f)

*Fig 2: Plotly faceted area chart for individual stock price trends.*

3.  **Moving Average Analysis:**
    *   Calculated 10-day (`MA10`) and 20-day (`MA20`) moving averages of the 'Close' price for each 'Ticker' using `df.groupby('Ticker')['Close'].rolling(window=...).mean()`.
    *   Generated separate **line charts for each ticker**, plotting the 'Close' price along with its `MA10` and `MA20` to identify trends and potential crossover signals.

![image](https://github.com/user-attachments/assets/888aacae-d711-4328-a884-3f14b710fd2d)

*Fig 3: Apple (AAPL) closing price with 10-day and 20-day Moving Averages. Bullish/bearish signals can be inferred from MA crossovers.*

4.  **Volatility Analysis:**
    *   Calculated daily percentage change (`.pct_change()`) of the 'Close' price for each ticker.
    *   Computed the 10-day rolling standard deviation of these percentage changes to represent `Volatility`.
    *   Created a **line chart** plotting `Volatility` over 'Date' for all tickers, colored by 'Ticker'.

![image](https://github.com/user-attachments/assets/562f6aa6-f75e-4be1-879b-f494bee8c066)

*Fig 4: Plotly line chart showing the 10-day rolling volatility for each stock.*

5.  **Correlation Analysis (Apple vs. Microsoft):**
    *   Created separate DataFrames for AAPL and MSFT containing 'Date' and 'Close' price.
    *   Merged these two DataFrames on 'Date' to get a combined DataFrame `df_corr` with AAPL and MSFT closing prices side-by-side.
    *   Generated a **scatter plot** of AAPL 'Close' price vs. MSFT 'Close' price, including an Ordinary Least Squares (OLS) `trendline` to visualize the correlation.

![image](https://github.com/user-attachments/assets/691bb7f4-51ed-4b91-bec4-93900c364f61)

*Fig 5: Scatter plot showing a strong positive correlation between Apple and Microsoft stock prices over the period.*

---

## 💡 Key Insights & Interpretations

*   **General Trends:** Visualizing closing prices (Fig 1 & 2) helps identify which stocks were outperforming or underperforming others during the 3-month period.
*   **Moving Average Signals (Fig 3):** When a shorter-term MA (MA10) crosses *above* a longer-term MA (MA20), it's often seen as a bullish signal (price likely to rise). Conversely, a cross *below* is bearish (price likely to fall). The individual stock charts allow for spotting these signals.
*   **Volatility Comparison (Fig 4):** The volatility plot shows which stocks experienced more significant price swings. Higher volatility implies higher risk but also potentially higher reward. In the sample, NFLX showed periods of higher volatility compared to AAPL, MSFT, and GOOG.
*   **Stock Correlation (Fig 5):** The scatter plot for AAPL and MSFT showed a strong positive linear relationship. This means their stock prices tended to move in the same direction during this period, suggesting they might be influenced by similar market factors or industry trends. This has implications for portfolio diversification.

---

*Day 94 of #100DaysOfDataScience explored essential techniques for stock market performance analysis using Python, yfinance, Pandas, and Plotly Express. Turning raw market data into actionable visual insights! - Vatsal Parikh*
