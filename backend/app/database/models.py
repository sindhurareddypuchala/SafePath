"""Central Database Models Registry

All active domain models are imported here to ensure Alembic and SQLAlchemy metadata
registration detect all entity tables.
"""
from app.database.base import Base
from app.modules.users.models import User, UserProfile, UserPreference, TrustedContact

__all__ = ["Base", "User", "UserProfile", "UserPreference", "TrustedContact"]
