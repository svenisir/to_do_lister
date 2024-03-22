from datetime import date

from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Calendar, SwitchTo

from dialogs.main_dialog.handlers import date_clicked
from states.states import MainSG

window = Window(
    Const(text=f'Выберете день, чтобы посмотреть задачи на этот день.'
               f'\nСегодня: {date.today().strftime("%A %d %B %Y")}'),
    Calendar(id='calendar', on_click=date_clicked),
    SwitchTo(text=Const('Назад'), id='back_btn', state=MainSG.start),
    state=MainSG.calendar
)
