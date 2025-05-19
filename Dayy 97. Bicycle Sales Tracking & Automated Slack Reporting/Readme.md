# Bicycle Sales Tracking & Automated Slack Reporting 🚲📈

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-yellowgreen?style=flat-square)](https://pandas.pydata.org/)
[![Slack SDK](https://img.shields.io/badge/Slack-SDK-blue?logo=slack&style=flat-square)](https://slack.dev/python-slack-sdk/)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_97-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

![image](https://github.com/user-attachments/assets/6921182c-580b-4cb3-ad69-d66df768394d)
*Fig 1: Monthly bicycle sales trend from January 2016 to April 2018.*

## 🎯 Project Goal: From Raw Sales Data to Automated Business Insights

Welcome to Day 97 of my #100DaysOfDataScience challenge! This project focuses on analyzing bicycle sales data spanning multiple years and automating the delivery of key sales insights directly to a Slack channel.

**Objectives:**

- Aggregate and analyze historical sales data to uncover monthly trends and top-performing sales staff.
- Automate the generation and posting of a concise, formatted sales update message to a Slack workspace.
- Demonstrate integration of data analysis with communication tools for real-time business reporting.

---

## 🛠️ Tech Stack & Tools

- **Python 3.8+**: Core programming language.
- **Pandas**: Data manipulation and aggregation.
- **Slack SDK for Python**: Posting messages to Slack channels programmatically.
- **Babel**: Formatting currency values for human-friendly display.
- **Data Source**: Historical bicycle sales data joined from orders and order items tables, spanning 2016 to 2018.

---

## 📊 Data Analysis Workflow

1. **Data Loading & Preparation:**
    - Joined orders and order items datasets to create a comprehensive sales DataFrame.
    - Calculated total sales per order item as `quantity * list_price * (1 - discount)`.
    - Aggregated total sales by month to observe trends over time.

2. **Monthly Sales Trend Visualization:**
    - Generated a time series of total monthly sales.
    - Observed seasonal fluctuations and growth patterns from 2016 through early 2018.

3. **Top Sales Staff Identification:**
    - Grouped sales data by staff member.
    - Calculated total sales attributed to each staff.
    - Identified top three performers for April 2018.

---

## 🤖 Slack Integration & Automated Reporting

![image](https://github.com/user-attachments/assets/a4c41e16-31e5-421e-8de1-73ccd106258a)

- Utilized the **Slack WebClient** from the `slack_sdk` package to authenticate and send messages.
- Crafted a clear, engaging sales update message including:
    - Total sales for the most recent month.
    - A ranked list of the top three sales staff with their individual sales figures formatted as USD currency.
    - A clickable link directing recipients to the data workspace for deeper exploration.
- Posted the message to a designated Slack channel (`sales-tracking`), enabling real-time team awareness.
  
---

## 📈 Key Insights

- **Total Sales:** Approximately $7.69 million in bicycle sales over the analyzed period.
- **Monthly Trends:** Notable peaks and troughs in sales volume, with a strong seasonal pattern.
- **Top Performers:** Staff members like Venita Daniel and Genna Serrano led sales in April 2018, driving significant revenue.

---

*Day 97 of #100DaysOfDataScience highlights the synergy between data analytics and communication platforms, showcasing how Python can empower teams with timely, actionable insights. - Vatsal Parikh*
