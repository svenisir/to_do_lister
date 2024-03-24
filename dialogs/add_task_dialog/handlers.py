from typing import Any
from datetime import date

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


async def correct_subtask(message: Message, widget: ManagedTextInput,
                          dialog_manager: DialogManager, text: str) -> None:
    dialog_manager.dialog_data['task']['subtasks'].add((text.strip(),))
    dialog_manager.dialog_data['task']['show_subtasks'] = True
    await dialog_manager.switch_to(state=AddTaskSG.begin)


async def error_text(message: Message, widget: ManagedTextInput,
                     dialog_manager: DialogManager, text: str):
    await message.answer(text='Недопустимый текст задачи. Попробуйте ещё раз.')


async def no_text(message: Message, widget: MessageInput,
                  dialog_manager: DialogManager) -> None:
    await message.answer(text='Это сообщение не содержит текст. Попробуйте ещё раз.')


async def back_with_category(callback: CallbackQuery, widget: Any,
                             dialog_manager: DialogManager, item_id: str):
    category_name = dialog_manager.dialog_data['task']['category_name']
    for btn in callback.message.reply_markup.inline_keyboard:
        if btn[0].callback_data.endswith(callback.data):
            category_name = btn[0].text
    dialog_manager.dialog_data['task']['category_name'] = category_name
    dialog_manager.dialog_data['task']['category_id'] = int(item_id)

    await dialog_manager.switch_to(state=AddTaskSG.begin)


async def add_date_task(callback: CallbackQuery, widget: Any,
                        dialog_manager: DialogManager, selected_date: date):
    dialog_manager.dialog_data['task']['date_task'] = selected_date
    await dialog_manager.switch_to(state=AddTaskSG.begin)


async def delete_subtasks(callback: CallbackQuery, widget: Any,
                          dialog_manager: DialogManager, item_id: str):
    subtask = ''
    for btn in callback.message.reply_markup.inline_keyboard:
        if btn[0].callback_data.endswith(callback.data):
            subtask = btn[0].text[2:]

    dialog_manager.dialog_data['task']['subtasks'].discard((subtask,))
