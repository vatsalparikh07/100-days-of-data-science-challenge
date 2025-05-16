from loguru import logger
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    A Pydantic-based settings class for managing application configurations.
    """

    # --- Pydantic Settings ---
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

    # --- MongoDB Atlas Configuration ---
    MONGODB_DATABASE_NAME: str = Field(
        default="decodingml_workshops",
        description="Name of the MongoDB database.",
    )
    MONGODB_URI: str = Field(
        default="mongodb://decodingml:decodingml@localhost:27017/?directConnection=true",
        description="Connection URI for the local MongoDB Atlas instance.",
    )
    MONGODB_RAG_COLLECTION_NAME: str = Field(
        default="rag",
        description="Name of the MongoDB collection for the RAG.",
    )

    # --- OpenAI API Configuration ---
    OPENAI_API_KEY: str = Field(
        description="API key for OpenAI service authentication.",
    )
    OPENAI_MODEL_ID: str = Field(
        default="gpt-4o-mini",
        description="Model ID for OpenAI service.",
    )

    # --- RAG Configuration ---
    RAG_TEXT_EMBEDDING_MODEL_ID: str = (
        "sentence-transformers/all-MiniLM-L6-v2"  # Alibaba-NLP/gte-large-en-v1.5
    )
    RAG_TEXT_EMBEDDING_MODEL_DIM: int = 384  # 1024
    RAG_TOP_K: int = 3
    RAG_DEVICE: str = "cpu"

    @field_validator("OPENAI_API_KEY")
    @classmethod
    def check_not_empty(cls, value: str, info) -> str:
        if not value or value.strip() == "":
            logger.error(f"{info.field_name} cannot be empty.")
            raise ValueError(f"{info.field_name} cannot be empty.")
        return value


try:
    settings = Settings()
except Exception as e:
    logger.error(f"Failed to load configuration: {e}")
    raise SystemExit(e)
