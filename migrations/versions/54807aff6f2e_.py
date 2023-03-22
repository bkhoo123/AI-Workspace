"""create_users_table
Revision ID: ffdc0a98111c
Revises:
Create Date: 2020-11-20 15:06:02.230689
"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = 'ffdc0a98111c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('BlockTypes',
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('type_id')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE BlockTypes SET SCHEMA {SCHEMA};")

    op.create_table('Templates',
    sa.Column('template_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('content', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('template_id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE Templates SET SCHEMA {SCHEMA};")

    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE Users SET SCHEMA {SCHEMA};")

    op.create_table('Workspaces',
    sa.Column('workspace_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['Users.user_id'], ),
    sa.PrimaryKeyConstraint('workspace_id')
    )

    if environment == "production":
            op.execute(f"ALTER TABLE Workspaces SET SCHEMA {SCHEMA};")

    op.create_table('Pages',
    sa.Column('page_id', sa.Integer(), nullable=False),
    sa.Column('workspace_id', sa.Integer(), nullable=False),
    sa.Column('template_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['template_id'], ['Templates.template_id'], ),
    sa.ForeignKeyConstraint(['workspace_id'], ['Workspaces.workspace_id'], ),
    sa.PrimaryKeyConstraint('page_id')
    )

    if environment == "Pages":
        op.execute(f"ALTER TABLE Templates SET SCHEMA {SCHEMA};")

    op.create_table('Blocks',
    sa.Column('block_id', sa.Integer(), nullable=False),
    sa.Column('page_id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('text_block', sa.JSON(), nullable=True),
    sa.Column('code_block', sa.JSON(), nullable=True),
    sa.Column('database_block', sa.JSON(), nullable=True),
    sa.Column('boardview_block', sa.JSON(), nullable=True),
    sa.Column('heading_block', sa.JSON(), nullable=True),
    sa.Column('table_block', sa.JSON(), nullable=True),
    sa.Column('bulleted_list_block', sa.JSON(), nullable=True),
    sa.Column('block_order', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['page_id'], ['Pages.page_id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['BlockTypes.type_id'], ),
    sa.PrimaryKeyConstraint('block_id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE Blocks SET SCHEMA {SCHEMA};")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Blocks')
    op.drop_table('Pages')
    op.drop_table('Workspaces')
    op.drop_table('Users')
    op.drop_table('Templates')
    op.drop_table('BlockTypes')
    # ### end Alembic commands ###
