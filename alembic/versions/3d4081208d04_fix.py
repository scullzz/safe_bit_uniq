"""fix

Revision ID: 3d4081208d04
Revises: 8a8e40cd39cf, 8c82f1806808
Create Date: 2024-11-10 01:58:10.625632

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d4081208d04'
down_revision: Union[str, None] = ('8a8e40cd39cf', '8c82f1806808')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
