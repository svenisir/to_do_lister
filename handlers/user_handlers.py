from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from sqlalchemy.ext.asyncio import async_sessionmaker

from states.states import MainSG
from database.queries.core import check_user
from database.queries.orm import insert_base_category

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, dialog_manager: DialogManager, session: async_sessionmaker):
    if not await check_user(async_session=session, user_id=message.from_user.id):
        await insert_base_category(async_session=session, user_id=message.from_user.id)

    await dialog_manager.start(state=MainSG.start, data={'first_show': True})
