# Analyzing Sora Discourse: Topic Modeling on Reddit Discussions 💬

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Wrangling-yellowgreen?style=flat-square&logo=pandas)](https://pandas.pydata.org/)
[![NLTK](https://img.shields.io/badge/NLTK-NLP_Preprocessing-orange?style=flat-square)](https://www.nltk.org/)
[![Gensim](https://img.shields.io/badge/Gensim-Topic_Modeling_(LDA)-blueviolet?style=flat-square)](https://radimrehurek.com/gensim/)
[![Visualization](https://img.shields.io/badge/Viz-WordCloud%2C_Matplotlib%2C_pyLDAvis-red?style=flat-square)](https://matplotlib.org/)
[![Paper](https://img.shields.io/badge/arXiv-2407.13071-b31b1b?style=flat-square)](https://arxiv.org/abs/2407.13071)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_84-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Uncovering Themes in the Sora Conversation

Welcome to Day 84 of my #100DaysOfDataScience challenge! When OpenAI announced **Sora**, its groundbreaking text-to-video model, online communities exploded with discussion. This project dives headfirst into that discourse, analyzing **thousands of Reddit comments** to understand the dominant themes, sentiments, and concerns surrounding this powerful new AI technology.

Using **Natural Language Processing (NLP)** techniques, specifically **Topic Modeling (LDA)**, we aim to:

1.  **Collect & Prepare:** Gather relevant Reddit comments from key AI and tech subreddits shortly after Sora's announcement.
2.  **Clean & Preprocess:** Transform messy, raw text data into a format suitable for robust analysis.
3.  **Identify Dominant Themes:** Employ Latent Dirichlet Allocation (LDA) to automatically discover the underlying topics being discussed.
4.  **Interpret & Visualize:** Analyze the topic keywords and use visualizations to understand the structure and focus of the public conversation.

**Why This Matters:** Understanding public perception is crucial as generative AI rapidly evolves. This analysis provides valuable insights into societal reactions, excitement, and anxieties surrounding cutting-edge AI advancements like Sora.

**Read the Full Research Paper:** [Analysing the Public Discourse around OpenAI's Text-To-Video Model 'Sora' using Topic Modeling](https://arxiv.org/abs/2407.13071)

![image](https://github.com/user-attachments/assets/eb8feccc-326a-42c3-ad77-49e644e75303)
*(Bar Charts showing Word Count and Importance of Topic Keywords)*

---

## ✨ Key Features & Concepts Mastered

*   **Targeted Data Collection:** Used **PRAW (Python Reddit API Wrapper)** to fetch ~2,000 comments from high-engagement posts across relevant subreddits (r/OpenAI, r/technology, r/singularity, r/vfx, r/ChatGPT) within a specific timeframe (Feb 1 - Apr 1, 2024).
*   **Comprehensive Text Preprocessing:** Implemented a robust cleaning pipeline:
    *   Lowercasing, removing non-alphanumeric characters & URLs (`regex`).
    *   **Tokenization:** Splitting text into individual words.
    *   **Stop Word Removal:** Using `nltk.corpus.stopwords`.
    *   **Lemmatization:** Reducing words to their base form using `nltk.stem.WordNetLemmatizer` for better topic coherence. Resulted in 1,827 cleaned comments.
*   **Feature Extraction:** Applied **Term Frequency-Inverse Document Frequency (TF-IDF)** using `gensim.models.TfidfModel` to weigh the importance of words across the corpus, highlighting terms characteristic of specific documents.
*   **Topic Modeling with LDA:**
    *   Utilized **Latent Dirichlet Allocation (LDA)** via `gensim.models.LdaModel` to probabilistically model topics within the text corpus.
    *   Performed **Coherence Score Analysis** (`gensim.models.CoherenceModel` with `c_v`) to determine the optimal number of topics (`k=4`), ensuring the identified topics were distinct and interpretable.
*   **Topic Interpretation:** Manually assigned meaningful labels to the computationally derived topics based on their highest probability keywords.
*   **Data Visualization for NLP:**
    *   **Word Clouds (`wordcloud` library):** Generated visual representations of the most frequent words within each topic.
    *   **Bar Charts (`matplotlib`/`seaborn`):** Visualized keyword importance within topics.
    *   **pyLDAvis:** Employed this interactive visualization tool to explore topic separation, keyword relevance, and topic prevalence across the corpus.
    *   **t-SNE (Potentially Used):** Dimensionality reduction (`sklearn.manifold.TSNE`) often used to visualize high-dimensional topic distributions in 2D space (as mentioned in `description.docx`).

![image](https://github.com/user-attachments/assets/78ac18e8-86d2-4a2f-b7ba-17e6d34a105b)
*(Word Clouds Visualizing Topic Keywords)*

---

## 🛠️ Tech Stack: The NLP & Analysis Toolkit

*   **Core Language:** Python 3.8+
*   **Data Handling:** Pandas
*   **Reddit API:** PRAW (Python Reddit API Wrapper)
*   **NLP Preprocessing:** NLTK (Tokenization, Stopwords, Lemmatization), `re` (Regular Expressions)
*   **Topic Modeling & Feature Extraction:** Gensim (`corpora.Dictionary`, `models.TfidfModel`, `models.LdaModel`, `models.CoherenceModel`)
*   **Dimensionality Reduction:** Scikit-learn (`sklearn.manifold.TSNE`) - *Implied/Standard Practice*
*   **Visualization:** WordCloud, Matplotlib, Seaborn, pyLDAvis
*   **Environment:** Jupyter Notebook (`solution.ipynb`)

---

## 🗺️ The Analytical Workflow: From Reddit Rants to Meaningful Themes

Our journey involved these key stages (detailed in `solution.ipynb` and the paper):

1.  **Data Acquisition:**
    *   Manually identified 10 high-comment Reddit posts (2 per subreddit) discussing Sora using relevant keywords.
    *   Used PRAW to fetch the top 200 comments (by score) from each post, capturing text, score, date, author, etc.

2.  **Data Cleansing Ritual:**
    *   Loaded raw data (`reddit_data_sora.csv`) into Pandas.
    *   Executed the preprocessing pipeline: lowercase -> remove noise (regex) -> tokenize -> remove stopwords -> lemmatize.
    *   Saved the cleaned data (`reddit_data_sora_preprocessed.csv`).

3.  **Preparing for Modeling:**
    *   Created a **Gensim Dictionary** (`corpora.Dictionary`) mapping words to IDs.
    *   Generated a **Corpus** using `dictionary.doc2bow` for each document.
    *   Applied **TF-IDF weighting** (`TfidfModel[corpus]`) to emphasize important terms.

4.  **Discovering Latent Topics (LDA):**
    *   Iteratively trained LDA models with varying numbers of topics (`k`).
    *   Calculated the **Coherence Score (c_v)** for each `k` to find the optimal balance between topic granularity and interpretability. **`k=4`** emerged as the best choice.
    *   Trained the final LDA model (`LdaModel(corpus=tfidf_corpus, id2word=dictionary, num_topics=4, ...)`).

5.  **Making Sense of the Topics:**
    *   Examined the top keywords associated with each of the 4 topics.
    *   Assigned descriptive titles based on these keywords (see Results section).

6.  **Visualizing the Discourse:**
    *   Generated **Word Clouds** for each topic to visually represent dominant terms.
    *   Created **Bar Charts** showing keyword probabilities within topics.
    *   Utilized **pyLDAvis** (`pyLDAvis.gensim_models.prepare`) for an interactive exploration of topic separation and keyword relevance. This tool is invaluable for validating and understanding LDA results.
    *   (Potentially) Used **t-SNE** to plot documents in 2D space, colored by their dominant topic, visualizing how well the topics cluster the comments.

![image](https://github.com/user-attachments/assets/ac43df7c-15f3-4e1f-9146-3ab6ede48d3f)
*(t-SNE Clustering of LDA Topics)*

---

## 💡 Unveiling the Conversation: The 4 Dominant Topics

The LDA model, optimized via coherence scores, revealed four distinct themes in the Reddit discussions about Sora:

1.  **Topic 1: AI Impact & Future Trends**
    *   *Keywords:* `ai`, `human`, `future`, `job`, `technology`, `model`, `make`, `people`, `time`, `year`
    *   *Interpretation:* Focused on the broader implications of Sora and similar AI – excitement about future capabilities mixed with concerns about job displacement, the pace of progress, and the human element in creativity.

2.  **Topic 2: Public Opinion & Ethical Concerns**
    *   *Keywords:* `people`, `think`, `artist`, `video`, `ai`, `make`, `thing`, `good`, `get`, `know`
    *   *Interpretation:* Captured reactions, opinions, and ethical debates. Discussions centered on whether Sora is "good" or "bad," its potential impact on artists, the nature of AI-generated content, and general public sentiment.

3.  **Topic 3: Artistic Expression & Video Creation**
    *   *Keywords:* `art`, `video`, `creative`, `artist`, `make`, `tool`, `use`, `ai`, `create`, `people`
    *   *Interpretation:* Explored Sora's potential as a new medium for creativity. Conversations touched upon its use as a tool for artists, the definition of AI art, and how it might change video production workflows.

4.  **Topic 4: Sora's Capabilities & Media Applications**
    *   *Keywords:* `model`, `movie`, `real`, `work`, `video`, `look`, `make`, `quality`, `year`, `time`
    *   *Interpretation:* Focused on the technical aspects and potential applications, particularly in media and entertainment. Discussions involved the realism ("look real"), quality, potential use in movies, the speed of development ("year", "time"), and how the model "works".

![image](https://github.com/user-attachments/assets/7950ce0d-27df-4b2f-ac64-ae6f0556763f)
*(Conceptual representation of pyLDAvis showing distinct topic clusters)*

---

## ✅ Significance & Key Learnings

*   **NLP Pipeline Mastery:** Successfully executed a complete NLP workflow from raw text collection to sophisticated topic modeling and interpretation.
*   **Understanding Public AI Perception:** Gained data-driven insights into how a groundbreaking AI technology like Sora is initially perceived – a mix of awe, excitement, fear, and ethical debate.
*   **Power of Unsupervised Learning:** Demonstrated how LDA can uncover hidden thematic structures in large amounts of unstructured text without pre-defined labels.
*   **Importance of Preprocessing:** Reinforced that careful text cleaning and preparation (tokenization, lemmatization) are critical for meaningful NLP results.
*   **TF-IDF vs. Count Vectorization:** Utilized TF-IDF to effectively weigh term importance for topic modeling.
*   **Coherence Scores for Model Selection:** Showcased a quantitative method for choosing the optimal number of topics in LDA.
*   **Visualization is Key:** Underscored the importance of tools like Word Clouds and pyLDAvis for interpreting and communicating topic modeling results effectively.

---

*Day 84 of #100DaysOfDataScience tackled the challenge of understanding public discourse on cutting-edge AI using NLP topic modeling. A fascinating look into the human side of technological disruption! - Vatsal Parikh*
