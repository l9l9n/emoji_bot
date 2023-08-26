from aiogram import types
from database.manager import CategoryManager,FilmManager
from bot_utils.keyboards import get_catergory_btns
from redis_client import redis_client
from aiogram.dispatcher import FSMContext
from states import UserMessageState



async def welcome_message(message:types.Message):
    text = """
        Привет , я бот для игры в угадай фильм по эмоджи.
        \nЧто бы начать игру, отправь мне сообщение "Start"
    """
    await message.answer(text)
    
    
async def start_game(message:types.Message):
    text = "Выберите категорию игры"
    user_id = message['from'].id
    data = await redis_client.get_user_data(user_id)
    if data:
        await message.answer('Вы уже в игре. Жулаете завершить игру')
    else:
        markup = get_catergory_btns()
        await message.answer(text, reply_markup=markup)

async def finish_game(message: types.Message):
    user_id = message['from'].id
    await redis_client.del_user_data(user_id)
    await message.answer("Game Over")
    await message.answer('Колл-во правильных ответов ')

async def start_category(call: types.CallbackQuery, state: FSMContext):
    user_data = await redis_client.get_user_data(call.message.chat.id)
    if user_data:
        text = """
            У вас уже есть активная игра. Завершите ее чтобы продолжить
    """
    else:
        choice = str(call.data).split('_')[1]
        data ={
            'level_choice':choice,
            'test':'test'
        }
        user_id = call.message.chat.id
        # print(call.message)
        # print(user_id)
        await UserMessageState.answer.set()
        await redis_client.cache_user_data(user_tg_id=user_id,data=data)
        await call.message.answer('Вы выбрали категорию игры,Игра началась')
    


async def get_movie(message:types.Message):
    films = FilmManager().get_films()
    for f in films:
        await message.answer(f"{f.emoji_text}")