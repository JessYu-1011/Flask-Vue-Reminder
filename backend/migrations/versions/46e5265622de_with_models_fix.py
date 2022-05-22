"""With models fix

Revision ID: 46e5265622de
Revises: c4893cbc1efe
Create Date: 2021-12-14 20:44:39.339086

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '46e5265622de'
down_revision = 'c4893cbc1efe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('subjects', 'done',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('subjects', 'done',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    # ### end Alembic commands ###
