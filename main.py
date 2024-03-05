import asyncio
import logging.config

from aiogram import Dispatcher, Bot
from config_data.config import load_config
from handlers.user_handlers import router
from logging_config.logging_settings import logging_config

logger = logging.getLogger(__name__)


async def main():
    logging.config.dictConfig(logging_config)
    logger.info('Starting_bot')

    config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
