# Day 70. 100 Days of Data Science Challenge - 04/11/2025

# 🩺 Cancer Diagnosis & Cost Analysis Dashboard (2004–2012)

![Dashboard Preview](https://pplx-res.cloudinary.com/image/upload/v1744473743/user_uploads/gRazwOZQLXxuhsr/image.jpg)

## 🌟 Project Overview

This Tableau dashboard dives deep into cancer diagnosis data and treatment costs in California from 2004 to 2012. By analyzing **diagnosis stages** across five major cancer types (Breast, Colon, Rectum, Lung, Prostate) and correlating them with **treatment costs**, this project provides actionable insights into disease prevalence, diagnosis trends, and healthcare expenditure.

The goal of this analysis is to uncover patterns that can inform early intervention strategies, optimize resource allocation, and improve patient outcomes.

**[🚀 Explore the Live Dashboard Here](https://public.tableau.com/app/profile/vatsalparikh/viz/cancer-cost-diagnosis-dashboard/Dashboard1)**

---

## 🔍 Key Questions Answered

This dashboard addresses critical questions in cancer diagnosis and treatment:

1. **What types of cancer are most prevalent?**
   - Visualize the total number of cases for Breast, Colon, Rectum, Lung, and Prostate cancers.
   - Compare prevalence across different diagnosis stages (Stage 0 to Stage IV).

2. **At what stage are most diagnoses happening?**
   - Analyze the distribution of cases by stage for each cancer type.
   - Identify trends in early vs. late-stage diagnoses.

3. **How does breast cancer treatment cost vary by stage?**
   - Compare treatment costs for breast cancer patients during the first year post-diagnosis (0–12 months) and the second year (12–24 months).
   - Highlight the financial impact of advanced-stage diagnoses.

4. **What is the total cost of breast cancer treatment in California from 2004–2012?**
   - Aggregate treatment costs by stage to understand the economic burden on healthcare systems.

---

## 📊 Insights & Findings

### 1. Cancer Prevalence by Type
- **Breast Cancer** dominates with over **164K Stage I/II cases**, followed by **Prostate Cancer** at **151K Stage I/II cases**.
- Late-stage diagnoses (Stage III/IV) are more common for **Lung Cancer**, highlighting the need for improved early detection methods.

### 2. Diagnosis Trends by Stage
- Most cancers are diagnosed at **Stage I/II**, except for Lung Cancer, which has a significant proportion of late-stage diagnoses (Stage III/IV).
- Early-stage detection (Stage 0) is highest for Breast Cancer (~49K cases).

### 3. Breast Cancer Treatment Costs
- Advanced stages (Stage III/IV) incur significantly higher costs:
  - **Stage IV:** $134K in the first year post-diagnosis vs. $22K in the second year.
  - Early-stage diagnoses (Stage I/II) have lower initial treatment costs ($82K) but higher follow-up costs ($35K).

### 4. Total Economic Impact
- Breast Cancer treatment costs in California from 2004–2012:
  - **Stage I/II:** $13.5B (largest share of total costs).
  - Late stages (III/IV): Combined $4.5B.
- Early intervention could reduce overall healthcare expenditure significantly.

---

## 🛠️ Tools & Methodology

### Data Sources
1. **Cancer Diagnosis Data** (`Cancer-Diagnoses-California-2004-2012.xlsx`):
   - Contains diagnosis counts across five cancer types and stages.
   - Key fields: `Stage Name`, `Breast`, `Colon`, `Rectum`, `Lung`, `Prostate`.

2. **Breast Cancer Treatment Costs** (`Breast-Cancer-Cost-by_-Stage.xlsx`):
   - Includes cost breakdowns for each stage during two post-diagnosis periods.
   - Key fields: `Disease stage`, `0–12 months postdiagnosis ($ cost)`, `12–24 months postdiagnosis ($ cost)`.

### Analytical Workflow
1. **Data Cleaning & Transformation**:
   - Removed missing values and standardized stage names.
   - Aggregated total cases and costs by stage for visualization.

2. **Visualization Design**:
   - Created bar charts to compare prevalence and diagnosis trends across stages.
   - Designed treemaps for cost analysis to highlight financial impact by stage.

3. **Interactive Elements**:
   - Filters for cancer type and diagnosis stage allow users to explore specific subsets of data.
   - Tooltip functionality provides detailed breakdowns for each visualization.

---

## 📈 Dashboard Features

### Visualizations Included:
1. **Cancer Prevalence by Type & Stage**:
   - Stacked bar chart comparing total cases across five cancer types and diagnosis stages.
  
![image](https://github.com/user-attachments/assets/69706364-1ed9-4901-9f48-e275046f0d1f)


2. **Diagnosis Trends Across Stages**:
   - Clustered bar chart showing stage-wise distribution for each type of cancer.
  
![image](https://github.com/user-attachments/assets/10e52ca9-e7d4-4856-a821-31980ff0a80b)

  
3. **Breast Cancer Treatment Costs**:
   - Side-by-side bar chart comparing first-year vs. second-year costs across all stages.
  
![image](https://github.com/user-attachments/assets/9263a4d9-8da2-4544-b63f-3560a63d3418)


4. **Total Economic Impact of Breast Cancer Treatment**:
   - Aggregated bar chart showing total cost by stage over an eight-year period.

![image](https://github.com/user-attachments/assets/bfd6205b-64a8-4662-af7a-f633acea34ce)

---

## 🚀 Next Steps

Potential enhancements include:
1. Adding time-series analysis to track yearly trends in diagnosis rates and costs.
2. Expanding the dataset to include other states or countries for comparative analysis.
3. Incorporating survival rates by stage to correlate financial impact with patient outcomes.
