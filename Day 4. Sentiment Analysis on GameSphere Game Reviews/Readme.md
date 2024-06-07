## Day 4. 100 Days of Data Science Challenge - 06/06/2024

## Sentiment Analysis on GameSphere Game Reviews

### Problem Statement

GameSphere, a leading digital distribution platform for video games, fosters a global community of gamers by hosting a vast collection of games and encouraging user reviews and recommendations. These reviews are crucial for developers and potential buyers, as they provide feedback and guide purchasing decisions. Automatically analyzing and classifying the sentiment of these reviews as positive (recommended) or negative (not recommended) can offer invaluable insights into a game's acceptance and its overall standing among users.

### Aim

The main objective of this project is to develop a model that can accurately determine the sentiment of user reviews on GameSphere as either positive or negative.

### Data

The dataset contains reviews of various games from the GameSphere platform. Each review includes:
- `review_id`: Unique identifier for the review
- `review_text`: Text content of the review
- `recommended`: Binary label indicating whether the review recommends the game (1) or not (0)

### Workflow

1. **Data Preprocessing**
    - Cleaning the review text (removing HTML tags, special characters, etc.)
    - Tokenization and stemming/lemmatization
    - Splitting data into training and testing sets

2. **Feature Extraction**
    - Using TF-IDF (Term Frequency-Inverse Document Frequency) to convert text data into numerical features

3. **Model Training**
    - Training different models (e.g., Logistic Regression, Naive Bayes, Support Vector Machine) on the training set

4. **Model Evaluation**
    - Evaluating the models using accuracy, precision, recall, and F1-score on the test set
    - Selecting the best performing model

5. **Deployment**
    - Deploying the selected model to predict the sentiment of new reviews

### Tools and Technologies

- **Programming Language**: Python
- **Libraries**:
  - `pandas` for data manipulation
  - `numpy` for numerical operations
  - `scikit-learn` for machine learning algorithms and evaluation metrics
  - `nltk` for natural language processing

### Results

The final model is evaluated on various metrics, and its performance is documented in the results directory. Detailed analysis and visualizations are provided to interpret the model's effectiveness.

### Future Work

- Exploring advanced NLP techniques like BERT or GPT for better performance
- Integrating the model with GameSphere’s platform for real-time sentiment analysis
- Continuously updating the model with new data to improve its accuracy and robustness

---

*This project is part of the 100 Days of Data Science Challenge. For daily updates and progress, visit the [GitHub repository](https://github.com/vatsalparikh07/100-days-of-data-science-challenge/tree/main).* 
