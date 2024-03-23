import logging

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.models.base import Base
from database.models.models import Task, Category

logger = logging.getLogger(__name__)


async def create_tables(engine: create_async_engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_task(async_session: async_sessionmaker, data: dict):
    async with async_session() as session:
        task = Task(user_id=data['user_id'], text=data['text'], category_id=data[''])
        session.add(task)
        await session.commit()


async def insert_base_category(async_session: async_sessionmaker, user_id: int):
    async with async_session() as session:
        work = Category(user_id=user_id, category_name='Работа')
        personally = Category(user_id=user_id, category_name='Личное')
        wishlist = Category(user_id=user_id, category_name='Список желаний')
        birthday = Category(user_id=user_id, category_name='День рождения')

        base_category = [work, personally, wishlist, birthday]
        for categ in base_category:
            session.add(categ)

        await session.commit()


async def insert_category(async_session: async_sessionmaker, user_id: int, category_name: str):
    async with async_session() as session:
        categ = Category(user_id=user_id, category_name=category_name)
        session.add(categ)
        await session.commit()
