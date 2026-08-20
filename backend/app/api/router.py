from fastapi import APIRouter

from app.modules.auth.router import router as auth_router

api_router = APIRouter()

api_router.include_router(auth_router)


@api_router.get("/info", tags=["System"])
async def get_system_info():
    """Returns basic service metadata and API status."""
    return {
        "service": "SafePath API Gateway",
        "status": "operational",
        "version": "0.1.0",
    }