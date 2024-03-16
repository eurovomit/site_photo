"""fix photo and  shooting

Revision ID: a8167e9195a9
Revises: 0ee5c29adb25
Create Date: 2024-03-14 23:19:42.914380

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8167e9195a9'
down_revision: Union[str, None] = '0ee5c29adb25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('photo', 'shooting_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('photo_shooting_id_fkey', 'photo', type_='foreignkey')
    op.create_foreign_key(None, 'photo', 'shooting', ['shooting_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'photo', type_='foreignkey')
    op.create_foreign_key('photo_shooting_id_fkey', 'photo', 'shooting', ['shooting_id'], ['id'])
    op.alter_column('photo', 'shooting_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
