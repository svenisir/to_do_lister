from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo

from states.states import MainSG

window = Window(
    Const('Выполненные задачи за всё время.'),
    SwitchTo(text=Const('Назад'), id='back_btn', state=MainSG.profile),
    state=MainSG.complete_tasks
)
