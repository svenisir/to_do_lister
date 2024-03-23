from datetime import date
from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from database.queries.core import select_category_name, del_category
from states.states import MainSG, AddTaskSG


async def change_tasks_state(callback: CallbackQuery,
                             button: Button,
                             dialog_manager: DialogManager):
    dialog_manager.dialog_data['tasks_state'] = button.widget_id


async def date_clicked(callback: CallbackQuery, widget,
                       dialog_manager: DialogManager, selected_date: date):
    dialog_manager.dialog_data['select_date'] = selected_date
    await dialog_manager.switch_to(state=MainSG.calendar_tasks)


async def go_begin_task(callback: CallbackQuery, button: Button,
                        dialog_manager: DialogManager):
    date_task = dialog_manager.dialog_data['select_date']
    await dialog_manager.start(state=AddTaskSG.begin, date={'date_task': date_task})


async def back_with_category(callback: CallbackQuery, widget: Any,
                             dialog_manager: DialogManager, item_id: str):
    session = dialog_manager.middleware_data['session']
    category_name = await select_category_name(async_session=session, categ_id=int(item_id))
    dialog_manager.dialog_data['category'] = {
        'name': category_name,
        'id': int(item_id)
    }
    await dialog_manager.switch_to(state=MainSG.tasks)


async def back_all_categories(callback: CallbackQuery, button: Button,
                              dialog_manager: DialogManager):
    dialog_manager.dialog_data['category'] = {
        'name': 'Все',
        'id': 0
    }
    await dialog_manager.switch_to(state=MainSG.tasks)


async def delete_category(callback: CallbackQuery, widget: Any,
                          dialog_manager: DialogManager, item_id: str):
    session = dialog_manager.middleware_data['session']
    await del_category(async_session=session, categ_id=int(item_id))
