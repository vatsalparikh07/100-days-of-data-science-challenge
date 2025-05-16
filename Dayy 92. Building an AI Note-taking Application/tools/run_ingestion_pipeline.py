import asyncio
from pathlib import Path

import click

from rag_workshop.config import settings
from rag_workshop.ingestion import ingest_documents


@click.command()
@click.option(
    "--documents-dir",
    type=click.Path(exists=True, path_type=Path),
    default=Path("../../workshops_data/rag"),
    help="Directory containing JSON documents to process",
)
def main(
    documents_dir: Path,
) -> None:
    """Run the document ingestion pipeline to process and store documents in MongoDB.

    This CLI tool processes documents from the specified directory, generates embeddings
    using the configured model, and stores both the documents and their embeddings in
    MongoDB for later retrieval.

    Args:
        documents_dir: Path to directory containing JSON documents to process.
            Each JSON file should contain document data in the expected format.

    Returns:
        None
    """

    asyncio.run(
        ingest_documents(
            documents_dir=documents_dir,
            embedding_model_id=settings.RAG_TEXT_EMBEDDING_MODEL_ID,
            embedding_model_dim=settings.RAG_TEXT_EMBEDDING_MODEL_DIM,
            device=settings.RAG_DEVICE,
        )
    )


if __name__ == "__main__":
    main()
