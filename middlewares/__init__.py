from sqlalchemy.ext.asyncio import async_sessionmaker
from aiogram import Dispatcher

from .database import Database


def setup_middlewares(
        dp: Dispatcher,
        smk: async_sessionmaker
):
    dp.update.outer_middleware(Database(smk))
