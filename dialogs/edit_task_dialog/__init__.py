from aiogram import Router

from .dialog import edit_task_dialog


def setup(router: Router) -> None:
    router.include_router(edit_task_dialog)
