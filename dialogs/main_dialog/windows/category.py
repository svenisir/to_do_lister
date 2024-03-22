from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, SwitchTo

from states.states import MainSG

window = Window(
    Const(text='Выберете категорию'),
    Button(text=Const('Добавить категорию'), id='add_category'),
    SwitchTo(text=Const('Назад'), id='back_btn', state=MainSG.tasks),
    state=MainSG.choose_category 
)

