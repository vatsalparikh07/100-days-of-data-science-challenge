# Day 73. 100 Days of Data Science Challenge - 04/14/2025

## 🚀 Snowpark Ad Spend ROI Predictor & Optimizer ❄️ [(Streamlit App hosted on Snowflake)](https://app.snowflake.com/tqbvvzz/xn73217/#/streamlit-apps/DASH_DB.DASH_SCHEMA.ZNZCUDJ576HPERAB?ref=snowsight_shared)

![3](https://github.com/user-attachments/assets/b28b7c2e-9f6c-48ae-9718-89fe8309f0f8)
*Interactive Streamlit app predicting high ROI based on optimized ad spend.*

## 🎯 Project Goal: From Raw Data to Smart Budget Decisions

Ever feel like you're guessing where your advertising dollars should go? This project tackles that head-on! We built an **end-to-end solution entirely within Snowflake** to help a fictional company, "SkiGear Co," optimize its advertising budget allocation across channels like Search, Social Media, Video, and Email.

Starting with raw campaign spend and revenue data stored in S3, we leverage the power of **Snowpark for Python**, **Snowpark ML**, **Snowflake Tasks**, and **Streamlit** to:

1.  **Ingest & Engineer Data:** Clean, transform, and join disparate datasets directly within Snowflake.
2.  **Train & Deploy an ML Model:** Build a predictive model (Linear Regression with polynomial features) to forecast ROI based on different budget mixes, all using Snowpark ML and managed by the Snowflake Model Registry.
3.  **Build an Interactive Optimizer App:** Create a user-friendly Streamlit application where business users can adjust budget sliders and instantly see the predicted ROI, enabling data-driven decision-making without needing to write code.

**The result?** An application that transforms complex data analysis into intuitive budget planning.

---

## ✨ Tech Stack & Core Concepts

This project showcases a modern, unified data science workflow on Snowflake:

*   ❄️ **Snowflake:** Cloud Data Platform (Warehouse, Database, Schema, Stages)
*   🏂 **Snowpark for Python:** Python API for querying and processing data *natively* in Snowflake (DataFrames, UDFs, Stored Procedures).
*   🤖 **Snowpark ML:** Integrated library for streamlined feature engineering (`PolynomialFeatures`, `StandardScaler`), model training (`LinearRegression`, `GridSearchCV`), and deployment (`Registry`).
*   ⚙️ **Snowflake Tasks & DAGs:** Orchestrating the data engineering pipeline for automated, scheduled execution.
*   📊 **Streamlit (in Snowflake):** Building and hosting the interactive web application directly within Snowsight.
*   🐍 **Python 3.9:** The language driving it all.
*   📊 **Altair:** For creating the interactive charts within the Streamlit app.

---

## 🗺️ The Journey: Building the Pipeline & App

This project unfolds in distinct, interconnected stages, all orchestrated within Snowflake:

### 1. Laying the Foundation: Setup & Data Engineering 🏗️

*   **Goal:** Ingest raw data from S3 and transform it into a clean, unified table ready for machine learning.
*   **Process:**
    *   **Setup:** Created Snowflake objects (Warehouse `DASH_S`, Database `DASH_DB`, Schema `DASH_SCHEMA`) and loaded raw CSVs (`campaign_spend`, `monthly_revenue`) from S3 stages using `COPY INTO`.
    *   **Snowpark DataFrames:** Loaded Snowflake tables directly into Snowpark DataFrames (`session.table(...)`).
    *   **Transformations:** Applied powerful DataFrame operations *natively* in Snowflake:
        *   Aggregated daily spend to monthly totals per channel (`group_by`, `agg`, `sum`).
        *   Reshaped data using `pivot` to get channels as columns (`SEARCH_ENGINE`, `SOCIAL_MEDIA`, etc.).
        *   Joined the transformed spend data with monthly revenue data (`join`).
    *   **Result:** A single table `SPEND_AND_REVENUE_PER_MONTH` containing monthly spend per channel alongside total revenue – perfect for training our ROI prediction model.
*   **Automation:** Encapsulated these transformations into Python functions (`campaign_spend_data_pipeline`, `monthly_revenue_data_pipeline`) and deployed them as **Snowflake Tasks**, creating a **DAG (Directed Acyclic Graph)** to ensure they run in the correct order (`dag_spend_task >> dag_revenue_task`). This automates the entire data prep process!

```
snow_df_spend_per_month = snow_df_spend_per_channel.pivot(
'CHANNEL',
['search_engine','social_media','video','email']
).sum('TOTAL_COST').sort('YEAR','MONTH')
```

### 2. Building the Crystal Ball: Machine Learning 🔮

*   **Goal:** Train a model to predict monthly `REVENUE` based on the spend across the four advertising channels.
*   **Process:**
    *   **Feature Prep:** Loaded the `SPEND_AND_REVENUE_PER_MONTH` table, dropped unnecessary columns (`YEAR`, `MONTH`), and handled missing values (`dropna`). Saved the final features and target into `MARKETING_BUDGETS_FEATURES`.
    *   **Snowpark ML Pipeline:** Defined a pre-processing and modeling pipeline using `snowflake.ml.modeling`:
        *   `PolynomialFeatures(degree=2)`: To capture potential non-linear interactions between channel spends.
        *   `StandardScaler()`: To scale features for better model performance.
        *   `LinearRegression()`: The chosen algorithm for predicting revenue.
    *   **Hyperparameter Tuning:** Used `GridSearchCV(cv=10)` to find the optimal model configuration directly within Snowflake, leveraging its elastic compute.
    *   **Model Training:** Executed `model.fit(train_df)` – training happens *inside* Snowflake, close to the data.
    *   **Model Registration:** Logged the trained pipeline (including preprocessors) to the **Snowflake Model Registry** (`registry.log_model(...)`) along with performance metrics (R2 scores). This makes the model easily discoverable and deployable.
*   **Result:** A trained, versioned, and managed ML model (`PREDICT_ROI`) ready for inference within Snowflake.

```
numeric_transformer = Pipeline(steps=[('poly', PolynomialFeatures(degree=2)), ('scaler', StandardScaler())])
preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features)])
pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', LinearRegression())])
model = GridSearchCV(estimator=pipeline, ...)
model.fit(train_df) # Training happens in Snowflake!
```

![ML Workflow Diagram](https://pplx-res.cloudinary.com/image/upload/v1744669997/user_uploads/QECvKgmlrpsTojB/4.jpg)
*Conceptual ML Workflow Leveraging Snowpark ML and Model Registry*

### 3. Bringing it to Life: The Streamlit App ✨

*   **Goal:** Create an interactive UI for business users to explore different budget scenarios and see predicted ROI without writing code.
*   **Process:**
    *   **Built with Streamlit:** Developed the application using Python and the `streamlit` library directly within Snowsight's Streamlit integration.
    *   **Interactive Controls:** Used `st.slider` to allow users to adjust budget allocations (0-100k scale) for each of the four channels.
    *   **Live Prediction:** On slider change, the app constructs a SQL query that calls the `predict` method of the registered model (`PREDICT_ROI!predict(...)`) directly within Snowflake, passing the user's budget inputs.
    *   **Instant Feedback:** Displayed the predicted revenue (`st.metric`) and calculated the percentage change compared to the previous month.
    *   **Visualization:** Used `altair` to create a dynamic chart showing historical spend/ROI alongside the *new* predicted "July" values based on the slider inputs.
    *   **Persistence:** Included a `st.button("❄️ Save to Snowflake")` that writes the user's chosen budget allocation and the corresponding predicted ROI back into the `BUDGET_ALLOCATIONS_AND_ROI` table in Snowflake, closing the loop.
*   **Result:** A fully functional, interactive web application hosted within Snowflake, providing immediate ROI predictions based on user inputs.

![SkiGear Co Streamlit App - Low ROI Scenario](https://pplx-res.cloudinary.com/image/upload/v1744669997/user_uploads/XsubwbfGHCmCURF/1.jpg)
*App showing a lower predicted ROI for a different budget mix.*

---

## 💡 Key Takeaways & Impact

*   **Unified Platform Power:** This entire project, from raw data ingestion to ML training to the interactive application, lives and runs *inside Snowflake*. This drastically reduces data movement, improves security, and simplifies orchestration.
*   **Snowpark Efficiency:** Performing data transformations directly on Snowflake data using familiar Python/Pandas-like syntax (Snowpark DataFrames) is powerful and efficient.
*   **Integrated ML:** Snowpark ML streamlines the process of training scikit-learn style models and managing them within Snowflake, making deployment much easier.
*   **Actionable Insights via Streamlit:** The final app empowers non-technical users to leverage a sophisticated ML model for practical budget planning, directly impacting business strategy.
*   **Automation is Key:** Using Snowflake Tasks and DAGs turns the data engineering steps into a repeatable, scheduled pipeline.

---

*This project demonstrates a complete, modern data science workflow built entirely on the Snowflake platform, showcasing how to bridge the gap between complex data processing, machine learning, and interactive business applications. Created by Vatsal Parikh.*
