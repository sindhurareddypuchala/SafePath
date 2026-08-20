"""initial_user_tables

Revision ID: 001_initial_user_tables
Revises: 
Create Date: 2026-08-20 00:00:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '001_initial_user_tables'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Enable PostGIS extension if available
    try:
        op.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
    except Exception:
        pass

    # Create users table
    op.create_table(
        'users',
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('account_status', sa.String(length=20), nullable=False, server_default='ACTIVE'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.CheckConstraint("account_status IN ('ACTIVE', 'SUSPENDED', 'DELETED')", name='check_user_account_status'),
        sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)

    # Create user_profiles table
    op.create_table(
        'user_profiles',
        sa.Column('profile_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('display_name', sa.String(length=100), nullable=False),
        sa.Column('phone_encrypted', sa.Text(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('profile_id'),
        sa.UniqueConstraint('user_id')
    )

    # Create user_preferences table
    op.create_table(
        'user_preferences',
        sa.Column('preference_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('route_preference', sa.String(length=20), nullable=False, server_default='BALANCED'),
        sa.Column('checkin_frequency_minutes', sa.Integer(), nullable=False, server_default='15'),
        sa.Column('escalation_contact_delay_seconds', sa.Integer(), nullable=False, server_default='120'),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.CheckConstraint("route_preference IN ('MAX_SAFETY', 'BALANCED', 'SAFETY_SPEED')", name='check_route_preference_enum'),
        sa.CheckConstraint('checkin_frequency_minutes BETWEEN 5 AND 60', name='check_checkin_frequency_range'),
        sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('preference_id'),
        sa.UniqueConstraint('user_id')
    )

    # Create trusted_contacts table
    op.create_table(
        'trusted_contacts',
        sa.Column('contact_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('contact_name', sa.String(length=100), nullable=False),
        sa.Column('phone_encrypted', sa.Text(), nullable=False),
        sa.Column('email_encrypted', sa.Text(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('contact_id')
    )
    op.create_index(op.f('ix_trusted_contacts_user_id'), 'trusted_contacts', ['user_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_trusted_contacts_user_id'), table_name='trusted_contacts')
    op.drop_table('trusted_contacts')
    op.drop_table('user_preferences')
    op.drop_table('user_profiles')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
