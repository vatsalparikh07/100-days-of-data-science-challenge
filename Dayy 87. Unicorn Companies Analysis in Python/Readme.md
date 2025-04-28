# 🦄 Day 87 – Unicorn Companies Analysis in Python

Welcome to **Day 87** of my coding journey!  
In this project, I dive deep into the fascinating world of **Unicorn Companies** — privately held startups valued at over **$1 billion**. Using **Python**, **pandas**, and **visualization libraries**, I analyze company valuations, founding patterns, funding stages, industries, and global distributions to uncover valuable business insights.

---

## 📚 Project Summary

**Goal**:  
Analyze key trends in unicorn companies to understand:
- Which industries and regions are producing unicorns
- How valuations differ by industry and geography
- How funding stages impact valuation
- How startup timelines to unicorn status are shrinking

**Skills Practiced**:
- Data cleaning and wrangling
- Exploratory data analysis (EDA)
- Building insightful, attractive visualizations
- Business intelligence storytelling


---

## 🗃️ Dataset Overview

The dataset used is **`unicorn_companies.csv`**, containing information like:

| Column            | Description                             |
|-------------------|-----------------------------------------|
| `Company`         | Name of the unicorn startup             |
| `Valuation`       | Valuation (e.g., "$1B", "$12B")         |
| `Date Joined`     | When they became unicorns               |
| `Industry`        | Industry category (e.g., FinTech, AI)   |
| `City` / `Country`| Location of headquarters                |
| `Funding Stage`   | Investment stage when unicorn status was achieved |
| `Investors`       | Major investors in the company          |
| `Year Founded`    | Year company was established            |

**Dataset Size**: ~1,200 records  
**Latest Data**: Up to early 2024

---

## 🛠️ Tools and Technologies

| Tool             | Purpose                              |
|------------------|--------------------------------------|
| Python 3.11       | Main programming language            |
| pandas           | Data loading, cleaning, analysis     |
| matplotlib       | Plotting static charts               |
| seaborn          | Advanced statistical visualizations  |
| Jupyter Notebook | Interactive analysis and reporting  |

---

## 📊 Workflow Overview

### 1️⃣ Data Loading and Initial Exploration
- Import dataset into pandas
- Inspect column names, data types, and missing values
- Parse `Valuation` and `Date Joined` columns into usable formats

### 2️⃣ Data Cleaning
- Remove dollar signs (`$`) and "B"/"M" suffixes to convert `Valuation` into floats
- Parse dates into proper `datetime` format
- Handle missing values (e.g., unknown funding stages)

### 3️⃣ Exploratory Data Analysis (EDA)
- Top industries producing unicorns
- Top countries and cities by unicorn count
- Average valuation by industry
- Funding stage distribution among unicorns
- Time between founding year and unicorn year ("speed to unicorn")

### 4️⃣ Visualization
- Pie charts, bar charts, line plots
- Trend analysis over time (yearly unicorn growth)

---

## 🎯 Key Business Questions Answered

- 🏢 Which industries dominate the unicorn ecosystem?
- 🌍 Which countries and cities produce the most unicorns?
- ⏳ How fast are modern startups reaching $1B valuations?
- 💸 What funding stages are typical at the unicorn inflection point?
- 📈 Which industries command the highest valuations?

---

## 📈 Visual Insights

| Chart Title                         | Key Insight |
|-------------------------------------|-------------|
| **Top 10 Unicorn-Producing Countries** | U.S. and China together dominate the unicorn landscape |
| **Top 10 Unicorn-Producing Cities**    | San Francisco, New York, and Beijing lead |
| **Industries with Most Unicorns**       | FinTech, AI, SaaS industries are booming |
| **Funding Stages Distribution**         | Most unicorns achieve $1B value during Series C or D |
| **Average Valuation per Industry**     | E-commerce and AI startups fetch the highest average valuations |

![image](https://github.com/user-attachments/assets/2ebce8f6-adb2-417e-9536-33579438e7c0)

![newplot](https://github.com/user-attachments/assets/674abd42-9bc0-466b-beb0-087fa2cbf3fa)

![newplot2](https://github.com/user-attachments/assets/57670b0b-05b6-4359-870f-8105e3255d65)

![newplo3t](https://github.com/user-attachments/assets/5cf201a3-b128-436a-9c40-cbacbac2815e)

---

## 🌍 Geographic Highlights

- 🇺🇸 **United States** produces **over 50%** of all unicorns
- 🇨🇳 **China** remains a strong second
- 🇮🇳 **India** is emerging rapidly as a unicorn hub
- 🏙️ **San Francisco**, **New York**, **Beijing**, and **Bangalore** are critical startup hubs

![visualization](https://github.com/user-attachments/assets/9d46b0b3-62eb-4a6d-a857-7ceb06e7b630)

---

## 💰 Valuation and Funding Insights

- 🧠 **FinTech** has the most unicorns but **E-commerce** and **Artificial Intelligence** startups often reach the highest valuations.
- 🔥 **Series C and Series D** are the sweet spots for unicorn emergence.
- ⏱️ New startups founded **after 2010** are reaching unicorn status **faster** than older companies.

---

## 🧠 Final Takeaways

- The path to a $1B valuation is becoming **shorter and more aggressive**.
- **Location still matters**, but emerging regions are catching up quickly.
- **Funding stage** dynamics show a heavy tilt toward later-stage investments for unicorn births.
- **Industries driving innovation** (FinTech, AI, SaaS) dominate unicorn creation globally.
