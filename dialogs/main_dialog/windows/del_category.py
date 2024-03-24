from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Select, SwitchTo, Column

from dialogs.main_dialog.getters import get_categories
from dialogs.main_dialog.handlers import delete_category
from states.states import MainSG

window = Window(
    Const(text='Выберете категорию, которую хотите удалить.'),
    Column(
        Select(
            Format('❌ {item[0]}'),
            id='del_categ',
            item_id_getter=lambda x: x[1],
            items='categories',
            on_click=delete_category,
        ),
    ),
    SwitchTo(text=Const('Назад'), id='back_btn', state=MainSG.choose_category),
    state=MainSG.delete_category,
    getter=get_categories
)
