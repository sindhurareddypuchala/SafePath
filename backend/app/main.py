from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.router import api_router
from app.database.session import check_database_health


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="SafePath Preventive Safety Intelligence & Journey Companion Platform API",
)


# CORS Configuration for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include the main API router.
# Authentication routes are already included inside app.api.router.
app.include_router(
    api_router,
    prefix=settings.API_V1_STR,
)


@app.get("/health/liveness", tags=["Health"])
async def liveness_check():
    """Basic health check endpoint returning server status."""
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT,
    }


@app.get("/health/readiness", tags=["Health"])
async def readiness_check():
    """
    Readiness probe verifying database connectivity and PostGIS status
    without exposing sensitive credentials.
    """
    db_health = await check_database_health()

    overall_status = (
        "ready"
        if db_health.get("status") == "connected"
        else "degraded"
    )

    return {
        "status": overall_status,
        "database": db_health,
        "redis": "configured_placeholder",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )