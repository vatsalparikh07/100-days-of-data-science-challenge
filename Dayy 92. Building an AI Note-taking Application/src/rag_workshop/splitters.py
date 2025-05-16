from langchain_text_splitters import RecursiveCharacterTextSplitter
from loguru import logger


def get_splitter(
    chunk_size: int,
) -> RecursiveCharacterTextSplitter:
    """Returns a token-based text splitter with overlap.

    Args:
        chunk_size: Number of tokens for each text chunk.

    Returns:
        RecursiveCharacterTextSplitter: A configured text splitter instance that splits text
            into chunks with 15% overlap between consecutive chunks.
    """

    chunk_overlap = int(0.15 * chunk_size)

    logger.info(
        f"Getting splitter with chunk size: {chunk_size} and overlap: {chunk_overlap}"
    )

    return RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
