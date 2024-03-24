from aiogram_dialog import Dialog

from .windows import begin, text, category, date_task, subtasks, delete_subtasks

add_task_dialog = Dialog(
    begin.window,
    text.window,
    category.window,
    date_task.window,
    subtasks.window,
    delete_subtasks.window
)
