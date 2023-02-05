from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from dispatcher import dp
from aiogram import types
from states import CallbackOnStart
from scripts.scripts import Main
from keyboard.inline.keyboard  import Keyboard

Keyboard = Keyboard()
db = Main()

markup = Keyboard.whileTest()
table_name = ''


@dp.message_handler(Command('test'))
async def on_start_test(message: types.Message, state:FSMContext): 
    if len(db.get_tests()) != 0:
        tests_markup = Keyboard.tests_markup()
        await message.answer('Выберите тест', reply_markup= tests_markup)
        await CallbackOnStart.Q1.set()
    else:
        await message.answer('Тестов для вас нет')
    
@dp.message_handler(state=CallbackOnStart.Q1)
async def tower(message: types.Message, state: FSMContext):

    answer = message.text
    if answer in db.get_tests():
        global table_name 
        table_name = answer
        if db.check_is_done(message.from_user.id, test_name = answer):
            await message.answer('Вы уже проходили этот тест', reply_markup=types.ReplyKeyboardRemove())

        else:   
            questions = db.get_questions(answer)  # ВВЕСТИ ТАБЛИЦУ ОТКУДА БРАТЬ ВОПРОСЫ 
            question = questions[0]
            await message.answer(question, reply_markup= markup)
            await state.update_data(tg_name=message.from_user.full_name) 
            await state.update_data(user_id= message.from_user.id)
            await state.update_data(test_name = answer)  #ВВЕДИТЕ НАЗАВАНИЕ ЧТОБЫ СОХРАНИТЬ ТЕСТ В БД
            await CallbackOnStart.next()
    else:
        await message.answer('Такого теста нет')

@dp.message_handler(state=CallbackOnStart.Q2)
async def tower(message: types.Message, state: FSMContext):
    questions = db.get_questions(table_name)
    answer = message.text

    if str(answer) != '✅ Завершить':
        await state.update_data(q1=answer)
        if len(questions) >= 2:
            await message.answer(questions[1], reply_markup= markup)
            await CallbackOnStart.next()
        else:
            data = await state.get_data()
            db.save_answers(data)
            await state.finish()
            await message.answer('Спасибо за ответы', reply_markup=types.ReplyKeyboardRemove())
    else:
        data = await state.get_data()
        db.save_answers(data)
        await state.finish()
        await message.answer('Прервано',reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=CallbackOnStart.Q3)
async def tower(message: types.Message, state: FSMContext):
    answer = message.text
    questions = db.get_questions(table_name)
    if str(answer) != '✅ Завершить':
        await state.update_data(q2=answer)
        if len(questions) >= 3:
            await message.answer(questions[2], reply_markup= markup)
            await CallbackOnStart.next()
        else:
            data = await state.get_data()
            db.save_answers(data)
            await state.finish()
            await message.answer('Спасибо за ответы', reply_markup=types.ReplyKeyboardRemove())
    else:
        data = await state.get_data()
        db.save_answers(data)
        await state.finish()
        await message.answer('Спасибо за ответы', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=CallbackOnStart.Q4)
async def tower(message: types.Message, state: FSMContext):
    answer = message.text
    questions = db.get_questions(table_name)
    if str(answer) != '✅ Завершить':
        await state.update_data(q3=answer)
        if len(questions) >= 4:
            await message.answer(questions[3], reply_markup= markup)
            await CallbackOnStart.next()
        else:
            data = await state.get_data()
            db.save_answers(data)
            await state.finish()
            await message.answer('Спасибо за ответы', reply_markup=types.ReplyKeyboardRemove())
    else:
        data = await state.get_data()
        db.save_answers(data)
        await state.finish()
        await message.answer('Спасибо за ответы', reply_markup=types.ReplyKeyboardRemove())




@dp.message_handler(state=CallbackOnStart.Q5)
async def tower(message: types.Message, state: FSMContext):
    answer = message.text
    questions = db.get_questions(table_name)
    if str(answer) != '✅ Завершить':
        await state.update_data(q4=answer)
        if len(questions) >= 5:
            await message.answer(questions[4], reply_markup= markup)
            await CallbackOnStart.next()
        else:
            data = await state.get_data()
            db.save_answers(data)
            await state.finish()
            await message.answer('Спасибо за ответы', reply_markup=types.ReplyKeyboardRemove())
    else:
        data = await state.get_data()
        db.save_answers(data)
        await state.finish()
        await message.answer('Спасибо за ответы', reply_markup=types.ReplyKeyboardRemove())



@dp.message_handler(state=CallbackOnStart.Q6)
async def tower(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(q5=answer)
    data = await state.get_data()
    db.save_answers(data)
    await state.finish()
    await message.answer('Спасибо за ответы', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()



