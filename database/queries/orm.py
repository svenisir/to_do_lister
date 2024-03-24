import logging

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.models.base import Base
from database.models.models import Task, Category, Subtasks

logger = logging.getLogger(__name__)


async def create_tables(engine: create_async_engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_task(async_session: async_sessionmaker, data: dict):
    async with async_session() as session:
        task_id = await session.execute(
            insert(Task).returning(Task.id),
            [
                {'user_id': data['user_id'], 'text': data['text'],
                 'category_id': data['category_id'] if data['category_id'] != 0 else None,
                 'date_task': data['date_task']}
            ]
        )

        task_id = task_id.scalar()

        await session.execute(
            insert(Subtasks),
            [
                {'task_id': task_id, 
                 'text': subtask[0],
                 'complete': False} for subtask in data['subtasks']
            ]
        )

        await session.commit()


async def insert_base_category(async_session: async_sessionmaker, user_id: int):
    async with async_session() as session:
        work = Category(user_id=user_id, category_name='Работа')
        personally = Category(user_id=user_id, category_name='Личное')
        wishlist = Category(user_id=user_id, category_name='Список желаний')
        birthday = Category(user_id=user_id, category_name='День рождения')

        base_category = [work, personally, wishlist, birthday]
        session.add_all(base_category)

        await session.commit()


async def insert_category(async_session: async_sessionmaker, user_id: int, category_name: str):
    async with async_session() as session:
        categ = Category(user_id=user_id, category_name=category_name)
        session.add(categ)
        await session.commit()
