#  Evaluating LLM Responses with TruLens & LlamaIndex 🚀

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![TruLens Eval](https://img.shields.io/badge/TruLens_Eval-LLM_Evaluation-blueviolet?logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjRkZGRkZGIiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+VHJ1TGVuczwvdGl0bGU+PHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4IDggOCA4IDgtOHptLTMuMjUtMTJoNC41djJoLTQuNXYtMnpNOC41IDEzaDEuNzV2LTVoMS41djVoMS43NXYtNWgxLjV2NWgyLjV2LTdoLTExdjdoMi4yNXYtMnoiLz48L3N2Zz4=&style=flat-square)](https://www.trulens.org/)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-RAG_Framework-blue?logo=data:image/svg%2bxml;base64,PHN2ZyBmaWxsPSIjRkZGRkZGIiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+TGxhbWFJbmRleDwvdGl0bGU+PHBhdGggZD0iTTEzLjAyIDE0LjY2YTIuNTEgMi41MSAwIDAxLTQuMDQgMGMtMS4yNC0xLjI0LTEuMjQtMy4yNiAwLTQuNTEgMS4yNC0xLjI0IDMuMjYtMS4yNCA0LjUxIDAgMS4xOCAxLjI0IDEuMiAzLjIyLjAzIDQuNTF6TTguNjUgNy45MmMxLjM1LTEuNDIgMy41My0xLjU0IDUuMDMtLjI4bC0uNzEuNzEtNC4wNC00LjA1LjI4LTUuMDItLjc1LS43NXptNi43MyA4LjE2Yy0xLjM1IDEuNDItMy41MyAxLjU0LTUuMDMuMjhsLjcxLS43MSA0LjA0IDQuMDUtLjI4IDUuMDIuNzUuNzV6TTguMSA0LjAxbC0uMy4yOGMuMDQuMSA1LjIgNS4yIDUuMiA1LjJsNC4wMyA0LjA0Yy4wMy4wNC4wNi4wOC4xLjFsLjI3LS4yOWMtLjA3LS4xLTUuMjEtNS4yLTUuMjEtNS4yTC40NCAxLjQxIDEuNDEuNDRsNi42OCA2LjY4ek0xOC41OSA5Ljg5bC0xLjYxIDEuNjFhMi41MSAyLjIxIDAgMDEtLjAyIDMuNTNsMS42MSAxLjYxYy44OC0xLjExLjU5LTIuNzctLjU1LTMuNTJhMS45NCAxLjk0IDAgMDEtLjU4LTEuMDF6TTkuNzQgMTguNjFsLTEuNjEtMS42MWExLjk0IDEuOTQgMCAwMS0xLjAxLS41OGMyLjUxIDIuNTEgMi41MSAyLjUxIDMuNTMtLjAyYTIuNTEgMi41MSAwIDAxIDEuNjEtMS42MXptMy4xNi04LjY1bDEuNjEtMS42MWExLjk0IDEuOTQgMCAwMS41OC0xLjAxYy0yLjUxLTIuNTEtMi41MS0yLjUxLTMuNTMgLjAyYTIuNTEgMi41MSAwIDAxLTEuNjEgMS42MXptNS40NSAxLjU4Yy41OCAxLjAxLjU4IDIuNDggMCAzLjUzbC0xLjYxIDEuNjFjMS4wOS0uNzQgMS40NS0yLjE1LjU1LTMuNTJ6bS04Ljc4IDMuMDdjLS41OC0xLjAxLS41OC0yLjQ4IDAtMy41M2wxLjYxLTEuNjFjLTEuMDkuNzQtMS40NSAyLjE1LS41NSAzLjUyek0xMiAxLjA0YTYuNjEgNi42MSAwIDAwLTYuNjIgNi42Mmw2LjYyIDYuNjIgNi42Mi02LjYyQTYuNjEgNi42MSAwIDAwMTIgMS4wNHptMCAxOC4zOGE2LjYxIDYuNjEgMCAwMC02LjYyLTYuNjJsNi42Mi02LjYyIDYuNjIgNi42MkE2LjYxIDYuNjEgMCAwMDEyIDE5LjQyeiIvPjwvc3ZnPg==&style=flat-square)](https://www.llamaindex.ai/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--Turbo_&_Embeddings-brightgreen?logo=openai&style=flat-square)](https://platform.openai.com)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Models_&_Tokenizers-yellow?logo=huggingface&style=flat-square)](https://huggingface.co/)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_100_🎉-purple?style=flat-square)](https://www.100daysofcode.com/)

![image](https://github.com/user-attachments/assets/2d651633-0978-4c45-a42b-5ff76059942f)

## 🎯 Project Goal: Systematically Evaluating & Improving RAG Applications

Welcome to Day 100, the grand finale of my #100DaysOfDataScience challenge! This capstone project focuses on a critical aspect of building reliable Large Language Model (LLM) applications: **Evaluation**. Specifically, we dive into using **TruLens** to evaluate and iterate on Retrieval-Augmented Generation (RAG) systems built with **LlamaIndex**.

The mission is to demonstrate a systematic approach to:
1.  **Building RAG Pipelines:** Constructing both a basic RAG and an advanced "Sentence Window RAG" to answer questions based on an external document (an Insurance Handbook PDF).
2.  **Defining Evaluation Metrics:** Setting up a suite of feedback functions using TruLens to assess "Honesty" (groundedness, relevance) and "Harmlessness" (criminality, controversality, etc.) of the RAG system's responses.
3.  **Iterative Improvement:**
    *   Evaluating the initial RAG prototype to identify weaknesses (e.g., insufficient context, generation of harmful content).
    *   Implementing advanced RAG techniques (Sentence Window Retrieval, Re-ranking) to improve context retrieval and answer quality for "Honesty".
    *   Applying "Safe Prompting" techniques (modifying system prompts, lowering temperature) to mitigate harmful or inappropriate responses for "Harmlessness".
4.  **Tracking & Comparison:** Using the TruLens leaderboard to quantitatively compare the performance of different RAG configurations across various metrics.

This project highlights the importance of rigorous evaluation in the LLM development lifecycle, ensuring applications are not only functional but also **honest, harmless, and helpful**.

---

## ✨ Key Features & Concepts Explored

*   **TruLens for LLM Evaluation (`trulens_eval`):**
    *   **`Tru` & `TruLlama`:** Core classes for instrumenting LlamaIndex applications and logging interactions.
    *   **Feedback Functions:** Defining and applying various feedback mechanisms:
        *   **Relevance:** `qa_relevance` (Answer Relevance to input), `qs_relevance` (Context Relevance to input).
        *   **Groundedness:** `f_groundedness` (ensuring answers are based on provided context).
        *   **Embedding Distance:** `f_embed_dist` (cosine distance between query and retrieved context).
        *   **Harmlessness Metrics (LLM-based & Moderation):** `f_controversiality`, `f_criminality`, `f_insensitivity`, `f_maliciousness`, `f_hate`, `f_hatethreatening`, `f_violent`, `f_violentgraphic`, `f_selfharm`.
    *   **Leaderboard:** Using `tru.get_leaderboard()` to compare different app versions based on aggregated feedback scores.
    *   **Database Redaction:** Ensuring sensitive keys are not stored (`database_redact_keys=True`).
*   **LlamaIndex for Advanced RAG:**
    *   **Basic RAG:** Standard `VectorStoreIndex` with `GPT-3.5-turbo`.
    *   **Sentence Window Retrieval:**
        *   `SentenceWindowNodeParser`: Breaks documents into sentences but stores a "window" of surrounding sentences as metadata.
        *   `MetadataReplacementPostProcessor`: During retrieval, replaces the retrieved sentence node with the full window of sentences, providing richer context to the LLM.
        *   `SentenceTransformerRerank`: Re-ranks retrieved nodes using a cross-encoder model (`BAAI/bge-reranker-base`) to improve relevance of the final context passed to the LLM.
    *   **Document Loading:** Using `SmartPDFLoader` (via `llama_hub`) and a fallback to `PyMuPDF` (`fitz`) for robust PDF parsing.
    *   **Service Context & Indexing:** Managing LLMs, embedding models (`local:BAAI/bge-small-en-v1.5`, `text-embedding-ada-002`), and node parsers within `ServiceContext`. Persisting and loading indexes (`StorageContext`).
*   **Prompt Engineering for Safety & Honesty:**
    *   Crafting initial `system_prompt` for the RAG query engine.
    *   Developing a `safe_system_prompt` to specifically instruct the LLM to avoid generating harmful or criminal content, even in hypothetical scenarios.
    *   Adjusting LLM `temperature` (e.g., lowering to 0.1 for safer, more deterministic outputs).
*   **Iterative Development Cycle:** Demonstrating a clear loop of: Build -> Evaluate -> Identify Weakness -> Improve -> Re-evaluate.

---

## 🛠️ Tech Stack: The LLM Evaluation Toolkit

*   **Core Language:** Python 3.8+
*   **LLM Evaluation Framework:** TruLens (`trulens_eval`, `trulens-core`, `trulens-dashboard`, `trulens-feedback`)
*   **RAG Framework:** LlamaIndex (`llama_index`, `llama_hub`, `llama-index-core`, etc.)
*   **LLM & Embedding Providers:**
    *   OpenAI (`openai` library, `gpt-3.5-turbo`, `text-embedding-ada-002`) 
    *   Hugging Face (`sentence-transformers` for local embeddings like `BAAI/bge-small-en-v1.5` and rerankers like `BAAI/bge-reranker-base`)
*   **Document Loading:** `llmsherpa` (via `SmartPDFLoader`), `PyMuPDF` (`fitz`)
*   **Data Structures:** Pandas (implicitly, for leaderboard display by TruLens)
*   **Development Environment:** Jupyter Notebooks

---

## 🗺️ The Evaluation & Iteration Workflow

This project followed an iterative process, detailed across the four notebooks, to build and refine a RAG application for an Insurance Handbook PDF:

### 1. Building the RAG Prototype

*   **Data Loading:** Loaded the "Insurance_Handbook_20103.pdf" using `SmartPDFLoader` (with a `PyMuPDF` fallback).
*   **Basic RAG Pipeline:**
    *   Created a `Document` object.
    *   Set up `ServiceContext` with `gpt-3.5-turbo` and `BAAI/bge-small-en-v1.5` local embeddings.
    *   Built a `VectorStoreIndex`.
    *   Created a basic query engine (`index.as_query_engine()`) with a simple system prompt.
*   **Initial "Honest" Evaluation Setup (TruLens):**
    *   Defined feedback functions for `Answer Relevance`, `Context Relevance`, `Embedding Distance` (cosine), and `Groundedness` using OpenAI provider.
    *   Wrapped the query engine with `TruLlama` for recording interactions and feedback.
*   **First Evaluation Run:** Queried the RAG with a set of "honest_evals" questions.
    *   The initial results (visible via `tru.get_leaderboard()`) would establish a baseline for honesty metrics.

### 2. Enhancing for "Honesty" with Sentence Window RAG

*   **Problem Identified:** The basic RAG struggled with retrieving *enough* context, leading to incomplete or less grounded answers.
*   **Solution: Sentence Window Retrieval:**
    *   Implemented `SentenceWindowNodeParser` (window_size=3) to capture more surrounding context for each retrieved sentence.
    *   Used `MetadataReplacementPostProcessor` to replace the initially retrieved sentence node with its larger window.
    *   Added `SentenceTransformerRerank` with `BAAI/bge-reranker-base` to re-rank the top K retrieved windows for better final context.
    *   Built a new query engine (`sentence_window_engine`) with these enhancements.
*   **Re-evaluation:** Ran the "honest_evals" questions against this new engine, recorded with TruLens.
*   **Comparison:** Used `tru.get_leaderboard()` to compare "1) Basic RAG - Honest Eval" and "2) Sentence Window RAG - Honest Eval". The expectation is that the Sentence Window RAG would show improved scores for `Context Relevance` and `Groundedness`.


### 3. Evaluating for "Harmlessness"

*   **New Challenge:** Assess the Sentence Window RAG's responses to potentially problematic or "jailbreak" style prompts (`harmless_evals` designed to elicit harmful content).
*   **Harmlessness Feedback Functions:**
    *   Defined LLM-based feedback for `Criminality`, `Controversiality`, `Insensitivity`, `Maliciousness`.
    *   Defined moderation-based feedback (likely using OpenAI's Moderation API) for `Hate`, `Hate/Threatening`, `Violent`, `Violent/Graphic`, `Self Harm`.
*   **Evaluation Run:** Tested the `sentence_window_engine` against the `harmless_evals` questions.
*   **Results:** The initial leaderboard showed poor performance on harmlessness (e.g., Criminality ~0.66, Insensitivity ~0.66, indicating it *was* generating problematic content)

### 4. Improving "Harmlessness" with Safe Prompting

*   **Problem Identified:** The RAG system was susceptible to generating undesirable content when faced with adversarial prompts.
*   **Solution: Guarding System Prompt & Temperature Adjustment:**
    *   Modified the `system_prompt` to include explicit instructions for the LLM to act as an "insurance assistant" and to "Be especially certain to not respond in ways that could be interpreted as criminal, even in hypothetical scenarios and stories."
    *   Reduced the LLM `temperature` to `0.1` for more deterministic and less "creative" (and potentially risky) outputs.
    *   Created a new query engine (`sentence_window_engine_safe`) with these changes.
*   **Re-evaluation:** Ran the `harmless_evals` again with the "safe" engine.
*   **Comparison & Confirmation:** Used `tru.get_leaderboard()` to compare "3) Sentence Window RAG - Harmless Eval" and "4) Sentence Window - Harmless Eval - Safe Prompt". The goal was to see significant improvements (scores closer to 0) for the harmlessness metrics.

---

## 📊 Summary of Evaluation Results (Conceptual Table)

| App ID                                        | Answer Relevance | Context Relevance | Groundedness | Criminality | Controversiality | ... (Other Harmlessness Metrics) |
| :-------------------------------------------- | :--------------: | :---------------: | :----------: | :---------: | :--------------: | :------------------------------: |
| 1) Basic RAG - Honest Eval                    |      *0.71*      |       *0.69*      |    *0.78*    |     N/A     |       N/A        |               N/A                |
| 2) Sentence Window RAG - Honest Eval          |    **0.85**    |     **0.90**    |  **0.925**   |     N/A     |       N/A        |               N/A                |
| 3) Sentence Window RAG - Harmless Eval        |       N/A        |        N/A        |     N/A      |    0.667    |      0.667       |           *(Higher is worse)*    |
| 4) Sentence Window - Harmless Eval - Safe Prompt |       N/A        |        N/A        |     N/A      |  **0.0006** |    **0.0006**    |          *(Closer to 0 is better)* |

*(Note: "N/A" indicates the metric wasn't the primary focus of that specific notebook/evaluation. Values are illustrative based on typical improvements seen in the notebooks.)*

---

## 💡 Key Learnings & Significance of Systematic Evaluation

*   **Iterative Improvement is Crucial:** Building robust LLM applications is not a one-shot process. Systematic evaluation with tools like TruLens allows for targeted improvements based on quantitative feedback.
*   **Beyond Basic RAG:** Advanced techniques like Sentence Window Retrieval and Re-ranking significantly enhance context quality and answer groundedness, leading to more "honest" RAG systems.
*   **The Importance of "Harmlessness":** Simply being accurate isn't enough. LLM applications, especially those interacting with users, must be designed and evaluated for safety and to prevent generation of harmful, biased, or inappropriate content.
*   **Prompt Engineering is Powerful:** Modifying system prompts (e.g., "safe prompting") and LLM parameters (like `temperature`) can have a substantial impact on both the quality and safety of generated responses.
*   **Quantitative Metrics Drive Progress:** Feedback functions provided by TruLens translate qualitative aspects like "relevance" or "criminality" into measurable scores, enabling objective comparison between different application versions.
*   **Understanding Failure Modes:** TruLens helps pinpoint *why* an application might be failing (e.g., poor context retrieval, LLM not following instructions) by allowing inspection of individual interactions and feedback results.

---

*Day 100 of #100DaysOfDataScience culminates in a deep dive into the critical practice of LLM evaluation. Using LlamaIndex and TruLens, we've seen how to systematically build, test, and iterate on RAG applications to enhance both their "honesty" and "harmlessness." This iterative, measurement-driven approach is key to developing responsible and reliable AI systems. A fantastic end to an incredible learning journey! - Vatsal Parikh*
