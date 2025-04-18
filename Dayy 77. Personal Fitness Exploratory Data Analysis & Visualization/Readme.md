# Day 77. 100 Days of Data Science Challenge - 04/18/2025 

## 💪 Personal Fitness Data Analysis & Visualization 📊

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-yellowgreen?style=flat-square&logo=pandas)](https://pandas.pydata.org/)
[![Plotly Express](https://img.shields.io/badge/Plotly-Interactive_Viz-blueviolet?style=flat-square&logo=plotly)](https://plotly.com/python/plotly-express/)
[![Dataset](https://img.shields.io/badge/Dataset-Personal_Fitness-orange?style=flat-square)](./fitness_data.csv)
[![Day 77](https://img.shields.io/badge/100DaysOfDataScience-Day_77-brightgreen?style=flat-square)](https://www.100daysofcode.com/) <!-- Update Day Number! -->

## 🚀 The Mission: Turning Raw Fitness Data into Actionable Insights

We all track our fitness – steps, sleep, workouts – but what stories does that data *really* tell? This project dives into a synthetic **personal fitness dataset** (`fitness_data.csv`), mimicking the kind of data you'd get from apps like Fitbit or Apple Health, over a **185-day period**.

Using the power of **Python**, **Pandas**, and **Plotly Express**, we'll go beyond simple tracking to:
*   🧹 **Clean and Prepare** the raw data.
*   ✨ **Engineer insightful new features** like 'Sleep Debt'.
*   📊 **Visualize trends** in steps, calories, sleep patterns, heart rate zones, and workout effectiveness.
*   🤔 **Uncover correlations** and patterns in daily activity and well-being metrics.

This project, part of my **#100DaysOfDataScience challenge (Day 77)**, showcases fundamental data analysis and visualization techniques applied to a relatable, real-world scenario. Let's see what the data reveals!

---

## 🛠️ The Tech Toolkit

*   **Core Language:** Python 3.8+
*   **Data Manipulation:** Pandas (for reading CSV, cleaning, transforming, feature engineering)
*   **Interactive Visualization:** Plotly Express (for histograms, line charts, scatter plots, bar charts)
*   **Environment:** Jupyter Notebook (`solution.ipynb`)

---

## 🗺️ The Data Landscape: `fitness_data.csv`

Our dataset captures daily metrics crucial for understanding fitness and well-being. Key columns include:

*   `date`: The day of recording.
*   `steps`: Daily step count.
*   `weight_kg`: Body weight in kilograms.
*   `resting_heart_rate`: Beats per minute at rest.
*   `sleep_hours`: Total sleep duration.
*   `active_minutes`: Total minutes of physical activity.
*   `total_calories_burned`: Daily energy expenditure.
*   `fat_burn_minutes`, `cardio_minutes`, `peak_minutes`: Time spent in different heart rate zones.
*   `workout_type`: Type of exercise (Running, Strength Training, Yoga, HIIT, Rest).
*   `workout_duration_minutes`: Length of the workout session.
*   `workout_calories`: Calories burned during the workout.
*   `workout_avg_hr`, `workout_max_hr`: Average and maximum heart rate during workouts.

*(See the `Data Dictionary` in `solution.ipynb` for full details)*

---

## 🔬 The Analysis Journey: From CSV to Insights

We followed a structured approach to explore the data (`solution.ipynb` has the full code!):

1.  **Loading & Initial Inspection:**
    *   Read the `fitness_data.csv` into a Pandas DataFrame (`pd.read_csv`).
    *   Performed initial checks: `.head()`, `.isnull().sum()` (found 6 rows with missing data, likely incomplete entries), `.describe()` for summary stats, `.dtypes` to verify column types.

2.  **Data Cleaning & Transformation:**
    *   Converted the `date` column to datetime objects (`pd.to_datetime`) for time-series analysis.
    *   Renamed columns for clarity (`weight` to `weight_kg`, `workout_duration` to `workout_duration_minutes`) using `.rename()`.

3.  **✨ Feature Engineering - Adding Context:**
    *   Calculated weight in pounds (`weight_lbs`) for easier interpretation (`weight_kg * 2.20462`).
    *   Extracted the `day_of_week` from the date (`.dt.day_name()`).
    *   Created a boolean `is_weekend` flag (`.isin(['Saturday', 'Sunday'])`).
    *   Engineered `sleep_debt` by comparing `sleep_hours` to a target (e.g., 7.5 hours).
    *   Calculated `cumulative_sleep_debt` using `.cumsum()` to track long-term sleep trends.


4.  **📊 Exploratory Visualization (using Plotly Express):**
    *   **Single Variable Trends:**
        *   Histograms (`px.histogram`) for `steps` and `total_calories_burned` distribution.
        *   Line charts (`px.line`) for `steps`, `total_calories_burned`, and `weight_kg`/`weight_lbs` over time (`date` as x-axis). Added markers (`mode='markers'`) for weekends on the steps chart.
        *   Multi-line chart for `sleep_hours`, `sleep_debt`, and `cumulative_sleep_debt` over time.
        *   Bar chart (`px.bar`) showing average `sleep_hours` grouped by `day_of_week`.
    *   **Multi-Variable Relationships:**
        *   Scatter plot (`px.scatter`) comparing `steps` vs `total_calories_burned`, including an OLS trendline (`trendline="ols"`).
        *   Scatter plot analyzing workouts: `workout_avg_hr` vs `workout_calories`, colored by `workout_type`, with point size representing `workout_duration_minutes`. Hover data shows `fat_burn_minutes`.

---

## 💡 Eureka! Key Insights Visualized

The visualizations revealed interesting patterns:

1.  **Activity Peaks & Valleys:**
    *   The `steps` line chart shows significant daily variation, often exceeding 10,000 but sometimes dipping below 5,000. Weekend activity isn't consistently higher or lower, suggesting a varied routine.
    *   `Total_calories_burned` closely mirrors `steps`, indicating steps are a primary driver of daily calorie expenditure in this dataset.
    
    ![image](https://github.com/user-attachments/assets/b309359e-2a69-4539-9299-4bba7b4399b6)

    ![image](https://github.com/user-attachments/assets/33914cf0-bb3e-4603-989d-364400ddfac3)

    ![image](https://github.com/user-attachments/assets/ae8dc23d-bab3-4f6f-a0de-d0a5863caf77)

1.  **The Sleep Debt Saga:**
    *   The multi-line sleep chart vividly shows periods of accumulating sleep debt (negative `cumulative_sleep_debt`) followed by recovery periods. Consistently hitting the 7.5-hour target seems challenging.
    *   Average sleep seems slightly higher on weekends (Saturday/Sunday), potentially indicating catch-up sleep, though daily variations exist.
    
    ![image](https://github.com/user-attachments/assets/0c46fa69-28b1-4fae-9e00-bbba44e67312)

2.  **Workout Effectiveness:**
    *   The workout scatter plot clearly differentiates workout types. `Running` and `HIIT` generally show higher average heart rates and calorie burn rates (calories per minute) compared to `Strength Training` and especially `Yoga`.
    *   `Strength Training` sessions vary greatly in duration and calorie burn, likely depending on the specific routine. `Yoga` shows lower intensity (average HR) and calorie burn.
    *   Points representing 'Rest' days cluster at (0,0) for workout metrics, as expected.
    
    ![image](https://github.com/user-attachments/assets/76b47ece-f07c-493b-8cf2-89d50fc582f5)

3.  **Weight Trend:**
    *   The weight line chart (visualized in kg and lbs) shows fluctuations but suggests a general trend over the 185 days (e.g., slight upward trend in the sample). Daily variations are normal.

    ![image](https://github.com/user-attachments/assets/cdcadd0a-d583-43d0-8277-92bd2f00d46c)

---

## ✅ Why This Matters: The Power of Personal Data Analysis

Analyzing your own fitness data (or a sample like this) is incredibly empowering:

*   **Identify Habits:** Spot patterns you might not notice day-to-day (e.g., "I consistently sleep less on Thursdays").
*   **Validate Feelings:** See if feeling tired correlates with measurable sleep debt or low activity.
*   **Optimize Routine:** Understand which workouts are most effective for calorie burn or hitting specific heart rate zones.
*   **Track Progress:** Visualize trends towards goals (weight loss/gain, increased steps, better sleep).
*   **Learn Core Data Skills:** Provides practical application of Pandas and visualization libraries – essential for any data professional.

---

*Day 77 of #100DaysOfDataScience complete! This project demonstrates how Python, Pandas, and Plotly can turn personal fitness tracking data into meaningful insights and compelling visualizations. Keep tracking, keep analyzing! - Vatsal Parikh*
