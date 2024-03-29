from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, Cancel, Row, Group, SwitchTo

from states.states import EditTaskSG

window = Window(
    Const('Тут будет ваша задача.'),
    Row(
        Button(text=Const('Выполнено'), id='confirm_task'),
        Button(text=Const('Удалить'), id='delete_task'),
    ),
    Group(
        SwitchTo(text=Const('Текст'), id='edit_text', state=EditTaskSG.egit_text),
        SwitchTo(text=Const('Категория'), id='edit_category', state=EditTaskSG.edit_category),
        SwitchTo(text=Const('Подзадачи'), id='edit_subtasks', state=EditTaskSG.edit_subtasks),
        SwitchTo(text=Const('Дата'), id='edit_date_task', state=EditTaskSG.edit_date_task),
        SwitchTo(text=Const('Время / напоминание'), id='edit_time_repeat', state=EditTaskSG.edit_time_repeat),
        SwitchTo(text=Const('Заметки'), id='edit_notes', state=EditTaskSG.edit_notes),
        width=3,
    ),
    Cancel(text=Const('Назад'), id='back_btn'),
    state=EditTaskSG.begin
)
