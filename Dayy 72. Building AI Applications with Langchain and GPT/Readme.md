# Day 72. 100 Days of Data Science Challenge - 04/13/2025

## 🧠 LangChain Chatbot: Your Personal AI Assistant

## 🚀 Project Overview

Welcome to the **LangChain Chatbot**! This project harnesses the power of **LangChain** and **OpenAI's GPT-3.5** to create an AI chatbot that can answer questions about LangChain itself. It's like having a knowledgeable friend who's always ready to help you navigate through the intricacies of LangChain documentation.

### 🌟 Why This Project?

- **Educational**: Learn how to integrate AI models with custom data to create intelligent applications.
- **Practical**: Build a chatbot that can assist developers in understanding LangChain's capabilities.
- **Innovative**: Explore the potential of Retrieval-Augmented Generation (RAG) in real-world applications.

## 🛠️ Key Features

- **Document Loading**: Utilizes `ReadTheDocsLoader` to ingest LangChain documentation.
- **Text Splitting**: Employs `RecursiveCharacterTextSplitter` for efficient document chunking.
- **Embeddings**: Generates embeddings using OpenAI's `text-embedding-ada-002` model.
- **Vector Database**: Stores embeddings in **Chroma** for semantic search capabilities.
- **Querying**: Performs similarity searches to retrieve relevant context for user queries.
- **Chat Interface**: A simple yet effective chat application to interact with the LangChain docs.

![image](https://github.com/user-attachments/assets/4649810d-03a7-4d62-b3c3-a6095cdf2100)

![image](https://github.com/user-attachments/assets/0aa98013-6645-4755-86ce-81f34e37e354)

## 📚 Getting Started

### Prerequisites

- **OpenAI Developer Account**: For API access.
- **Python 3.8+**: With the following packages installed:
```
pip install openai==0.27.1 langchain==0.0.191 chromadb==0.3.26 tiktoken==0.4.0
```

1. **Load the Data**:
```
from langchain.document_loaders import ReadTheDocsLoader

loader = ReadTheDocsLoader("rtdocs/python.langchain.com/en/latest", features="html.parser")
raw_documents = loader.load()
```

2. **Split the Documents**:
```
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = splitter.split_documents(raw_documents)
```
3. **Embed and Store**:
```
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

embedding_function = OpenAIEmbeddings()
db = Chroma.from_documents(documents=documents, embedding=embedding_function, persist_directory="my-embeddings")
db.persist()
```

## 🔍 Querying the Chatbot

### Example Query

```
question = "show an example of adding memory to a chain"
context_docs = db.similarity_search(question)
```

### Creating the Prompt

```
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
template="""Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

<context> {context} </context>
Question: {question}
Helpful Answer, formatted in markdown:""",
input_variables=["context", "question"]
)
```

### Running the Chatbot
```
from langchain.chains.llm import LLMChain
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)
qa_chain = LLMChain(llm=llm, prompt=prompt)

result = qa_chain({
"question": question,
"context": "\n".join([doc.page_content for doc in context_docs])
})

print(result["text"])
```

## 📈 Performance Metrics

- **Total Tokens**: 1,530,817
- **Estimated Cost**: $0.61 (for embedding all documents)

## 🌐 Useful Links

- [LangChain Documentation](https://python.langchain.com/en/latest/index.html)
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [OpenAI Pricing](https://openai.com/pricing/)

## 🧩 Going Further

### Enhancements

- **Document Cleanup**: Remove unnecessary text from documents before embedding.
- **Streaming Responses**: Implement streaming for a more interactive chat experience.
- **Source Attribution**: Return source documents or links to the user for transparency.
- **Memory Support**: Add conversation memory to the chatbot for context-aware responses.

### Caveats

While LangChain is excellent for prototyping, consider the following for production:

- **Documentation**: Often lacks depth, requiring code inspection for full understanding.
- **Abstraction**: Many layers of abstraction can complicate customization.
- **Opinionated**: Customizing chains or agents might require re-implementing parts of LangChain.
