# Day 38. 100 Days of Data Science Challenge - 03/10/2025
# 📝 Gender Bias in Student Reviews: A Text Analysis Project  

## 🌟 Project Overview  

**Do students describe professors differently based on gender?**  

Language shapes how we perceive people, especially in workplaces and classrooms. Research suggests that **gendered language** can impact hiring, teaching evaluations, and leadership opportunities.  

In this project, I conducted a **Natural Language Processing (NLP) analysis** on **student reviews of professors** from **RateMyProfessors.com** to uncover **potential gender biases** in the way students describe male vs. female professors.  

🛠️ **Key Technologies:** Python, NLP, Web Scraping, Data Visualization  
📈 **Techniques Used:** Web Scraping, Tokenization, TF-IDF, Sentiment Analysis  

---

## 🎯 Project Objectives  

✅ **Scrape professor reviews** from RateMyProfessors.com  
✅ **Label gender** using pronouns from student reviews  
✅ **Perform text analysis** to find commonly used words for male vs. female professors  
✅ **Visualize patterns** in student perceptions of professors based on gender  

By analyzing thousands of reviews, we aim to **identify hidden biases** and contribute to the conversation on **gender equality in academia**.  

---

## 📂 Data Collection & Preparation  

- **Web Scraping:** Collected professor reviews using **Python’s `urllib` and `lxml`**  
- **Gender Labeling:** Assigned gender labels based on pronoun frequency in reviews  
- **Data Preprocessing:** Cleaned, tokenized, and lemmatized text for analysis  
- **Final Dataset:** 9,787 professor reviews with **rating, sentiment, and gender labels**  

---

## 🛠 Analytical Approach  

### 1️⃣ **Web Scraping & Data Cleaning**  
- Extracted professor **ratings, student comments, and sentiment labels**  
- Used **Python’s `urllib` and `lxml`** for scraping  

### 2️⃣ **Gender Labeling using Pronouns**  
- Assigned "Male" or "Female" labels based on **pronoun frequency**  
- Noted limitations: **non-binary professors underrepresented** due to lack of pronouns  

### 3️⃣ **Text Processing & NLP**  
- Tokenized and lemmatized text using **NLTK & sklearn**  
- Removed **stopwords and common words** (e.g., “professor,” “class”)  

### 4️⃣ **TF-IDF & Sentiment Analysis**  
- Used **TF-IDF vectorization** to identify most important words in reviews  
- Applied **sentiment analysis** to compare positive vs. negative descriptions for male vs. female professors  

### 5️⃣ **Visualization & Insights**  
- Created **bar plots, box plots, and word clouds** to illustrate differences in word usage  
- Analyzed **how language differs in high vs. low-rated reviews**  

---

## 🔥 Key Findings & Insights  

| **Gender**  | **Most Common Positive Words** | **Most Common Negative Words** |  
|------------|-------------------------------|-------------------------------|  
| **Male**   | "brilliant," "hilarious," "genius" | "arrogant," "unorganized," "boring" |  
| **Female** | "caring," "supportive," "nice"  | "bossy," "strict," "moody"    |  

### ✨ Key Takeaways  

- **Male professors** were more likely to be described using **intellectual adjectives** (*"brilliant," "genius"*)  
- **Female professors** were more often described based on **personality traits** (*"caring," "kind"*)  
- **Negative reviews** of female professors included words like **"bossy" and "strict"**, while male professors were criticized for being **"arrogant" or "boring"**  
- These patterns suggest **gendered expectations** in academia, influencing how students evaluate professors  

---

## 🎨 Visualizations  

📊 **Bar Plot:** Gender-based differences in professor ratings  
📈 **TF-IDF Word Cloud:** Most frequent positive and negative words by gender  
📉 **Box Plot:** Distribution of ratings for male vs. female professors  

🚀 **[View Dashboard Screenshots]()**  

---

## 🚧 Challenges & Solutions  

### Challenge: **Ensuring Accurate Gender Labeling**  
✅ Used **pronoun-based labeling** but acknowledged its limitations  

### Challenge: **Handling Imbalanced Data**  
✅ Applied **TF-IDF normalization** to prevent common words from dominating results  

### Challenge: **Bias in Sentiment Analysis**  
✅ Used **context-aware interpretation** rather than relying solely on sentiment scores  

---

## 💡 Future Enhancements  

🔹 **Expand Data Sources:** Scrape reviews from **additional platforms (e.g., Glassdoor, student forums)**  
🔹 **Sentiment Analysis Upgrade:** Implement **BERT-based NLP models** for context-aware bias detection  
🔹 **Interactive Dashboard:** Build a **Streamlit app** to explore gender bias in real-time  

---

### ✨ Final Thoughts  

This project was an **eye-opening dive into language, bias, and academia**. By leveraging **NLP and data visualization**, I uncovered **hidden patterns in student reviews** that contribute to gendered perceptions in education.  

📢 If you're interested in **NLP, gender studies, or AI ethics**, let's connect and discuss this further! 😊  
