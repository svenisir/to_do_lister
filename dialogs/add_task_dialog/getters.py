from aiogram_dialog import DialogManager


async def get_task_params(dialog_manager: DialogManager, **kwargs):
    params = dialog_manager.dialog_data['task'] = dialog_manager.dialog_data.get('task', {})

    if not params.get('text'):
        params['text'] = 'Вы пока не добавили текста задачи'

    if not params.get('category'):
        params['category'] = dialog_manager.start_data.get('category', 'Все')

    if not params.get('date_task'):
        params['date_task'] = dialog_manager.start_data['date_task']

    if not params.get('subtasks'):
        params['subtasks'] = 'Вы не добавили подзадачи'

    # dialog_manager.dialog_data['task'] = params

    return params
