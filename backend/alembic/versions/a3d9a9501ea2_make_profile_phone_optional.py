"""make profile phone optional

Revision ID: a3d9a9501ea2
Revises: 001_initial_user_tables
Create Date: 2026-08-20 17:34:56.868419
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a3d9a9501ea2"
down_revision: Union[str, Sequence[str], None] = "001_initial_user_tables"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "user_profiles",
        "phone_encrypted",
        existing_type=sa.Text(),
        nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        "user_profiles",
        "phone_encrypted",
        existing_type=sa.Text(),
        nullable=False,
    )