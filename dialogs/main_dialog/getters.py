import logging
from datetime import date

from aiogram.types import User
from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager

from database.queries.core import select_category

logger = logging.getLogger(__name__)


async def get_name(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    if dialog_manager.start_data:
        name_data = {
            'name': event_from_user.full_name or 'пользователь',
            'first_show': True
        }
        dialog_manager.start_data.clear()
    else:
        name_data = {
            'first_show': False
        }

    return name_data


async def get_state_category(dialog_manager: DialogManager, state: FSMContext, **kwargs):
    tasks_state = dialog_manager.dialog_data.get('tasks_state', 'active')

    tasks = {
        'active': 'Активные',
        'uncomplete': 'Невыполненные',
        'complete': 'Выполненные',
        'active_state': False,
        'uncomplete_state': False,
        'complete_state': False,
    }

    if tasks_state == 'active':
        tasks['active'] = '✓ Активные'
        tasks['active_state'] = True
    elif tasks_state == 'uncomplete':
        tasks['uncomplete'] = '✓ Невыполненные'
        tasks['uncomplete_state'] = True
    else:
        tasks['complete'] = '✓ Выполненные'
        tasks['complete_state'] = True

    category = dialog_manager.dialog_data.get('category', {'name': 'Все', 'id': 0})
    dialog_manager.dialog_data['category'] = category
    tasks.update({'category_name': category['name'].lower()})

    return tasks


async def get_select_date(dialog_manager: DialogManager, **kwargs):
    selected_date: date = dialog_manager.dialog_data['select_date']
    selected_date: str = selected_date.strftime("%A ").title() + \
                         str(int(selected_date.strftime("%d"))) + \
                         selected_date.strftime(" %B %Y")
    dialog_manager.dialog_data['select_date'] = selected_date
    return {'select_date': selected_date}


async def get_categories(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    session = dialog_manager.middleware_data['session']
    categories = await select_category(async_session=session, user_id=event_from_user.id)
    return {'categories': categories}
