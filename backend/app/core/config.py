import os
from pathlib import Path

from dotenv import load_dotenv


# Load backend/.env file if present
_env_path = Path(__file__).resolve().parent.parent.parent / ".env"

if _env_path.exists():
    load_dotenv(dotenv_path=_env_path)


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "SafePath")
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")

    # JWT Authentication Settings
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15")
    )

    # PostgreSQL / PostGIS Settings
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "safepath_db")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "safepath_user")
    POSTGRES_PASSWORD: str = os.getenv(
        "POSTGRES_PASSWORD",
        "safepath_password_dev",
    )

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        """Async SQLAlchemy connection URL for FastAPI app execution."""
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )

    @property
    def SQLALCHEMY_SYNC_DATABASE_URI(self) -> str:
        """Sync SQLAlchemy connection URL for Alembic migration executions."""
        return (
            f"postgresql+psycopg2://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )

    # Redis Settings
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))


settings = Settings()