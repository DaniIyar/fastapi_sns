"""add content column to posts table

Revision ID: 07604f6555da
Revises: 93cc699e82c4
Create Date: 2025-01-27 14:22:28.840485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07604f6555da'
down_revision: Union[str, None] = '93cc699e82c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
