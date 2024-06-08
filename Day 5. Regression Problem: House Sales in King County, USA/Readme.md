# Day 5. 100 Days of Data Science Challenge - 07/06/2024

# House Sales Prediction in King County, USA

## Project Description

This project aims to predict house prices in King County, USA, using various regression models. The dataset includes house sales data between May 2014 and May 2015, and the goal is to predict the price of a house based on its attributes.

## Dataset

The dataset includes the following columns:

- **id**: Unique ID for each home sold
- **date**: Date of the home sale
- **price**: Price of each home sold (scale = 1e5. For example, 1.2 means $120,000)
- **bedrooms**: Number of bedrooms
- **bathrooms**: Number of bathrooms, where .5 accounts for a room with a toilet but no shower
- **sqft_living**: Square footage of the apartments interior living space
- **sqft_lot**: Square footage of the land space
- **floors**: Number of floors
- **waterfront**: A dummy variable for whether the apartment was overlooking the waterfront or not
- **view**: An index from 0 to 4 of how good the view of the property was
- **condition**: An index from 1 to 5 on the condition of the apartment
- **grade**: An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design
- **sqft_above**: The square footage of the interior housing space that is above ground level
- **sqft_basement**: The square footage of the interior housing space that is below ground level
- **yr_built**: The year the house was initially built
- **yr_renovated**: The year of the house’s last renovation
- **zipcode**: What zipcode area the house is in
- **lat**: Latitude
- **long**: Longitude
- **sqft_living15**: The square footage of interior housing living space for the nearest 15 neighbors
- **sqft_lot15**: The square footage of the land lots of the nearest 15 neighbors

## Project Steps

### 1. Data Analysis

- **Descriptive Statistics**: Provide summary statistics for the dataset.
- **Data Visualization**: Plot histograms, boxplots, scatter plots, and correlation heatmaps to understand the relationships between features and the target variable.

### 2. Data Pre-processing & Feature Engineering

- **Handling Missing Values**: Fill missing values with appropriate measures (mean for numerical columns, mode for the date column).
- **Handling Outliers**: Remove outliers based on the distribution of the target variable.
- **Feature Scaling**: Standardize features using `StandardScaler`.
- **Feature Selection**: Use ANOVA to assess the significance of each feature and remove non-significant ones.

### 3. Modeling

- **Model Training**: Train multiple regression models including Linear Regression, Ridge, Lasso, ElasticNet, Random Forest, Gradient Boosting, and XGBoost.
- **Model Evaluation**: Evaluate models using 5-fold cross-validation with RMSE and R2 score as metrics.
- **Model Selection**: Select the best-performing model based on evaluation metrics.

### 4. Evaluation and Reporting

- **Final Model**: Use the selected model to make predictions on the test set and report the performance.
- **Comparison**: Compare predicted prices with actual prices for both train and test datasets.

## Results

- The **Random Forest Regression** model was selected as the optimal model due to its low RMSE and high R2 score on both the training and test datasets.

## Conclusion

The project demonstrates how to predict house prices using various regression models and highlights the importance of data pre-processing, feature engineering, and model evaluation in building an effective predictive model.

---

*This project is part of the 100 Days of Data Science Challenge. For daily updates and progress, visit the [GitHub repository](https://github.com/vatsalparikh07/100-days-of-data-science-challenge/tree/main).* 
