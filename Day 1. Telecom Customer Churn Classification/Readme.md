## Day 1. 100 Days of Data Science Challenge
## Binary Classification - Telecom company Customer Churn Classification

#### Problem Statement

In the telecom industry, understanding and predicting customer churn is crucial for retaining customers and maintaining revenue. In this examination, we aim to classify potential churn customers based on numerical and categorical features using binary classification techniques. The dataset provided contains various attributes related to customer demographics, services, and contract details.

#### Dataset Attributes

- **customerID**: Customer ID
- **gender**: Gender of the customer (Male, Female)
- **SeniorCitizen**: Whether the customer is a senior citizen or not (1, 0)
- **Partner**: Whether the customer has a partner or not (Yes, No)
- **Dependents**: Whether the customer has dependents or not (Yes, No)
- **tenure**: Number of months the customer has stayed with the company
- **PhoneService**: Whether the customer has a phone service or not (Yes, No)
- **MultipleLines**: Whether the customer has multiple lines or not (Yes, No, No phone service)
- **InternetService**: Customer’s internet service provider (DSL, Fiber optic, No)
- **OnlineSecurity**: Whether the customer has online security or not (Yes, No, No internet service)
- **OnlineBackup**: Whether the customer has online backup or not (Yes, No, No internet service)
- **DeviceProtection**: Whether the customer has device protection or not (Yes, No, No internet service)
- **TechSupport**: Whether the customer has tech support or not (Yes, No, No internet service)
- **StreamingTV**: Whether the customer has streaming TV or not (Yes, No, No internet service)
- **StreamingMovies**: Whether the customer has streaming movies or not (Yes, No, No internet service)
- **Contract**: The contract term of the customer (Month-to-month, One year, Two year)
- **PaperlessBilling**: Whether the customer has paperless billing or not (Yes, No)
- **PaymentMethod**: The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))
- **MonthlyCharges**: The amount charged to the customer monthly
- **TotalCharges**: The total amount charged to the customer
- **Churn**: Whether the customer churned or not (Yes or No)

#### Sections

1. **Data Analysis**:
   - Summarize the data.
   - Analyze and discuss the relationships between the data attributes and label.
   
2. **Data Pre-processing & Feature Engineering**:
   - Discuss the steps you would take to clean and prepare the data for modeling.
   - Perform Feature Engineering on the dataset.

3. **Modeling**:
   - Train at least three different classifier models and optimize hyperparameters.
   - Implement a validation pipeline utilizing 5-fold cross-validation.
   
4. **Evaluation and Reporting**:
   - Select a model that is expected to perform optimally on the unseen data and provide the predictions accordingly.
