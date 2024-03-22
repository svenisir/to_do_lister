from datetime import date

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

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
