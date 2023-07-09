import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BOT_TOKEN')

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Резерв BUBBLY', web_app=WebAppInfo(url='https://rozetka.ua')))
    await message.answer('Привіт', reply_markup=markup)

    


executor.start_polling(dp)




