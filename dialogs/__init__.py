from aiogram import Dispatcher, Router

from dialogs import main_dialog, add_task_dialog


def setup(dp: Dispatcher) -> None:
    dp.include_router(setup_all_dialogs())


def setup_all_dialogs() -> Router:
    router = Router()

    main_dialog.setup(router)
    add_task_dialog.setup(router)

    return router
