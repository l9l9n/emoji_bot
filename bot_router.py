from aiogram import Bot, Dispatcher
from bot_utils.hendlers import welcome_massage
from config import TOKEN

bot = Bot(token=TOKEN)

dp = Dispatcher(bot=bot)

dp.register_message_handler(welcome_massage, commands=['start'])