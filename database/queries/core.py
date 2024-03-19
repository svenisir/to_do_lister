import logging

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

logger = logging.getLogger(__name__)


async def check_connection(engine: create_async_engine):
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1, 2, 3"))
        logger.info('Successful connection to db')
