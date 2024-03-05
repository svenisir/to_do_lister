import asyncio

from aiogram import Dispatcher, Bot
from config_data.config import load_config
from handlers.user_handlers import router


async def main():

    config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
