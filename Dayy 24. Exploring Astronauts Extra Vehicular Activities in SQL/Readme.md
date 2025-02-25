# Day 24. 100 Days of Data Science Challenge - 02/24/25

# Astronaut Extravehicular Activity (EVA) Analysis: A SQL Journey Through Spacewalks  
*Analyzing 60+ years of human spaceflight history through Extravehicular Activities*

## 🚀 Project Overview  
This project dives into the fascinating world of space exploration by analyzing astronaut extra-vehicular activities (EVA) using SQL. By leveraging datasets on astronaut missions, we uncover patterns in EVA durations, purposes, and programs over time.

**Key Objectives:**
- Analyze the most common EVA purposes.
- Calculate the total material collected during EVAs.
- Identify astronauts with the most EVA time.
- Explore cumulative EVA durations over time by space program.

---

## 📂 Data Description  
The dataset contains detailed records of astronaut EVAs, including:  

| **Column**   | **Description**                                                                 |
|--------------|---------------------------------------------------------------------------------|
| `date`       | Date of the EVA                                                                |
| `country`    | Country conducting the EVA                                                     |
| `vehicle`    | Spacecraft or station used for the EVA                                         |
| `duration`   | Duration of the EVA in minutes                                                 |
| `crew`       | Astronaut(s) involved in the EVA                                               |
| `purpose`    | Purpose of the EVA (e.g., repair, installation, photography)                   |
| `year`       | Year of the EVA                                                                |
| `program`    | Space program (e.g., Apollo, ISS, Gemini)                                      |

---

## 🔧 Key SQL Queries and Insights  

### 1. Most Common Types of EVAs  
Using text pattern matching (`ILIKE`) and `CASE` statements, we categorized EVAs into four main types: photography, collection, installation, and repair.

```
SELECT
SUM(photography) AS count,
'photography' AS type
FROM purposes
UNION
SELECT
SUM(collection) AS count,
'collection' AS type
FROM purposes
UNION
SELECT
SUM(installation) AS count,
'installation' AS type
FROM purposes
UNION
SELECT
SUM(repair) AS count,
'repair' AS type
FROM purposes
ORDER BY count DESC;
```

**Results:**  
- Installations: 189 EVAs  
- Repairs: 77 EVAs  
- Collections: 16 EVAs  
- Photography: 13 EVAs  

---

**Results:**  
- Installations: 189 EVAs  
- Repairs: 77 EVAs  
- Collections: 16 EVAs  
- Photography: 13 EVAs  

---

### 2. Total Material Collected During EVAs  
Using regular expressions (`SUBSTRING`) to extract numerical values from text descriptions in the `purpose` column, we calculated the total amount of geological material collected during EVAs.  

```
WITH weights AS (
SELECT
SUBSTRING(purpose, '(\d+.?\d*) lb of ((rock)|(geologic))') AS weight
FROM evas
)
SELECT SUM(weight::NUMERIC) AS total_material_collected
FROM weights;
```
**Total Material Collected:**  
1,008.3 lbs of geological material.

---

### 3. Astronauts with the Most EVA Time  
By splitting the `crew` column into individual astronauts and summing their respective durations, we identified astronauts with the highest cumulative EVA time.  
```
WITH astronauts_split AS (
SELECT
SPLIT_PART(crew, ',', 1) AS astronaut,
duration
FROM evas
UNION ALL
SELECT
SPLIT_PART(crew, ',', 2) AS astronaut,
duration
FROM evas
WHERE SPLIT_PART(crew, ',', 2) != ''
)
SELECT astronaut, SUM(duration) AS total_duration
FROM astronauts_split
GROUP BY astronaut
ORDER BY total_duration DESC
LIMIT 10;
```
**Top Astronauts by Total EVA Time:**  
1. Jerry Ross: 3,501 minutes  
2. Anatoly Solovyev: 3,086 minutes  
3. Mike Lopez-Alegria: 3,344 minutes  
---

### 4. Cumulative Time Spent in EVAs Over Time by Program  
Using a window function (`SUM() OVER`) to calculate cumulative durations by year and program:  
```
SELECT
year,
program,
SUM(duration) OVER(PARTITION BY program ORDER BY year) AS cumulative_duration
FROM (
SELECT year, program, SUM(duration) AS duration
FROM evas
GROUP BY year, program
) subquery;
```

**Insights:**  
- Apollo missions saw a sharp increase in cumulative EVA durations during moon landings (1969–1972).  
- ISS dominates modern EVAs with over 20,000 cumulative minutes.
  
---

## 🌌 Key Findings  

1. **EVA Purposes:**  
   - Installations dominate modern EVAs due to ISS construction.
   - Repairs remain critical for spacecraft functionality.

2. **Material Collection:**  
   - A total of **1,008 lbs** of geological material has been collected during EVAs.

3. **Astronaut Contributions:**  
   - Jerry Ross leads with over **58 hours** of EVA time.

4. **Program Evolution:**  
   - Early programs like Gemini had shorter experimental EVAs.
   - Apollo missions introduced longer lunar surface activities.
   - ISS missions emphasize maintenance and installations.

---

## 🛠️ Technical Skills Demonstrated  

1. **SQL Aggregations:**  
   - Used `SUM`, `COUNT`, and `GROUP BY` to analyze cumulative metrics.

2. **Text Pattern Matching:**  
   - Extracted numerical data using regular expressions (`SUBSTRING`) for advanced text analysis.

3. **Data Splitting and Transformation:**  
   - Split multi-value columns (`crew`) into individual rows for detailed analysis.

4. **Window Functions:**  
   - Applied cumulative calculations to analyze trends over time.

---

## 📚 Lessons Learned  

1. **SQL for Complex Analysis:**  
   SQL is a powerful tool for extracting insights from structured datasets with advanced techniques like text parsing and window functions.

2. **Evolving Mission Objectives:**  
   The shift from short experimental EVAs to long-duration maintenance tasks reflects advancements in space technology.

3. **Data Cleaning Challenges:**  
   Handling multi-value columns like `crew` required creative solutions to ensure accurate analysis.

---

*"This project highlights how data science can bring historical achievements to life while deepening technical expertise."*  
