# Day 35. 100 Days of Data Science Challenge - 03/07/2025
# 📊 A/B Testing in R: Did Our Experiment Work?

## 🌟 Project Overview  

On Day 35, I ventured into the world of **A/B Testing** using **R**, tackling a fictional dataset that simulates customer spending behavior before and after an experiment. The dataset spans seven months, with the experiment conducted in **October**, aiming to determine if the new treatment (product or experience) led to increased spending.

---

## 🎯 Key Highlights  

- **Experiment Design:** Analyzed pre- and post-experiment data to gauge the treatment's impact.  
- **Data Analysis:** Used both **t-tests** and **linear regression models** to draw conclusions.  
- **Visual Storytelling:** Created compelling visuals to showcase spending trends over time.  
- **Statistical Rigor:** Evaluated the power of the experiment and calculated necessary sample sizes for significance.  

---

## 🔬 What I Learned  

### 💡 **Technical Skills Mastered**  

- **Data Wrangling in R:** Leveraged `tidyverse` for data manipulation and aggregation.  
- **Statistical Testing:** Conducted **Welch Two Sample t-tests** to compare groups.  
- **Regression Modeling:** Built a linear regression model and corrected standard errors using `sandwich` and `lmtest` packages.  
- **Power Analysis:** Estimated the sample size needed for statistically significant results using `power.t.test()`.  

### 🧠 **Analytical Insights**  

- The treatment group showed a statistically significant increase in spending post-experiment (`p-value = 0.00119`).  
- The **New Group** had higher average spending than the **Existing Group** during the A/B testing period.  
- The experiment's effect size suggested that a sample size of **500 per group** would be needed for strong statistical power.  

---

## 📈 Methodology  

### 1. **Data Collection & Preparation**  

The dataset consisted of **1,500 rows** and **398 unique customers**, capturing monthly spending from **July 2022** to **January 2023**. Key variables included:  

- `Group`: Identifies if a customer is in the **New** (treatment) or **Existing** (control) group.  
- `Treated`: Indicates whether the treatment was applied (1 for treatment, 0 otherwise).  
- `Dollars`: The amount spent by each customer.  

### 2. **Exploratory Data Analysis (EDA)**  

- **Customer Distribution:** The dataset had a nearly even split between the `New` and `Existing` groups.  
- **Spending Trends:** A time series plot revealed an initial uptick in spending among the **New Group** during the experiment.  

### 3. **Statistical Testing**  

- **A/B Test Results:**  
  - Compared average spending between groups using a **t-test**.  
  - The **New Group** had a higher mean spending ($52.43) compared to the **Existing Group** ($50.24), with a marginal **p-value of 0.09274**.  

- **Pre vs. Post Analysis in the New Group:**  
  - A significant increase in spending post-treatment, with a p-value of **0.00119**, indicating a meaningful impact of the experiment.  

### 4. **Modeling Approach**  

- Built a **linear regression model** with `Treated`, `Group`, and `Month` as predictors.  
- The `Treated` variable showed a positive effect on spending (**Estimate = 4.51**, **p = 0.01076**).  
- Corrected standard errors using **clustered standard errors** to account for repeated customer observations.  

---

## 🏆 Results  

| **Metric**              | **New Group**   | **Existing Group** | **Significance** |  
|-------------------------|-----------------|--------------------|------------------|  
| **Average Spending**    | $52.43          | $50.24             | *p = 0.09274*    |  
| **Before Treatment**    | $47.86          | N/A                |                  |  
| **After Treatment**     | $52.43          | N/A                | *p = 0.00119*    |  
| **Regression Estimate** | +$4.51 (Treated)| -$1.90 (Group)     | *p = 0.01076*    |  

### ✨ **Key Insights:**  

- The experiment led to a **statistically significant increase** in spending among the **New Group**.  
- The **treatment effect** was strong enough to be detected in both **t-tests** and **regression analysis**.  
- The experiment was well-powered, but a larger sample size could have improved the robustness of the findings.  

---

## 🚧 Challenges Faced  

- **Balancing Data Complexity:** Managed duplicated observations and ensured data integrity by aggregating spending data.  
- **Statistical Power:** Evaluated whether the sample size was sufficient to detect meaningful differences, using `power.t.test()`.  
- **Model Interpretation:** Needed to correct standard errors to avoid misleading results due to repeated measurements of the same customers.  

---

## 💡 Future Work  

- **Broader Analysis:** Incorporate additional customer features (e.g., demographics) to refine the analysis.  
- **Experiment Iteration:** Test different treatment variations to see if certain changes drive higher spending.  
- **Dashboard Creation:** Build an interactive **Shiny app** for live monitoring of A/B test results.  

---

## 📝 Conclusion  

This project reinforced the power of **A/B Testing** and the importance of a solid experimental design. It highlighted how statistical techniques, when paired with robust visualization, can transform raw data into actionable insights. The results provided clear evidence that the new treatment was effective, and the journey from data collection to hypothesis testing showcased the full spectrum of **data science** in action.  

Thanks for joining me on Day 35! If you're passionate about **data science**, **R programming**, or **experiment design**, let’s connect! 😊  
