# Day 53. 100 Days of Data Science Challenge - 03/25/2025

# DeepSeek-R1 RAG Chatbot: Local PDF Query Assistant

## Overview

This project demonstrates a local AI-powered assistant that processes PDF documents and responds to user queries using a Retrieval-Augmented Generation (RAG) pipeline. By leveraging the DeepSeek-R1 (1.5B) model, Ollama for local LLM execution, and LangChain for document processing and semantic search, this solution empowers users to securely query and extract insights from rich PDF content—without relying on external cloud services.

This solution is designed not only to showcase technical prowess using state-of-the-art components like vector embeddings and Gradio-based interactive interfaces but also to enhance data security and privacy by keeping sensitive documents local.

---

## Key Features

- **Local LLM Operation:**  
  Run the DeepSeek-R1 model locally via Ollama to generate responses without connecting to external servers.

- **Document Preprocessing & Embedding:**  
  Extracts text from PDFs using PyMuPDF, splits text into manageable chunks with an overlapping context, and generates semantic embeddings using OllamaEmbeddings for accurate retrieval.

- **Vector-Based Semantic Search:**  
  Organizes the generated embeddings using Chroma (a vector database) to allow context-aware searches that go beyond mere keyword matching.

- **Retrieval-Augmented Generation (RAG):**  
  Combines retrieval of salient document chunks with LLM-based text generation to answer user queries accurately based on real content.

- **Interactive Chat Interface:**  
  Employs Gradio to create a user-friendly web application that accepts PDF uploads and text queries, providing immediate AI-driven responses.

- **Local Data Security:**  
  Ensures all document processing and inference occur locally, protecting sensitive data from being exposed to external services.

---

## Technical Architecture
![image](https://github.com/user-attachments/assets/fc485c43-f8c4-4807-a30a-1d9d680aac25)

### Data Pipeline & Processing

1. **PDF Processing:**  
   - *Loader:* `PyMuPDFLoader` extracts raw text from uploaded PDF files.  
   - *Text Splitting:* `RecursiveCharacterTextSplitter` segments documents into chunks (500 characters with 100-character overlap) for optimal embedding.

2. **Embedding Generation & Storage:**  
   - *Embedding:* `OllamaEmbeddings` converts text chunks into high-dimensional vectors using the DeepSeek-R1 model.
   - *Vector Database:* ChromaDB organizes and persists embeddings in a local directory (`./chroma_db`), enabling efficient semantic retrieval.

3. **RAG Pipeline:**  
   - *Retrieval:* A custom retriever fetches the most contextually relevant document chunks based on the user's query.
   - *Combination:* The retrieved chunks are merged into a coherent text block using a helper function (`combine_docs`).
   - *Response Generation:* The `ollama_llm` function formats the query with context and generates a final, cleaned answer using DeepSeek-R1.

### Core Code Components

| Component                | Functionality                                                             |
|--------------------------|---------------------------------------------------------------------------|
| `process_pdf(pdf_bytes)` | Loads the PDF, splits text into chunks, generates embeddings, and stores them in a vector store. |
| `combine_docs(docs)`     | Merges retrieved document chunks into a continuous text passage.         |
| `ollama_llm(question, context)` | Formats the prompt and invokes DeepSeek-R1 via Ollama to respond to the query.   |
| `rag_chain(question, text_splitter, vectorstore, retriever)` | Integrates retrieval of context and language model inference for accurate responses.  |
| `ask_question(pdf_bytes, question)` | High-level function that ties together PDF processing and the RAG pipeline.     |
| Gradio Interface         | Provides a web-based user interface to upload PDFs and ask questions interactively. |

---

## Usage

- **Upload a PDF:**  
Use the provided file upload option in the Gradio UI to select and upload a PDF document.

![image](https://github.com/user-attachments/assets/544887d9-db53-4e99-8bba-4d038efdf99a)

- **Ask a Question:**  
Type your question into the text box (e.g., "What are the key findings in the quarterly report?") and submit.

- **Receive an AI-Generated Response:**  
Your question is processed through the RAG pipeline, combining semantic retrieval and language model reasoning to return a detailed answer.

![image](https://github.com/user-attachments/assets/820b91ea-5531-46ca-82ba-d9bb2fdd3f53)

---

## Insights & Impact

- **Enhanced Document Understanding:**  
The system provides context-aware responses that draw directly from the uploaded PDF content, making it ideal for academic, business, and legal document analysis.

- **Data Privacy and Security:**  
By processing documents locally, the solution ensures that sensitive data is never transmitted over the internet, mitigating privacy risks.

- **Scalability in Application:**  
The modular architecture allows for easy integration of additional features (e.g., predictive analytics, sentiment analysis) and support for various document formats.

- **Democratization of AI Tools:**  
This project demonstrates how advanced AI techniques can be deployed locally with open-source tools, making state-of-the-art technology accessible to a broader audience.

---

## Future Enhancements

- **Real-Time Data Integration:**  
Incorporate live data sources for up-to-date document analysis.

- **Enhanced User Interaction:**  
Develop a mobile-responsive interface and add voice query capabilities.

- **Extended File Support:**  
Expand support to other document formats such as DOCX and HTML.

- **Advanced Analytics:**  
Integrate additional modules for sentiment analysis, trend detection, and financial forecasting.

---

## Conclusion

This project illustrates the fusion of modern AI techniques, advanced document processing, and interactive user interfaces to create a secure, local solution for querying complex PDFs. It represents a significant step towards making AI-powered document analysis both accessible and privacy-conscious.
