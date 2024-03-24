from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.input import TextInput, MessageInput

from dialogs.add_task_dialog.handlers import (text_check, correct_text,
                                              error_text, no_text)
from states.states import AddTaskSG

window = Window(
    Const('Введите текст задачи'),
    TextInput(
        id='text_input',
        type_factory=text_check,
        on_success=correct_text,
        on_error=error_text
    ),
    MessageInput(
        func=no_text,
        content_types=ContentType.ANY
    ),
    SwitchTo(text=Const('Назад'), id='back_btn', state=AddTaskSG.begin),
    state=AddTaskSG.text
)
