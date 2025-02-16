# Day 16. 100 Days of Data Science Challenge - 02/16/2025

# Fundamentals of NLP: Regex, Tokenization, and Search Prediction

## 📝 Project Overview  
Ever wondered how **news headlines** are structured or how **search engines predict your next word**?  
In this project, I dive deep into **Natural Language Processing (NLP)** techniques to analyze **New York Times headlines**, build an **autocompletion tool**, and compare text extraction with ChatGPT.  

🛠 **Techniques Used:**  
✔️ **Regex & Named Entity Recognition (NER)** for detecting proper nouns in headlines  
✔️ **Text Preprocessing & Vocabulary Building** (Tokenization, Lemmatization, Frequency Analysis)  
✔️ **Autocomplete Suggestion System** using **Levenshtein Distance**  
✔️ **ChatGPT Comparison** – Evaluating AI vs. custom NLP for text extraction  

---

## 📰 Dataset: New York Times Headlines  
📌 **Source:** `nytimes_data_final.csv` (A collection of NYT headlines)  
📌 **Scope:** Extracting named entities, building vocabulary, and analyzing frequency patterns  

### **Sample Data**  
📰 "Biden Meets with World Leaders at UN Summit"  
📰 "Donald Trump Speaks at Rally Amid Controversy"  
📰 "Indiana University Researches AI in Healthcare"  

The dataset is processed to **identify named entities, extract unique words, and analyze word frequencies**.  

---

## 🛠 Project Breakdown  

### 🔹 **1. Regex & Named Entity Extraction**  
📌 **Goal:** Detect all **proper nouns (named entities)** in headlines  
📌 **Method:**  
   - Build **regular expressions** to extract names (e.g., "Joe Biden", "Donald Trump")  
   - Count **unique named entities**
     
📌 **Outcome:** Extracted **dozens of unique names** and printed headlines containing them  

### 🔹 **2. Vocabulary Building & Frequency Analysis**  
📌 **Goal:** Create a **cleaned vocabulary** from the headlines  
📌 **Steps:**  
   - Tokenize words  
   - Convert to **lowercase** (case folding)  
   - Apply **lemmatization** to get base forms  
   - Store unique words in a **vocabulary set**
     
📌 **Outcome:**  
   - Built a vocabulary of **unique words**  
   - Plotted a **word frequency distribution** for the **top 100 most common words**  

### 🔹 **3. Autocompletion Tool (Search Engine-Style Predictions)**  
📌 **Goal:** Predict **possible word completions** based on user input  
📌 **Method:**  
   - Load words from the **WordList.txt** file  
   - Use **Levenshtein Distance** to find the closest matches  
   - Return the **K most probable** words for autocompletion
      
📌 **Example:**  
   - Input: `"why i"`  
   - Output: `["why is", "why it", "why i’m"]`  

### 🔹 **4. ChatGPT Comparison**  
📌 **Goal:** Compare **ChatGPT's performance** vs. my **Regex-based entity extraction**  
📌 **Steps:**  
   - Run **ChatGPT** on the same task (extract named entities from headlines)  
   - Analyze **differences in accuracy & recall**  
   - Document **strengths & weaknesses** of each approach
     
📌 **Findings:**  
   - **ChatGPT** is **better at contextual understanding** but sometimes **over-generates** names  
   - **Regex-based extraction** is **precise** but **misses variations & ambiguous cases**  
   - **Combining both** could create a **more powerful extraction pipeline**  

---

## 📊 Key Insights & Learnings  

✔️ **Regex is powerful but limited** – It struggles with **ambiguous names** or variations.  
✔️ **Levenshtein Distance is useful for autocompletion**, but real-world search engines use **probabilistic models** (e.g., Markov Chains, Transformers).  
✔️ **Frequency analysis reveals hidden patterns** – Some words appear **significantly more** than others in news headlines.  
✔️ **ChatGPT vs. Regex** – AI models **understand context** but require validation for **accuracy**.  

---

## 📌 Future Enhancements  

🔹 **Improve Named Entity Recognition (NER)** using spaCy or NLTK.  
🔹 **Use n-grams or Markov Models** to enhance autocompletion accuracy.  
🔹 **Test ChatGPT’s latest versions** to see improvements in text extraction.  
🔹 **Expand to other text sources** (e.g., social media posts, scientific papers).  

---

## 💡 Reflections  

This project was a **fascinating mix of NLP, search engine logic, and AI comparison**.  
From **building regex rules** to **evaluating AI performance**, I gained insights into how **language models process text** and how **autocompletion systems work behind the scenes**.  

📰 **Next Steps:**  
- Explore **transformer-based models** (e.g., BERT) for **contextual word predictions**.  
- Try **Named Entity Recognition (NER)** using **spaCy** for better accuracy.  
- Implement **word embeddings** to improve **autocomplete predictions**.  
