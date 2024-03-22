from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format, Multi
from aiogram_dialog.widgets.kbd import Button, Cancel, Row, SwitchTo

from dialogs.add_task_dialog.handlers import add_task
from dialogs.add_task_dialog.getters import get_task_params
from states.states import AddTaskSG

window = Window(
    Multi(
        Const('Составьте свою задачу!'),
        Format('<b>Текст:</b>\n{text}'),
        Format('<b>Категория:</b>\n{category}'),
        Format('<b>Дата:</b>\n{date_task}'),
        Format('<b>Подзадачи:</b>\n{subtasks}'),
        sep='\n\n'
    ),
    SwitchTo(text=Const('Добавьте текст задачи'), id='text', state=AddTaskSG.text),
    Button(text=Const('Выберете категорию'), id='category'),
    Button(text=Const('Добавьте дату'), id='date'),
    Button(text=Const('Добавьте подзадачу'), id='subtask'),
    Button(text=Const('Шаблон задачи'), id='pattern'),
    Row(
        Button(text=Const('Добавить задачу'), id='add_task', on_click=add_task),
        Cancel(text=Const('Назад'), id='back_btn')
    ),
    state=AddTaskSG.begin,
    getter=get_task_params
)
