# 🧠 Building an AI Note-taking Application

[![Python](https://img.shields.io/badge/Python-Modern_Stack-blue?logo=python&style=flat-square)](https://www.python.org)
[![LLMs](https://img.shields.io/badge/LLMs-Llama_Fine--Tuning-orange?logo=huggingface&style=flat-square)](https://huggingface.co/models)
[![RAG](https://img.shields.io/badge/RAG-Advanced_Techniques-yellowgreen?style=flat-square)](https://arxiv.org/abs/2312.10997)
[![MLOps](https://img.shields.io/badge/MLOps-ZenML%2C_Comet%2C_Opik-blueviolet?style=flat-square)](https://zenml.io/)
[![Database](https://img.shields.io/badge/DB-MongoDB_Vector_Search-green?logo=mongodb&style=flat-square)](https://www.mongodb.com/products/platform/vector-search)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_92-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

![image](https://github.com/user-attachments/assets/2e30ad86-ca8d-47b6-832f-bd011b54e980)
*Fig 1: Detailed architecture of the "Second Brain" AI Assistant, showcasing data flow from Notion to an interactive agent.*

## 🎯 Project Goal: Architecting a Production-Ready Personal AI Research Assistant

Welcome to Day 92 of my #100DaysOfDataScience challenge! Today's project is an ambitious dive into building a **"Second Brain" AI Assistant**. Inspired by the open-source course from Decoding ML, this endeavor aims to create a sophisticated system that allows you to converse with your personal knowledge base – in this case, data extracted from Notion.

The goal isn't just a simple chatbot; it's to architect and implement a **production-ready, agentic Retrieval-Augmented Generation (RAG) system** powered by fine-tuned Large Language Models (LLMs) and robust MLOps practices. Imagine asking complex questions about your research notes, ideas, and digital resources and getting synthesized, contextually relevant answers directly from *your* data.

**Key Components Explored:**
1.  **Data Ingestion & Processing:** From Notion (or S3 snapshots) to a structured, queryable format.
2.  **Advanced RAG Implementation:** Beyond naive RAG, incorporating techniques like contextual retrieval and hybrid search.
3.  **LLM Fine-Tuning:** Specializing an open-source LLM (like Llama) for tasks like summarization.
4.  **Agentic Architecture:** Building an agent that can use multiple tools (retrieval, summarization) to answer user queries.
5.  **LLMOps & MLOps Best Practices:** Implementing data/model registries, experiment tracking, pipeline orchestration, and observability.

---

## ✨ Core Concepts & Technologies:

This project touches upon a wide array of cutting-edge AI and MLOps concepts:

*   **"Second Brain" Concept:** Leveraging personal knowledge management systems (like Notion) as the foundation for an AI assistant [4].
*   **FTI Architecture (Feature, Training, Inference):** A design pattern for structuring production ML systems, ensuring clear separation of concerns.
*   **Data Pipelines (Offline):**
    *   **Data Collection:** Extracting data from sources like Notion API and storing raw documents (e.g., in S3).
    *   **ETL (Extract, Transform, Load):** Crawling embedded links (using `Crawl4AI`), normalizing content to Markdown, computing quality scores (using LLMs), and loading into a document database (e.g., **MongoDB**).
*   **Feature Pipelines (Offline):**
    *   **RAG Feature Pipeline:** Implementing advanced pre-retrieval RAG techniques (e.g., Contextual Retrieval needing a summarization LLM, Hybrid Search). This involves chunking, embedding, and loading into a **MongoDB vector index**.
    *   **Dataset Generation Pipeline:** Using distillation techniques to create high-quality instruction datasets (e.g., for summarization) from the processed documents. Storing this in a **Data Registry** (e.g., Hugging Face Datasets).
*   **Training Pipeline (Offline):**
    *   Fine-tuning an open-source LLM (e.g., Llama 3.1 8B) using the generated instruct dataset. Tools like **Unsloth** for efficient fine-tuning and **Comet** for experiment tracking (metrics, hyperparameters) are highlighted.
    *   Storing the fine-tuned model in a **Model Registry** (e.g., Hugging Face Model Hub).
*   **Inference Pipelines (Online):**
    *   **Summarization Inference Pipeline:** Deploying the fine-tuned summarization LLM as a real-time inference endpoint (e.g., on **Hugging Face Dedicated Endpoints**).
    *   **Agentic Inference Pipeline:** The core AI assistant. Built using an agent framework (e.g., **Hugging Face smolagents**) that utilizes multiple tools:
        *   **Retriever Tool:** Interacts with the MongoDB vector database to fetch relevant chunks.
        *   **Summarization Tool:** Uses the fine-tuned summarization LLM to synthesize answers or condense retrieved context.
*   **Observability Pipeline (Online):**
    *   **Prompt Monitoring & LLM Evaluation:** Using tools like **Opik** for monitoring complex prompt traces and evaluating agentic/RAG applications.
*   **Orchestration & MLOps Tooling:**
    *   **ZenML:** Orchestrating and managing the offline data, feature, and training pipelines, providing tracking and a UI for pipeline history.
    *   **Python Project Management:** Using modern tools like `uv` and `ruff`.
*   **LangChain (Judicious Use):** While the course emphasizes building from scratch for intuition, it also shows how to use and *extend* LangChain components for specific tasks like loading/retrieving from MongoDB vector databases.

---

## 🛠️ Tech Stack & Tools:

*   **Core AI/ML:**
    *   LLMs: **Llama 3.1 8B** (example for fine-tuning), **OpenAI Models** (for quality scoring, potentially agents)
    *   Fine-Tuning: **Unsloth**
    *   Embeddings & Vector Search: **MongoDB Atlas Vector Search**
    *   Agent Framework: **Hugging Face smolagents**
    *   RAG Implementation: Custom, potentially with LangChain extensions
*   **Data Management & Processing:**
    *   Data Source Example: **Notion**
    *   Web Crawling: **Crawl4AI**
    *   Document Database: **MongoDB**
    *   Vector Database: **MongoDB Atlas Vector Search**
    *   Data/Model Registries: **Hugging Face Hub**
*   **MLOps & Workflow:**
    *   Orchestration: **ZenML**
    *   Experiment Tracking: **Comet**
    *   Observability (Prompt Monitoring & LLM Evaluation): **Opik**
    *   Deployment: **Hugging Face Dedicated Endpoints** (for serverless inference)
*   **Programming & Utilities:**
    *   Language: **Python**
    *   Project Management: `uv`, `ruff`
    *   UI (Optional): Gradio (for agent interaction)

---

## 🗺️ The Architectural Vision:

The system is architected with a clear distinction between offline and online pipelines, following MLOps best practices:

**Offline Pipelines (Orchestrated by ZenML):**
1.  **Data Collection & ETL:** Raw Notion documents are collected, links within them are crawled, all content is normalized to Markdown, quality-scored by an LLM, and stored in MongoDB.
2.  **Filtering (for RAG):** Medium-to-high quality documents are selected for the RAG pipeline.
3.  **RAG Feature Pipeline:** Documents are chunked, embedded, and loaded into the MongoDB Vector Index. This pipeline might also generate summaries for contextual retrieval.
4.  **Filtering (for Fine-Tuning):** High-quality documents are selected for generating a summarization dataset.
5.  **Dataset Generation Feature Pipeline:** A summarization instruct dataset is created (e.g., via distillation) and stored in a Data Registry.
6.  **Training Pipeline:** The summarization LLM (e.g., Llama) is fine-tuned on this dataset and stored in a Model Registry.

**Online Pipelines (Real-time Interaction):**
7.  **User Query:** A user asks a question via a UI (e.g., Gradio).
8.  **Agentic Layer:** The agent receives the query.
    *   It uses its **Retriever Tool** to perform a semantic search on the **MongoDB Vector Index**, fetching the top K relevant chunks.
    *   If needed, it uses its **Summarization Tool** (which calls the fine-tuned **Summarization Inference Pipeline** deployed on Hugging Face) to process retrieved documents or synthesize an answer.
9.  **Answer Generation:** The agent formulates and returns the answer to the user.
10. **Observability:** **Opik** monitors prompt traces from the agent and evaluates the LLM's responses.

This architecture emphasizes decoupling, scalability, and continuous improvement through MLOps practices.

---

## 💡 Key Learnings & Objectives from Undertaking This Project

Following the "Second Brain AI Assistant" course blueprint is an ambitious endeavor. Key learnings for Day 92 and beyond would include:

*   **Full-Stack LLM Application Design:** Understanding how to architect complex, production-grade AI systems beyond simple notebooks.
*   **The Nuances of Advanced RAG:** Moving past basic RAG to implement techniques that improve retrieval relevance and answer quality (e.g., contextual retrieval, hybrid search).
*   **The Value of Fine-Tuning:** Realizing when and how to fine-tune smaller, open-source LLMs for specialized tasks (like summarization) to improve performance and reduce reliance on larger, more expensive models.
*   **MLOps in Practice:** Gaining hands-on experience with essential MLOps tools for orchestration (ZenML), experiment tracking (Comet), and observability (Opik). This is critical for building reliable and maintainable AI systems.
*   **Agentic Systems:** Learning how to build AI agents that can reason and use multiple tools to accomplish complex tasks.
*   **Data as the Foundation:** Reinforcing the "garbage in, garbage out" principle – the importance of high-quality data pipelines (collection, cleaning, quality scoring) for both RAG and fine-tuning.
*   **Offline vs. Online Distinction:** Clearly understanding the different requirements and deployment strategies for batch processing (offline pipelines) and real-time services (online pipelines).

---

*Day 92 of #100DaysOfDataScience sets the stage for an exciting and comprehensive project: building a personalized "Second Brain" AI assistant. This endeavor, guided by the Decoding ML open-source course, will explore advanced RAG, LLM fine-tuning, agentic architectures, and crucial MLOps practices. The journey to unlock the wisdom of my own digital mind has begun! - Vatsal Parikh*
