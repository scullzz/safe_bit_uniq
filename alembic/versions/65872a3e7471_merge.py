"""merge

Revision ID: 65872a3e7471
Revises: 6b517b700478, 99e403f1531f
Create Date: 2024-11-09 20:29:47.826352

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65872a3e7471'
down_revision: Union[str, None] = ('6b517b700478', '99e403f1531f')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
