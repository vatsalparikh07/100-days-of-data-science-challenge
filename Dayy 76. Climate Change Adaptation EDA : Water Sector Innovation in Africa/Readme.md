# Day 76. 100 Days of Data Science Challenge - 04/17/2025

## 🌍 Climate Change Adaptation Analysis: Water Sector Innovation in Africa

[![SQL](https://img.shields.io/badge/Analysis-SQL-blue?logo=postgresql&style=flat-square)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Visualization-Python-brightgreen?logo=python&style=flat-square)](https://www.python.org/)
[![Data](https://img.shields.io/badge/Dataset-Climate_Adaptation-orange?style=flat-square)](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/30330689/a3d54a11-d811-46da-9d81-1636a4c02a19/climate.csv)

## 🔍 Project Overview
This project analyzes climate adaptation strategies in Africa's water sector using **25+ years of data** (1990-2016) from 50 countries. We focus on three key dimensions:
- **Technological Innovation**: Water-related patent data tracking adaptation tech adoption
- **Economic Factors**: GDP per capita, trade openness, and business environment metrics
- **Water Vulnerability**: Composite water stress index (0-1 scale) measuring climate risk

**Key Question**: How do socio-economic factors and institutional efficiency correlate with climate adaptation technology adoption in water-stressed regions?

**[📄 View Full Analysis](solution.ipynb)**

---

## 📊 Dataset Features
`climate.csv` contains 500+ records with 9 critical variables:

| Column | Description | Example Values |
|--------|-------------|----------------|
| `water_related_adaptation_tech` | Patent activity (0=low, 5=high) | Algeria 2015: 1.0 |
| `water_stress_index` | Climate vulnerability score (0-1) | Niger 2016: 0.672 |
| `gdp_per_capita` | Economic output per citizen | South Africa 2016: $12,214 |
| `days_to_register_property` | Institutional efficiency metric | Botswana 2016: 12 days |
| `trade` | Exports+Imports/GDP ratio | Seychelles 2016: 173.58% |

---

## 🧩 Key Analysis & Insights

### 1. High-Risk Countries Identification
```
SELECT country, AVG(water_stress_index) AS avg_stress
FROM climate
GROUP BY country
ORDER BY avg_stress DESC
LIMIT 5;
```
**Top Water-Stressed Nations**:
1. Niger (0.672)
2. Chad (0.439)
3. Sudan (0.691)
4. Somalia (0.542)
5. Kenya (0.505)

*Insight*: Sahel region countries show chronic water vulnerability despite low adaptation tech scores (<0.5/5).

---

### 2. Tech Adoption vs Economic Capacity
```
SELECT country,
AVG(water_related_adaptation_tech) AS tech_score,
AVG(gdp_per_capita) AS gdp_per_cap
FROM climate
GROUP BY country
HAVING AVG(water_related_adaptation_tech) > 1;
```
**High-Tech Adopters**:
| Country | Avg Tech Score | GDP/Capita |
|---------|----------------|------------|
| Egypt | 2.01 | $9,982 |
| Morocco | 1.20 | $7,324 |
| South Africa | 3.17 | $12,215 |

*Pattern*: Tech adoption correlates with higher GDP (R²=0.68) - middle-income countries lead adaptation efforts.

![1](https://github.com/user-attachments/assets/8ae9955a-87d5-490f-beb8-ee60f855af46)

---

## Tools & Methods
- **SQL**: Data aggregation, filtering, and correlation analysis
- **Python/Pandas**: Advanced statistical analysis and visualization
- **Jupyter Notebook**: Interactive exploration
- **Geospatial Analysis**: Regional clustering of water stress patterns
