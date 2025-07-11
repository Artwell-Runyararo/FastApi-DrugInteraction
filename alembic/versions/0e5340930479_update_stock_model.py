"""Update Stock Model

Revision ID: 0e5340930479
Revises: e4eb3388c09a
Create Date: 2025-04-28 23:12:47.293851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e5340930479'
down_revision = 'e4eb3388c09a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('medicines', sa.Column('pharmacy_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'medicines', 'pharmacies', ['pharmacy_id'], ['pharmacy_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'medicines', type_='foreignkey')
    op.drop_column('medicines', 'pharmacy_id')
    # ### end Alembic commands ###
