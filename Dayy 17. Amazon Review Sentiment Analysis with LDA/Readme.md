# Day 17. 100 Days of Data Science Challenge - 02/17/2025

# Amazon Review Sentiment Analysis with LDA

## 📝 Project Overview  
This project focuses on analyzing **Amazon customer reviews** using **Latent Dirichlet Allocation (LDA) for topic modeling** and **Logistic Regression for sentiment classification**.  
The goal is to **identify key themes in reviews** and classify sentiment as **positive or negative** using text data.  

🛠 **Key Techniques Used:**  
✔️ **Text Preprocessing** – Tokenization, Stopword Removal, Cleaning  
✔️ **Topic Modeling** – Latent Dirichlet Allocation (LDA)  
✔️ **Sentiment Classification** – Logistic Regression  
✔️ **Feature Engineering** – TF-IDF Vectorization  
✔️ **Model Evaluation** – Accuracy, Precision, Recall, F1-Score  

---

## 🗂 Dataset: Amazon Product Reviews  
📌 **Source:** `amazon_cells_labelled.txt`  
📌 **Size:** **1,000 reviews** (**500 positive, 500 negative**)  
📌 **Labels:** **Binary sentiment (1 = Positive, 0 = Negative)**  

### **Example Data**  
- **Positive Review:** `"Good case, excellent value."` → `1`  
- **Negative Review:** `"Battery dies quickly, charger stopped working."` → `0`  

---

## 🛠 Project Breakdown  

### 🔹 **1. Data Preprocessing**  
📌 **Goal:** Clean text for topic modeling and sentiment analysis.  
📌 **Steps:**  
   - Removed **punctuation, emoticons, and non-ASCII characters**  
   - Converted text to **lowercase**  
   - Eliminated **stopwords** using NLTK  
📌 **Outcome:** Cleaned text data ready for **LDA and TF-IDF vectorization**.  

---

### 🔹 **2. Topic Modeling with LDA**  
📌 **Goal:** Discover key themes in customer reviews.  
📌 **Method:**  
   - Converted text into a **document-term matrix** using **CountVectorizer**.  
   - Applied **LDA with 5 topics** to group similar words together.  
📌 **Extracted Key Terms per Topic:**  
   - **Topic 0:** product, work, great, good, phone (**General product quality**)  
   - **Topic 1:** battery, charge, life, time, phone (**Battery issues**)  
   - **Topic 2:** headset, sound, quality, use, ear (**Audio device feedback**)  
   - **Topic 3:** phone, case, work, fit, good (**Product design**)  
   - **Topic 4:** work, great, good, use, quality (**Positive experiences**)  

📌 **Example Topic:**  
🔹 **Negative Topic (Battery Issues)** → `"Battery dies quickly, charger stopped working."`  

📌 **Outcome:** LDA successfully grouped words into **meaningful categories**, helping identify common concerns in customer reviews.  

---

### 🔹 **3. Sentiment Classification (Supervised Learning)**  
📌 **Goal:** Predict whether a review is **positive or negative**.  
📌 **Method:**  
   - Used **TF-IDF Vectorization** to convert text into numerical features.  
   - Trained **Logistic Regression** with an **80-20 train-test split**.  
📌 **Results:**  
   - **Accuracy:** 79%  
   - **Precision:** 80%  
   - **Recall:** 79%  
   - **F1-Score:** 79%  

📌 **Key Findings:**  
✔️ **Positive Words:** `"great," "excellent," "love"`  
✔️ **Negative Words:** `"poor," "waste," "disappointed"`  

📌 **Outcome:** Logistic Regression provided a **balanced performance** in sentiment classification.  

---

## 📊 Key Insights & Learnings  

✔️ **LDA helped uncover key themes** – battery life, sound quality, and product durability were top concerns.  
✔️ **Sentiment classification performed well**, but handling **negations** (e.g., `"not good"`) remains a challenge.  
✔️ **TF-IDF was more effective** than simple word counts for feature extraction.  
✔️ **Equal distribution of positive/negative reviews improved model fairness**.  

---

## 📌 Future Enhancements  

🔹 **Hyperparameter tuning** – Optimize LDA topics and logistic regression parameters.  
🔹 **Try advanced models** – Experiment with SVM, Random Forests, or BERT for sentiment analysis.  
🔹 **Improve negation handling** – Capture phrases like `"not good"` more effectively.  
🔹 **Topic coherence metrics** – Use **Coherence Score** to evaluate LDA topic quality.  

---

## 💡 Reflections  

This project demonstrated how **NLP techniques like LDA and logistic regression** can extract insights from text.  
I learned the **importance of text preprocessing, topic modeling, and feature engineering** in sentiment analysis.  

📝 **Next Steps:**  
- Implement **word embeddings (Word2Vec, GloVe)** for feature extraction.  
- Extend the dataset and compare **deep learning models (LSTMs, Transformers)**.  
- Improve chatbot capabilities using **retrieval-based and generative AI models**.  

---
