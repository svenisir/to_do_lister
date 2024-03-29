import locale
from datetime import date

from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Row, SwitchTo, Button, Select, ScrollingGroup

from dialogs.main_dialog.getters import get_state_category
from dialogs.main_dialog.handlers import change_tasks_state, begin_add_task, begin_edit_task
from states.states import MainSG

locale.setlocale(locale.LC_ALL, 'ru_Ru.UTF-8')

window = Window(
    Const(f'📝 Задачи на сегодня:\n{date.today().strftime("%A %d %B %Y").title()}'),
    Row(
        SwitchTo(text=Format('🎲 Категория: {category_name}'), id='category_btn', state=MainSG.choose_category),
        Button(text=Const(text='⭐️ Добавить задачу'), id='add_task', on_click=begin_add_task)
    ),
    Row(
        Button(text=Format('🔅 {active}'), id='active', on_click=change_tasks_state),
        Button(text=Format('❌ {uncomplete}'), id='uncomplete', on_click=change_tasks_state),
        Button(text=Format('✅ {complete}'), id='complete', on_click=change_tasks_state)
    ),
    ScrollingGroup(
        Select(
            Format("{item[text]}"),
            id='active_task',
            item_id_getter=lambda x: x['id'],
            items='active_tasks',
            on_click=begin_edit_task
        ),
        id='tasks_active',
        width=1,
        height=7,
        hide_on_single_page=True,
        when='active_state'
    ),
    ScrollingGroup(
        Select(
            Format("{item[text]}"),
            id='uncomplete_task',
            item_id_getter=lambda x: x['id'],
            items='uncomplete_tasks',
        ),
        id='tasks_uncomplete',
        width=1,
        height=7,
        hide_on_single_page=True,
        when='uncomplete_state'
    ),
    ScrollingGroup(
        Select(
            Format("{item[text]}"),
            id='complete_task',
            item_id_getter=lambda x: x['id'],
            items='complete_tasks',
        ),
        id='tasks_complete',
        width=1,
        height=7,
        hide_on_single_page=True,
        when='complete_state'
    ),
    SwitchTo(text=Const('⬅️ Назад'), id='back_btn', state=MainSG.start),
    state=MainSG.tasks,
    getter=get_state_category
)
