"""fix kindergarten and group

Revision ID: 7909ea6c4420
Revises: 4521362b0d93
Create Date: 2024-03-14 22:14:09.093709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7909ea6c4420'
down_revision: Union[str, None] = '4521362b0d93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('group', 'kindergarten_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('group_kindergarten_id_fkey', 'group', type_='foreignkey')
    op.create_foreign_key(None, 'group', 'kindergarten', ['kindergarten_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'group', type_='foreignkey')
    op.create_foreign_key('group_kindergarten_id_fkey', 'group', 'kindergarten', ['kindergarten_id'], ['id'])
    op.alter_column('group', 'kindergarten_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
