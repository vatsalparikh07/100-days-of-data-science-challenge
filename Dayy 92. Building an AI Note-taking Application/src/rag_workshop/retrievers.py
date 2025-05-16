from langchain_mongodb.retrievers import (
    MongoDBAtlasParentDocumentRetriever,
)
from loguru import logger

from rag_workshop.config import settings
from rag_workshop.embeddings import get_embedding_model
from rag_workshop.splitters import get_splitter


def get_retriever(
    embedding_model_id: str,
    k: int = 3,
    device: str = "cpu",
) -> MongoDBAtlasParentDocumentRetriever:
    """Creates and returns a MongoDB Atlas retriever configured with the specified embedding model.

    Args:
        embedding_model_id (str): Identifier for the embedding model to use.
        k (int, optional): Number of top results to return. Defaults to 3.
        device (str, optional): Device to run the embedding model on ('cpu' or 'cuda'). Defaults to "cpu".

    Returns:
        MongoDBAtlasParentDocumentRetriever: Configured retriever instance that can search
            documents in MongoDB Atlas using the specified embedding model.
    """

    logger.info(
        f"Getting retriever using '{embedding_model_id}' on '{device}' with {k} top results"
    )

    embedding_model = get_embedding_model(embedding_model_id, device)

    retriever = MongoDBAtlasParentDocumentRetriever.from_connection_string(
        connection_string=settings.MONGODB_URI,
        embedding_model=embedding_model,
        child_splitter=get_splitter(200),
        parent_splitter=get_splitter(800),
        database_name=settings.MONGODB_DATABASE_NAME,
        collection_name=settings.MONGODB_RAG_COLLECTION_NAME,
        text_key="page_content",
        search_kwargs={"k": k},
    )

    return retriever
