"""Alembic env — wired to the Flask app's config + models."""
import os
from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

from app import create_app
from app.config import normalize_database_url
from app.db import db

def _compare_type(context, inspected_column, metadata_column, inspected_type, metadata_type):
    """SQLite stores everything as TEXT/INTEGER/REAL/BLOB; do not report VARCHAR/JSON/DateTime/Boolean vs TEXT/INTEGER."""
    if context.dialect.name != "sqlite":
        return None                                    # default, strict comparison
    def aff(t):
        n = str(t).upper()
        return "INT" if ("INT" in n or "BOOL" in n) else "TEXT"
    return aff(inspected_type) != aff(metadata_type)


config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

flask_app = create_app()
# ALEMBIC_DATABASE_URL lets tests and one-off runs target another database without touching app config
_url = normalize_database_url(os.environ.get("ALEMBIC_DATABASE_URL", "")) or flask_app.config["SQLALCHEMY_DATABASE_URI"]
config.set_main_option("sqlalchemy.url", _url.replace("%", "%%"))
target_metadata = db.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=_compare_type,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=_compare_type,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
