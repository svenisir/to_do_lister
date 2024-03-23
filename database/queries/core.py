import logging

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

logger = logging.getLogger(__name__)


async def check_connection(engine: create_async_engine):
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1, 2, 3"))
        logger.info('Successful connection to db')


async def check_user(async_session: async_sessionmaker, user_id: int):
    async with async_session() as session:
        result = await session.execute(text(f"SELECT DISTINCT user_id "
                                         f"FROM category "
                                         f"WHERE user_id = {user_id}"))
    return result.all()


async def select_category(async_session: async_sessionmaker, user_id: int):
    async with async_session() as session:
        result = await session.execute(text(f"SELECT category_name, id "
                                            f"FROM category "
                                            f"WHERE user_id = {user_id}"))
    return result.all()


async def select_category_name(async_session: async_sessionmaker, categ_id: int):
    async with async_session() as session:
        result = await session.execute(text(f"SELECT category_name "
                                            f"FROM category "
                                            f"WHERE id = {categ_id}"))
    return result.scalar()


async def check_category(async_session: async_sessionmaker, categ_name: str):
    async with async_session() as session:
        result = await session.execute(text(f"SELECT category_name "
                                            f"FROM category "
                                            f"WHERE category_name = \'{categ_name}\'"))
        return result.all()


async def del_category(async_session: async_sessionmaker, categ_id: int):
    async with async_session() as session:
        await session.execute(text(f"DELETE FROM category "
                                   f"WHERE id = {categ_id}"))
        await session.commit() 
