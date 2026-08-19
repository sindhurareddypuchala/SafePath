import os

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "SafePath")
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")
    
    # PostgreSQL / PostGIS Settings Placeholder
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "safepath_db")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "safepath_user")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "safepath_password_dev")
    
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    # Redis Cache & Ephemeral Session Store Settings Placeholder
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))

settings = Settings()
