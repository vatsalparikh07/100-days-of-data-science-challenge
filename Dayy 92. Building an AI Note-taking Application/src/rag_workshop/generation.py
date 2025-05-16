from typing import Any, List

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

from rag_workshop.config import settings
from rag_workshop.retrievers import get_retriever


def create_rag_chain() -> Any:
    """Creates and configures a RAG (Retrieval Augmented Generation) chain.

    The chain combines a retriever, prompt template, and language model to perform
    question answering over retrieved documents. It follows these steps:
    1. Retrieves relevant documents using the configured retriever
    2. Combines documents into context
    3. Processes the question with a prompt template
    4. Generates an answer using ChatGPT

    Returns:
        Any: A configured chain that takes a question string as input and returns
            an answer string based on retrieved context. Returns "I DON'T KNOW" if
            no relevant context is found.
    """

    retriever = get_retriever(
        embedding_model_id=settings.RAG_TEXT_EMBEDDING_MODEL_ID,
        k=settings.RAG_TOP_K,
        device=settings.RAG_DEVICE,
    )

    # Retrieve and parse documents
    retrieve = {
        "context": retriever
        | (lambda docs: "\n\n".join([d.page_content for d in docs])),
        "question": RunnablePassthrough(),
    }

    template = """Answer the question based only on the following context. If no context is provided, respond with I DON'T KNOW: \
{context}

Question: {question}
"""
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(temperature=0, model="gpt-4o")
    parse_output = StrOutputParser()

    return retrieve | prompt | llm | parse_output


def get_documents_for_query(query: str) -> List[str]:
    """Retrieves relevant documents for a given search query.

    Args:
        query: The search query to find matching documents.
            Should be a natural language question or keywords.

    Returns:
        List[str]: A list of document contents (as strings) that match the query,
            ordered by relevance. The number of results is limited by the
            RAG_TOP_K setting.
    """

    retriever = get_retriever(
        embedding_model_id=settings.RAG_TEXT_EMBEDDING_MODEL_ID,
        k=settings.RAG_TOP_K,
        device=settings.RAG_DEVICE,
    )
    documents = retriever.invoke(query)

    return [doc.page_content for doc in documents]
