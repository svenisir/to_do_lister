from aiogram_dialog import Dialog
from .windows import start, tasks, category, calendar, calendar_tasks, profile, completed_tasks, settings


main_dialog = Dialog(
    start.window,
    tasks.window,
    category.window,
    calendar.window,
    calendar_tasks.window,
    profile.window,
    completed_tasks.window,
    settings.window
)
