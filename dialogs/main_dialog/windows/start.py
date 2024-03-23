from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import SwitchTo
from states.states import MainSG
from dialogs.main_dialog.getters import get_name

window = Window(
    Format('Привет, {name}!', when='first_show'),
    Const('Выбери необходимое меню.'),
    SwitchTo(text=Const('Задачи'), id='tasks_btn', state=MainSG.tasks),
    SwitchTo(text=Const('Календарь'), id='calendar_btn', state=MainSG.calendar),
    SwitchTo(text=Const('Профиль'), id='profile_btn', state=MainSG.profile),
    SwitchTo(text=Const('Настройки'), id='settings_btn', state=MainSG.settings),
    state=MainSG.start,
    getter=get_name
)
