from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Button

from dialogs.main_dialog.getters import get_select_date
from dialogs.main_dialog.handlers import begin_add_task
from states.states import MainSG

window = Window(
    Format('Задачи на выбранный день.\n\n{select_date}'),
    Row(
        Button(text=Const('Добавить задачу'), id='add_task', on_click=begin_add_task),
        SwitchTo(text=Const('Назад'), id='back_btn', state=MainSG.calendar)
    ),
    state=MainSG.calendar_tasks,
    getter=get_select_date
)
