import logging

from sqlalchemy.ext.asyncio import create_async_engine

from database.models.base import Base
from database.models.models import User

logger = logging.getLogger(__name__)


async def create_tables(engine: create_async_engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)