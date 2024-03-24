from aiogram_dialog import Dialog

from .windows import begin, text, category

add_task_dialog = Dialog(
    begin.window,
    text.window,
    category.window
)
