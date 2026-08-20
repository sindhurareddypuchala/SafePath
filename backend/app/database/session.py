from typing import AsyncGenerator, Dict, Any
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import text
from app.core.config import settings

# SQLAlchemy 2.0 Async Engine
async_engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=False,
    pool_pre_ping=True,
    future=True
)

# Async Session Factory
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency generator yielding an AsyncSession instance."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

async def check_database_health() -> Dict[str, Any]:
    """
    Safely probes PostgreSQL connectivity and PostGIS status.
    Returns status metadata without exposing credentials or sensitive details.
    """
    try:
        async with async_engine.connect() as conn:
            # Query basic connectivity
            await conn.execute(text("SELECT 1;"))
            
            # Query PostGIS status
            postgis_status = "unavailable"
            try:
                postgis_res = await conn.execute(text("SELECT PostGIS_Full_Version();"))
                postgis_version = postgis_res.scalar()
                if postgis_version:
                    postgis_status = "enabled"
            except Exception:
                postgis_status = "extension_missing"

            return {
                "status": "connected",
                "postgres": "available",
                "postgis": postgis_status
            }
    except Exception:
        return {
            "status": "disconnected",
            "postgres": "unavailable",
            "postgis": "unavailable",
            "message": "Database server unreachable on configured host/port"
        }
