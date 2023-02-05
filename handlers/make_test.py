from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command


from dispatcher import dp
from aiogram import types
from states.make_test_states import CallbackMakeTest
from filters import isAdmin
from scripts.scripts import Main
from keyboard.inline.keyboard  import Keyboard

Keyboard = Keyboard()
markup = Keyboard.whileTest()
db = Main()


@dp.message_handler(isAdmin(), Command('maketest'))
async def maketest(message: types.Message):

    await message.answer('Введите название теста в бд: ', reply_markup= markup)
    await CallbackMakeTest.Q1.set()

@dp.message_handler(state=CallbackMakeTest.Q1)
async def tower(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '✅ Завершить':
        await state.finish()
        await message.answer('Прервано', reply_markup=types.ReplyKeyboardRemove())
    else:
        await state.update_data(table_name=answer)
        await message.answer('Введите вопрос: ')
        await CallbackMakeTest.next()


@dp.message_handler(state=CallbackMakeTest.Q2)
async def tower(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(q1=answer)
    data = await state.get_data()
    db.save_questions(data, message.from_user.id)
    await state.finish()
    await message.answer('Вопрос успешно добавлен', reply_markup=types.ReplyKeyboardRemove())





