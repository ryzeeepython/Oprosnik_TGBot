from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from dispatcher import dp
from aiogram import types

from keyboard.inline.keyboard  import Keyboard

Keyboard = Keyboard()
markup = Keyboard.startmenu()

@dp.message_handler(Command('start'))
async def on_start_test(message: types.Message):

    await message.answer('Привет, ' + str(message.from_user.full_name) + '\nЭто бот - опросник', reply_markup= markup)