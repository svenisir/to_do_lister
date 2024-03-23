from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import Cancel, Button, SwitchTo, Row

from dialogs.add_category_dialog.getters import get_category_name
from dialogs.add_category_dialog.handlers import add_category
from states.states import AddCategorySG

window = Window(
    Format('<i>Добавить категорию:</i> {categ_name}?'),
    Row(
        Button(text=Const('Добавить'), id='add_category', on_click=add_category),
        SwitchTo(text=Const('Редактировать'), id='edit_category', state=AddCategorySG.category_input),
    ),
    Cancel(text=Const('Назад'), id='back_btn'),
    state=AddCategorySG.category_confirm,
    getter=get_category_name
)
