from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Select, Column, Row

from dialogs.main_dialog.getters import get_categories
from dialogs.add_task_dialog.handlers import back_with_category
from states.states import AddTaskSG, AddCategorySG

window = Window(
    Const(text='Выберете категорию'),
    SwitchTo(text=Const('Все'), id='all_category', state=AddTaskSG.begin),
    Column(
        Select(
            Format('{item[0]}'),
            id='categ',
            item_id_getter=lambda x: x[1],
            items='categories',
            on_click=back_with_category,
        ),
    ),
    Row(
        Start(text=Const('Добавить категорию'), id='add_category', state=AddCategorySG.category_input),
        SwitchTo(text=Const('Назад'), id='back_btn', state=AddTaskSG.begin),
    ),
    state=AddTaskSG.choose_category,
    getter=get_categories
)
