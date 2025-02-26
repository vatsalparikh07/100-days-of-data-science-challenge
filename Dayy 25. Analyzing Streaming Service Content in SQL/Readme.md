# Day 25. 100 Days of Data Science Challenge - 02/25/25

# Streaming Service Content Analysis with SQL
*Exploring streaming platforms through SQL queries and data analysis*

## 🎥 Project Overview  
This project analyzes content from four major streaming services: **Amazon Prime**, **Hulu**, **Netflix**, and **Disney+**. By leveraging SQL, we explore the following questions:  
- Which platform has the most family-friendly content?  
- Which platform has the highest-rated content?  
- How do critics' and audiences' ratings differ over time?  

The analysis focuses on combining datasets, handling missing values, and extracting insights from structured data.

---

## 📂 Data Description  

The dataset includes information about movies and TV shows across four streaming platforms. Key columns:  

| **Column**         | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| `id`               | Unique identifier for each title                                               |
| `title`            | Title of the movie/TV show                                                     |
| `year`             | Release year                                                                   |
| `age`              | Age rating (e.g., "7+", "18+")                                                 |
| `imdb`             | IMDb rating                                                                    |
| `rotten_tomatoes`  | Rotten Tomatoes score                                                          |
| `genre`            | Genre of the title                                                            |
| `service`          | Streaming service (Amazon, Hulu, Netflix, Disney)                              |

---

## 🔧 Key SQL Queries and Insights  

### 1. Combining Data Across Platforms  
To analyze all platforms together, we used a `UNION ALL` query to combine the datasets while preserving service information:  

```
WITH service_data AS (
SELECT *, 'amazon' AS service FROM amazon
UNION ALL
SELECT *, 'hulu' AS service FROM hulu
UNION ALL
SELECT *, 'netflix' AS service FROM netflix
UNION ALL
SELECT *, 'disney' AS service FROM disney
)
SELECT * FROM service_data;
```

### 2. Handling Missing Data  
We inspected missing values in key columns (`imdb`, `age`, `rotten_tomatoes`) using conditional aggregation:  

```
SELECT
SUM(CASE WHEN imdb IS NULL THEN 1 ELSE 0 END) AS imdb_missing,
SUM(CASE WHEN age IS NULL THEN 1 ELSE 0 END) AS age_missing,
SUM(CASE WHEN rotten_tomatoes IS NULL THEN 1 ELSE 0 END) AS rt_missing
FROM service_data;
```

**Findings:**  
- IMDb ratings were missing for ~30% of entries.  
- Rotten Tomatoes scores were missing for ~40% of entries.  

### 3. Most Family-Friendly Streaming Service  
To determine which platform has the highest percentage of family-friendly content, we used pattern matching (`ILIKE`) to identify relevant genres:  
```
SELECT
service,
AVG(CASE
WHEN genre ILIKE '%kids%' OR genre ILIKE '%family%' OR genre ILIKE '%children%'
THEN 1 ELSE 0 END) * 100 AS pct_family_friendly
FROM service_data
GROUP BY service
ORDER BY pct_family_friendly DESC;
```


**Results:**  
| **Service**   | **% Family-Friendly Content** |
|---------------|-------------------------------|
| Netflix       | 11.06%                        |
| Hulu          | 10.99%                        |
| Amazon Prime  | 8.32%                         |

### 4. Highest-Rated Content by Platform  
We calculated the average Rotten Tomatoes scores for each platform, splitting results by movies and TV shows:  
```
SELECT
service,
CASE WHEN type = 'Movie' THEN 'Movie' ELSE 'TV Show' END AS type,
AVG(SPLIT_PART(rotten_tomatoes, '/', 1)::NUMERIC) AS avg_rt_score
FROM service_data
GROUP BY service, type
ORDER BY avg_rt_score DESC;
```

**Results:**  
| **Service**   | **Type**   | **Avg Rotten Tomatoes Score** |
|---------------|------------|-------------------------------|
| Hulu          | Movie      | 60.48                        |
| Disney+       | Movie      | 60.05                        |
| Netflix       | Movie      | 54.97                        |

### 5. Audience vs Critics Ratings Over Time  
To analyze how audience and critic ratings diverged over time, we calculated the average absolute difference between IMDb scores and Rotten Tomatoes scores: 
```
WITH scores AS (
SELECT
TO_DATE(year::TEXT, 'YYYY') AS release_date,
SPLIT_PART(rotten_tomatoes, '/', 1)::NUMERIC AS rt_score,
SPLIT_PART(imdb, '/', 1)::NUMERIC * 10 AS imdb_score
FROM service_data
WHERE imdb IS NOT NULL AND rotten_tomatoes IS NOT NULL AND year >= 2000
)
SELECT
release_date,
AVG(ABS(imdb_score - rt_score)) AS avg_difference
FROM scores
GROUP BY release_date
ORDER BY release_date;
```


**Findings:**  
- Audience and critic ratings diverged significantly in recent years (post-2010).  

---

## 🌟 Key Insights  

1. **Family-Friendly Content:**  
   - Netflix leads in family-friendly content with ~11% of its catalog geared toward children and families.

2. **Highest-Rated Content:**  
   - Hulu has the highest-rated movies on average (60.48/100).  

3. **Audience vs Critics:**  
   - The gap between audience and critic ratings has widened over time, indicating differing preferences.

4. **Data Challenges:**  
   - Missing values in IMDb and Rotten Tomatoes scores limited some analyses.

---

## 🛠️ Technical Skills Demonstrated  

1. **SQL Joins & Unions:** Combined multiple datasets while preserving platform-specific details.
2. **Text Parsing & Pattern Matching:** Used `ILIKE` and `SPLIT_PART()` to extract insights from text data.
3. **Handling Missing Data:** Identified null values and accounted for them in calculations.
4. **Aggregations & Grouping:** Leveraged conditional aggregation for platform comparisons.

---

## 📚 Lessons Learned  

1. **SQL for Multi-Dataset Analysis:** Combining datasets with different structures requires careful planning to preserve key details.
2. **Data Cleaning is Crucial:** Handling missing or inconsistent data is essential for accurate analysis.
3. **Streaming Trends are Complex:** Audience preferences vary significantly across platforms and content types.
