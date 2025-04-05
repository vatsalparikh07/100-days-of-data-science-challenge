# Day 64. 100 Days of Data Science Challenge - 04/05/2025

# 🍔 Fast Food, Fat Stats & Fatal Facts  
> **Mapping the geography and nutrition of America’s fast food culture**  

## 📍 Project Snapshot

This project dives deep into the data behind the United States' fast food obsession. By combining **nutritional data** from over **1,000 menu items** with **location data** for **10,000+ restaurants**, we explore the link between fast food availability and **public health metrics** like obesity.

We’ve used powerful visualizations to illuminate how a $142.55 billion industry may be silently shaping America's health crisis.

![image](https://github.com/user-attachments/assets/61e6a4e1-630b-4549-97a5-2ad4965915c0)
*Urban clusters and obesity rates across the U.S.*

---

## 🎯 Goals & Objectives

- **📌 Map fast food hotspots** across urban and rural U.S.
- **🍽️ Visualize nutritional patterns** (calories, sodium, sugar, fat)
- **⚠️ Identify public health risks** linked to fast food density
- **📊 Reveal correlations** between nutrients and geographic clusters
- **🎯 Highlight chain-specific trends** in nutritional content

---

## 📚 What We Did (aka The Recipe)

### 🧾 Datasets Used

- **Fast Food Locations:** 10K+ restaurants from Datafiniti’s business database  
- **Nutrition Dataset:** 1,072 menu items from 6 major chains  
- **Public Health Data:** CDC obesity statistics, US Census data

### 🧼 Data Preprocessing

- Cleaned and standardized units  
- Removed duplicates and null values  
- Converted strings to floats for nutritional metrics  
- Aggregated data by chain and region  

---

## 📈 The Visualization Menu

### 🍟 Nutritional Breakdown

- **Violin Plots** – Show fat distribution across chains

![image](https://github.com/user-attachments/assets/00103efd-8605-4858-b83b-0d5dec5cbb4e)

- **Box Plots** – Saturated fat outliers? You bet.

![image](https://github.com/user-attachments/assets/5942e2de-f17d-474a-94ef-dd71cf228cda)

- **Scatter Plots** – Calories vs Sodium, Sugar vs Calories

![image](https://github.com/user-attachments/assets/0ac2fedb-9516-45b5-9c48-c7bb3c4169c6)

- **Histograms** – Skewed sugar levels in desserts & drinks

![image](https://github.com/user-attachments/assets/d8bcec3c-8d13-402d-9c97-0817dc776b43)


> 🧠 **Insights:**  
> - 72% of items exceeded one or more daily limits  
> - KFC’s family items routinely hit 2500mg+ sodium  
> - McDonald's desserts often surpass 50g of sugar  

### 🗺️ Geographic Heat

- **Folium Interactive Maps** – Clustered, clickable, filterable  
- **Choropleth Layers** – Fast food density vs. obesity rates  
- **Bubble Maps** – Zoom into cities with >500+ outlets  
- **Highway Proximity** – 78% of outlets are within 2 miles of major highways

> 🧭 **Findings:**  
> - Atlanta has 1,072 fast food locations (highest)  
> - Urban areas house 65% of all restaurants  
> - Restaurant density correlates (r=0.78) with state obesity rates  

![image](https://github.com/user-attachments/assets/9ef2cfb5-3e38-482a-96d4-2d3c6424fcbc)
*Calories vs Sugar: The red line marks the daily limit (25g).*

---

## 🧠 Mind-blowing Insights

| Chain         | Sodium Leader 🧂 | Sugar Overload 🍬 | Nutritional Consistency 📉 |
|---------------|------------------|-------------------|-----------------------------|
| McDonald’s    | Moderate          | **Highest**       | Medium                      |
| KFC           | **Highest**       | High              | Low                         |
| Pizza Hut     | Low               | Low               | **Most consistent**         |
| Taco Bell     | Medium            | Medium            | Regional clustering         |

- Family-sized items often contain **140–180%** of sodium recommendations  
- Breakfast items showed unusually high sodium levels  
- Urban areas have fast food outlets every **1.2 miles** on average  

---

## 🧭 Visual Walkthrough

### 📌 Filterable Brand Maps  
Color-coded clusters by chain – explore individual restaurants or zoom in by city.

![image](https://github.com/user-attachments/assets/cc06f8e6-7bd5-49dc-a61d-69865b791d17)

![image](https://github.com/user-attachments/assets/a5464240-1a3a-49d9-b5b7-435f72306ec2)

### 🍴 Nutrient Explosion  
Tree maps and scatter plots that scream, “That’s too much sodium!”

![image](https://github.com/user-attachments/assets/24c600e5-53e9-44c6-a7e8-003b28ed4771)

![image](https://github.com/user-attachments/assets/25d0614c-fa53-45a6-be3f-7f5af65ea6e4)

---

## 🙌 Special Mentions

- 📦 [Datafiniti Fast Food Dataset](https://www.kaggle.com/datasets/datafiniti/fast-food-restaurants)  
- 📊 Folium, Plotly, Pandas, NumPy, Matplotlib  
- 🏥 CDC, FDA, WHO guidelines on sodium/sugar  
- 📌 U.S. Census demographic overlays  
