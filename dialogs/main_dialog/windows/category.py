from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Select, Column, Row, ScrollingGroup, Button

from dialogs.main_dialog.getters import get_categories
from dialogs.main_dialog.handlers import back_with_category, back_all_category
from states.states import MainSG, AddCategorySG

window = Window(
    Const(text='Выберете категорию'),
    ScrollingGroup(
        Column(
            Button(text=Const('Все'), id='all_category', on_click=back_all_category),
            Select(
                Format('{item[0]}'),
                id='categ',
                item_id_getter=lambda x: x[1],
                items='categories',
                on_click=back_with_category,
            ),
        ),
        id='category',
        width=1,
        height=7,
        hide_on_single_page=True
    ),
    Row(
        Start(text=Const('Добавить категорию'), id='add_category', state=AddCategorySG.category_input),
        SwitchTo(text=Const('Удалить категории'), id='del_category', state=MainSG.delete_category),
    ),
    SwitchTo(text=Const('Назад'), id='back_btn', state=MainSG.tasks),
    state=MainSG.choose_category,
    getter=get_categories
)
