from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Button, Select, ScrollingGroup

from dialogs.main_dialog.getters import get_select_date
from dialogs.main_dialog.handlers import begin_add_task, begin_edit_task
from states.states import MainSG

window = Window(
    Format('Задачи на выбранный день.\n\n{select_date}'),
    ScrollingGroup(
        Select(
            Format('{item[text]}'),
            id='tasks',
            item_id_getter=lambda x: x['id'],
            items='tasks',
            on_click=begin_edit_task
        ),
        id='tasks_scroll',
        width=1,
        height=7,
        hide_on_single_page=True
    ),
    Row(
        Button(text=Const('Добавить задачу'), id='add_task', on_click=begin_add_task),
        SwitchTo(text=Const('Назад'), id='back_btn', state=MainSG.calendar)
    ),
    state=MainSG.calendar_tasks,
    getter=get_select_date
)
