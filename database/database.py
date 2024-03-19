from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config_data.config import DatabaseConfig


def create_db_engine(db: DatabaseConfig, echo: bool = False):
    return create_async_engine(db.DATABASE_URL_asyncpg, echo=echo)


def create_sessionmaker(engine: create_async_engine) -> async_sessionmaker:
    return async_sessionmaker(bind=engine)
