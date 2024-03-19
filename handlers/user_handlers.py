from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from database.models.models import User
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import text

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, session: async_sessionmaker):
    async with session() as s:
        user = User(
            id=message.from_user.id,
            name=message.from_user.first_name,
            is_premium=bool(message.from_user.is_premium),
            surname=message.from_user.last_name,
            fullname=message.from_user.username
        )
        s.add(user)
        await s.commit()

    # async with session() as s:
    #     s.execute(text("SELECT "))
    await message.answer(text=f'Привет {message.from_user.first_name}!')
