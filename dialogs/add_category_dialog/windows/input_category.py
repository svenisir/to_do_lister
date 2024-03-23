from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.input import TextInput, MessageInput

from dialogs.add_category_dialog.handlers import (category_check, correct_category,
                                                  error_category, no_category)
from states.states import AddCategorySG

window = Window(
    Const('Введите название категории'),
    TextInput(
        id='category_input',
        type_factory=category_check,
        on_success=correct_category,
        on_error=error_category
    ),
    MessageInput(
        func=no_category,
        content_types=ContentType.ANY
    ),
    Cancel(text=Const('Назад'), id='back_btn'),
    state=AddCategorySG.category_input
)
