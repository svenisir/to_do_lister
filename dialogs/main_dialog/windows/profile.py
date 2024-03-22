from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo

from states.states import MainSG

window = Window(
    Const('Профиль'),
    SwitchTo(text=Const('Выполненные задачи'), id='completed_tasks', state=MainSG.complete_tasks),
    SwitchTo(text=Const('Назад'), id='back_btn', state=MainSG.start),
    state=MainSG.profile
)
