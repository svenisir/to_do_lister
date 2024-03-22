from sqlalchemy.ext.asyncio import async_sessionmaker
from aiogram import Dispatcher
from aiogram.fsm.storage.redis import Redis

from .database import Database
from .throttling import ThrottlingMiddleware


def setup_middlewares(
        dp: Dispatcher,
        smk: async_sessionmaker,
        redis: Redis = None
):
    dp.update.outer_middleware(Database(smk))
    dp.update.outer_middleware(ThrottlingMiddleware(redis))
