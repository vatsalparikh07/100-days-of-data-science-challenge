# Day 29. 100 Days of Data Science Challenge - 03/01/2025

# Carbon Footprint Analysis with SQL
*Analyzing global product carbon footprints (PCFs) to identify key emission drivers*


## 🌍 Project Overview  
This project analyzes **product carbon footprints (PCFs)** from over 800 products across 28 countries using SQL. The dataset reveals greenhouse gas emissions (measured in CO₂ equivalent) across product lifecycles. Key focus areas include:
- Identifying high-emission industries and countries
- Analyzing emission distribution across production stages (upstream/operations/downstream)
- Exploring company-specific footprints (e.g., Coca-Cola, Daikin Industries)

**Technical Focus**:  
- Advanced SQL filtering and aggregation
- Data normalization techniques
- Plotly visualization for geo-distribution

---

## 📂 Dataset Structure  
**Table**: `product_emissions`  

| **Column**               | **Description**                                  |
|--------------------------|--------------------------------------------------|
| `year`                   | Reporting year (2013-2017)                       |
| `product_name`           | Product description                              |
| `company`                | Reporting company                                |
| `country`                | Company headquarters location                    |
| `industry_group`         | Industry classification                          |
| `carbon_footprint_pcf`   | Total CO₂ equivalent emissions                   |
| `upstream_percent_total_pcf` | % emissions from raw materials/supply chain     |
| `operations_percent_total_pcf` | % emissions from manufacturing processes      |
| `downstream_percent_total_pcf` | % emissions from product use/disposal         |

---

## 🔑 Key SQL Concepts Applied  

1. **Pattern Matching**  
   Used `LIKE 'Coca-Cola%'` to aggregate data across Coca-Cola subsidiaries globally.

2. **Temporal Filtering**  
   Identified the most recent data year (2017) using `MAX(year)`.

3. **Advanced Aggregation**  
   Calculated industry emissions with:
```
SELECT industry_group,
ROUND(SUM(carbon_footprint_pcf), 1) AS total_industry_footprint
FROM product_emissions
WHERE year = 2017
GROUP BY industry_group
ORDER BY total_industry_footprint DESC;
```

4. **Lifecycle Analysis**  
Compared emission distribution across production stages for Daikin air conditioners.

---

## 🌟 Critical Insights  

### Industry Analysis (2017)
| **Industry**       | **Total Emissions (CO₂e)** | **% of Dataset** |
|---------------------|----------------------------|------------------|
| Materials          | 2,251,225                 | 41%              |
| Capital Goods      | 167,587                   | 7%               |
| Food & Beverage    | 67,351                    | 28%              |

- **Materials industry** dominated emissions despite representing only 12% of 2017 records
- **98% of Daikin's emissions** occur upstream (refrigerant production)

### Geographic Trends
- **Germany** and **USA** accounted for 52% of total emissions
- **Spain's** high emissions driven by Gamesa Corporación Tecnológica (wind turbine manufacturing)

---

## 📊 Visualization Highlights  
**Plotly Charts**:
1. **Country Emission Distribution**: Revealed unexpected leaders like Spain  
2. **Industry Representation**: Showed disparity between data volume and emission impact  
3. **Lifecycle Breakdown**: Visualized upstream dominance in manufacturing sectors

![Emissions by Country](https://cdn.mathpix.com/cropped/2025_03_02_d365b2e48dcc852d69acg-6.jpg?height=630&width=1721&top_left_y=339&top_left_x=190)

---

## 🛠️ Technical Challenges  
1. **Data Normalization**  
- Converted percentage strings (e.g., "3.96%") to numerical values
- Harmonized company naming conventions (e.g., "Coca-Cola HBC AG" vs "Coca-Cola Enterprises")

2. **Outlier Handling**  
- Identified wind turbine manufacturing as major emission source in Spain
- Addressed inconsistent regional classifications (e.g., "Calamhin" typo)

---

## 📚 Lessons Learned  
1. **Emission Hotspots**  
Upstream processes often dominate footprints (e.g., 97% of Daikin's AC emissions)

2. **Data Paradox**  
High-emission industries may have sparse representation (Materials: 12% records, 41% emissions)

3. **SQL for Sustainability**  
Window functions and CTEs enable complex supply chain analysis

---

*"This analysis revealed how SQL can uncover critical sustainability insights hidden in operational data."*
