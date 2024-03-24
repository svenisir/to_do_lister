from datetime import date
from typing import Any

from time import perf_counter

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select

from database.queries.core import select_category_name, del_category
from states.states import MainSG, AddTaskSG


async def drop_dialog_data(callback: CallbackQuery, button: Button,
                           dialog_manager: DialogManager):
    dialog_manager.dialog_data.clear()


async def change_tasks_state(callback: CallbackQuery,
                             button: Button,
                             dialog_manager: DialogManager):
    dialog_manager.dialog_data['tasks_state'] = button.widget_id


async def date_clicked(callback: CallbackQuery, widget,
                       dialog_manager: DialogManager, selected_date: date):
    dialog_manager.dialog_data['select_date'] = selected_date
    await dialog_manager.switch_to(state=MainSG.calendar_tasks)


async def back_with_category(callback: CallbackQuery, widget: Select,
                             dialog_manager: DialogManager, item_id: str):
    # Вариант рабочий, но работает дольше, чем через callback
    # session = dialog_manager.middleware_data['session']
    # category_name = await select_category_name(async_session=session, categ_id=int(item_id))

    category_name = dialog_manager.dialog_data['category']['name']
    for btn in callback.message.reply_markup.inline_keyboard:
        if btn[0].callback_data.endswith(callback.data):
            category_name = btn[0].text

    dialog_manager.dialog_data['category'] = {
        'name': category_name,
        'id': int(item_id)
    }
    await dialog_manager.switch_to(state=MainSG.tasks)


async def delete_category(callback: CallbackQuery, widget: Any,
                          dialog_manager: DialogManager, item_id: str):
    session = dialog_manager.middleware_data['session']
    await del_category(async_session=session, categ_id=int(item_id))


async def begin_add_task(callback: CallbackQuery, button: Button,
                         dialog_manager: DialogManager):
    category = dialog_manager.dialog_data.get('category', {'name': 'Все', 'id': 0})
    start_data = {'category_name': category['name'],
                  'category_id': category['id'],
                  'date_task': dialog_manager.dialog_data.get('select_date', date.today())}
    await dialog_manager.start(state=AddTaskSG.begin, data=start_data)
