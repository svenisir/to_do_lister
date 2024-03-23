from typing import Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button

from database.queries.core import check_category
from database.queries.orm import insert_category
from states.states import AddCategorySG


def category_check(text: Any):
    if all([word.isalnum() for word in text.split()]):
        return text
    raise ValueError


async def correct_category(message: Message, widget: ManagedTextInput,
                           dialog_manager: DialogManager, text: str):
    dialog_manager.dialog_data['category'] = text.strip()
    await dialog_manager.switch_to(state=AddCategorySG.category_confirm)


async def error_category(message: Message, widget: ManagedTextInput,
                         dialog_manager: DialogManager, text: str):
    await message.answer(text='Некорректное имя категории. Попробуйте ещё раз.')


async def no_category(message: Message, widget: MessageInput,
                      dialog_manager: DialogManager):
    await message.answer(text='Этот формат сообщения не может быть категорией!')


async def add_category(callback: CallbackQuery, button: Button,
                       dialog_manager: DialogManager):
    session = dialog_manager.middleware_data['session']
    categ_name = dialog_manager.dialog_data.get('category')
    if not await check_category(async_session=session, categ_name=categ_name):
        await insert_category(async_session=session,
                              category_name=categ_name,
                              user_id=callback.from_user.id)
    await dialog_manager.done()
