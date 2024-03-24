import locale
from datetime import date

from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Row, SwitchTo, Button

from dialogs.main_dialog.getters import get_state_category
from dialogs.main_dialog.handlers import change_tasks_state, begin_add_task
from states.states import MainSG

locale.setlocale(locale.LC_ALL, 'ru_Ru.UTF-8')

window = Window(
    Const(f'Задачи на сегодня:\n{date.today().strftime("%A %d %B %Y").title()}'),
    Row(
        SwitchTo(text=Format('Категория: {category_name}'), id='category_btn', state=MainSG.choose_category),
        Button(text=Const(text='Добавить задачу'), id='add_task', on_click=begin_add_task)
    ),
    Row(
        Button(text=Format('{active}'), id='active', on_click=change_tasks_state),
        Button(text=Format('{uncomplete}'), id='uncomplete', on_click=change_tasks_state),
        Button(text=Format('{complete}'), id='complete', on_click=change_tasks_state)
    ),
    SwitchTo(text=Const('Назад'), id='back_btn', state=MainSG.start),
    state=MainSG.tasks,
    getter=get_state_category
)
