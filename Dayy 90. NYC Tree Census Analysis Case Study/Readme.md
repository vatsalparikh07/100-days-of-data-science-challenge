## NYC Tree Census Analysis: Identifying Optimal Species for Manhattan 🏙️🌳

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Wrangling-yellowgreen?style=flat-square&logo=pandas)](https://pandas.pydata.org/)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-Spatial_Analysis-9cf?style=flat-square)](https://geopandas.org/)
[![Visualization](https://img.shields.io/badge/Viz-Matplotlib%2C_Seaborn%2C_Missingno-blueviolet?style=flat-square)](https://matplotlib.org/)
[![Dataset](https://img.shields.io/badge/Dataset-NYC_OpenData-orange?style=flat-square)](https://opendata.cityofnewyork.us/data/)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_90-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Data-Driven Recommendations for Urban Greening

Welcome to Day 90 of my #100DaysOfDataScience challenge! Urban trees are vital infrastructure, improving air quality, reducing heat, and enhancing well-being. This project tackles a real-world urban planning problem: **Which tree species are the best candidates for future planting on the streets of Manhattan?**

Working with the **2015 NYC Street Tree Census** and **Neighborhood Tabulation Area (NTA)** data, this analysis aims to provide data-driven recommendations to the city's planning department. We define "best" based on the city's priorities: **tree size (using trunk diameter, `tree_dbh`, as a proxy) and overall health (`health`)**.

**The Mission:**
*   Ingest, clean, and integrate tree census data with neighborhood geographic information.
*   Focus specifically on trees within **Manhattan**.
*   Analyze species distribution, size characteristics, health status, and common problems.
*   Identify species that tend to be both **large** and **healthy** within the Manhattan environment.
*   Visualize findings to support recommendations.

---

## ✨ Key Features & Concepts Mastered

*   **Geospatial Data Integration:** Utilized **GeoPandas** to perform a **spatial join**, accurately identifying trees located *within* Manhattan NTA boundaries by linking point geometry (from tree lat/lon) with polygon geometry (from neighborhood shapefile).
*   **Data Cleaning & Preparation:**
    *   Handled missing values (`NaN`) in critical columns like `health` and `spc_common` using `fillna` (with 'Unknown') and strategic dropping (`dropna`) where appropriate.
    *   Addressed data inconsistencies and filtered for relevant tree statuses (focusing on 'Alive' trees).
    *   Visualized missing data patterns using `missingno`.
*   **Exploratory Data Analysis (EDA):**
    *   Analyzed distributions of tree diameter (`tree_dbh`) and health status (`health`).
    *   Identified the most common tree species (`spc_common`) planted in Manhattan.
*   **Species Performance Analysis:**
    *   Calculated key statistics (mean/median `tree_dbh`, health status proportions, problem indicator frequencies) **grouped by species** (`.groupby('spc_common')`).
    *   Filtered out species with insufficient counts (`n > threshold`) to ensure robust analysis.
    *   Ranked species based on combined criteria of average size and prevalence of 'Good' health ratings.
*   **Problem Indicator Analysis:** Investigated the frequency of root, trunk, and branch problems (`root_stone`, `trunk_wire`, etc.) across different species to identify more resilient varieties.
*   **Data Visualization:** Employed **Matplotlib** and **Seaborn** to create informative plots:
    *   Histograms for `tree_dbh`.
    *   Bar charts for species counts, average diameter by species, and health status by species.
    *   Matrix plot (`missingno.matrix`) for visualizing data completeness.
    *   (Potentially) Geospatial plots showing tree distribution or health patterns across Manhattan NTAs.

---

## 🛠️ Tech Stack: The Urban Data Science Toolkit

*   **Core Language:** Python 3.8+
*   **Data Handling:** Pandas (DataFrames, CSV I/O, cleaning, aggregation)
*   **Geospatial Analysis:** GeoPandas (GeoDataFrames, spatial join `sjoin`, reading GeoJSON/Shapefiles)
*   **Numerical Computing:** NumPy
*   **Missing Data Visualization:** MissingNo (`msno`)
*   **Static Visualization:** Matplotlib (`pyplot`), Seaborn
*   **Environment:** Jupyter Notebook (`solution.ipynb`)

---

## 🗺️ The Analytical Workflow: From Census Data to Planting Recommendations

This project follows a structured approach to analyzing the urban forest (detailed in `solution.ipynb`):

1.  **Load & Integrate Data:**
    *   Read the tree census CSV (`trees.csv`) into a Pandas DataFrame (`trees`).
    *   Read the neighborhood boundaries GeoJSON (`neighborhoods.geojson`) into a GeoPandas GeoDataFrame (`neighborhoods`).
    *   **Crucial Step:** Convert the `trees` DataFrame into a GeoDataFrame (`trees_gdf`) using `gpd.GeoDataFrame(...)` with geometry created from `longitude` and `latitude` columns (`gpd.points_from_xy`), ensuring the Coordinate Reference System (CRS) matches the `neighborhoods` data.
    *   Perform a **spatial join** (`gpd.sjoin(trees_gdf, manhattan_neighborhoods, predicate='within')`) to filter for trees strictly within Manhattan boundaries, creating `manhattan_trees`. This is more accurate than simple string matching on `nta_name`.

2.  **Initial Cleaning & EDA:**
    *   Inspect `manhattan_trees` for missing values using `.isnull().sum()` and visualize patterns with `msno.matrix()`.
    *   Handle `NaN`s in `spc_common` and `health` (e.g., `fillna('Unknown')`).
    *   Filter out non-relevant statuses (keep only `status == 'Alive'`).
    *   Visualize the distribution of `tree_dbh` using `sns.histplot`.
    *   Visualize the counts of different `health` statuses (`sns.countplot`).
    *   Identify and visualize the top N most common species (`value_counts().head(N)`, `sns.barplot`).

![image](https://github.com/user-attachments/assets/eb7bf2c9-72bf-4832-9b5c-1c607ad34371)
*Fig 2: Visualizing missing values using Missingno.*

![image](https://github.com/user-attachments/assets/6a6fa28d-e8a0-453b-87a6-e5b2ebfd1331)
*Fig 3: Distribution of Dead Trees in Manhattan.*

3.  **Species Performance Analysis:**
    *   Group the `manhattan_trees` DataFrame by `spc_common`.
    *   Calculate key metrics per species:
        *   Mean and Median `tree_dbh`.
        *   Count of trees (`size()`).
        *   Proportion of 'Good', 'Fair', 'Poor' health statuses (`value_counts(normalize=True)` within groups).
        *   Proportion of trees with specific problems (e.g., `root_stone == 'Yes'`).
    *   Filter out species with low counts (e.g., `n < 50`) for more reliable statistics.
    *   Combine metrics into a summary DataFrame.

![image](https://github.com/user-attachments/assets/0ea7adc8-68cb-4191-89b5-693c64d95126)
*Fig 4: Most common tree species in Manhattan*

4.  **Identifying "Best" Species & Visualization:**
    *   Filter the summary DataFrame for species with a high proportion of 'Good' health ratings (e.g., > 80%).
    *   Sort these healthy species by their mean or median `tree_dbh` in descending order.
    *   Visualize the top candidates using bar charts comparing average diameter and potentially health distribution.
    *   Optionally, visualize species with low problem indicator rates.

![image](https://github.com/user-attachments/assets/7fa318b9-6011-4aeb-8ddc-4edc706181bd)
*Fig 5: Count of Trees per Neighbourhood*

![image](https://github.com/user-attachments/assets/b9b27865-784a-497d-b107-c1b84c5fcb9f)
*Fig 6: A visualization of Manhattan's neighborhoods and tree locations*

5.  **Drawing Conclusions & Recommendations:**
    *   Synthesize the findings: Identify species that consistently appear large, healthy, and relatively problem-free in the Manhattan context based on the 2015 data.
    *   Acknowledge limitations (single year snapshot, potential biases in census data).

---

## 💡 Key Insights & Impact

![image](https://github.com/user-attachments/assets/51d03d92-5e31-43fd-985f-c933a3827ca0)
*Fig 7: Tree species the city should plant based on typical findings for NYC Tree Census data*

*   **Dominant Species:** Manhattan streets are often dominated by species like Honeylocust, Callery Pear, Ginkgo, and London Planetree. Understanding their performance is crucial.
*   **Size vs. Health Trade-offs:** Some large-growing species might be more prone to health issues or infrastructure conflicts (root problems), while smaller species might be healthier but provide less canopy cover. The analysis aims to find the sweet spot.
*   **Species Resilience:** Identified species (e.g., potentially Zelkova, certain Oaks, or Maples depending on specific results) that exhibit both good size potential and higher proportions of 'Good' health ratings with fewer reported problems in the Manhattan environment.
*   **Actionable Recommendations:** Provided the NYC planning department with a data-driven short-list of species likely to thrive and contribute positively to the urban canopy based on historical performance.
*   **Geospatial Context is Key:** Using GeoPandas ensures the analysis is accurately confined to Manhattan, preventing skewed results from including trees in other boroughs.

---

*Day 90 of #100DaysOfDataScience successfully combined Pandas, GeoPandas, and visualization to extract meaningful recommendations for NYC's urban forest management. Applying data science for greener cities! - Vatsal Parikh*
