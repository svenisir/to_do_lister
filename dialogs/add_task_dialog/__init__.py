from aiogram import Router

from .dialog import add_task_dialog


def setup(router: Router) -> None:
    router.include_router(add_task_dialog)