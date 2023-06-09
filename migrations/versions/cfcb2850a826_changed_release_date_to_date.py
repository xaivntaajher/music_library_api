"""changed release date to date

Revision ID: cfcb2850a826
Revises: 94270038b5e5
Create Date: 2023-04-24 13:40:32.307411

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cfcb2850a826'
down_revision = '94270038b5e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.alter_column('release_date',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.Date(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.alter_column('release_date',
               existing_type=sa.Date(),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###
