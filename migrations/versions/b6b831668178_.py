"""empty message

Revision ID: b6b831668178
Revises: 381a73286a13
Create Date: 2022-01-24 07:06:26.546925

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b6b831668178'
down_revision = '381a73286a13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('create_datetime', sa.DateTime(), nullable=True),
    sa.Column('is_del', sa.Boolean(), server_default=sa.text('0'), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('username')
    )
    op.drop_index('username', table_name='user')
    op.drop_table('user')
    op.add_column('calendar', sa.Column('is_closed', sa.Boolean(), server_default=sa.text('0'), nullable=True))
    op.drop_column('calendar', 'is_del')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calendar', sa.Column('is_del', mysql.TINYINT(display_width=1), server_default=sa.text("'0'"), autoincrement=False, nullable=True))
    op.drop_column('calendar', 'is_closed')
    op.create_table('user',
    sa.Column('uid', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('is_del', mysql.TINYINT(display_width=1), server_default=sa.text("'0'"), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'user', ['username'], unique=False)
    op.drop_table('users')
    # ### end Alembic commands ###
