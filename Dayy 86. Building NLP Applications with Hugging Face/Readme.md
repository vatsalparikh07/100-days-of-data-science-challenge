# NLP Showcase: Rent the Runway Review Analysis ✨👗

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Wrangling-yellowgreen?style=flat-square&logo=pandas)](https://pandas.pydata.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Transformers-orange?style=flat-square)](https://huggingface.co/)
[![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-Embeddings-blueviolet?style=flat-square)](https://www.sbert.net/)
[![Visualization](https://img.shields.io/badge/Viz-Seaborn%2C_Matplotlib-red?style=flat-square)](https://matplotlib.org/)
[![Dataset](https://img.shields.io/badge/Dataset-RentTheRunway-lightgrey?style=flat-square)](https://cseweb.ucsd.edu//~jmcauley/datasets.html#clothing_fit)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_86-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Unlocking Customer Insights with Modern NLP

Welcome to Day 86 of my #100DaysOfDataScience challenge! Today, we're diving into the world of **Natural Language Processing (NLP)** using the powerful **Hugging Face ecosystem** to analyze customer reviews from the **Rent the Runway dataset** (`runway.csv`). This dataset provides a rich mix of textual reviews, ratings, user metadata, and item details – perfect for applying cutting-edge NLP techniques.

**The Mission:**
*   Demonstrate foundational NLP workflows using Hugging Face `transformers` and `sentence-transformers`.
*   Perform **Sentiment Analysis** to gauge overall customer satisfaction.
*   Generate **Text Embeddings** to capture the semantic meaning of reviews.
*   Implement **Semantic Search** to find reviews conceptually similar to a given query.
*   Showcase essential **Text Preprocessing** steps and **Data Visualization** for interpretation.

This project highlights how readily accessible tools like Hugging Face can transform raw text into valuable business intelligence, helping understand customer voice at scale.

---

## ✨ Key Features & Concepts Mastered

*   **Hugging Face Pipelines:** Utilized the high-level `pipeline()` abstraction for quick and efficient **Sentiment Analysis** using a fine-tuned `distilbert` model.
*   **Text Preprocessing:** Implemented a standard cleaning pipeline for the `review_text` data:
    *   Replacing specific characters (`/` with space).
    *   Removing punctuation (`string.punctuation`).
    *   Removing digits (`regex`).
    *   Normalizing whitespace (`regex`).
    *   Lowercasing (`.str.lower()`).
*   **Sentiment Visualization:** Employed **Seaborn** and **Matplotlib** to visualize the distribution of sentiment scores (histogram) and track sentiment trends over time (bar plot by year).
*   **Sentence Embeddings:** Generated dense vector representations of review text using `sentence-transformers` with the popular `all-MiniLM-L6-v2` model, capturing semantic meaning beyond keywords.
*   **Semantic Search:** Implemented efficient similarity search using `sentence_transformers.util.semantic_search` to find the top-k reviews most similar (based on cosine similarity of embeddings) to a given query text.
*   **Pandas for Data Wrangling:** Leveraged Pandas throughout for data loading, cleaning, transformation, feature engineering (e.g., extracting 'year'), and results handling.

---

## 🛠️ Tech Stack: The NLP Power Tools

*   **Core Language:** Python 3.8+
*   **Data Manipulation:** Pandas, NumPy
*   **NLP Core:**
    *   Hugging Face `transformers` (`pipeline`)
    *   `sentence-transformers` (`SentenceTransformer`, `util.semantic_search`)
*   **Text Processing:** `re` (Regular Expressions), `string`
*   **Visualization:** Matplotlib (`pyplot`), Seaborn
*   **Environment:** Jupyter Notebook (`solution.ipynb`)
*   **Display:** `IPython.display` (`display`, `Markdown`)

**Models Used:**
*   Sentiment Analysis: `distilbert-base-uncased-finetuned-sst-2-english` (via HF Pipeline)
*   Embeddings: `all-MiniLM-L6-v2` (via Sentence Transformers)

---

## 🗺️ The Analytical Workflow: From Raw Reviews to Semantic Understanding

This project followed a structured pipeline, detailed within `solution.ipynb`:

1.  **Loading & Initial Checks (`Task 1`):**
    *   Loaded `runway.csv` into a Pandas DataFrame (`runway`), ensuring `review_date` was parsed correctly (`parse_dates`).
    *   Inspected data types (`.info()`), missing values, and basic structure.

2.  **Text Cleansing Ritual (`Task 2`):**
    *   Applied a series of string operations (`.str.replace`, `.str.translate`) and regex (`re.sub` implicitly via `.str.replace`) to the `review_text` column.
    *   Created a new column `review_text_cleaned` containing the processed, lowercase text, ready for NLP tasks.

3.  **Gauging the Mood: Sentiment Analysis (`Task 3`):**
    *   Instantiated a Hugging Face `pipeline` specifically for `"sentiment-analysis"` using the `distilbert-base-uncased-finetuned-sst-2-english` model.
    *   Passed the `review_text_cleaned` column (as a list) to the pipeline.
    *   Extracted the resulting sentiment `label` ('POSITIVE'/'NEGATIVE') and `score` (confidence) into new DataFrame columns (`clean_sentiment_category`, `clean_sentiment_score`).

4.  **Visualizing Sentiment (`Task 4 & 5`):**
    *   **Distribution:** Created a **histogram** (`seaborn.histplot`) of the `clean_sentiment_score`, revealing a strong skew towards positive reviews.
    *   **Trends Over Time:** Extracted the `year` from `review_date`. Grouped review counts by `year` and `clean_sentiment_category`. Visualized this using a **grouped bar chart** (`seaborn.barplot`), showing the dominance of positive reviews across all years in the dataset.

![image](https://github.com/user-attachments/assets/55748f37-3b05-40b7-9285-52aa7d22d33e)
*Fig 1: Distribution heavily skewed towards positive sentiment.*

![image](https://github.com/user-attachments/assets/d04a183c-052c-4ac7-8fc8-09962621b5b4)
*Fig 2: Positive reviews consistently outnumber negative ones each year.*

5.  **Capturing Meaning: Text Embeddings (`Task 6 & 7`):**
    *   Instantiated a `SentenceTransformer` using the efficient `all-MiniLM-L6-v2` model. This model is great for generating general-purpose sentence embeddings.
    *   Used the `model.encode()` method to convert the `review_text_cleaned` into a list of dense numerical vectors (`embeddings`), capturing their semantic content.

6.  **Finding Similar Voices: Semantic Search (`Task 8 & 9`):**
    *   Defined example `query_texts`.
    *   Encoded the queries using the *same* Sentence Transformer model.
    *   Utilized `semantic_search(query_embeddings, embeddings, top_k=5)` to efficiently find the 5 reviews whose embeddings had the highest **cosine similarity** to each query embedding.
    *   Displayed the query and its top 5 most semantically similar reviews from the dataset, demonstrating the ability to find conceptually related text beyond simple keyword matching.

![image](https://github.com/user-attachments/assets/be92169c-b138-42e9-a01d-f0a4c009f407)
*Fig 3: Embeddings visualized for 'rented for' reasons and category using t-SNE*

---

## 💡 Key Learnings & Impact

*   **Hugging Face Simplifies NLP:** The `pipeline` and `sentence-transformers` libraries make complex tasks like sentiment analysis and embedding generation remarkably accessible.
*   **Preprocessing Still Matters:** Even with powerful transformer models, basic text cleaning improves consistency and can enhance performance/reduce noise.
*   **Sentiment Analysis Use Cases:** Quickly gauge overall customer feeling, track trends, and identify areas needing attention (though this dataset was overwhelmingly positive).
*   **Embeddings Unlock Deeper Meaning:** Sentence embeddings capture semantic nuances that keyword searches miss, enabling powerful applications like semantic search, clustering, and recommendation.
*   **Semantic Search for Exploration:** Finding reviews similar to a specific theme (e.g., "dress for a wedding," "comfortable fit") becomes easy, helping users discover relevant feedback or allowing businesses to analyze recurring topics.

---

*Day 86 of #100DaysOfDataScience successfully applied modern NLP techniques using Hugging Face to extract valuable insights from customer reviews. From sentiment trends to semantic search, these tools empower data-driven understanding of text data! - Vatsal Parikh*
