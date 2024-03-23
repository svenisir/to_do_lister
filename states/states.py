from aiogram.fsm.state import State, StatesGroup


class MainSG(StatesGroup):
    start = State()
    tasks = State()
    choose_category = State()
    calendar = State()
    calendar_tasks = State()
    profile = State()
    complete_tasks = State()
    settings = State()


class AddTaskSG(StatesGroup):
    begin = State()
    text = State()
    data_task = State()
    subtasks = State()
    pattern = State()


class AddCategorySG(StatesGroup):
    category_input = State()
    category_confirm = State()
