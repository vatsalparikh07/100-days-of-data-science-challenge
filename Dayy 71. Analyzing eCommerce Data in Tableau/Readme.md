# Day 71. 100 Days of Data Science Challenge - 04/12/2025

## 📈 eCommerce Analytics & Shipping Cost Optimization Dashboard

**✨ Ready to see data in action? Explore the LIVE Interactive Dashboard! ✨**
**[➡️ Click Here to Launch on Tableau Public](https://public.tableau.com/app/profile/vatsalparikh/viz/EcommerceDataAnalysisDashboard/What-ifAnalysis)**

![Executive Dashboard Preview](https://pplx-res.cloudinary.com/image/upload/v1744505516/user_uploads/ITgdeUFGdFUnqya/1.jpg)

![image](https://github.com/user-attachments/assets/5e6e4f38-0eb7-4031-96c5-c66af904bdc8)

## 🚀 The Mission: From Raw Sales Data to Strategic Insights for Munchy's Pet Supply

Running an eCommerce business is tough. You need to know what's selling, who's buying, *and* how to keep costs like shipping from eating into your profits. This project dives headfirst into the sales data of **Munchy's Pet Supply**, a fictional store, using **Tableau** to transform messy CSV files into an intuitive, actionable business intelligence dashboard.

The goal wasn't just to *report* numbers, but to **uncover strategic insights** – identifying top products, understanding customer geography, and crucially, exploring ways to **optimize shipping costs** through a powerful **what-if analysis**.

---

## 📊 Meet the Dashboards: Two Sides of the Coin

This Tableau workbook features two distinct, yet connected, dashboards designed for different analytical needs:

1.  **The Executive Overview:** Your command center for business health.
    *   **KPIs at a Glance:** Tracks total Sales, Profit, overall Shipping Costs (Baseline), and Profit Margin %.
    *   **Top Performers:** Instantly identifies the best-selling products and categories driving the business.
    *   **Where's the Market?:** A geo-map visualizing sales distribution across US states, highlighting key customer concentration areas.

2.  **The What-If Shipping Analysis:** A strategic tool for cost optimization.
    *   **Interactive Cost Simulation:** Uses a parameter to let users model the impact of changing the average number of items per shipment.
    *   **Baseline vs. Scenario:** Directly compares current ("Baseline") shipping costs against the simulated ("What-if") scenario.
    *   **Cost Savings Potential:** Calculates the potential dollar savings based on the what-if scenario.
    *   **Product-Level Impact:** Shows how simulated shipping costs affect individual products.
    *   **Trend Analysis:** Visualizes the cumulative impact of shipping cost changes over time.

---

## 💾 The Data Under the Hood: Connecting the Dots

This analysis weaves together data from four distinct sources, requiring careful **data modeling** within Tableau to establish relationships:

1.  **`fact_sales.csv`:** The heart of the operation – transaction-level details including `Customer ID`, `Product Description`, `Stock Code`, `Quantity`, `Sales`, `Unit Price`, and `Transaction Date`.
2.  **`dim_customers.csv`:** Information about the buyers, linking `Customer ID` to location data like `Order City`, `Order State`, `Latitude`, and `Longitude`.
3.  **`dim_products.csv`:** Details about each item, including `Stock Code`, `Weight`, `Landed Cost` (COGS + freight), `Shipping_Cost_1000_r` (average cost per 1000 miles), `Description`, and `Category`.
4.  **`state_region_mapping.csv`:** A crucial lookup table used for **data cleaning**, mapping various state abbreviations and names (e.g., "ca", "California", "CALIFORNIA") to a standardized `State` code and `Region` (East, West, Central, Other).

**Data Modeling Approach:** Relationships were established primarily using `Customer ID` (linking Sales to Customers) and `Stock Code` (linking Sales to Products). The `state_region_mapping.csv` was joined to `dim_customers.csv` on the state field to standardize geographic data.

---

## 🛠️ Building the Insights: Methodology & Tableau Techniques

Bringing this dashboard to life involved several key steps and Tableau features:

*   **Data Modeling & Relationships:** Defining joins between the four CSV files based on common keys (`Customer ID`, `Stock Code`, State variations) directly within Tableau's data source pane.
*   **Calculated Fields:** Creating essential metrics not present in the raw data:
    *   `Profit`: Calculated likely as `Sales - (Landed Cost * Quantity) - Shipping Cost`.
    *   `Profit %`: `Profit / Sales`.
    *   `Baseline Shipping Cost`: Calculated based on existing data and assumptions (e.g., cost per 1000 miles, weight).
    *   `What-if Shipping Cost`: A dynamic calculation incorporating the **parameter** for quantity and potentially adjusted cost assumptions (like the 70% cost for additional items mentioned).
    *   `Shipping Cost Difference`: `Baseline Shipping Cost - What-if Shipping Cost`.
*   **Parameters:** Implementing the "What if Quantity" slider/input field – a core feature allowing users to interactively change assumptions and see immediate results in the What-if analysis dashboard.
*   **Geo-Mapping:** Utilizing the cleaned `State` data and potentially generated `Latitude`/`Longitude` to create the Sales by State map.
*   **Visualization Choices:** Selecting appropriate charts (Bar charts for rankings, Maps for geography, Area charts for trends over time, Text tables for KPIs) to best communicate the insights.
*   **Dashboard Design & Interactivity:** Arranging visualizations logically, adding clear titles and annotations, and ensuring filters/parameters update relevant charts seamlessly.

---

## 💡 Key Discoveries & Strategic Takeaways

Digging into the data revealed valuable insights for Munchy's Pet Supply:

1.  **Volume vs. Profit Paradox:** While everyday items like **Pet Food and Disposables** drive the majority of *sales volume*, higher-margin **Electronics** (like Pet Cameras) are the most *profitable* products. This highlights the need for a balanced inventory and marketing strategy.
2.  **Geographic Strongholds:** A significant concentration of customers resides in **California, Florida, and Texas**. These states are prime candidates for targeted marketing campaigns, localized promotions, or potentially even regional fulfillment centers to reduce shipping costs.
3.  **The Shipping Cost Challenge:** The baseline shipping cost ($385K) represents a substantial portion of expenses (compared to $427K profit). Optimizing this is critical.
4.  **Optimizing Shipping via Quantity:** The What-if analysis demonstrates significant potential savings ($117K+) by increasing the average items per shipment. This strongly suggests a strategic opportunity: **Target customers who frequently buy single items with quantity discount promotions** (e.g., "Buy 2, Save 10% on Shipping") to encourage larger orders and lower the per-item shipping cost.
5.  **Product-Specific Shipping Costs:** High-volume, lower-margin items like "Taste of the Wild" food contribute significantly to baseline shipping costs. Strategies might involve bundling these with higher-margin items or exploring different shipping methods for bulky products.

---

## 🚀 Impact & Business Value

This dashboard transforms raw data into a strategic asset for Munchy's Pet Supply, enabling:

*   **Data-Driven Marketing:** Focus campaigns on high-value states (CA, FL, TX).
*   **Profit Optimization:** Identify and promote high-margin products (Electronics).
*   **Cost Reduction Strategy:** Implement targeted promotions (quantity discounts) to directly address the single-item shipping cost issue identified in the What-if analysis.
*   **Inventory Management:** Balance stock levels based on both sales volume and profitability.
*   **Executive Decision Support:** Provides clear, visual KPIs and actionable insights for leadership.

---

*This project showcases the power of Tableau not just for reporting, but for interactive analysis and strategic simulation, turning complex eCommerce data into clear business opportunities. Created by Vatsal Parikh.*
