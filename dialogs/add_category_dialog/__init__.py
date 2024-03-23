from aiogram import Router

from .dialog import add_category_dialog


def setup(router: Router) -> None:
    router.include_router(add_category_dialog)
