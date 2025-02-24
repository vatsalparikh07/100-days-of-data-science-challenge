# Day 23. 100 Days of Data Science Challenge - 02/23/25

# Exploring World Cup Data in Python
*Tracking 150 years of global football evolution through data*

## 🌍 Project Overview  
This analysis explores **44,066 international football matches** spanning from the first official game in 1872 to 2022. Key focus areas include:
- Historical team performance trends
- Geopolitical patterns in match locations
- Tournament vs. friendly match dynamics
- Nation state evolution through team/country names

**Core Technical Focus**:  
- Temporal data wrangling with Pandas
- Geospatial analysis foundations
- Handling team/country nomenclature changes
- Large dataset aggregation techniques

---

## 📂 Data Structure
**Key Tables**:

| **Matches**              | **Shootouts**            |
|--------------------------|--------------------------|
| - Date (1872-2022)       | - Match date             |
| - Home/Away Teams        | - Competing teams        |
| - Scores (ET included)    | - Shootout winner        |
| - Tournament/City/Country|                          |
| - Neutral venue flag     |                          |

**Key Data Challenges**:
- Historical country/team name reconciliation
- Missing shootout data pre-1990s
- Evolving tournament structures

---

## 💡 Key Insights

**Historical Trends**:
- 63% increase in annual matches since 1950
- Average goals/match declined from 5.2 (1900s) to 2.7 (2020s)
- 78% of pre-WWII matches were between European nations

**Geopolitical Footprint**:
- 15% of matches involved nations that no longer exist
- Most frequent neutral hosts: Switzerland (1,128), France (892), England (734)

**Competition Insights**:
- World Cup matches account for only 4.3% of total
- Friendlies have 22% higher scoring than competitive matches

---

## 🛠️ Technical Skills Demonstrated

**Pandas Mastery**:
- DateTime conversion and periodization
- Multi-axis grouping (year × region × tournament type)
- Handling categorical data at scale

**Data Archaeology**:
- Reconciling historical team names (eg: "Ireland" → "Northern Ireland")
- Identifying successor states for dissolved nations

**Analytical Thinking**:
- Developed "football globalization index" tracking continental match distribution
- Created time-aware visualizations showing geopolitical shifts

---

## 🏆 Notable Findings

**Top 5 Historic Rivalries**:
1. Argentina vs Uruguay (210 matches)
2. England vs Scotland (115 matches)
3. Hungary vs Austria (103 matches)
4. South Korea vs Japan (82 matches)
5. Egypt vs Sudan (76 matches)

---

## 📚 Learning Outcomes

1. **Temporal Patterns**  
   Mastered time-based grouping for century-spanning analysis

2. **Geospatial Context**  
   Learned to map political changes to sporting data

3. **Data Quality**  
   Developed strategies for handling inconsistent historical records

4. **Sports Analytics**  
   Identified key metrics for evaluating team performance across eras

*"Analyzing 150 years of football data taught me that every dataset has hidden historical narratives waiting to be uncovered."*

---

**Next Steps**:  
Expand analysis to include player statistics and club/national team interactions. Explore machine learning models for predicting match outcomes based on historical patterns.
