# KNIME Bike Sales Analysis & Visualization 🚲📊

[![KNIME](https://img.shields.io/badge/Tool-KNIME_AP-yellow?logo=knime&style=flat-square)](https://www.knime.com/)
[![Data Source](https://img.shields.io/badge/Data-CSV_&_Excel-blue?style=flat-square)](./) <!-- Link to data folder if applicable -->
[![Visualization](https://img.shields.io/badge/Viz-KNIME_Nodes-blueviolet?style=flat-square)](https://hub.knime.com/knime/spaces/Examples/latest/05_Reporting/01_BIRT/01_Simple_Reporting_with_KNIME_Nodes)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_88-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

![image](https://github.com/user-attachments/assets/3e9d75b4-80e2-454b-8e35-095e51fbfa76)
*Fig 1: Complete KNIME workflow for bike sales data analysis.*

## 🎯 Project Goal: Visual Workflow for Business Insights with KNIME

Welcome to Day 88 of my #100DaysOfDataScience challenge! Today, we step into the powerful world of **visual programming** with the **KNIME Analytics Platform**. This project demonstrates how to build an end-to-end data analysis workflow – from reading raw data to generating insightful visualizations and exporting results – entirely through KNIME's intuitive node-based interface.

**The Mission:**
*   Analyze historical bike sales data (`bike_sales.csv`) enriched with product information (`product_info.xlsx`).
*   Perform common data preparation, transformation, aggregation, and visualization tasks using standard KNIME nodes.
*   Answer key business questions about sales performance, customer demographics, product categories, and regional trends.
*   Showcase the efficiency and clarity of building complex data pipelines visually, without extensive coding.
*   (Bonus) Explore appending new data (`bike_sales_2024.csv`) and applying conditional logic.

This project highlights KNIME's strength as a low-code/no-code platform for data science, making complex analysis accessible and reproducible.

---

## ✨ Key Features & Concepts Mastered

*   **Visual Workflow Design:** Constructed a multi-stage analytical pipeline using KNIME's drag-and-drop interface.
*   **Multi-Source Data Input:** Read and integrated data from different file types (`CSV Reader`, `Excel Reader`).
*   **Data Blending/Joining:** Enriched sales data with product details (price, category) using the `Value Lookup` node (similar to a VLOOKUP or Left Join).
*   **Data Transformation & Feature Engineering:**
    *   Calculated new metrics (e.g., Revenue) using the `Expression` node.
    *   Extracted date components (Year) using `String to DateTime` and `Extract Date&Time Part` nodes.
    *   Manipulated data types (`Number to String`).
*   **Data Aggregation & Summarization:**
    *   Summarized sales quantities using `Row Aggregator`.
    *   Grouped data and calculated aggregates (e.g., Sum of Revenue by Year and Country) using the powerful `Pivot` node.
    *   Utilized `GroupBy` for summarizing data (seen in Bonus section).
*   **Data Filtering:** Selected specific subsets of data based on criteria (e.g., filtering for 'Bikes' category) using the `Row Filter` node.
*   **Conditional Logic:** Applied rules using the `Rule Engine` node (seen in Bonus section).
*   **Integrated Visualization:** Generated various plots directly within the workflow:
    *   `Histogram` (for Age Distribution).
    *   `Bar Chart` (for Orders by Country).
    *   `Pie Chart` & `Sunburst Chart` (for Revenue by Category).
    *   `Stacked Area Chart` (for Bike Revenue Evolution by Country).
*   **Data Export:** Wrote processed results to an Excel file using `Excel Writer`.
*   **Workflow Organization:** Structured the analysis logically using Annotations and distinct levels (Warm up, Level 1, Level 2, Level 3, Bonus).

---

## 🛠️ Tech Stack: The KNIME Node Toolkit

*   **Core Platform:** **KNIME Analytics Platform**
*   **Key Nodes Used:**
    *   **I/O:** `CSV Reader`, `Excel Reader`, `Excel Writer`
    *   **Manipulation:** `Value Lookup`, `Row Aggregator`, `Expression`, `Row Filter`, `String to DateTime`, `Extract Date&Time Part`, `Pivot`, `Number to String`, `Concatenate` (implied for Bonus), `Rule Engine` (Bonus), `GroupBy` (Bonus)
    *   **Visualization:** `Histogram`, `Bar Chart`, `Pie Chart`, `Sunburst Chart`, `Stacked Area Chart`
    *   **Aesthetics:** `Color Manager`
*   **Underlying Concepts:** Visual Programming, Node-Based Workflows, Data Blending, ETL (Extract, Transform, Load), In-Platform Visualization.

---

## 🗺️ The Workflow: A Visual Journey Through Bike Sales Data

The KNIME workflow progresses through logical stages, clearly visible in the screenshots:

**Phase 0: Data Input & Warm-up** [Fig 2, Fig 3]
*   **Nodes:** `CSV Reader` (loads `bike_sales.csv`), `Excel Reader` (loads `product_info.xlsx`).
*   **Analysis:** Immediately generates initial insights:
    *   Customer Age Distribution (`Histogram`).
    *   Total Orders per Country (`Bar Chart`).

![image](https://github.com/user-attachments/assets/8af84ad5-eb6e-4d95-a368-246df8b77b87)

*Fig 2: Reading CSV/Excel and initial 'Warm up' visualizations.*

**Phase 1: Identifying Top Products** [Fig 3]
*   **Nodes:** `Value Lookup` (joins sales data with product details using `Product` / `Product_Code`), `Row Aggregator`.
*   **Goal:** Determine the best-selling product.
*   **Process:** The `Value Lookup` adds product category, name, and price to each sale. The `Row Aggregator` likely sums `Order_Quantity` grouped by `Product_Name` or `Product_Code`.

![image](https://github.com/user-attachments/assets/57e543de-1077-4932-9eb6-c85483b18be8)

*Fig 3: Detail showing Level 1 analysis using Value Lookup and Aggregation.*

**Phase 2: Analyzing Revenue by Category** [Fig 4]
*   **Nodes:** `Expression` (calculates Revenue, probably `Order_Quantity * Product_Price`), `Color Manager`, `Pie Chart`, `Sunburst Chart`.
*   **Goal:** Understand which product category generates the most revenue.
*   **Process:** Calculates revenue per line item, then aggregates (likely implicitly within chart nodes or via a preceding aggregator) to visualize the proportion of total revenue coming from each `Product_Category`.

**Phase 3: Tracking Bike Revenue Evolution** [Fig 4]
*   **Nodes:** `Row Filter` (isolates 'Bikes' category), `String to DateTime` + `Extract Date&Time Part` (gets the 'Year' from 'Date'), `Pivot` (groups by 'Year' and 'Country', summing calculated 'Revenue'), `Number to String` (likely formatting for chart labels), `Stacked Area Chart`.
*   **Goal:** Visualize how revenue specifically from *Bikes* changed over the years for different countries.
*   **Process:** This level filters the data, extracts the year, pivots to create a time-series summary by country, and displays it using a `Stacked Area Chart`.

![image](https://github.com/user-attachments/assets/4d079be8-e9c3-439f-93bc-0998b2a66d21)

*Fig 4: Detail showing Level 2 (Category Revenue) and Level 3 (Bike Revenue Evolution) analysis, plus Export.*

**Phase 4: Export & Bonus Analysis** [Fig 4, Fig 1]
*   **Nodes:** `Excel Writer` (saves results), `Rule Engine`, `GroupBy` (visible in overview, likely used in Bonus section).
*   **Goal:** Export final results and potentially analyze new data (`bike_sales_2024.csv`).
*   **Process:** The `Excel Writer` saves the processed data (the pivoted time-series data from Level 3). The 'Bonus' section suggests appending new data and applying rules or grouping for further analysis (e.g., comparing 2024 to previous years).

---

## 💡 Key Insights & Discoveries

Based on the workflow structure, this analysis revealed insights such as:

*   **Customer Demographics:** The age distribution of bike buyers (e.g., concentrated in 25-45 range).
*   **Top Markets:** Which countries (e.g., United States, Australia) dominate the total orders.
*   **Best-Selling Items:** The specific product (via `Row Aggregator` in Level 1) with the highest sales volume.
*   **Revenue Drivers:** Which product category (`Bikes`, `Accessories`, `Clothing`) contributes most significantly to overall revenue (Level 2 Charts).
*   **Growth Trends:** How bike sales revenue evolved year-over-year across different countries, identifying growing or shrinking markets (Level 3 Stacked Area Chart).

---

## ✅ Why KNIME for This Analysis?

This project highlights the advantages of using KNIME for data analysis workflows:

*   **Visual Clarity:** The node-based pipeline makes the entire analysis process transparent and easy to follow, even for complex sequences.
*   **Low-Code Efficiency:** Complex tasks like data blending, pivoting, and visualization are achieved by configuring nodes, drastically reducing the need for coding.
*   **Reproducibility:** The workflow itself serves as documentation and can be easily re-run with updated data.
*   **Integrated Environment:** Handles data input, transformation, analysis, visualization, and output within a single platform.
*   **Accessibility:** Lowers the barrier to entry for performing sophisticated data analysis.

---

## 🚀 Potential Next Steps with KNIME

This foundational workflow can be readily extended:

*   **Profitability Analysis:** Join with cost data (if available) and use `Math Formula` or `Expression` nodes to calculate profit margins.
*   **Customer Segmentation:** Use `K-Means` or `DBScan` nodes to cluster customers based on purchasing behavior or demographics.
*   **Time Series Forecasting:** Employ nodes like `ARIMA Learner` or `Linear Regression Learner` (after more date feature engineering) to predict future sales.
*   **Interactive Dashboarding:** Use KNIME's dashboarding capabilities or integrate with Tableau/Power BI via dedicated connectors.
*   **Advanced Visualization:** Explore more complex chart types or use Python/R scripting nodes within KNIME for custom plots.

---

*Day 88 of #100DaysOfDataScience successfully demonstrated building a comprehensive data analysis pipeline visually using KNIME Analytics Platform. A powerful testament to low-code/no-code data science! - Vatsal Parikh*
