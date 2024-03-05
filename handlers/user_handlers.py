from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=f'Привет {message.from_user.first_name}!')
