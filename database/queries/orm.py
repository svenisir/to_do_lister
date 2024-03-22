import logging

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.models.base import Base
from database.models.models import Task

logger = logging.getLogger(__name__)


async def create_tables(engine: create_async_engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_task(async_session: async_sessionmaker, data: dict):
    async with async_session() as session:
        task = Task(user_id=data['user_id'], text=data['text'])
        session.add(task)
        await session.commit()


