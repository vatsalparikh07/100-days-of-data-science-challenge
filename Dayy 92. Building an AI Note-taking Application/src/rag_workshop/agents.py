import json
from typing import Any

from langchain_mongodb.retrievers.parent_document import (
    MongoDBAtlasParentDocumentRetriever,
)
from loguru import logger
from smolagents import LiteLLMModel, Tool, ToolCallingAgent

from rag_workshop.config import settings
from rag_workshop.retrievers import get_retriever


def build_agent() -> Any:
    """Builds and configures a tool-calling agent with MongoDB retriever capability.

    Returns:
        Any: A configured ToolCallingAgent instance with MongoDB retriever tool.
    """
    retriever_tool = MongoDBRetrieverTool()

    model = LiteLLMModel(
        model_id=settings.OPENAI_MODEL_ID,
        api_base="https://api.openai.com/v1",
        api_key=settings.OPENAI_API_KEY,
    )

    agent = ToolCallingAgent(
        tools=[retriever_tool],
        model=model,
        max_steps=3,
        verbosity_level=2,
    )

    return agent


class MongoDBRetrieverTool(Tool):
    """A tool for performing semantic search queries against a MongoDB vector database.

    This tool integrates with MongoDB Atlas to perform vector similarity search
    for document retrieval. It formats the results in XML-style markup for
    structured access to document metadata and content.

    Attributes:
        name (str): The identifier for this tool
        description (str): Detailed description of the tool's capabilities
        inputs (dict): Schema definition for the expected input parameters
        output_type (str): The type of data returned by this tool
    """

    name = "mongodb_vector_search_retriever"
    description = """Use this tool to search and retrieve relevant documents from a knowledge base using semantic search.
    This tool performs similarity-based search to find the most relevant documents matching the query.
    Best used when you need to:
    - Find specific information from stored documents
    - Get context about a topic
    - Research historical data or documentation
    The tool will return multiple relevant document snippets."""

    inputs = {
        "query": {
            "type": "string",
            "description": """The search query to find relevant documents for using semantic search.
            Should be a clear, specific question or statement about the information you're looking for.""",
        }
    }
    output_type = "string"

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.retriever = self.__load_retriever()

    def __load_retriever(self) -> MongoDBAtlasParentDocumentRetriever:
        return get_retriever(
            embedding_model_id=settings.RAG_TEXT_EMBEDDING_MODEL_ID,
            k=settings.RAG_TOP_K,
            device=settings.RAG_DEVICE,
        )

    def forward(self, query: str) -> str:
        """Executes the semantic search query against MongoDB.

        Args:
            query (str): A JSON string containing the search query parameter.
                Expected format: {"query": "search text"}

        Returns:
            str: XML-formatted string containing search results with document
                metadata and content. Each result includes document title, URL,
                and relevant content snippets.

        Raises:
            Exception: If document retrieval fails, logs debug info and returns
                error message.
        """
        try:
            query = self.__parse_query(query)
            relevant_docs = self.retriever.invoke(query)

            formatted_docs = []
            for i, doc in enumerate(relevant_docs, 1):
                formatted_docs.append(
                    f"""
<document id="{i}">
<title>{doc.metadata.get("title")}</title>
<url>{doc.metadata.get("url")}</url>
<content>{doc.page_content.strip()}</content>
</document>
"""
                )

            result = "\n".join(formatted_docs)
            result = f"""
<search_results>
{result}
</search_results>
When using context from any document, also include the document URL as reference, which is found in the <url> tag.
"""
            return result
        except Exception:
            logger.opt(exception=True).debug("Error retrieving documents.")

            return "Error retrieving documents."

    def __parse_query(self, query: str) -> str:
        """Extracts the query string from JSON input.

        Args:
            query (str): JSON string containing the query parameter.

        Returns:
            str: The extracted query string.

        Raises:
            json.JSONDecodeError: If the input string is not valid JSON.
        """
        query_dict = json.loads(query)

        return query_dict["query"]
