"""merge

Revision ID: 8c82f1806808
Revises: 52d5f5a412b5, f081807b94f9
Create Date: 2024-11-09 21:26:10.386086

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c82f1806808'
down_revision: Union[str, None] = ('52d5f5a412b5', 'f081807b94f9')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
