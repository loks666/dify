"""add workflow

Revision ID: b289e2408ee2
Revises: 16830a790f0f
Create Date: 2024-02-19 12:47:24.646954

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b289e2408ee2'
down_revision = '17b5ab037c40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workflow_app_logs',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tenant_id', postgresql.UUID(), nullable=False),
    sa.Column('app_id', postgresql.UUID(), nullable=False),
    sa.Column('workflow_id', postgresql.UUID(), nullable=False),
    sa.Column('workflow_run_id', postgresql.UUID(), nullable=False),
    sa.Column('created_from', sa.String(length=255), nullable=False),
    sa.Column('created_by_role', sa.String(length=255), nullable=False),
    sa.Column('created_by', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='workflow_app_log_pkey')
    )
    with op.batch_alter_table('workflow_app_logs', schema=None) as batch_op:
        batch_op.create_index('workflow_app_log_app_idx', ['tenant_id', 'app_id'], unique=False)

    op.create_table('workflow_node_executions',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tenant_id', postgresql.UUID(), nullable=False),
    sa.Column('app_id', postgresql.UUID(), nullable=False),
    sa.Column('workflow_id', postgresql.UUID(), nullable=False),
    sa.Column('triggered_from', sa.String(length=255), nullable=False),
    sa.Column('workflow_run_id', postgresql.UUID(), nullable=True),
    sa.Column('index', sa.Integer(), nullable=False),
    sa.Column('predecessor_node_id', sa.String(length=255), nullable=True),
    sa.Column('node_id', sa.String(length=255), nullable=False),
    sa.Column('node_type', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('inputs', sa.Text(), nullable=True),
    sa.Column('process_data', sa.Text(), nullable=True),
    sa.Column('outputs', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('error', sa.Text(), nullable=True),
    sa.Column('elapsed_time', sa.Float(), server_default=sa.text('0'), nullable=False),
    sa.Column('execution_metadata', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('created_by_role', sa.String(length=255), nullable=False),
    sa.Column('created_by', postgresql.UUID(), nullable=False),
    sa.Column('finished_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='workflow_node_execution_pkey')
    )
    with op.batch_alter_table('workflow_node_executions', schema=None) as batch_op:
        batch_op.create_index('workflow_node_execution_node_run_idx', ['tenant_id', 'app_id', 'workflow_id', 'triggered_from', 'node_id'], unique=False)
        batch_op.create_index('workflow_node_execution_workflow_run_idx', ['tenant_id', 'app_id', 'workflow_id', 'triggered_from', 'workflow_run_id'], unique=False)

    op.create_table('workflow_runs',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tenant_id', postgresql.UUID(), nullable=False),
    sa.Column('app_id', postgresql.UUID(), nullable=False),
    sa.Column('sequence_number', sa.Integer(), nullable=False),
    sa.Column('workflow_id', postgresql.UUID(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('triggered_from', sa.String(length=255), nullable=False),
    sa.Column('version', sa.String(length=255), nullable=False),
    sa.Column('graph', sa.Text(), nullable=True),
    sa.Column('inputs', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('outputs', sa.Text(), nullable=True),
    sa.Column('error', sa.Text(), nullable=True),
    sa.Column('elapsed_time', sa.Float(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_tokens', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('total_steps', sa.Integer(), server_default=sa.text('0'), nullable=True),
    sa.Column('created_by_role', sa.String(length=255), nullable=False),
    sa.Column('created_by', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('finished_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='workflow_run_pkey')
    )
    with op.batch_alter_table('workflow_runs', schema=None) as batch_op:
        batch_op.create_index('workflow_run_triggerd_from_idx', ['tenant_id', 'app_id', 'triggered_from'], unique=False)

    op.create_table('workflows',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tenant_id', postgresql.UUID(), nullable=False),
    sa.Column('app_id', postgresql.UUID(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('version', sa.String(length=255), nullable=False),
    sa.Column('graph', sa.Text(), nullable=True),
    sa.Column('features', sa.Text(), nullable=True),
    sa.Column('created_by', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('updated_by', postgresql.UUID(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='workflow_pkey')
    )
    with op.batch_alter_table('workflows', schema=None) as batch_op:
        batch_op.create_index('workflow_version_idx', ['tenant_id', 'app_id', 'version'], unique=False)

    with op.batch_alter_table('apps', schema=None) as batch_op:
        batch_op.add_column(sa.Column('workflow_id', postgresql.UUID(), nullable=True))

    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('workflow_run_id', postgresql.UUID(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('workflow_run_id')

    with op.batch_alter_table('apps', schema=None) as batch_op:
        batch_op.drop_column('workflow_id')

    with op.batch_alter_table('workflows', schema=None) as batch_op:
        batch_op.drop_index('workflow_version_idx')

    op.drop_table('workflows')
    with op.batch_alter_table('workflow_runs', schema=None) as batch_op:
        batch_op.drop_index('workflow_run_triggerd_from_idx')

    op.drop_table('workflow_runs')
    with op.batch_alter_table('workflow_node_executions', schema=None) as batch_op:
        batch_op.drop_index('workflow_node_execution_workflow_run_idx')
        batch_op.drop_index('workflow_node_execution_node_run_idx')

    op.drop_table('workflow_node_executions')
    with op.batch_alter_table('workflow_app_logs', schema=None) as batch_op:
        batch_op.drop_index('workflow_app_log_app_idx')

    op.drop_table('workflow_app_logs')
    # ### end Alembic commands ###
