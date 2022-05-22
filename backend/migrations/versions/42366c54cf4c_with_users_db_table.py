"""With users db Table

Revision ID: 42366c54cf4c
Revises: f3daf0081f18
Create Date: 2022-01-04 19:20:50.365581

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '42366c54cf4c'
down_revision = 'f3daf0081f18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'subjects', 'users', ['users_id'], ['id'])
    op.drop_column('subjects', 'user')
    op.drop_column('subjects', 'users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subjects', sa.Column('users', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('subjects', sa.Column('user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    # ### end Alembic commands ###