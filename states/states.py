from aiogram.fsm.state import State, StatesGroup


class MainSG(StatesGroup):
    start = State()
    tasks = State()
    choose_category = State()
    delete_category = State()
    calendar = State()
    calendar_tasks = State()
    profile = State()
    complete_tasks = State()
    settings = State()


class AddTaskSG(StatesGroup):
    begin = State()
    text = State()
    choose_category = State()
    data_task = State()
    subtasks_input = State()
    subtasks_delete = State()
    pattern = State()


class AddCategorySG(StatesGroup):
    category_input = State()
    category_confirm = State()


class EditTaskSG(StatesGroup):
    begin = State()
    egit_text = State()
    edit_category = State()
    edit_date_task = State()
    edit_subtasks = State()
    edit_time_repeat = State()
    edit_notes = State()
