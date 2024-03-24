from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import SwitchTo, Select, Column

from dialogs.add_task_dialog.getters import get_del_subtasks
from dialogs.add_task_dialog.handlers import delete_subtasks
from states.states import AddTaskSG

window = Window(
    Const('Выберете подзадачи, которые хотите удалить.'),
    Column(
        Select(
            Format('❌ {item[1]}'),
            id='del_subtasks',
            item_id_getter=lambda x: x[0],
            items='subtasks',
            on_click=delete_subtasks
        ),
    ),
    SwitchTo(text=Const('Назад'), id='back_btn', state=AddTaskSG.subtasks_input), 
    state=AddTaskSG.subtasks_delete,
    getter=get_del_subtasks
)
