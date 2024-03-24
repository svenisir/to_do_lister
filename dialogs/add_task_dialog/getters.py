from copy import deepcopy

from aiogram_dialog import DialogManager


async def get_task_params(dialog_manager: DialogManager, **kwargs):
    dialog_manager.dialog_data['task'] = dialog_manager.dialog_data.get('task', {})
    params = deepcopy(dialog_manager.dialog_data['task'])

    if not params.get('text'):
        params['text'] = 'Вы пока не добавили текста задачи'
        params['add_text'] = False
    else:
        params['add_text'] = True

    if not params.get('category_name'):
        params['category_name'] = dialog_manager.start_data.get('category_name')
        dialog_manager.dialog_data['task']['category_name'] = params['category_name']

    if not params.get('category_id'):
        params['category_id'] = dialog_manager.start_data.get('category_id')
        dialog_manager.dialog_data['task']['category_id'] = params['category_id']

    if not params.get('date_task'):
        params['date_task'] = dialog_manager.start_data.get('date_task').strftime("%A %d %B %Y").title()
        dialog_manager.dialog_data['task']['date_task'] = params['date_task']

    if not params.get('subtasks') and not dialog_manager.dialog_data['task'].get('subtasks'):
        params['subtasks'] = 'Вы не добавили подзадачи'
        dialog_manager.dialog_data['task']['subtasks'] = []

    return params
