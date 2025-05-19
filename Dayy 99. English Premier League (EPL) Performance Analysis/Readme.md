# English Premier League (EPL) Performance Analysis (2000-2022) ⚽

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-yellowgreen?style=flat-square&logo=pandas)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-orange?style=flat-square&logo=seaborn)](https://seaborn.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-blueviolet?style=flat-square)](https://matplotlib.org/)
[![Dataset](https://img.shields.io/badge/Dataset-EPL_2000--2022-lightgrey?style=flat-square)](./EPL.csv)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_99-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Unveiling Trends in 22 Seasons of English Premier League Football

Welcome to Day 99 of my #100DaysOfDataScience challenge! This project dives into **22 seasons of English Premier League (EPL) data (2000-2001 to 2021-2022)** to analyze team performance, qualification thresholds for European competitions, relegation battles, and the strong correlation between points and goal difference.

Using **Python (Pandas, Seaborn, Matplotlib)**, we aim to:
1.  **Load & Clean:** Ingest and prepare the EPL dataset (`EPL.csv`), focusing on key performance indicators (Position, Points, Goals For, Goal Difference) and season outcomes (Qualification/Relegation).
2.  **Categorical Data Simplification:** Streamline the verbose 'Qualification or relegation' column into concise categories (Champions League, Europa, Relegated, -) for easier analysis.
3.  **Performance Threshold Analysis:** Determine the typical points (Pts) and goal difference (GD) required to qualify for Champions League and Europa League, and the typical points of relegated teams across seasons.
4.  **Trend Visualization:** Create line plots to visualize how the points tally for EPL winners and the points threshold for relegation (18th position) have evolved over the 22 seasons.
5.  **Years in EPL vs. European Qualification:** Analyze and visualize the number of seasons each team has spent in the EPL versus the number of times they've qualified for European competitions.
6.  **Team-Specific Performance (Chelsea):** Focus on Chelsea to track their seasonal performance (Goal Difference and Points) and observe correlations.
7.  **Correlation Exploration (Global):** Investigate the overall relationship between average points achieved and average goal difference across all teams.

This project showcases how data analysis can reveal long-term trends, performance benchmarks, and interesting patterns in one of the world's most competitive football leagues.

---

## ✨ Key Features & Concepts Mastered

*   **Data Ingestion & Selection:** Read CSV data into Pandas DataFrame (`pd.read_csv`) and selected relevant columns for analysis (`epl_condensed`).
*   **Data Cleaning & Transformation:**
    *   Renamed columns for brevity (`.rename(columns=...)`) .
    *   Applied a custom function (`update_result`) using `.apply()` to transform the 'Result' (formerly 'Qualification or relegation') column into simplified categories. This involved string searching (`'Champions League' in result`) and conditional logic.
*   **Exploratory Data Analysis (EDA) with Pandas:**
    *   Filtering DataFrames based on conditions (e.g., `epl_condensed[epl_condensed.Result == 'Champions League']`) .
    *   **Grouping & Aggregation:** Used `.groupby('Season').agg({'Pos':'max', 'Pts':'min', 'GD':'min'})` to find seasonal thresholds for Champions League/Europa League qualification. Used `.groupby('Team').agg({'GD':'mean', 'Pts':'mean'})` for team-level average stats .
    *   Calculating value counts (`.value_counts()`) for categorical data (e.g., number of seasons each team in EPL, number of European qualifications).
*   **Time Series Visualization (Seaborn & Matplotlib):**
    *   Created **line plots** (`sns.lineplot`) to visualize trends in points for EPL winners and the 18th-placed (relegation zone) teams over the 22 seasons. Customized with markers, colors, titles, and rotated x-axis labels for readability .
    *   Used `ax.twinx()` to create a dual-axis line plot for Chelsea, comparing Goal Difference and Points on the same chart but with independent y-axes.
*   **Categorical & Relational Plotting:**
    *   **Bar Charts** (`sns.barplot`) to display the number of years each team has been in the EPL and the number of years they've qualified for European competitions.
    *   **Scatter Plot** (`sns.scatterplot`) to visualize the relationship between average team Goal Difference ('GD') and average team Points ('Pts') across all seasons.
*   **Statistical Insights:**
    *   Calculated the mean difference in points between winners and relegated teams.
    *   Calculated the correlation coefficient between winners' points and relegated teams' points (`.corr()`), and between average team GD and average team Pts.

---

## 🛠️ Tech Stack: The Analyst's Python Toolkit

*   **Core Language:** Python 3.8+
*   **Data Manipulation & Analysis:** Pandas
*   **Static Visualization:** Matplotlib (`pyplot`), Seaborn
*   **Development Environment:** Jupyter Notebook
*   **Display Utilities:** `IPython.display` (`display`, `Markdown`)

---

## 🗺️ The Analytical Workflow: From League Tables to Performance Insights

This project followed a structured approach:

1.  **Setup & Data Loading (`Task 0 & 1`):**
    *   Imported `pandas`, `seaborn`, `matplotlib.pyplot`, and `IPython.display`.
    *   Loaded `EPL.csv` into `epl` DataFrame and created `epl_condensed` with selected columns: 'Season', 'Team', 'Pos', 'Pts', 'GF', 'GD', 'Qualification or relegation'.

2.  **Cleaning the Outcome Column (`Task 2`):**
    *   Defined `update_result(result)` function to map detailed 'Qualification or relegation' strings to simpler categories: 'Champions League', 'Europa', 'Relegated', or '-'.
    *   Renamed the column to 'Result' and applied the `update_result` function.
    *   Verified with `epl_condensed['Result'].value_counts()`.

3.  **Analyzing Qualification Thresholds (`Task 3 & 4`):**
    *   Filtered for teams qualifying for 'Champions League' (`cl_qual`) and 'Europa' (`eu_qual`).
    *   Grouped by 'Season' and aggregated to find the maximum position, minimum points, and minimum goal difference that secured qualification for each competition in each season.
    *   Printed these stats, noting that typically 70+ points for CL and 55+ for Europa are needed, but with outliers due to cup competitions.

4.  **Visualizing Winners vs. Relegation Trends (`Task 5`):**
    *   Filtered `epl_condensed` for EPL Winners (`Pos == 1`) and the 18th-placed teams (`Pos == 18`).
    *   Plotted their 'Pts' over 'Season' on a single line chart for comparison.
    *   Calculated mean points difference (~54.3 pts) and a weak negative correlation (`-0.31`) between these two series.

![image](https://github.com/user-attachments/assets/13deeca8-12ae-47d5-b9ec-a477ac8feddc)
*Fig 1: Line plot comparing the points tally of EPL winners (purple) and the 18th-placed teams (pink) from 2000-01 to 2021-22.*

5.  **EPL Longevity vs. European Success (`Task 6`):**
    *   Calculated `team_counts` (years each team in EPL) and `euro_year_counts` (years each team qualified for Europe).
    *   Created two separate bar charts to visualize these counts, highlighting teams with consistent EPL presence and European qualification success.

![image](https://github.com/user-attachments/assets/9e32d977-c610-4ba7-a592-4ff212451cda)
*Fig 2: Bar chart showing the number of seasons each team spent in the EPL (2000-2022).*

![image](https://github.com/user-attachments/assets/633c67f2-f752-4dd1-92c3-65cc7757af9c)
*Fig 3: Bar chart showing the number of seasons each team qualified for European competitions.*

6.  **Team Deep Dive: Chelsea's GD vs. Pts (`Task 7`):**
    *   Filtered data for 'Chelsea'.
    *   Created a dual-axis line plot: 'GD' on the primary y-axis and 'Pts' on the secondary y-axis, both plotted against 'Season'.
    *   Observed a strong visual similarity in the shapes of the two lines, suggesting a correlation. Highlighted the 2015-16 season as an outlier where Chelsea didn't qualify for Europe.

![image](https://github.com/user-attachments/assets/8384f83c-1aa4-4be7-8c9a-3bdd947505a3)
*Fig 4: Dual-axis line plot showing Chelsea's Goal Difference (GD) and Points (Pts) per season, indicating a strong correlation.*

7.  **Global Correlation: Pts vs. GD (`Task 8`):**
    *   Grouped the original `epl` data by 'Team' and calculated the mean 'GD' and mean 'Pts' for each team over their EPL tenure.
    *   Created a scatter plot of mean 'GD' vs. mean 'Pts'.
    *   Calculated and printed a very strong positive correlation coefficient of **0.99** between these two average metrics.

![image](https://github.com/user-attachments/assets/fa6017db-0165-4ab1-b001-7ca1cd5ab27a)
*Fig 5: Scatter plot showing a very strong positive correlation (0.99) between average team Goal Difference and average team Points across all seasons.*

---

## 💡 Key Insights & Observations

*   **Strong Pts-GD Correlation:** The most striking finding is the near-perfect correlation (0.99) between a team's average Goal Difference and their average Points per season. This underscores GD as a powerful indicator of overall team strength and league performance.
*   **Qualification Nuances:** While points thresholds exist, European qualification (especially Europa League) can be significantly impacted by domestic cup winners, leading to outliers in terms of league position or points needed.
*   **League Dynamics:** The ~54-point average gap between winners and the 18th position highlights the competitive spread in the EPL. The weak negative correlation between winner's points and relegation points suggests these two ends of the table behave somewhat independently, though higher overall league quality might slightly raise both ends.
*   **Team Consistency (and Outliers):** Visualizing individual team performance (like Chelsea's) quickly highlights periods of dominance, decline, and specific outlier seasons (e.g., Chelsea's 2015-16).
*   **EPL Stalwarts:** Bar charts of EPL years reveal a core group of teams with consistent presence (Manchester United, Arsenal, Chelsea, Liverpool, Everton, Tottenham) and also teams that have fluctuated more.

---

## ✅ Why This Matters: Data Storytelling with Python

*   **Historical Perspective:** Provides a data-driven look at long-term performance standards and competitive dynamics in a major sports league.
*   **Analytical Power of Pandas:** Demonstrates how Pandas can be used to effectively clean, filter, group, and aggregate sports data for meaningful analysis.
*   **Visual Communication:** Seaborn and Matplotlib enable clear visualization of trends, comparisons, and relationships that might be hidden in raw tables.
*   **Foundation for Advanced Analysis:** This type of exploratory analysis is a crucial first step before more complex modeling (e.g., predicting match outcomes, season simulations).

---

*Day 99 of #100DaysOfDataScience involved a deep dive into 22 seasons of English Premier League data, using Python's data science stack to uncover trends, analyze team performance, and visualize the dynamics of qualification and relegation. Almost at the finish line! - Vatsal Parikh*
