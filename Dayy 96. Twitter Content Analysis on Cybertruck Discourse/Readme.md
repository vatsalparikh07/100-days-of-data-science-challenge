# 🚚💬 Cybertruck Discourse Shift: A Twitter Content Analysis 

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-yellowgreen?style=flat-square&logo=pandas)](https://pandas.pydata.org/)
[![Content Analysis](https://img.shields.io/badge/Method-Qualitative_Content_Analysis-orange?style=flat-square)](https://en.wikipedia.org/wiki/Content_analysis)
[![Visualization](https://img.shields.io/badge/Viz-Matplotlib%2C_Seaborn-blueviolet?style=flat-square)](https://matplotlib.org/)
[![Dataset](https://img.shields.io/badge/Dataset-Twitter_Cybertruck-lightgrey?style=flat-square)](./data.xlsx)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_96-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Understanding Public Perception Shifts from Concept to Production

Welcome to Day 96 of my #100DaysOfDataScience challenge! Today's project is a **qualitative content analysis** of Twitter discourse surrounding the **Tesla Cybertruck**. We investigate how public opinions and engagement patterns shifted from the initial prototype unveiling in **November 2019** to the official production model launch in **November/December 2023**. This research is particularly relevant given the significant changes in the Cybertruck's price, range, and specifications between these two milestones.

**The Mission:**
1.  **Collect & Curate:** Manually gather a targeted dataset of 50 tweets from Twitter (25 from 2019, 25 from 2023) based on keywords, hashtags, and minimum engagement, focusing on the two weeks post-event for each period.
2.  **Develop a Codebook:** Create mutually exclusive categories to classify tweet content (Positive Appreciation, Critical Feedback, Trolls/Humour/Memes, Negative Reactions).
3.  **Qualitative Coding:** Manually code each tweet according to the developed codebook.
4.  **Quantitative Analysis:** Analyze the frequency distribution of tweet categories and compare engagement metrics (Likes, Retweets, Replies) across categories and time periods.
5.  **Visualize Findings:** Use **Python (Pandas, Matplotlib, Seaborn)** to generate charts illustrating the shifts in discourse and engagement.

This study aims to fill a gap by specifically focusing on perception shifts from an automotive *concept announcement* to its *final production model*, using the Cybertruck as a compelling case study.

---

## ✨ Key Features & Research Concepts

*   **Longitudinal Comparative Analysis:** Directly compares Twitter discourse from two distinct, critical time points (2019 concept reveal vs. 2023 production launch).
*   **Qualitative Content Analysis Framework:**
    *   **Codebook Development:** Iteratively developed a robust 4-category codebook (Positive Appreciation, Critical Feedback, Trolls/Humour/Memes, Negative Reactions) with clear definitions and examples to ensure coding consistency.
    *   **Manual Coding:** Each of the 50 tweets was manually assigned to one of the four categories. Specific rules were applied for mutually exclusive categorization (e.g., critical feedback trumped positive sentiment if both present).
*   **Engagement Metrics Analysis:**
    *   Collected Likes, Retweets, Replies for each tweet.
    *   Calculated a composite "Engagement Score" (sum of Likes, Retweets, Replies). *Note: Views were only available for 2023 data and thus not used in the primary engagement score comparison between years*.
*   **Data Handling with Pandas:** Used Pandas to read data from Excel, aggregate engagement scores by category (`.groupby().sum()`), and prepare data for plotting.
*   **Visualization for Comparison:** Leveraged Matplotlib and Seaborn to create:
    *   Stacked bar charts comparing the *count* of tweets per category before and after launch.
    *   Stacked bar charts comparing the *total engagement score* (Likes + Retweets + Replies) per category for both 2019 and 2023.
*   **Focus on Public Perception Dynamics:** Investigated not just *what* was said, but *how much attention* different types of comments received, and how this changed over time.

---

## 🛠️ Tech Stack & Methodologies

*   **Core Data Handling & Analysis:** Python, Pandas
*   **Data Source:** Manually collected Twitter data
*   **Analytical Method:** Qualitative Content Analysis (manual coding based on a defined codebook) followed by quantitative frequency and engagement analysis.
*   **Visualization Tools:** Matplotlib, Seaborn
*   **Development Environment:** Jupyter Notebook (`Content_Analysis.ipynb`).

---

## 🗺️ The Research Workflow: From Tweets to Trends

The project followed these key steps:

1.  **Data Collection (Manual):**
    *   Searched Twitter using keywords ("Tesla Cybertruck", #cybertruck, etc.) for the two weeks following Nov 20, 2019, and Nov 30, 2023.
    *   Selected 25 representative tweets (original, retweets, replies) from each period, ensuring they met minimum engagement criteria.
    *   Recorded Tweet text, Username, Date, Engagement metrics (Likes, Retweets, Replies, Views for 2023) into the Excel file.

2.  **Codebook Development & Qualitative Coding:**
    *   Developed the 4-category codebook iteratively.
    *   Manually assigned each tweet to one category. This information is present in the 'Category' column of the Excel sheets.

3.  **Quantitative Analysis (Python & Pandas):**
    *   Loaded the "Before Launch" and "After Launch" sheets from `Supplemental Material.xlsx` into Pandas DataFrames.
    *   Calculated `value_counts()` for the 'Category' column in each DataFrame to get tweet frequencies per category.
    *   Used `groupby('Category')` and `sum()` on engagement columns (`Engagement(Likes)`, `Engagement(Retweets)`, `Engagement(Replies)`) to get total engagement per category for each period.

4.  **Visualization (Matplotlib & Seaborn):**
    *   **Tweet Category Distribution (Fig 1 in Paper):** Created a stacked bar chart showing the raw count of tweets in each category for 2019 ("Before Launch") and 2023 ("After Launch") combined onto single bars per category.
    *   **Engagement Score per Category (Fig 2 & 3 in Paper):** Generated separate stacked bar charts for 2019 and 2023, showing the total engagement score (Likes + Retweets + Replies) for each tweet category. The bars were stacked by Likes, Retweets, and Replies to show their individual contributions.

---

## 💡 Unveiling the Discourse Shift: Key Findings & Visualizations

The analysis revealed a notable shift in public sentiment and the nature of engagement:

*   **Shift in Tweet Categories (Figure 1 in Paper, adapted from Notebook Plot):**
    *   **2019 (Concept Reveal):** "Positive Appreciation" was the largest category (32% of tweets). "Negative Reactions" was the smallest (20%).
    *   **2023 (Production Launch):** "Negative Reactions" became the most prevalent category (32%). "Critical Feedback" decreased (from 28% to 20%). "Trolls/Humour/Memes" remained stable (20%).
    *   **Overall (Notebook Plot):** Combining both periods, "Positive Appreciation" still had the highest total count of tweets (15), followed by "Negative Reactions" (13), "Critical Feedback" (12), and "Trolls/Humour/Memes" (10).

![image](https://github.com/user-attachments/assets/1937f516-7d25-4f0c-a9b6-6e5dcef877fe)
    *Fig 1: Tweet Category Distribution Across Both Periods (Stacked)*

*   **Shift in Engagement Focus:**
    *   **2019 Engagement (Figure 2 in Paper):** "Trolls/Humour/Memes" generated the highest total engagement score (nearly 130,000), driven largely by Elon Musk's high-engagement tweet. "Positive Appreciation" was the second most engaged category. *Likes* were the primary driver of engagement scores across all categories.
![image](https://github.com/user-attachments/assets/7f9b4562-2090-4bf0-b41a-c0f0dfff2274)
    *Fig 2: Total Engagement Score by Category - 2019 (Pre-Launch)*

    *   **2023 Engagement (Figure 3 in Paper):** "Critical Feedback" (led by MKBHD's tweet) became the most engaged category (total score ~39,815), followed by "Positive Appreciation". This indicates a shift towards more critical discussions gaining traction after the production model details (price, specs) were revealed. Again, *Likes* dominated the engagement composition.
![image](https://github.com/user-attachments/assets/3a4ba20c-5f60-49a3-854c-176dfc609abe)

    *Fig 3: Total Engagement Score by Category - 2023 (Post-Launch)*

**Key Conclusions from the Paper:**
*   There was a discernible decrease in positive sentiment and constructive criticism from the 2019 concept reveal to the 2023 production launch.
*   Negative reactions increased as aspects like pricing and specifications deviated from original promises.
*   While humorous content was highly engaging initially, the discourse shifted towards more critical content gaining attention by 2023.
*   Despite a drop, "Positive Appreciation" still constituted a significant portion of tweets overall.
  
---

*Day 96 of #100DaysOfDataScience applied qualitative content analysis and Python-driven quantitative metrics to explore the fascinating shift in public discourse around the Tesla Cybertruck. A deep dive into how product evolution shapes perception! - Vatsal Parikh*
