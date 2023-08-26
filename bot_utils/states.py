from aiogram.dispatcher.filters.state import StatesGroup, State


class UserMessageState(StatesGroup):
    answer = State()
    film_text = State()