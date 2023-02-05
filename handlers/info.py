from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from dispatcher import dp
from aiogram import types
from keyboard.inline.keyboard  import Keyboard

Keyboard = Keyboard()

markup = Keyboard.startmenu()


@dp.message_handler(Text(equals='🚨 Инфо'))
@dp.message_handler(Command('info'))
async def on_start_test(message: types.Message):  
    await message.answer('Donate: (ссылка на донат)\nOther Projects: GitHub: https://github.com/ryzeeepython\nПо всем вопросам  - @s_ryzeee', reply_markup= markup)