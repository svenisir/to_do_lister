from aiogram import Router

from .dialog import main_dialog


def setup(router: Router) -> None:
    router.include_router(main_dialog)
