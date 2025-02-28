# Day 27. 100 Days of Data Science Challenge - 02/27/25

# Time Series Analysis of Thames River in Python
*Exploring historical tide level data to uncover patterns and trends*

## 🌊 Project Overview  
This project focuses on analyzing **tide levels of the Thames River** at London Bridge using Python. By working with a century-long time series dataset (1911–1995), we explore water level trends, seasonal variations, and high/low tide patterns. The analysis includes data cleaning, visualization, statistical summaries, and an introduction to autocorrelation for forecasting.

**Key Objectives:**
- Clean and preprocess the dataset for analysis.
- Visualize and summarize high and low tide water levels.
- Explore seasonal and yearly variations in water levels.
- Compute autocorrelation to identify periodic patterns.

---

## 📂 Dataset Description  

The dataset contains tide level measurements from London Bridge spanning over 80 years. Key columns include:  

| **Column**         | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| `datetime`         | Date and time of the measurement                                                |
| `water_level`      | Tide level in meters relative to Ordnance Datum Newlyn (m ODN)                  |
| `is_high_tide`     | Flag indicating high tide (`1`) or low tide (`0`)                               |

---

---

## 🔧 Key Steps in Analysis  

1. **Data Cleaning**  
   - Renamed columns for clarity.
   - Converted `datetime` to a proper datetime format.
   - Converted `water_level` to a float for numerical analysis.
   - Added `month` and `year` columns for temporal grouping.

2. **Visualizing High and Low Tides**  
   - Created histograms to compare the distributions of high and low tides.  
   - Used boxplots to identify ranges, medians, and outliers.  

3. **Seasonal Trends in Water Levels**  
   - Grouped data by month and year to explore seasonal variations.  
   - Analyzed monthly trends for specific years (1927–1929).  

4. **Autocorrelation Analysis**  
   - Computed autocorrelation at daily, biweekly, monthly, and yearly frequencies to identify periodic patterns.

---

## 🌟 Key Findings  

1. **Tidal Patterns:**  
   - High tides average ~3.26 m ODN; low tides average ~-2.38 m ODN.
   - Seasonal variation is evident, with higher water levels in winter months.

2. **Autocorrelation:**  
   - Strong biweekly patterns align with lunar cycles (waxing/waning moon).
   - Lower autocorrelation at yearly frequencies indicates less predictable long-term patterns.

3. **Historical Trends:**  
   - Over the years analyzed (1927–1929), monthly trends remain consistent across years.

4. **Data Challenges:**  
   - Handling missing or incomplete records required careful preprocessing.

---

## 🛠️ Technical Skills Demonstrated  

1. **Data Cleaning:**  
   - Converted raw text files into structured DataFrames.
   - Handled large datasets with over 115,000 rows efficiently.

2. **Visualization:**  
   - Created histograms, boxplots, and line plots to explore distributions and trends.

3. **Time-Series Analysis:**  
   - Used resampling techniques for monthly/seasonal aggregation.
   - Computed autocorrelations to identify periodic patterns.

4. **Statistical Summaries:**  
   - Generated descriptive statistics to summarize key metrics like mean, median, and variance.

---

## 📚 Lessons Learned  

1. **Time-Series Complexity:**  
   Time-series datasets often exhibit seasonal and periodic behaviors that require specialized techniques like resampling and autocorrelation analysis.

2. **Visualization is Key:**  
   Visual tools like histograms and line plots are invaluable for identifying trends and anomalies in large datasets.

3. **Domain Knowledge Matters:**  
   Understanding tidal cycles (e.g., lunar influence) helped interpret the results effectively.

---

*"This project deepened my understanding of time-series analysis while providing fascinating insights into historical tidal patterns on the Thames River."*  
