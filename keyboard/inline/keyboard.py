#from aiogram.types import ReplyKeyboardMarkup
from aiogram import types
from scripts.scripts import Main

db = Main()

class Keyboard:
    def whileTest(self):
        list_button_name = ['✅ Завершить']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
        keyboard.add(*list_button_name)

        return keyboard

    def startmenu(self):
        list_button_name = ['❗️ Начать тест', '🚨 Инфо']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
        keyboard.add(*list_button_name)

        return keyboard

    def tests_markup(self):
        tests = db.get_tests()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
        keyboard.add(*tests)
        return keyboard


