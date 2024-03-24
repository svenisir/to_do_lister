from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format, Multi, List
from aiogram_dialog.widgets.kbd import Button, Cancel, Row, SwitchTo, Group

from dialogs.add_task_dialog.handlers import add_task
from dialogs.add_task_dialog.getters import get_task_params
from states.states import AddTaskSG

window = Window(
    Multi(
        Const('Составьте свою задачу!'),
        Format('<b>Текст:</b>\n{text}'),
        Format('<b>Категория:</b>\n{category_name}'),
        Format('<b>Дата:</b>\n{date_task}'),
        Multi(
            Format('<b>Подзадачи:</b>'),
            List(
                field=Format('\t\t\t• {item[0]}'),
                items='subtasks'
            ),
        ),
        sep='\n\n'
    ),
    Group(
        SwitchTo(text=Const('Текст задачи'), id='text', state=AddTaskSG.text),
        SwitchTo(text=Const('Категория'), id='category', state=AddTaskSG.choose_category),
        SwitchTo(text=Const('Дата'), id='date', state=AddTaskSG.data_task),
        SwitchTo(text=Const('Подзадачи'), id='subtask', state=AddTaskSG.subtasks_input),
        Button(text=Const('Шаблон задачи'), id='pattern'),
        width=2
    ),
    Row(
        Button(text=Const('Добавить задачу'), id='add_task', on_click=add_task, when='add_text'),
        Cancel(text=Const('Назад'), id='back_btn')
    ),
    state=AddTaskSG.begin,
    getter=get_task_params
)
