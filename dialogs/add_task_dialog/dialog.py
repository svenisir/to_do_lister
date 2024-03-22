from aiogram_dialog import Dialog

from .windows import begin, text

add_task_dialog = Dialog(
    begin.window,
    text.window_input
)
