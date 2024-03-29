import logging
from datetime import date
from copy import deepcopy

from aiogram.types import User
from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager

from database.queries.core import select_category, select_tasks, select_tasks_on_day

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


async def get_state_category(event_from_user: User, dialog_manager: DialogManager,
                             state: FSMContext, **kwargs):
    tasks_state = dialog_manager.dialog_data.get('tasks_state', 'active')

    if dialog_manager.dialog_data.get('tasks') is None:
        tasks = deepcopy(await select_tasks(async_session=dialog_manager.middleware_data['session'],
                                            user_id=event_from_user.id))
        dialog_manager.dialog_data['tasks'] = tasks
    else:
        tasks = dialog_manager.dialog_data['tasks']

    tasks_dict = {
        'active': 'Активные',
        'uncomplete': 'Невыполненные',
        'complete': 'Выполненные',
        'active_state': False,
        'uncomplete_state': False,
        'complete_state': False,
    }

    if tasks_state == 'active':
        tasks_dict['active'] = '✓ Активные'
        tasks_dict['active_state'] = True
    elif tasks_state == 'uncomplete':
        tasks_dict['uncomplete'] = '✓ Невыполненные'
        tasks_dict['uncomplete_state'] = True
    else:
        tasks_dict['complete'] = '✓ Выполненные'
        tasks_dict['complete_state'] = True

    category = dialog_manager.dialog_data.get('category', {'name': 'Все', 'id': None})
    dialog_manager.dialog_data['category'] = category
    tasks_dict['category_name'] = category['name']

    active_tasks = []
    complete_tasks = []
    uncomplete_tasks = []

    def sort_task(_task):
        if not _task['complete']:
            if _task['date_task'] >= date.today():
                active_tasks.append(_task)
            else:
                uncomplete_tasks.append(_task)
        else:
            complete_tasks.append(_task)

    for task in tasks:
        if category['id'] is None:
            sort_task(task)
        elif task['category_id'] == category['id']:
            sort_task(task)

    tasks_dict.update(
        {
            'active_tasks': active_tasks,
            'uncomplete_tasks': uncomplete_tasks,
            'complete_tasks': complete_tasks
        }
    )
    dialog_manager.is_preview()
    return tasks_dict


async def get_select_date(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    selected_date: date = dialog_manager.dialog_data['select_date']

    if dialog_manager.dialog_data.get('tasks') is None:
        tasks = deepcopy(await select_tasks_on_day(async_session=dialog_manager.middleware_data['session'],
                                                   user_id=event_from_user.id,
                                                   date_task=selected_date))
        dialog_manager.dialog_data['tasks'] = tasks
    else:
        tasks = dialog_manager.dialog_data['tasks']

    selected_date: str = selected_date.strftime("%A ").title() + \
                         str(int(selected_date.strftime("%d"))) + \
                         selected_date.strftime(" %B %Y")
    return {'select_date': selected_date,
            'tasks': tasks}



async def get_categories(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    session = dialog_manager.middleware_data['session']
    categories = await select_category(async_session=session, user_id=event_from_user.id)
    return {'categories': categories}
