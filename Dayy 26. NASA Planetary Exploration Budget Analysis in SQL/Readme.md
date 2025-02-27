# Day 26. 100 Days of Data Science Challenge - 02/26/25

# NASA Planetary Exploration Budget Analysis in SQL
*Unveiling NASA's planetary exploration spending patterns over the decades*

## 🚀 Project Overview  
This project explores NASA's planetary exploration budgets using SQL, analyzing costs across missions, destinations, and time. By leveraging inflation-adjusted data, we gain insights into the financial priorities of NASA's space programs and the economic factors influencing space exploration.

**Key Objectives:**
- Calculate total and inflation-adjusted costs for all planetary missions.
- Identify the most expensive mission and destination.
- Analyze spending trends over time and across destinations.
- Explore budget allocation by mission components (e.g., spacecraft, operations).

---

## 📂 Data Description  

### **Tables Used**:
1. **`mission_budgets`**  
   Contains detailed cost breakdowns for each mission by fiscal year.  
   | **Column**        | **Description**                                                                 |
   |-------------------|---------------------------------------------------------------------------------|
   | `mission`         | Name of the mission                                                            |
   | `fiscal_year`     | Fiscal year of the budget                                                      |
   | `cost_type`       | Fine-grained aspect of the project (e.g., "Spacecraft")                        |
   | `cost_group`      | Broader aspect of the project (e.g., "Development/Implementation")             |
   | `cost_MUSD`       | Cost in million US dollars                                                    |

2. **`inflation`**  
   Provides inflation adjustment factors for each fiscal year.  
   | **Column**              | **Description**                                                         |
   |-------------------------|-------------------------------------------------------------------------|
   | `fiscal_year`           | Fiscal year                                                            |
   | `inflation_adjustment`  | Factor to adjust costs to current currency values                      |

3. **`mission_details`**  
   Contains metadata about each mission, including its destination and program.  
   | **Column**              | **Description**                                                         |
   |-------------------------|-------------------------------------------------------------------------|
   | `mission`               | Name of the mission                                                    |
   | `destination`           | Destination in the solar system                                        |
   | `program`               | NASA program associated with the mission                               |

---

## 🔧 Key SQL Queries and Insights  

### 1. Total Cost of All Missions (Inflation Adjusted)  
We calculated the total inflation-adjusted cost for all planetary missions:  

```
SELECT SUM("cost_MUSD" * inflation_adjustment) AS adjusted_total_cost_MUSD
FROM mission_budgets
LEFT JOIN inflation
USING (fiscal_year);
```

**Result:**  
NASA has spent approximately **$195 billion (adjusted)** on planetary exploration.

### 2. Most Expensive Mission  
To find the most expensive mission in NASA's history:  
```
SELECT mission, SUM("cost_MUSD" * inflation_adjustment) AS adjusted_total_cost_MUSD
FROM mission_budgets
LEFT JOIN inflation
USING (fiscal_year)
GROUP BY mission
ORDER BY adjusted_total_cost_MUSD DESC
LIMIT 1;
```

**Result:**  
The **Viking program** was NASA's most expensive mission, costing approximately **$7.2 billion (adjusted)**.

### 3. Spending Trends Over Time  
To analyze how NASA's spending evolved over time:  
```
SELECT fiscal_year, SUM("cost_MUSD" * inflation_adjustment) AS adjusted_total_cost_MUSD
FROM mission_budgets
LEFT JOIN inflation
USING (fiscal_year)
GROUP BY fiscal_year
ORDER BY fiscal_year;
```

We visualized this data using a bar plot:  

**Insights:**  
- Peaks in spending correspond to major projects like Apollo and Viking missions.
- Budget fluctuations reflect economic conditions and political priorities.

### 4. Spending by Destination  
To identify which destinations received the most funding:  

```
SELECT destination, SUM("cost_MUSD" * inflation_adjustment) AS adjusted_total_cost_MUSD
FROM mission_budgets
LEFT JOIN inflation USING (fiscal_year)
LEFT JOIN mission_details USING (mission)
GROUP BY destination
ORDER BY adjusted_total_cost_MUSD DESC;
```

**Results:**  
| **Destination**       | **Total Cost (Adjusted)** |
|------------------------|---------------------------|
| Mars                  | $31.7 billion            |
| Outer Planets         | $21.8 billion            |
| The Moon              | $12.9 billion            |

### 5. Spending by Mission Component (Cost Type)  
To determine which parts of a mission are most expensive:  
```
SELECT cost_type, AVG("cost_MUSD") AS average_cost
FROM mission_budgets
GROUP BY cost_type
ORDER BY average_cost DESC;
```

**Results:**  
| **Cost Type**                  | **Average Cost (MUSD)** |
|--------------------------------|-------------------------|
| Implementation (incl LV)       | $185.75                |
| Development (incl LV)          | $104.88                |
| Formulation                    | $102.18                |

### 6. Programs with Multiple Destinations  
To find NASA programs with missions targeting multiple destinations:  
```
SELECT program, COUNT(DISTINCT destination) AS num_destinations
FROM mission_details
GROUP BY program
HAVING COUNT(DISTINCT destination) > 1;
```

**Programs with Multiple Destinations:**  
1. Discovery Program – 14 destinations  
2. Mariner Program – 6 destinations  

---

## 🌌 Key Findings  

1. **Total Spending:**  
   - NASA has spent approximately **$195 billion (adjusted)** on planetary exploration since its inception.

2. **Most Expensive Mission:**  
   - The Viking program was the most expensive at **$7.2 billion**, reflecting its ambitious goals of landing on Mars.

3. **Destination Priorities:**  
   - Mars received the highest funding (~$31.7 billion), followed by Outer Planets (~$21.8 billion).

4. **Spending Trends:**  
   - Peaks in spending align with major missions like Apollo and Viking.
   - Recent years show steady investment in Mars and ISS-related projects.

5. **Mission Components:**  
   - Implementation and development account for the largest share of costs.

6. **Program Diversity:**  
   - Programs like Discovery target multiple destinations, showcasing NASA's broad exploration goals.

---

## 🛠️ Technical Skills Demonstrated  

1. **SQL Joins & Aggregations:** Combined multiple tables to calculate total costs and analyze trends.
2. **Inflation Adjustment:** Applied correction factors to ensure accurate comparisons over time.
3. **Data Visualization:** Used Python libraries like Plotly to create insightful visualizations.
4. **Text Analysis in SQL:** Grouped and filtered data based on categorical columns like `destination`.

---

## 📚 Lessons Learned  

1. **Budget Analysis Requires Context:** Adjusting for inflation is crucial when comparing costs across decades.
2. **Mars Dominates Funding:** Mars remains a key focus for NASA due to its scientific potential.
3. **SQL for Financial Analysis:** SQL is an effective tool for analyzing large-scale financial datasets.
