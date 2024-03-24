from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Calendar, SwitchTo

from dialogs.add_task_dialog.handlers import add_date_task
from states.states import AddTaskSG

window = Window(
    Const('Выберете дату для вашей задачи'),
    Calendar(id='calendar', on_click=add_date_task),
    SwitchTo(text=Const('Назад'), id='back_btn', state=AddTaskSG.begin),
    state=AddTaskSG.data_task
)
