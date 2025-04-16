# Day 75. 100 Days of Data Science Challenge - 04/16/2025

# 📊 SQL Fundamentals: NYC Airbnb Data Exploration 🗽

[![SQL](https://img.shields.io/badge/Language-SQL-blue?style=flat-square&logo=postgresql)](https://www.postgresql.org/)
[![Dataset](https://img.shields.io/badge/Dataset-NYC_Airbnb-orange?style=flat-square)](https://github.com/vatsalparikh07/100-days-of-data-science-challenge/tree/main/Dayy%2075.%20SQL%20Fundamentals%3A%20NYC%20Airbnb%20Data%20Exploration/airbnb_data.csv) <!-- Update this link! -->
[![Day 75](https://img.shields.io/badge/100DaysOfDataScience-Day_74-brightgreen?style=flat-square)](https://www.100daysofcode.com/) <!-- Update Day Number if needed -->


## 🎯 Project Goal: Mastering SQL Basics with Real-World Data

Welcome to a hands-on exploration designed for **SQL beginners**! This project demystifies the fundamental language of databases – **SQL (Structured Query Language)** – by applying it to a real-world dataset: **NYC Airbnb listings**. Forget abstract examples; we're diving into actual data to answer practical questions and build essential data analysis skills.

**Why this project?**
*   **Foundational Skill Building:** SQL is non-negotiable for almost any data role. This project builds that crucial base.
*   **Practical Application:** Learn commands like `SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`, and aggregate functions (`AVG`, `MAX`, `COUNT`) by solving realistic problems.
*   **Insight Generation:** Go beyond just running queries – understand *what* the results tell you about the NYC Airbnb market.
*   **Confidence Booster:** Move from theory to practice and gain confidence in querying databases.

---

## 🗺️ The Data Landscape: NYC Airbnb Listings (`airbnb_data.csv`)

Our dataset is a snapshot of Airbnb listings in New York City, containing rich information we can explore. Key columns include:

*   `listing_id`: Unique identifier for each listing.
*   `description`: Host's description of the property.
*   `neighbourhood_full`: Borough and specific neighborhood (e.g., "Brooklyn, Flatlands").
*   `room_type`: 'Private Room', 'Entire place', or 'Shared room'.
*   `price`: The nightly cost in USD.
*   `rating`: Guest rating (0-5).
*   `number_of_reviews`, `reviews_per_month`: Indicators of popularity and activity.
*   `availability_365`: Number of days the listing is available per year.
*   `number_of_stays`: Estimated total stays (often derived from reviews).

---

## 🤔 The Analytical Quest: Answering Key Business Questions

We used SQL to interrogate the data and find answers to specific questions, simulating common data analysis tasks:

1.  **Popularity Contest:** Identify the Top 10 most reviewed `Private Room` listings.
2.  **Budget Finds:** Discover the 10 cheapest `Private Room` listings available.
3.  **Availability Snapshot:** Calculate the average annual availability (in days) for `Private Room`s.
4.  **Elusive Listings:** Find listings with low availability (<30 days/year) AND few reviews (<10). Why might these exist?
5.  **Review Volume by Type:** Determine which `room_type` gathers the most reviews on average.
6.  **"Always Open" Analysis:** Analyze the count, average price, and average availability for listings available >250 days/year, segmented by `room_type`.
7.  **(Bonus) Luxury Tier:** Find the maximum price for each `room_type` among frequently available listings (>100 days/year).

---

## 🛠️ The Analyst's Toolkit: Core SQL Commands Used

These fundamental SQL commands were our primary tools for exploration:

*   **`SELECT`**: Specifies the columns to retrieve (e.g., `SELECT price, rating` or `SELECT *` for all).
*   **`FROM`**: Indicates the source table (e.g., `FROM 'airbnb_data.csv'`).
*   **`WHERE`**: Filters rows based on conditions (e.g., `WHERE room_type == 'Entire place' AND price < 100`). Used `==` for equality and `<`/`>` for comparison.
*   **`ORDER BY`**: Sorts the output rows based on column values (`ASC` for ascending, `DESC` for descending).
*   **`LIMIT`**: Restricts the query to return only the top N rows.
*   **`GROUP BY`**: Groups rows with identical values in specified columns, enabling aggregate calculations on each group.
*   **`AVG()`, `MAX()`, `COUNT()`**: Aggregate functions used with `GROUP BY` to calculate the average, maximum, or count within each group.
*   **`AS`**: Assigns temporary, readable aliases to columns (e.g., `AVG(price) AS average_daily_rate`).
*   **`--`**: Used for adding comments to explain the SQL code.

---

## 💡 Unearthing Insights: What the Data Revealed

Here are some key findings extracted using the SQL queries (See `solution.pdf` for exact queries and full results):

### 🥇 Most Talked About: Top Reviewed Private Rooms (Q1)
*   **Technique:** Used `WHERE room_type == 'Private Room'`, `ORDER BY number_of_reviews DESC`, `LIMIT 10`.
*   **Insight:** This quickly highlights listings with high engagement, potentially indicating popular locations, great hosts, or high turnover. Listings like `16276632` (Cozy Room near LGA) and `166172` (LG Private Room in Bushwick) topped this list in the sample, suggesting high traffic areas or value propositions resonate strongly.

### 💰 Finding Value: Cheapest Private Rooms (Q2)
*   **Technique:** Used `WHERE room_type == 'Private Room'`, `ORDER BY price ASC`, `LIMIT 10`.
*   **Insight:** Identified the absolute lowest price points (some potentially as low as $10-$30 in the sample!). This is useful for budget analysis but also flags potential outliers or listings with unique circumstances (e.g., very basic amenities, specific guest requirements like 'FEMALE ONLY').

### 📅 Availability Patterns: Average & Extremes (Q3 & Q6)
*   **Technique:** `AVG(availability_365)` with `WHERE` for Q3; `GROUP BY room_type`, `AVG()`, `COUNT()` with `WHERE availability_365 > 250` for Q6.
*   **Insight (Q3):** The average `Private Room` was available around **118 days** a year, indicating many aren't full-time rentals.
*   **Insight (Q6):** Listings available almost year-round (>250 days) show clear price segmentation: 'Entire place' averages ~$240, 'Private Room' ~$90, and 'Shared room' ~$51. 'Shared rooms' in this high-availability group are open the most days on average (~348), suggesting a specific business model targeting constant occupancy at a lower price point.

| Room Type    | Avg Availability (>250 Days) | Listings Count (>250 Days) | Average Price (>250 Days) |
| :----------- | :--------------------------- | :------------------------- | :------------------------ |
| Entire place | ~314 days                    | ~842                       | ~$239.59                  |
| Private Room | ~327 days                    | ~830                       | ~$90.25                   |
| Shared room  | ~348 days                    | ~67                        | ~$51.49                   |
*(Conceptual results based on Q6 analysis)*

### ❓ The Mystery Listings: Low Availability & Few Reviews (Q4)
*   **Technique:** `WHERE availability_365 < 30 AND number_of_reviews < 10`.
*   **Insight:** Found **2,245 listings** fitting this profile. These could represent various scenarios: hosts only renting sporadically, new listings yet to gain traction, listings primarily used by the host, or potentially inactive listings. It highlights a segment that operates very differently from high-volume rentals.

### 🏆 Price Ceilings: Most Expensive (Bonus)
*   **Technique:** `MAX(price)` with `WHERE availability_365 > 100`, `GROUP BY room_type`.
*   **Insight:** Showcased the extreme upper end of the market, with 'Entire place' options reaching prices like **$8000/night**, vastly exceeding the max for 'Private Room' (~$1002) or 'Shared room' (~$165) among frequently available listings.

---

## ✅ Why This Matters: SQL is Your Data Compass

Think of SQL as the fundamental way to navigate the vast oceans of data stored in databases. Mastering these basic commands is critical because they allow you to:

*   **Precisely Target Data:** Pull exactly the information needed, avoiding overwhelming data dumps.
*   **Perform Initial Analysis:** Quickly understand distributions, find extremes, and validate assumptions.
*   **Aggregate for Insights:** Summarize vast amounts of data into meaningful metrics (averages, counts, maximums).
*   **Lay the Groundwork:** Prepare clean, relevant data subsets for more advanced analysis in tools like Python, R, or Tableau.

This project solidifies these essential first steps.

---

*Day 75 of #100DaysOfDataScience is in the books! This project provided practical, hands-on experience with fundamental SQL queries, turning raw Airbnb data into understandable insights. Happy querying! - Vatsal Parikh*
