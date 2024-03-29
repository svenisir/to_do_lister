import logging
from datetime import date

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

logger = logging.getLogger(__name__)


async def check_connection(engine: create_async_engine):
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1, 2, 3"))
        logger.info('Successful connection to db')


async def check_user(async_session: async_sessionmaker, user_id: int):
    async with async_session() as session:
        stat = text("SELECT DISTINCT user_id FROM category WHERE user_id =:id")
        stat = stat.bindparams(id=user_id)
        result = await session.execute(stat)
    return result.all()


async def select_category(async_session: async_sessionmaker, user_id: int):
    async with async_session() as session:
        stat = text("SELECT category_name, id FROM category WHERE user_id =:id")
        stat = stat.bindparams(id=user_id)
        result = await session.execute(stat)
    return result.all()


async def select_category_name(async_session: async_sessionmaker, categ_id: int):
    async with async_session() as session:
        stat = text("SELECT category_name FROM category WHERE id =:id")
        stat = stat.bindparams(id=categ_id)
        result = await session.execute(stat)
    return result.scalar()


async def check_category(async_session: async_sessionmaker, categ_name: str):
    async with async_session() as session:
        stat = text(f"SELECT category_name FROM category WHERE category_name =:categ")
        stat = stat.bindparams(categ=categ_name)
        result = await session.execute(stat)
        return result.all()


async def del_category(async_session: async_sessionmaker, categ_id: int):
    async with async_session() as session:
        stat = text(f"DELETE FROM category WHERE id =:id")
        stat = stat.bindparams(id=categ_id)
        await session.execute(stat)
        await session.commit()


async def select_tasks(async_session: async_sessionmaker, user_id: int):
    async with async_session() as session:
        stat = text(f"SELECT text, id, category_id, date_task, complete "
                    f"FROM tasks "
                    f"WHERE user_id=:id")
        stat = stat.bindparams(id=user_id)
        res = await session.execute(stat)
        await session.commit()
    return res.mappings().all()


async def select_tasks_on_day(async_session: async_sessionmaker, user_id: int, date_task: date):
    async with async_session() as session:
        stat = text(f"SELECT text, id, category_id, date_task, complete "
                    f"FROM tasks "
                    f"WHERE user_id=:id and date_task=:date_task")
        stat = stat.bindparams(id=user_id, date_task=date_task)
        res = await session.execute(stat)
        await session.commit()
    return res.mappings().all()
