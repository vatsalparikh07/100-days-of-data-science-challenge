# Day 59. 100 Days of Data Science Challenge - 03/31/2025

## Agentic AI System for Supply Chain Management for International Shipping

*Please have a look at this solution notebook for in-depth working of the code - [Link](https://www.datacamp.com/datalab/w/66fd4f17-7b5e-4599-94af-837623611bdb/edit)*

*Leveraging RAG Architecture with MongoDB Atlas and LLMs for Intelligent Contract Management*

![image](https://github.com/user-attachments/assets/7965158b-5825-4abd-aa12-135972ef5b79)

## 🚀 Technologies & Tools  

This project leverages a **cutting-edge AI-powered stack** for intelligent **supply chain & contract management**.  

### 🛠 Core Technologies  
- **🐍 Python** – The backbone for data ingestion & AI workflows.  
- **📊 Pandas** – Efficient data manipulation & contract processing.  
- **📦 Hugging Face Datasets** – Centralized shipping contract data management.  
- **🧠 VoyageAI API** – 1024D semantic embeddings with `voyage-finance-2`.  
- **💾 MongoDB Atlas** – Acts as a **vector store** & operational DB.  
- **🔗 PyMongo** – Secure database interactions.  

### 🤖 AI & NLP Components  
- **📝 Anthropic Claude** – LLM for **human-like contract insights**.  
- **🔍 LangChain + LangGraph + Motor** – AI agent workflows, async ops, tracing.  
- **📡 Tavily API** – Fetches **real-time shipping news**.  
- **💬 Cohere API** – Advanced NLP & text generation.  

### ⚡ Utilities & Visualization  
- **⏳ tqdm** – Tracks long-running processes like embedding generation.  
- **📊 Mermaid** – Creates **diagrams** for system architecture & data flow.  

# Part 1: Semantic Search and RAG Implementation

## Overview and Motivation

International shipping contracts are notoriously complex. They contain detailed clauses about tariffs, insurance, delivery timelines, and penalties. Combine this with the dynamic nature of supply chain operations—such as inventory updates, route optimization, and cross-departmental collaboration—and the challenge is clear: non-technical staff need a simple way to access accurate, critical information.

Our solution leverages a Retrieval-Augmented Generation (RAG) architecture augmented by:
- **MongoDB Atlas** for both operational storage and vector indexing.  
- **VoyageAI**’s financial language model for generating high-dimensional (1024D) semantic embeddings.  
- **Large Language Models (LLMs)** to convert retrieved data into clear, human-friendly answers.

The goal is to enable fast, natural language querying of contract and shipping data, reducing operational errors while saving time and lowering costs.

![image](https://github.com/user-attachments/assets/0a773cca-9327-444f-999e-f98ac1d27439)


---

## Data Ingestion and Preparation

### Data Loading

- **Source:** The shipping contracts dataset is loaded from a centralized repository (e.g., hosted on Hugging Face).  
- **Schema Overview:** Each record contains key data fields such as:
  - *Contract Number, Effective Date, Shipper, Receiver*
  - *Goods Description, Shipping Method, Origin, Destination*
  - *Liability, Customs & Compliance, Inventory Status, etc.*

A representative table of the schema:

| Field                   | Description                                  |
|-------------------------|----------------------------------------------|
| Contract Number         | Unique identifier for each contract/shipment |
| Effective Date          | Date the contract becomes active              |
| Shipper/Receiver        | Entities responsible for dispatch and receipt  |
| Goods Description       | Itemized details of the cargo                 |
| Shipping Method         | Mode of transportation (e.g., Ocean, Rail)     |
| Origin & Destination    | Port locations or origins and endpoints        |
| Compliance Information  | Terms for customs, insurance, and penalties     |

This structured approach allows subsequent processing steps to focus on the most relevant contractual metadata.

### Embedding Generation

To capture the semantic meaning of each contract, we combine several fields (e.g., *Shipper, Receiver, Goods Description,* etc.) into a unified text representation. This text is then transformed into a vector embedding using VoyageAI’s "voyage-finance-2" model, which outputs a 1024-dimensional vector.

**Key Benefits of Embedding Generation:**
- **Semantic Context:** Captures the inherent relationships between various contract fields.
- **Efficient Retrieval:** Translates high-dimensional text into vectors that can be quickly compared using cosine similarity.
- **Scalability:** Supports high-volume data by simplifying the search process.


---

## MongoDB Atlas: Operational and Vector Database

### Database Setup

MongoDB Atlas is not only used to store the raw shipping contract data but also the associated vector embeddings. The connection details (such as MONGO_URI) are securely managed via environment variables to ensure that the sensitive configuration remains protected.

### Configuring a Vector Index

A dedicated vector search index is created in MongoDB Atlas to speed up similarity-based queries. The key parameters of the vector index include:

| Parameter                                | Value                        |
|------------------------------------------|------------------------------|
| **Embedding Field**                      | `embedding`                  |
| **Model Dimension**                      | 1024                         |
| **Similarity Metric**                    | Cosine similarity            |
| **Candidate Pool Size** (`numCandidates`)| 150                          |
| **Top Results Returned** (`limit`)       | 5                            |

This index setup enables the system to perform fast and accurate retrievals by comparing the query vector with document embeddings.

---

## Semantic Search Workflow

1. **Query Handling:**
   - A user submits a natural language query (e.g., “What are the customs requirements for toys shipped to Canada?”).
   - The query is converted to a 1024-dimensional vector using the same embedding generation process.

2. **Vector Search Execution:**
   - The query vector is input into a MongoDB aggregation pipeline that uses a specialized `$vectorSearch` stage.
   - The pipeline retrieves the documents that most closely match the query vector and then projects only the necessary metadata (such as contract number, shipper, receiver, relevant compliance info, etc.).

3. **Hybrid Retrieval:**
   - While the vector search provides a semantic basis for similarity, the system can optionally integrate full-text search results to capture exact keyword matches, ensuring a robust, hybrid approach to information retrieval.

---

## Integration with LLM for Retrieval-Augmented Generation

Once the relevant documents are retrieved using the semantic search pipeline, the data is passed to a Large Language Model (such as Anthropic’s Claude) that synthesizes this information into an easily digestible answer. This step bridges the gap between raw, technical data and actionable business insights for users who may not have a technical background.

# Part 2: Making Things Agentic

![image](https://github.com/user-attachments/assets/aa477706-09ee-4658-87b3-405dcdcb500b)

## Overview

In Part 1, we explored how semantic search and Retrieval-Augmented Generation (RAG) enable efficient querying of complex supply chain data. Now, we take the system a step further by making it *agentic*. This means empowering the system with intelligent tools that can not only retrieve information but also take actions, such as updating shipment statuses or fetching real-time news. These agents work collaboratively to provide actionable insights and streamline operations.

Imagine an operations manager asking, "Update Shipment SHP-2024-001 to 'Delayed' and notify all stakeholders!" With our agentic system, this isn't just a manual lookup followed by updates—it’s a single natural language command that triggers the appropriate tools to act autonomously.

---

## Multi-Agent Framework

Our agentic system is composed of several specialized tools designed to handle specific tasks. Each tool operates autonomously but integrates seamlessly into the broader workflow. Below are the key tools and their functions:

### **Agentic Tools**

| Tool Name                          | Functionality                          | Example Use Case                           |
|------------------------------------|----------------------------------------|-------------------------------------------|
| **Hybrid Search Tool**             | Multimodal document retrieval          | *"What are the customs requirements for toys shipped to Canada?"* |
| **Transit Status Update Tool**     | Updates shipment status in real time   | *"Update Shipment SHP-2024-001 to 'Delayed'."* |
| **Inventory Status Query Tool**    | Retrieves inventory status             | *"What shipments are 'Awaiting Customs Clearance'?"* |
| **Real-Time News Retrieval Tool**  | Fetches live news related to shipments | *"Get news updates about Shipment SHP-2024-001."* |

---

## Creating the Tools

### 1. **Hybrid Search Tool**
The Hybrid Search Tool combines vector-based semantic search and full-text search to deliver highly relevant results. It uses MongoDB Atlas for both vector indexing and text indexing.

**Implementation Highlights:**
- Vector embeddings are generated using VoyageAI's financial model.
- A vector index is created for similarity-based searches.
- A text index is added for keyword-based precision.

**Example Query:**
```
query = "What are the customs requirements for toys shipped to Canada?"
hybrid_search_result = hybrid_search.get_relevant_documents(query)
```

**Output:**
```
Contract Number: SHP-2024-0196
Origin: Port of Santos, Brazil
Destination: Port of Vancouver, Canada
Customs and Compliance: Receiver responsible for destination customs
```


---

### 2. **Transit Status Update Tool**
This tool allows users to update the transit status of shipments directly in MongoDB.

**Implementation Highlights:**
- Uses MongoDB's `$update` operation to modify the `Current Transit Status` field.
- Ensures real-time visibility of shipment progress across stakeholders.

**Example Command:**

```
update_transit_status("SHP-2024-001,Delayed")
```

**Output:**
```
Successfully updated status of shipment SHP-2024-001 to 'Delayed'.
```


---

### 3. **Inventory Status Query Tool**
This tool retrieves contracts based on their inventory status (e.g., "Delivered", "Awaiting Customs Clearance").

**Implementation Highlights:**
- Filters contracts using MongoDB's `$find` operation.
- Projects relevant fields like `Contract Number`, `Goods Description`, `Origin`, and `Destination`.

**Example Command:**
```get_contracts_by_inventory_status("Awaiting Customs Clearance", limit=5)```

**Output:**
```
[
{
"Contract Number": "SHP-2024-0002",
"Goods Description": "Clothing",
"Origin": "Port of New York, USA",
"Destination": "Port of Santos, Brazil",
"Inventory Status": "Awaiting Customs Clearance"
},
...
]
```


---

### 4. **Real-Time News Retrieval Tool**
Global supply chains are often impacted by external events like port strikes or geopolitical disruptions. This tool fetches real-time news related to specific shipments using Tavily API.

**Implementation Highlights:**
- Integrates Tavily API for live news updates.
- Combines local and foreign sources to provide comprehensive coverage.

**Example Command:**
```get_real_time_news_on_shipment_by_contract("SHP-2024-001", max_local=5, max_foreign=2)```

**Output:**
```
[
{
"Headline": "Port Strike in Vancouver Causes Delays",
"Source": "Local News",
"Date": "2025-04-01"
},
...
]
```


---

## Agent Workflow

The agents work collaboratively to handle complex queries and actions. Below is an example workflow:

1. **User Query:**  
   *"Update Shipment SHP-2024-001 to 'Delayed' and fetch relevant news."*

2. **Action Execution:**  
   - The Transit Status Update Tool modifies the shipment's status in MongoDB.
   - The Real-Time News Retrieval Tool fetches live updates about the shipment.

3. **Response Generation:**  
   The system synthesizes the results into a human-friendly summary.

---

## Visualizing Agent Collaboration

Below is a simplified diagram illustrating how agents interact within the system:

![image](https://github.com/user-attachments/assets/231500f8-10d0-4c6c-a1ba-a7231e1405c3)

---

## Chatting with our AI Agent Live Working Example 

Below is a working example of a live interactive session with our AI-powered Assistant - 

> **User:** Hi there  
> **Assistant:** ----Calling Agent Node-------  
> Hello! Welcome to our AI-powered Logistics Assistant. I'm here to help you with any questions or tasks related to international shipping operations, contract details, shipment information, inventory data, and supply chain updates. How may I assist you today?  
>  
> **User:** What can you do?  
> **Assistant:** ----Calling Agent Node-------  
> Certainly! I’m designed to:
> 1. **Retrieve Information:** Provide details on contracts, shipments, and inventory by performing hybrid searches.
> 2. **Manage Shipment Status:** Update transit statuses (e.g., mark shipments as Delayed or On Schedule) in real time.
> 3. **Analyze Contracts & Inventory:** Offer insights by reviewing contract terms and current inventory statuses.
> 4. **Optimize the Supply Chain:** Inform you about shipping routes, delays, and customs requirements.
> 5. **Fetch Real-Time News:** Retrieve current news on logistics-related disruptions that might affect your operations.
>  
> For example, you can ask:
> 
> - "What are the customs requirements for electronics shipped to Canada?"
> - "Update the status of Shipment SHP-2024-001 to 'Delayed'."
> - "Fetch news about shipment SHP-2024-0007."
>  
> **User:** Can you get me some news on SHP-2024-0007?  
> **Assistant:** ----Calling Agent Node-------  
> [Tool Call: **get_real_time_news_on_shipment_by_contract** executed]  
> *Using real-time data from integrated news APIs…*  
> **Assistant:** Based on the latest data, here’s a summary of recent news relevant to shipment SHP-2024-0007:  
> - **Headline:** *Red Sea Crisis Impacts Port of Piraeus*  
> - **Details:** Disruptions at the Port of Piraeus have led to changes in shipping volumes and transit delays.
> - *(Additional news items are also available that consider local congestion and logistics factors.)*  
>  
> **User:** Update SHP-2024-0007 to not delayed  
> **Assistant:** ----Calling Agent Node-------  
> [Tool Call: **update_transit_status** executed with input “SHP-2024-0007,On Schedule”]  
> **Assistant:** Great news! The status of shipment **SHP-2024-0007** has been successfully updated from "Delayed" to "On Schedule".  
>  
> **Assistant (summary):**  
> - **Contract Number:** SHP-2024-0007  
> - **Previous Status:** Delayed  
> - **New Status:** On Schedule  
>  
> This update ensures that the shipment of Furniture from Gonzales-Cox to Smith, Garcia and Gilbert (traveling from Port of Melbourne, Australia to Port of Piraeus, Greece) now reflects its current progress accurately.


