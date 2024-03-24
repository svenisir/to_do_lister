from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format, Multi
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
        Format('<b>Подзадачи:</b>\n{subtasks}'),
        sep='\n\n'
    ),
    Group(
        SwitchTo(text=Const('Текст задачи'), id='text', state=AddTaskSG.text),
        SwitchTo(text=Const('Категория'), id='category', state=AddTaskSG.choose_category),
        Button(text=Const('Дата'), id='date'),
        Button(text=Const('Подзадачи'), id='subtask'),
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
