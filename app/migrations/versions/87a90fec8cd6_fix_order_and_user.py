"""fix order and user

Revision ID: 87a90fec8cd6
Revises: ea1cb7f85fa8
Create Date: 2024-03-14 23:36:57.475956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87a90fec8cd6'
down_revision: Union[str, None] = 'ea1cb7f85fa8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False))
    op.alter_column('order', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('order_user_id_fkey', 'order', type_='foreignkey')
    op.create_foreign_key(None, 'order', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('order', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('date', sa.DATE(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.create_foreign_key('order_user_id_fkey', 'order', 'user', ['user_id'], ['id'])
    op.alter_column('order', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('order', 'created_at')
    # ### end Alembic commands ###