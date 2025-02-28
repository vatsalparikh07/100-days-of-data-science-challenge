# Day 28. 100 Days of Data Science Challenge - 02/28/25

# Students' Mental Health Analysis in SQL
*Exploring the impact of social connectedness and cultural stress on student mental health*

## 🧠 Project Overview  
This project analyzes a dataset on the mental health of domestic and international students at a Japanese university. Using SQL, we explore how factors like social connectedness and acculturative stress affect mental health outcomes. Additionally, we visualize these insights using Python's Plotly library.

**Key Objectives:**
- Compare mental health scores (PHQ-9, SCS, ASISS) between domestic and international students.
- Investigate the influence of age and length of stay on mental health scores.
- Identify trends in social connectedness and acculturative stress.
- Visualize findings through interactive plots.

---

## 📂 Dataset Description  

The dataset contains survey responses from 268 students, including both domestic and international participants. Key columns include:  

| **Column**         | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| `inter_dom`        | Student type: Domestic (`Dom`) or International (`Inter`)                      |
| `Region`           | Region of origin for international students                                    |
| `Age`              | Age of the student                                                            |
| `Stay`             | Length of stay in Japan (in years)                                             |
| `ToDep`            | Total PHQ-9 score (depression diagnostic test)                                 |
| `ToSC`             | Total SCS score (social connectedness scale)                                   |
| `ToAS`             | Total ASISS score (acculturative stress scale)                                 |

---

## 🔧 Key Analysis Steps  

### 1. Data Inspection  
- Verified the dataset contains 268 records.  
- Checked for missing or unclassified rows in the `inter_dom` column.  
- Examined the regional distribution of international students.

### 2. Summary Statistics  
- Calculated minimum, maximum, and average scores for PHQ-9, SCS, and ASISS across all students.  
- Compared these statistics between domestic and international students.

### 3. Impact of Age on Mental Health Scores  
- Grouped international students by age to calculate average scores for PHQ-9, SCS, and ASISS.  
- Identified trends in mental health outcomes across different age groups.

### 4. Influence of Length of Stay  
- Analyzed how the length of stay in Japan impacts the mental health scores of international students.  

### 5. Visualizations with Plotly  
- Created histograms to compare PHQ-9 score distributions between domestic and international students.  
- Used box plots to visualize score ranges and outliers for each group.  
- Built an interactive heatmap to explore correlations between continuous variables like age, stay duration, and mental health scores.

---

## 🌟 Key Findings  

1. **Mental Health Differences:**  
   - International students show higher average PHQ-9 scores (depression) compared to domestic students.
   - Social connectedness (SCS) is lower among international students, while acculturative stress (ASISS) is significantly higher.

2. **Age Trends:**  
   - Younger international students (ages 17–20) tend to have lower depression scores but higher acculturative stress compared to older students.

3. **Length of Stay:**  
   - Students who have stayed longer in Japan report lower acculturative stress but do not show significant differences in depression scores.

4. **Regional Insights:**  
   - The majority of international students come from Asia, followed by Europe and North America.

5. **Correlations:**  
   - Strong negative correlation between social connectedness (SCS) and depression (PHQ-9).  
   - Positive correlation between acculturative stress (ASISS) and depression.

---

## 🛠️ Technical Skills Demonstrated  

1. **SQL Analysis:**  
   - Used aggregation functions (`MIN`, `MAX`, `AVG`) to compute summary statistics.
   - Applied conditional filtering to separate domestic and international student data.
   - Grouped data by categorical variables like age and region for detailed analysis.

2. **Data Visualization with Plotly:**  
   - Created histograms, box plots, and heatmaps for interactive exploration.
   - Added dropdown interactivity to filter visualizations by student type.

3. **Correlation Analysis:**  
   - Computed Pearson correlation coefficients to identify relationships between variables.

4. **Data Cleaning:**  
   - Identified unclassified rows in the dataset and excluded them from analysis.

---

## 📚 Lessons Learned  

1. **Mental Health Analysis Requires Context:**  
   Understanding cultural and social factors is crucial when interpreting mental health data.

2. **SQL for Exploratory Data Analysis:**  
   SQL is a powerful tool for grouping, filtering, and summarizing complex datasets.

3. **Visualization Enhances Insights:**  
   Interactive plots help uncover patterns that might be missed in raw data summaries.

4. **Correlation ≠ Causation:**  
   While correlations provide valuable clues, further investigation is needed to establish causality.

---

*"This project highlights how data science can provide actionable insights into critical issues like student mental health."*  
