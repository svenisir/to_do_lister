import logging

from aiogram_dialog import DialogManager, StartMode, ShowMode

from states.states import MainSG

logger = logging.getLogger(__name__)


async def on_unknown_intent(event, dialog_manager: DialogManager):
    logger.error('Restarting dialog: %s', event.exeption)
    await dialog_manager.start(
        state=MainSG.start, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND
    )
