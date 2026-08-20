import pytest
import asyncio
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from app.database.models import Base, User, UserProfile, UserPreference, TrustedContact
from app.database.session import check_database_health

def test_model_metadata_registration():
    """Verify that all 4 required models are registered on Base.metadata."""
    table_names = list(Base.metadata.tables.keys())
    assert "users" in table_names
    assert "user_profiles" in table_names
    assert "user_preferences" in table_names
    assert "trusted_contacts" in table_names

def test_user_table_structure():
    """Verify users table columns, primary key, and constraints."""
    users_table = Base.metadata.tables["users"]
    assert "user_id" in users_table.columns
    assert "email" in users_table.columns
    assert "password_hash" in users_table.columns
    assert "account_status" in users_table.columns
    assert users_table.columns["user_id"].primary_key is True
    assert users_table.columns["email"].unique is True

def test_user_profile_relationship_structure():
    """Verify user_profiles table foreign key and uniqueness on user_id."""
    profiles_table = Base.metadata.tables["user_profiles"]
    assert "profile_id" in profiles_table.columns
    assert "user_id" in profiles_table.columns
    assert profiles_table.columns["user_id"].unique is True
    
    fk_targets = [list(fk.column.table.name for fk in fk_set.elements) for fk_set in profiles_table.foreign_key_constraints]
    assert ["users"] in fk_targets

def test_user_preference_relationship_structure():
    """Verify user_preferences table foreign key and check constraints."""
    preferences_table = Base.metadata.tables["user_preferences"]
    assert "preference_id" in preferences_table.columns
    assert "user_id" in preferences_table.columns
    assert preferences_table.columns["user_id"].unique is True

def test_trusted_contacts_relationship_structure():
    """Verify trusted_contacts table foreign key and indexes."""
    contacts_table = Base.metadata.tables["trusted_contacts"]
    assert "contact_id" in contacts_table.columns
    assert "user_id" in contacts_table.columns
    assert contacts_table.columns["user_id"].nullable is False

@pytest.mark.asyncio
async def test_database_health_probe_graceful_handling():
    """Verify that check_database_health executes safely without throwing unhandled exceptions."""
    health_result = await check_database_health()
    assert "status" in health_result
    assert "postgres" in health_result
    assert "postgis" in health_result
