# Day 31. 100 Days of Data Science Challenge - 03/03/2025

# Air Force Personnel Data Exploration in Python
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-%23150458)](https://pandas.pydata.org/) 
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75)](https://plotly.com/python/)

## 🔍 Project Focus  
Analyze 2010 US Air Force personnel data to uncover demographic patterns in gender representation, racial diversity, and career progression through paygrade levels.

---

## 📊 Dataset Overview  
- **Source**: [data.gov](https://catalog.data.gov/dataset/demographics-profile-of-active-duty-military-personnel)
- **Records**: 331,486 personnel (Air Force subset)
- **Key Features**:
  ```['service', 'gender', 'race', 'hispanicity', 'paygrade', 'count']```
- **Demographic Groups**:
- Gender: Male/Female
- Race: 7 categories including WHITE (63.2%), BLACK (14.8%), ASIAN (4.1%)
- Paygrades: Enlisted (E00-E09), Warrant Officers (W01-W05), Commissioned Officers (O01-O10)

---

## 🔬 Key Analyses  

### 1️⃣ Gender Distribution  
![Gender Distribution](https://github.com/user-attachments/assets/f079085a-b9b1-4704-981e-900e3b625736)  
- **Male Dominance**: 80.6% of personnel (267,286)  
- **Female Representation**: 19.4% (64,200)  

```px.bar(total_counts_by_gender, x='count', y='gender', title="Personnel by Gender")```

### 2️⃣ Racial Composition  
```
race_order = ['WHITE', 'BLACK', 'ASIAN', 'AMI/ALN', 'MULTI', 'P/I', 'UNK']
px.bar(total_counts_by_race, x='count', y='race', category_orders={'race': race_order})
```
- **Top 3 Races**:  
  | Race   | Percentage | Count  |
  |--------|------------|--------|
  | White  | 63.2%      | 209,532|
  | Black  | 14.8%      | 49,087 |
  | Asian  | 4.1%       | 13,612 |

### 3️⃣ Career Progression Insights  
**Highest Achieved Paygrades**:  
```air_force_nz.query('gender == "FEMALE"').tail(1)[['paygrade', 'count']]```

| Gender | Highest Paygrade | Count |
|--------|------------------|-------|
| Female | O09              | 1     |
| Hispanic| O08             | 1     |

**Paygrade Distribution**:  
![Paygrade Pattern](https://github.com/user-attachments/assets/9c211a1e-2547-4d0e-84e6-4610fcb3d0b5)  

```
px.line(total_counts_by_paygrade, x='paygrade', y='count', title="Personnel Distribution Across Paygrades")
```
---

## 🛠️ Technical Workflow  
1. **Data Preparation**
```
air_force = dod_demographics.query('service == "Air Force"')
air_force_nz = air_force.sort_values('paygrade').query('count > 0')
```

2. **Group Analysis**  
```
Gender analysis
air_force.groupby('gender').sum().reset_index()

Race analysis with sorting
total_counts_by_race.sort_values('count', ascending=False)
```

3. **Visual Exploration**  
- Horizontal bar plots for demographic comparisons  
- Line charts for ordinal paygrade analysis  

---

## 💡 Key Findings  
1. **Gender Disparity**:  
- Male personnel outnumber females 4:1 overall  
- Highest female officer at O09 vs male at O10

2. **Racial Representation**:  
- White personnel dominate senior paygrades  
- Asian representation peaks at mid-level positions

3. **Career Progression**:  
- Enlisted personnel (E grades) make up 82% of force  
- Officer ranks (O grades) show exponential drop-off above O06

---

## 🧠 Skills Practiced  
- **Data Wrangling**: pandas filtering/sorting (`query()`, `sort_values()`)  
- **Group Analysis**: `groupby()` operations with count aggregation  
- **Visual Storytelling**: Plotly bar/line plots for demographic patterns  
- **Military Analytics**: Understanding DoD paygrade structures and career progression
