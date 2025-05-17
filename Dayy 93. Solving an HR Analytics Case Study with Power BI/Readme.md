# 📊 HR Analytics Dashboard with Power BI

[![Power BI](https://img.shields.io/badge/Tool-Power_BI-yellow?logo=powerbi&style=flat-square)](https://powerbi.microsoft.com/)
[![Data Source](https://img.shields.io/badge/Data-Fictional_HR_Data-orange?style=flat-square)](./) <!-- Assuming data is local or link to source -->
[![Visualization](https://img.shields.io/badge/Focus-HR_Analytics_&_Attrition-blueviolet?style=flat-square)](https://en.wikipedia.org/wiki/People_analytics)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_93-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Actionable HR Insights Through Interactive Visualization

Welcome to Day 93 of my #100DaysOfDataScience challenge! Today's project dives into the critical field of **Human Resources (HR) Analytics**, demonstrating how **Microsoft Power BI** can be used to transform raw employee data into a powerful, interactive dashboard. This dashboard aims to provide HR professionals at a fictional software company, "Atlas Labs," with clear visibility into key workforce metrics and, crucially, to **understand the factors impacting employee attrition**.

**The Mission:**
*   Ingest and model data related to employees, their performance, and satisfaction levels.
*   Calculate and visualize key HR metrics: headcount, active/inactive employees, attrition rates.
*   Analyze employee demographics, department distributions, and hiring trends over time.
*   Investigate correlations between factors like job role, business travel, overtime, and attrition rates.
*   Build an intuitive, interactive dashboard that allows HR users to slice and dice the data to uncover actionable insights for improving retention and employee happiness.

This project showcases the end-to-end process of building an HR analytics solution in Power BI, from data modeling to insightful dashboard design.

---

## ✨ Key Features & Concepts Mastered

*   **Data Modeling in Power BI:** Connecting multiple data sources/tables (`DimEmployee`, `FactPerformanceRating`, `DimEducationLevel`, `DimSatisfiedLevel`, `DimRatingLevel`) and establishing relationships to create a coherent data model.
*   **DAX for Custom Calculations:** Creating measures and calculated columns using **Data Analysis Expressions (DAX)** for metrics like:
    *   Total Employees, Active Employees, Inactive Employees.
    *   Attrition Rate (`% Attrition Rate`).
    *   Average Salary.
    *   Cumulative Headcount, Leave Balance Analysis.
*   **Interactive Visualizations:** Utilizing a variety of Power BI visuals to present data effectively:
    *   **Cards:** For displaying key performance indicators (KPIs) like Total Employees, Attrition Rate.
    *   **Line Charts:** To show trends over time (e.g., Total Employees by Year).
    *   **Treemaps:** For hierarchical data display (e.g., Total Employees by Department and Job Role).
    *   **Bar Charts (Clustered/Stacked):** For comparisons (e.g., Attrition Rate by Job Role, Attrition by Business Travel/Overtime).
    *   **(Potentially)** Pie/Donut charts for proportions, Combo charts for multiple metrics.
*   **Slicers & Filters:** Implementing interactive controls (e.g., an "Attrition" slicer allowing users to view data for "All", "Yes", or "No" attrition cases) for dynamic data exploration.
*   **Dashboard Design Principles:** Structuring the dashboard into logical pages (Overview, Attrition) for clarity and ease of navigation.
*   **Power Query for ETL:** Implicitly, Power BI uses Power Query for initial data loading, cleaning, and transformation steps before modeling.
*   **Understanding HR Metrics:** Applying domain knowledge to select and calculate relevant metrics for HR analytics.

---

## 🛠️ Tech Stack: The Power BI Analytics Suite

*   **Core Tool:** **Microsoft Power BI Desktop**
*   **Data Manipulation & Modeling:**
    *   Power Query (for ETL)
    *   Power Pivot / Data Model (for relationships and schema)
    *   DAX (Data Analysis Expressions) (for measures and calculated columns)
*   **Data Source:** Excel files / CSVs containing employee, performance, and dimension tables.
*   **Key Power BI Visuals Used:** Cards, Line Charts, Treemaps, Bar Charts, Slicers.

---

## 🗺️ The Dashboard Structure & Key Insights

The HR Analytics Dashboard is organized to provide both high-level overviews and deeper dives into specific areas, particularly attrition:

### 1. Overview Page

*   **KPI Cards:**
    *   **Total Employees:** 1470 (when Attrition=All), 261 (when Attrition=Yes)
    *   **Active Employees:** 1233, 199 (when Attrition=Yes)
    *   **Inactive Employees:** 237, 62 (when Attrition=Yes)
    *   **% Attrition Rate:** 16.1% (overall), 23.8% (when filtering for Attrition=Yes, this represents the proportion of the 'attrited' group, which is inherently 100% attrited; the 16.1% is the key overall rate).
*   **Total Employees by Year (Line Chart):** Shows fluctuations in headcount over the years (e.g., a dip around 2016, subsequent recovery).
*   **Total Employees by Department and Job Role (Treemap):** Highlights dominant departments (e.g., Technology with Software Engineers, Data Scientists) and job roles (e.g., Sales Executive) in terms of employee numbers.
*   **Total Employees and Average of Salary by Ethnicity (Bar & Line Combo Chart):** Visualizes employee counts and average salary trends across different ethnic groups.

![Screenshot 2025-05-16 195107](https://github.com/user-attachments/assets/0db56e70-f21f-48bf-b8f1-8b97b5c21420)
*Fig 1: Overview Page showing key HR metrics for all employees.*

![Screenshot 2025-05-16 195158](https://github.com/user-attachments/assets/f7b70103-95c1-4c7d-a4c7-cbaa0bf725b1)
*Fig 2: Overview Page filtered by the "Attrition = Yes" slicer, showing characteristics of employees who left.*

### 2. Attrition Page:

This page drills down into the factors influencing employee attrition:

*   **% Attrition Rate by Department and Job Role (Horizontal Bar Chart):** Identifies job roles with the highest attrition rates. In the sample, **Sales Representative** shows the highest rate (~35%), followed by **Recruiter** and **Data Scientist**. This is a critical insight for retention strategies.
*   **% Attrition Rate and Total Employees by Business Travel (Bar & Line Combo Chart):** Compares attrition across travel frequencies. "Frequent Traveller" category shows a significantly higher attrition rate (~25%) compared to "Some Travel" or "No Travel".
*   **% Attrition Rate by OverTime (Bar Chart):** Clearly shows that employees working **OverTime ("Yes")** have a dramatically higher attrition rate (~30%) compared to those who do not (~10%).

![Screenshot 2025-05-16 195120](https://github.com/user-attachments/assets/da68cbba-3deb-4af3-b9fc-9f76caa118cd)
*Fig 3: Attrition Page highlighting key drivers of employee turnover.*

---

## 💡 Key Insights & Business Impact

The dashboard effectively visualizes critical HR insights, enabling data-driven decision-making:

*   **Attrition Drivers Identified:** The analysis strongly suggests that specific **Job Roles** (Sales Rep, Recruiter), frequent **Business Travel**, and working **OverTime** are significant contributors to higher employee attrition.
*   **Departmental Focus:** The Technology department, while large, might have specific roles (e.g., Data Scientist, Software Engineer) with notable attrition that need targeted attention.
*   **Headcount Trends:** The "Total Employees by Year" chart provides a historical perspective on company growth and potential periods of concern.
*   **Interactive Exploration:** The use of slicers (e.g., for Attrition status) allows HR managers to dynamically filter the entire dashboard and see how KPIs and distributions change for specific employee segments (e.g., characteristics of those who left vs. those who stayed).
*   **Foundation for Action:** These insights can directly inform HR initiatives, such as reviewing workloads for high-attrition roles, re-evaluating travel policies, or improving work-life balance for overtime staff.

---

## ✅ Why This Matters: Power BI for Strategic HR

*   **Democratizing Data:** Power BI empowers HR teams to perform complex analysis and derive insights without needing deep coding expertise.
*   **Clear Visual Communication:** Complex HR data is transformed into intuitive charts and KPIs, making it easier to communicate findings to stakeholders.
*   **Proactive Problem Solving:** By identifying attrition drivers, organizations can proactively implement retention strategies.
*   **Monitoring Key Metrics:** Provides a centralized view for tracking essential HR KPIs over time.

---

*Day 93 of #100DaysOfDataScience demonstrates the power of Power BI for comprehensive HR analytics. By transforming raw data into an interactive dashboard, we can uncover key drivers of employee attrition and provide actionable insights for better workforce management.*
