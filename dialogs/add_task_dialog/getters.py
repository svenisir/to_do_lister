from copy import deepcopy

from aiogram_dialog import DialogManager


async def get_task_params(dialog_manager: DialogManager, **kwargs):
    dialog_manager.dialog_data['task'] = dialog_manager.dialog_data.get('task', {})
    params = deepcopy(dialog_manager.dialog_data['task'])
    task_data = dialog_manager.dialog_data['task']

    if not params.get('text'):
        params['text'] = 'Вы пока не добавили текста задачи'
        params['add_text'] = False
    else:
        params['add_text'] = True

    if not params.get('category_name'):
        params['category_name'] = dialog_manager.start_data.get('category_name')
        task_data['category_name'] = params['category_name']

    if not params.get('category_id'):
        params['category_id'] = dialog_manager.start_data.get('category_id')
        task_data['category_id'] = params['category_id']

    if not params.get('date_task'):
        params['date_task'] = dialog_manager.start_data.get('date_task').strftime("%A %d %B %Y").title()
        task_data['date_task'] = dialog_manager.start_data.get('date_task')
    else:
        params['date_task'] = task_data['date_task'].strftime("%A %d %B %Y").title()

    if not params.get('subtasks') and not task_data.get('subtasks'):
        params['subtasks'] = [('Вы не добавили подзадачи',)]
        task_data['subtasks'] = set()

    return params


async def get_del_subtasks(dialog_manager: DialogManager, **kwargs):
    tasks = dialog_manager.dialog_data['task']['subtasks']
    subtasks = [task[0] for task in tasks] if tasks else []
    return {'subtasks': enumerate(subtasks)}
