from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput

from states.states import AddTaskSG
from database.queries.orm import insert_task


async def add_task(callback: CallbackQuery,
                   button: Button,
                   dialog_manager: DialogManager) -> None:
    session = dialog_manager.middleware_data['session']
    data: dict = dialog_manager.dialog_data['task']
    data.update({'user_id': callback.from_user.id})
    await insert_task(async_session=session, data=data)
    await dialog_manager.done()


def text_check(text: str) -> str:
    if all([word.isalnum() for word in text.split()]):
        return text
    raise ValueError


async def correct_text(message: Message, widget: ManagedTextInput,
                       dialog_manager: DialogManager, text: str) -> None:
    dialog_manager.dialog_data['task']['text'] = text
    await dialog_manager.switch_to(state=AddTaskSG.begin)


async def error_text(message: Message, widget: ManagedTextInput,
                     dialog_manager: DialogManager, text: str):
    await message.answer(text='Недопустимый текст задачи. Попробуйте ещё раз.')


async def no_text(message: Message, widget: MessageInput,
                  dialog_manager: DialogManager) -> None:
    await message.answer(text='Это сообщение не содержит текст. Попробуйте ещё раз.')
