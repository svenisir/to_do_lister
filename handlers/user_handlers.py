from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager

from states.states import MainSG

from sqlalchemy.ext.asyncio import async_sessionmaker

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MainSG.start, data={'first_show': True})
