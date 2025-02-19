# Day 18. 100 Days of Data Science Challenge - 02/18/2025

<h1>📊 Vector Databases, Semantic Search & Retrieval-Augmented Generation (RAG)</h1>

<p align="center">
    <img src="https://img.shields.io/badge/NLP-Vector%20Databases-blue" alt="NLP">
    <img src="https://img.shields.io/badge/Search-Semantic%20Search-brightgreen" alt="Semantic Search">
    <img src="https://img.shields.io/badge/OpenAI-Embeddings-orange" alt="OpenAI">
    <img src="https://img.shields.io/badge/Pinecone-VectorDB-red" alt="Pinecone">
</p>

## 🚀 Project Overview  

This project explores **vector databases, embeddings, and retrieval-augmented generation (RAG)** to power **semantic search and chatbot retrieval systems**.  

💡 **Key Goals:**  
- Store and retrieve **high-dimensional embeddings** efficiently using **Pinecone**.  
- Implement **semantic search** using **OpenAI embeddings** and **metadata filtering**.  
- Build a **retrieval-augmented chatbot** that fetches relevant documents before generating answers.  

---

## 📂 Datasets Used  

| Dataset | Description |
|---------|------------|
| 📖 **SQuAD (`squad_dataset.csv`)** | Extracted Q&A pairs for knowledge retrieval |
| 🎥 **YouTube Transcripts (`youtube_rag_data.csv`)** | Text from educational videos for chatbot queries |

Each dataset was **converted into embeddings** and stored in **Pinecone** for efficient retrieval.  

---

## 🔧 Technologies & Tools  

| **Technology** | **Use Case** |
|--------------|------------|
| 🟢 **Pinecone** | Vector database for storing & retrieving embeddings |
| 🟠 **OpenAI Embeddings** | Converts text into high-dimensional vectors |
| 🔵 **FAISS (Future Work)** | Alternative for large-scale similarity search |
| 🟣 **Metadata Filtering** | Restricts search results using structured attributes |
| 🟡 **RAG (Retrieval-Augmented Generation)** | Enhances chatbot accuracy with retrieved documents |

---

## 🏗 Project Breakdown  

### 🔹 1️⃣ Creating & Managing a Pinecone Index  
📌 **Goal:** Store and manage vector representations of text data.  
📌 **Steps:**  
✅ Created a **Pinecone index** with `cosine` similarity for efficient retrieval.  
✅ Configured a **1536-dimensional vector space** to store embeddings.  
✅ Ingested text data along with metadata (e.g., source, timestamp).  

---

### 🔹 2️⃣ Embedding Text Data into Vector Space  
📌 **Goal:** Convert raw text into vector embeddings.  
📌 **Method:**  
✅ Used **OpenAI’s `text-embedding-3-small` model** to generate **1536-dimensional embeddings**.  
✅ Processed **SQuAD and YouTube transcripts** for storage in Pinecone.  
✅ Stored embeddings **with metadata** (e.g., title, category, date).  

📌 **Outcome:** Text data transformed into a **searchable semantic space**.  

---

### 🔹 3️⃣ Semantic Search & Metadata Filtering  
📌 **Goal:** Retrieve the most **meaningful** text passages from the database.  
📌 **Methods Used:**  
🔹 **Querying by Vector Similarity** – Find most relevant documents.  
🔹 **Metadata Filtering** – Restrict search results (e.g., `year = 2024`, `genre = "AI"`).  
🔹 **Top-K Retrieval** – Return the **K most relevant** results.  

📌 **Example Query:**  
💬 **User Question:** `"What is in front of the Notre Dame Main Building?"`  
🔍 **Search Method:** Query embeddings + Top-5 vector matches  
📖 **Retrieved Answer:** `"The golden statue of Mary stands in front of the Notre Dame Main Building."`  

📌 **Outcome:** A **highly accurate search system** that understands **meaning, not just keywords**.  

---

### 🔹 4️⃣ Retrieval-Augmented Generation (RAG) for Chatbots  
📌 **Goal:** Improve chatbot responses by **retrieving documents before answering**.  
📌 **Method:**  
✅ Implemented **retrieval functions** to fetch **relevant sources**.  
✅ Used **context-aware prompting** to feed retrieved text into OpenAI’s GPT model.  
✅ Built a **question-answering pipeline** integrating **search + generative AI**.  

📌 **Example:**  
💬 **User Query:** `"How to build next-level Q&A with OpenAI?"`  
📖 **Retrieved Sources:** YouTube videos on **transformers and Q&A models**  
🤖 **Generated Answer:** `"To build a next-level Q&A system, use OpenAI embeddings, Pinecone for retrieval, and fine-tune a transformer model on relevant datasets."`  

📌 **Outcome:** A **chatbot that retrieves knowledge before generating answers**, improving factual accuracy.  

---

## 📊 Key Learnings  

✅ **Vector databases enable scalable AI-powered search**.  
✅ **Embeddings capture deep semantic relationships between words**.  
✅ **Metadata filtering refines search results** for more precise queries.  
✅ **RAG (Retrieval-Augmented Generation) enhances chatbot accuracy**, grounding responses in retrieved knowledge.  

---

## 🔮 Future Enhancements  

🟢 **Hybrid Search** – Combine **BM25 keyword search + Embeddings** for better retrieval.  
🟠 **Fine-Tuned Embeddings** – Train custom embedding models for domain-specific retrieval.  
🔵 **Expand Knowledge Base** – Add more datasets (research papers, customer queries).  
🟣 **Improved RAG Models** – Enhance document ranking for chatbot queries.  

---

## 🔥 Next Steps  

📌 **Test FAISS vs. Pinecone** for large-scale retrieval.  
📌 **Integrate real-time search updates** for dynamic content.  
📌 **Fine-tune OpenAI embeddings** for improved relevance in Q&A.  

---
