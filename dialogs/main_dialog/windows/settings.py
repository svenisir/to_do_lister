from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo

from states.states import MainSG

window = Window(
    Const('Пока вообще не придумал, что тут будет, но надеюсь, что-то полезное'),
    SwitchTo(text=Const('Назад'), id='back_btn', state=MainSG.start),
    state=MainSG.settings 
)
