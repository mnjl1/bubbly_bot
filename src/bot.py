import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BOT_TOKEN')

bot = Bot(token)
dp = Dispatcher(bot)

WEBAPP_URL = 'https://mnjl1.github.io/bubbly_bot/'

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Резерв BUBBLY', web_app=WebAppInfo(url=WEBAPP_URL)))
    await message.answer('Привіт', reply_markup=markup)

    

executor.start_polling(dp)




