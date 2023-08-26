from aiogram import Bot, Dispatcher
from bot_utils.hendlers import *
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2


redis_storage = RedisStorage2(host='localhost', port=6379)
bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=MemoryStorage())

dp.register_message_handler(welcome_message,commands=['start'])
# dp.register_message_handler(get_movie,commands=["movie"])
dp.register_message_handler(start_game, commands=['start_game'])
dp.register_message_handler(finish_game, commands=['finish_game'])
dp.register_message_handler(send_question, state=UserMessageState.answer)
dp.register_callback_query_handler(
    start_category,
    lambda c: str(c.data).startswith('category_'))
