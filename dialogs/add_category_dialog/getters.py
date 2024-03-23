from aiogram_dialog import DialogManager


async def get_category_name(dialog_manager: DialogManager, **kwargs):
    return {'categ_name': dialog_manager.dialog_data['category']}
