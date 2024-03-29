import asyncio
import logging.config

from aiogram import Dispatcher, Bot
from aiogram.filters import ExceptionTypeFilter
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram_dialog import setup_dialogs
from aiogram_dialog.api.exceptions import UnknownIntent
from config_data.config import load_config
from database.database import create_db_engine, create_sessionmaker
from database.queries import core, orm
from middlewares import setup_middlewares
from handlers.user_handlers import router
from handlers.error_handlers import on_unknown_intent
from dialogs import setup
from logging_config.logging_settings import logging_config

logger = logging.getLogger(__name__)


async def main():
    logging.config.dictConfig(logging_config)
    logger.info('Starting_bot')

    config = load_config()

    if config.tg_bot.use_redis:
        redis = Redis(host='localhost')
        storage = RedisStorage(redis=redis)
    else:
        storage = MemoryStorage()

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode='HTML')) 
    dp = Dispatcher(storage=storage)

    dp.errors.register(
        on_unknown_intent,
        ExceptionTypeFilter(UnknownIntent)
    )

    engine = create_db_engine(db=config.db, echo=True)
    session_factory = create_sessionmaker(engine)
    setup_middlewares(dp=dp, smk=session_factory)

    await core.check_connection(engine)
    await orm.create_tables(engine)

    dp.include_router(router)
    setup(dp)
    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
