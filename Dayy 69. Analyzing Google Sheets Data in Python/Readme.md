# Day 69. Analyzing Google Sheets Data in Python - 04/10/2025

# 📊 Google Analytics Data Exploration with Python & SQL

Welcome to a hands-on data analysis project built around **real-world Google Analytics 360 data**. This repo dives into user session data from the [Google Merchandise Store](https://shop.googlemerchandisestore.com/) on **August 1, 2017**, using a blend of **SQL**, **pandas**, and **plotly** to uncover insights into user behavior and digital performance.

---

## 📌 Project Summary

This project demonstrates how to:
- Connect and query Google Sheets using SQL
- Load and preprocess GA360 session data in Python
- Visualize key traffic patterns and user behaviors
- Evaluate which acquisition channels lead to **real transactions**
- Identify conversion performance by device, channel, and time

Data used is anonymized and public, ideal for e-commerce analytics practice.

![1](https://github.com/user-attachments/assets/cf2e0622-7db3-4117-948b-12b96e043cca)

---

## 📁 Dataset Overview

**Source**: [Google Analytics sample dataset](https://support.google.com/analytics/answer/7586738?hl=en)

| Column            | Description                              |
|-------------------|------------------------------------------|
| `visitId`         | Unique session ID                        |
| `visitStartTime`  | Session start timestamp                  |
| `visitNumber`     | Number of visits by the user             |
| `channelGrouping` | Acquisition channel (e.g., Organic, Paid)|
| `browser`         | User's browser                           |
| `operatingSystem` | OS used by the visitor                   |
| `deviceCategory`  | Device type: desktop, mobile, tablet     |
| `continent`       | User's continent                         |
| `transactions`    | Total transactions from the session      |

Rows: ~2,556

---

## 🧪 Key Analytical Tasks

### 🧵 1. Data Loading & Cleaning
- Connected to the Google Sheet using SQL queries
- Converted timestamps to human-readable datetimes
- Adjusted timezones to reflect local (PST) usage behavior

### 📊 2. Exploratory Data Analysis
- Sessions by:
  - 🌍 Continent
  - 📱 Device category
  - 🚦 Channel grouping
- Interactive bar and pie charts using `plotly.express`

### ⏱️ 3. Hourly Visit Patterns
- Extracted session timestamps and grouped visits by hour
- Visualized channel traffic patterns throughout the day

### 💸 4. Conversion Effectiveness
- Calculated **transactions per session** for each channel
- Visualized which traffic sources bring in paying customers

---

## 📈 Visual Insights

| Metric                     | Visualization | Insight |
|---------------------------|---------------|---------|
| Sessions by Channel       | Pie chart     | Organic Search leads in traffic |
| Sessions by Device        | Pie chart     | Desktop is dominant (~68%) |
| Hourly Visits per Channel | Line chart    | Referral and Direct peak early |
| Conversion per Channel    | Bar chart     | Referral has the highest transactions/session |

---

## 📌 Highlights

- 📊 **Referral traffic** led to the highest conversion rate (≈6.6%)
- 🌍 Majority of sessions came from **North America**
- 💻 **Desktop users** were most likely to convert
- 🕒 **Mid-day hours** saw peak activity from Organic Search

![2](https://github.com/user-attachments/assets/7b1da5ab-a741-4a41-89e2-04b66d2f9da2)

---

## 🛠️ Tools & Technologies

| Tool       | Purpose                        |
|------------|--------------------------------|
| `Google Sheets` | Cloud-hosted dataset      |
| `SQL`           | Structured queries for filtering data |
| `pandas`        | Data manipulation in Python |
| `plotly.express`| Interactive visualizations |


---

## 🧠 Business Takeaways

- Not all traffic is equal: **volume ≠ value**
- Acquisition strategy should prioritize **referral partnerships**
- Time-of-day analysis can inform **campaign timing**
- Device-based segmentation can drive **UX design priorities**
