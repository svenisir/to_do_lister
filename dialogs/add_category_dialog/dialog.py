from aiogram_dialog import Dialog

from .windows import input_category, confirm_category

add_category_dialog = Dialog(
    input_category.window,
    confirm_category.window
)
