from aiogram import executor
from bot_router import dp
from sys import argv
from init_db import create_tables


if __name__ == "__main__":
    data = argv 
    if data[1] == 'migrate':
        create_tables()
        print('Таблицы создались')
    elif data[1] == 'runbot':
        print('Бот запущен')
        executor.start_polling(dp, skip_updates=True)
    else:
        print('Напишите правильную команду!')


