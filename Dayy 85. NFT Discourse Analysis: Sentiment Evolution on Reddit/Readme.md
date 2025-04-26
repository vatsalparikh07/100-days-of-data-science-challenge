# NFT Discourse Analysis: Sentiment Evolution on Reddit 💬📊

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![PRAW](https://img.shields.io/badge/PRAW-Reddit_API-yellowgreen?style=flat-square)](https://praw.readthedocs.io/)
[![VADER](https://img.shields.io/badge/VADER-Sentiment_Analysis-orange?style=flat-square)](https://github.com/cjhutto/vaderSentiment)
[![Visualization](https://img.shields.io/badge/Viz-Matplotlib%2C_Seaborn-blueviolet?style=flat-square)](https://matplotlib.org/)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_85-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Charting the Emotional Rollercoaster of NFTs on Reddit

Welcome to Day 85 of my #100DaysOfDataScience challenge! Non-Fungible Tokens (NFTs) have been a whirlwind – from astronomical sales like Beeple's $69M artwork in March 2021 to a dramatic market cool-down. How did the public *feel* about this journey? This project dives into the heart of the conversation, analyzing **Reddit discussions** from key moments to track the **evolution of public sentiment**.

Using **Natural Language Processing (NLP)** techniques, specifically **VADER for sentiment analysis**, we:
1.  **Collected Targeted Data:** Gathered over 690 relevant comments from r/NFT and r/CryptoCurrency around four pivotal timeframes using **PRAW**.
2.  **Preprocessed for Quality:** Cleaned the text, filtered by language (`langdetect`), and removed noise.
3.  **Quantified Emotion:** Applied the VADER model to score each comment's sentiment from highly negative (-1) to highly positive (+1) and categorized them.
4.  **Visualized the Narrative:** Created insightful plots using **Matplotlib** and **Seaborn** to illustrate how sentiment shifted during market highs and lows.

**Why track sentiment?** Online platforms like Reddit are crucibles where narratives about new technologies are forged. Understanding these sentiment dynamics provides a powerful lens into public perception, market psychology, and the societal impact of disruptive innovations like NFTs.

---

## ✨ Key Features & Concepts Mastered

*   **Event-Driven Data Collection:** Used **PRAW** to precisely target Reddit comments around significant NFT market events:
    *   Pre-/Post-Beeple's $69M Sale (Feb/Apr 2021).
    *   Pre-/Post-Market Crash (Feb/Apr 2022).
*   **Robust Text Preprocessing:** Implemented essential cleaning steps:
    *   Exclusion of deleted/removed authors.
    *   **Language Filtering:** Ensured analysis focused on English comments using `langdetect`.
    *   Removal of non-ASCII characters for cleaner text input.
*   **Rule-Based Sentiment Analysis (VADER):** Leveraged **VADER (Valence Aware Dictionary and sEntiment Reasoner)**, optimized for social media nuances, to assign a compound sentiment score (`-1` to `+1`) to each comment.
*   **Sentiment Categorization:** Defined clear thresholds to classify scores into five distinct categories: *Very Negative* (`<-0.5`), *Somewhat Negative* (`-0.5` to `-0.1`), *Neutral* (`-0.1` to `0.1`), *Somewhat Positive* (`0.1` to `0.5`), *Very Positive* (`>0.5`).
*   **Temporal Sentiment Tracking:** Analyzed sentiment distribution shifts *across the four key event timeframes* and calculated *monthly percentage changes* in positive and negative sentiments to highlight trends over time.
*   **Effective Data Visualization:** Utilized **Matplotlib** and **Seaborn** to communicate findings clearly:
    *   `boxplot` & `histplot`: Showed the overall skew and concentration of sentiment scores.
    *   `countplot` & Percentage Bar Charts: Displayed the distribution across the five sentiment categories.
    *   Stacked Bar Charts & Line Plots: Visualized the crucial changes in sentiment percentages linked to market events.

![image](https://github.com/user-attachments/assets/ac4d0407-becf-4364-a1f5-c734abb38f63)
*Fig 1: Subset of Data after Cleaning and Sentiment Labelling*

---

## 🛠️ Tech Stack: The Sentiment Analyst's Toolkit

*   **Core Language:** Python 3.8+
*   **Reddit API Interaction:** PRAW (Python Reddit API Wrapper)
*   **Data Manipulation:** Pandas (DataFrames, CSV I/O, concatenation, grouping)
*   **Sentiment Analysis Engine:** VADER (`vaderSentiment.SentimentIntensityAnalyzer`)
*   **Natural Language Utilities:** `langdetect` (for language filtering)
*   **Data Visualization:** Matplotlib (`pyplot`), Seaborn
*   **Development Environment:** Jupyter Notebook (`solution.ipynb`)
*   **Supporting:** `datetime`, `timedelta`, `numpy`, `tabulate`

---

## 🗺️ The Analytical Workflow: From Reddit Threads to Sentiment Trends

Our process involved several key stages, meticulously documented in `solution.ipynb` and the research paper:

1.  **Targeted Data Harvesting (PRAW):**
    *   Defined specific URLs for high-engagement posts in r/NFT and r/CryptoCurrency related to the four key periods.
    *   Used PRAW's `reddit.submission(url=...)` and iterated through `submission.comments` (limiting to top comments) to extract `Author`, `Text`, `Date` (converted from UTC timestamp), `Score`, `Author_ID`, and `Subreddit`.
    *   Saved raw data into four event-specific CSV files.

2.  **Consolidation & Cleansing (Pandas):**
    *   Read the four CSVs into Pandas DataFrames.
    *   Concatenated them into a single master DataFrame (`merged_df`) using `pd.concat`.
    *   Applied crucial cleaning: Filtered out rows where `Author` was '[deleted]', used `langdetect` within a `try-except` block to keep only 'en' comments, and removed non-ASCII characters from the `Text` column. Saved as `nft_reddit_data.csv`.

3.  **Sentiment Scoring (VADER):**
    *   Initialized the `SentimentIntensityAnalyzer`.
    *   Applied the `polarity_scores` method to the cleaned `Text` of each comment, extracting the `compound` score and storing it in a new `Sentiment_Score` column.
    *   Created a `Sentiment_Category` column by applying the defined thresholds (Very Negative to Very Positive) to the `Sentiment_Score`.

4.  **Temporal & Event-Based Grouping (Pandas):**
    *   Converted the 'Date' column to datetime objects.
    *   Grouped the DataFrame by the four distinct event periods to analyze sentiment distribution changes.
    *   Grouped the DataFrame by month (`df['Date'].dt.to_period('M')`) to calculate monthly percentage changes in positive (`Score > 0.1`) and negative (`Score < -0.1`) sentiments.

5.  **Visual Storytelling (Matplotlib & Seaborn):**
    *   **Overall Distribution (Fig 2):** Used `sns.boxplot` and `sns.histplot` on `Sentiment_Score` to show the central tendency (around neutral) and the positive skew.
    *   **Category Breakdown (Table 2 & Bar Charts):** Calculated value counts and percentages for `Sentiment_Category` and visualized them using bar plots, showing 'Very Positive' (34.3%) as the largest single category overall.
    *   **Event Comparison (Fig 3):** Created stacked bar charts showing the *percentage* distribution of sentiment categories for each of the four event periods. This visually highlights the shift from >60% positive during Beeple's Sale to rising negativity post-crash.
    *   **Temporal Trends (Fig 4 & 5):** Plotted the calculated monthly percentage changes for positive and negative sentiments using line plots (`sns.lineplot`), clearly showing the post-Beeple positive spike and the steady rise in negativity after the market crash.

---

## 💡 Unveiling the Narrative: Key Sentiment Shifts Visualized

The visualizations paint a clear picture of the NFT sentiment rollercoaster on Reddit:

*   **Sentiment Distribution (Figure 2 in Paper):** While many comments were neutral, the overall distribution leaned slightly positive, but with significant tails indicating strong opinions on both ends.

    ![Sentiment Distribution Chart](https://cdn.mathpix.com/cropped/2025_04_26_78b8780ca905cb2cac9ag-3.jpg?height=569&width=1571&top_left_y=1115&top_left_x=251)
    *Fig 2: Distribution of Sentiment Scores (Box Plot & Histogram)*

*   **Sentiment Across Events (Figure 3 in Paper):** This stacked bar chart is crucial. It shows the dramatic shift:
    *   **Beeple Sale Hype:** Over 60% Positive comments.
    *   **Market Peak:** Neutrality grows to ~30%, positivity dips slightly.
    *   **Market Crash:** Negativity (Somewhat + Very) jumps significantly (~27%).
    *   **Post Decline:** Negativity further solidifies as the dominant trend.
    
    ![Sentiment by Event Chart](https://cdn.mathpix.com/cropped/2025_04_26_78b8780ca905cb2cac9ag-4.jpg?height=872&width=1320&top_left_y=826&top_left_x=368)
    *Fig 3: Sentiment Category Percentage Distribution around Key Events*

*   **Temporal Sentiment Flow (Figures 4 & 5 in Paper):** The line plots confirm the event-based findings, illustrating:
    *   A sharp peak in positive sentiment percentage right after the Beeple sale (Fig 4).
    *   A steady, concerning rise in negative sentiment percentage following the market crash (Fig 5).
    
    ![Positive Sentiment Trend Chart](https://cdn.mathpix.com/cropped/2025_04_26_78b8780ca905cb2cac9ag-5.jpg?height=772&width=1571&top_left_y=254&top_left_x=251)
    *Fig 4: Percentage Change in Positive Sentiments Over Time*

    ![Negative Sentiment Trend Chart](https://cdn.mathpix.com/cropped/2025_04_26_78b8780ca905cb2cac9ag-5.jpg?height=775&width=1569&top_left_y=1217&top_left_x=249)
    *Fig 5: Percentage Change in Negative Sentiments Over Time*

---

## ✅ Significance & Why This Study Matters

*   **Market Psychology Mirror:** Demonstrates how public discourse on platforms like Reddit closely reflects and potentially influences volatile tech market trends.
*   **VADER's Strength:** Showcases the effectiveness of VADER for capturing sentiment nuances in informal social media text.
*   **Event-Based Analysis Power:** Highlights the value of segmenting analysis around key external events to understand their impact on public opinion.
*   **Quantifying Online Narratives:** Provides a data-driven method to move beyond anecdotal evidence when discussing public perception of technologies like NFTs.

---

*Day 85 of #100DaysOfDataScience successfully mapped the emotional landscape surrounding NFTs on Reddit, revealing how online sentiment ebbed and flowed with real-world market events. Understanding these dynamics is crucial in the age of rapid technological change! - Vatsal Parikh*
