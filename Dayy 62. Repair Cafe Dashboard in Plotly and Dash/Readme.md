# Day 62. 100 Days of Data Science Challenge - 04/03/2025

# 🛠️ Repair Café Dashboard

An interactive dashboard built with Plotly and Dash to analyze repair data from global Repair Café events. The dashboard provides insights into repair success rates, commonly repaired products, and repair outcomes across various categories. 

[**Visit the live dashboard here**](https://repair-cafe-dashboard.onrender.com/) (Please allow upto 1 min. for the app to render as I'm using a free tier deployment service🥹)

---

## 📊 Key Metrics

The Repair Café Dashboard tracks and visualizes the following key metrics:

- **Total Repairs Attempted**: 75,251  
- **Overall Success Rate**: 53%  
- **Categories Analyzed**: 39  
- **Unique Products**: 944  

### Summary View:
![Key Metrics](https://pplx-res.cloudinary.com/image/upload/v1743779301/user_uploads/YxsbScSxYadixTl/image.jpg)

---

## 📈 Dashboard Insights

### 1. Products by Status Fixed (%)
![Products by Status Fixed](https://pplx-res.cloudinary.com/image/upload/v1743779275/user_uploads/lvzwUEzGoLpqQPW/image.jpg)

This scatter plot visualizes the repair success rate for each product type:
- Each dot represents a product, with its size indicating the volume of repair attempts.
- The green shaded area highlights products with above-average success rates (53%).
- Example: Remote controls cluster near the average success rate, indicating moderate repairability.

---

### 2. Top Product Categories
![Top Product Categories](https://pplx-res.cloudinary.com/image/upload/v1743779301/user_uploads/YxsbScSxYadixTl/image.jpg)

#### Top 10 Categories by Volume:
1. **Vacuum Cleaners**: 7,025 attempts  
2. **Coffee Makers**: 6,931 attempts  
3. **Hi-Fi Separates**: 5,981 attempts  
4. **Lamps**: 5,068 attempts  
5. **Power Tools**: 4,959 attempts  
6. **Small Kitchen Items**: 4,451 attempts  
7. **Watches/Clocks**: 3,757 attempts  
8. **Small Home Electricals**: 3,679 attempts  
9. **Food Processors**: 3,101 attempts  
10. **Sewing Machines**: 2,851 attempts  

These categories represent the most frequently repaired items at Repair Cafés.

---

### 3. Detailed Product Analysis
![Detailed Product Table](https://pplx-res.cloudinary.com/image/upload/v1743779306/user_uploads/wnvTvDGMavABgvy/image.jpg)

The detailed table provides insights into individual product types:
- **Repair Superstars**:
  - Sewing Machines: 69.6% success rate
  - Lamps/Lighting: 68.4% success rate
  - Vacuum Cleaners: 61.7% success rate
- **Challenging Products**:
  - Electric Kettles: Only a 40.9% success rate with a high "end-of-life" percentage (50%).
  - Printers: A low success rate of 35.2%, with many deemed beyond repair (42.6%).

---

## 🔍 Key Observations

1. **Mechanical vs Electronic Products**
   - Mechanical products like sewing machines and clocks have higher repair success rates.
   - Complex electronics like laptops and printers show lower success rates but higher "repairable" statuses, indicating potential for improvement with specialized tools or expertise.

2. **Volume Leaders**
   - Coffee makers and vacuum cleaners dominate repair attempts, accounting for over 13,000 items combined.

3. **Repair Challenges**
   - Items like electric kettles and printers highlight areas where manufacturers could improve design for better repairability.

4. **Community Impact**
   - The dashboard showcases the value of Repair Cafés in extending product lifespans and reducing waste.

---

## 📊 Interactive Features

The dashboard includes powerful filtering and visualization tools:
- Filter by product category (e.g., "Remote Control").
- View detailed statistics for each product type.
- Export data as CSV for further analysis.
- Reset filters to explore the full dataset.

---

## 👀 Visual Highlights

### Scatter Plot of Repair Success Rates
This scatter plot shows the distribution of repair outcomes across all products:
- Green shaded area indicates above-average success rates.
- Larger dots represent higher volumes of repair attempts.

### Radial Charts for Categories and Products
Two radial charts highlight:
1. The top product categories by volume.
2. The most commonly presented products and their respective repair outcomes.

### Tabular Data View
The detailed table provides a breakdown of each product type's total repairs, fixed percentage, repairable percentage, and end-of-life percentage.

---

## Conclusion

The Repair Café Dashboard provides actionable insights into community repair efforts by analyzing over 75,000 repair records across nearly 1,000 unique products. By identifying high-success categories and challenging items, this tool helps Repair Cafés optimize their operations and focus on areas where they can make the biggest impact.

[Explore the live dashboard here!](https://repair-cafe-dashboard.onrender.com/)

