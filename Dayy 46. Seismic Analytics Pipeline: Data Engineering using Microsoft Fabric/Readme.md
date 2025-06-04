## 🌍 Seismic Analytics Pipeline: Data Engineering using Microsoft Fabric

Welcome to my **Seismic Analytics Pipeline** project! This is a dynamic, end-to-end data engineering solution built using **Microsoft Fabric**, designed to process and analyze earthquake data from around the globe. 

---

## 📖 Project Overview

This project leverages **Microsoft Fabric** to implement a robust **Medallion Architecture** for processing seismic event data sourced from the **USGS Earthquake API**. By combining the capabilities of **Data Factory**, **Lakehouse**, and **Power BI**, the pipeline seamlessly ingests, transforms, enriches, and visualizes earthquake data. The final output is an interactive dashboard that provides meaningful insights into global seismic activity.

The pipeline is divided into three layers:
1. **Bronze Layer**: Raw data ingestion and storage.
2. **Silver Layer**: Data transformation and cleansing.
3. **Gold Layer**: Enriched, business-ready data for reporting.

---

## 🏗️ Dynamics of Microsoft Fabric in Action

### 1. **Data Factory for Orchestration**
Microsoft Fabric’s **Data Factory** serves as the backbone of this pipeline, orchestrating notebooks for each layer:
- The pipeline executes sequentially, ensuring smooth transitions from raw data ingestion (Bronze) to enriched reporting-ready datasets (Gold).
- Parameters like `start_date` and `end_date` are dynamically passed to automate daily processing.

![Pipeline Execution](https://pplx-res.cloudinary.com/image/upload/v1742392021/user_uploads/iBaPHPYSTujNEyp/Data-Pipeline.jpg)

---

### 2. **Lakehouse as Centralized Storage**
The **Lakehouse** acts as the unified storage layer for all datasets:
- Raw GeoJSON files are stored in the `Files` folder during Bronze processing.
- Transformed tables (Silver layer) and enriched tables (Gold layer) are stored as Delta tables, enabling efficient querying and seamless integration with Power BI.
- The Lakehouse simplifies governance with centralized security policies and metadata management.

![Lakehouse Explorer](https://pplx-res.cloudinary.com/image/upload/v1742392021/user_uploads/BRaYRhXyVnizGhx/lakehouse.jpg)

---

### 3. **PySpark Notebooks for Processing**
Each layer leverages PySpark notebooks for scalable processing:
- **Bronze Layer**: Fetches raw earthquake data from the USGS API using Python’s `requests` library and stores it in its original format.
- **Silver Layer**: Cleanses and reshapes data by extracting key attributes (e.g., magnitude, coordinates, timestamps) and converting Unix time into human-readable formats.
- **Gold Layer**: Enriches data with geographical context using reverse geocoding (`reverse_geocoder` library) and adds significance classifications (`Low`, `Moderate`, `High`) based on impact scores (`sig`).

---

### 4. **Power BI for Visualization**
The final dataset feeds into an interactive Power BI dashboard that provides actionable insights:
- Earthquake distribution across countries visualized on a map.
- Magnitude analysis by type (`magType`) and region.
- Significance trends categorized by impact levels (`Low`, `Moderate`, `High`).

![Power BI Dashboard](https://pplx-res.cloudinary.com/image/upload/v1742392021/user_uploads/MvTnQXnKxQnqdAW/Sample-Power-BI-report.jpg)

---

## 🔑 Key Features of the Pipeline

### Bronze Layer: Raw Data Ingestion
- Fetches earthquake data from the USGS Earthquake API in GeoJSON format.
- Stores unprocessed data in the Lakehouse’s `Files` folder for traceability.

### Silver Layer: Data Transformation
- Converts GeoJSON files into structured tabular datasets.
- Extracts key attributes like magnitude (`mag`), coordinates (`latitude`, `longitude`), and timestamps (`time`).
- Cleanses data by converting Unix time into standard datetime formats.

### Gold Layer: Data Enrichment
- Adds country codes using reverse geocoding based on latitude and longitude.
- Introduces significance classifications (`Low`, `Moderate`, `High`) based on impact scores (`sig`).
- Prepares business-ready datasets for reporting.

---

## 📊 Insights & Results

The pipeline processes seismic event data to reveal meaningful insights:
1. Total Earthquakes Processed: **1,684**
2. Countries with Highest Activity: United States (US), Puerto Rico (PR), Japan (JP)
3. Most Common Magnitude Type: Local Magnitude (`ml`)
4. Significance Breakdown:
   - Low Impact: ~1,500 events
   - Moderate Impact: ~200 events
   - High Impact: Minimal occurrences

The Power BI dashboard enables users to interact with these insights dynamically, filtering by date ranges, significance levels, and magnitude types.

---

## 🌟 Why Microsoft Fabric?

Microsoft Fabric stands out as a unified platform that simplifies complex workflows while delivering high performance:
1. **Unified Architecture**: Combines orchestration (Data Factory), storage (Lakehouse), processing (PySpark), and visualization (Power BI) under one roof.
2. **Scalability**: Handles large-scale datasets efficiently with Delta tables and Spark-based processing.
3. **Integration**: Seamlessly connects with other Microsoft tools like Azure Synapse Analytics, Dynamics 365, and Teams.
4. **Governance & Security**: Ensures robust governance through centralized policies and role-based access controls.

---

## 🌍 Future Enhancements

While this project already delivers significant value, there’s room to expand its capabilities:
- Implement real-time streaming support for live earthquake updates.
- Integrate machine learning models to predict seismic activities based on historical patterns.
- Enhance geospatial analysis with city-level details for granular insights.

---

## 💡 Reflections & Learnings

This project was an incredible opportunity to explore how Microsoft Fabric can transform raw data into impactful insights. From orchestrating multi-layered pipelines in Data Factory to enriching datasets with geospatial intelligence in PySpark notebooks, every step highlighted the power of modern analytics platforms.

Some key takeaways:
- The Medallion Architecture ensures structured refinement of datasets at scale.
- Reverse geocoding adds immense value when working with geospatial datasets.
- Power BI’s integration with Lakehouse simplifies reporting workflows dramatically.
