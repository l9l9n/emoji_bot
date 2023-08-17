from aiogram import types


async def welcome_massage(message:types.Message):
    text = """
    Привет, я бот для игры в угадай фильм по эмоджи.
    \nЧто бы начать игру, отправь мне сообщение 'Start'
    """
    await message.answer(text)


