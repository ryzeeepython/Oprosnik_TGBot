
from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
import config
from aiogram.dispatcher.handler import CancelHandler
from dispatcher import dp, bot

class isAdmin(BoundFilter):

    async def check(self, message: types.Message):
        for i in config.Admins:
            if str(i) == str(message.from_user.id):
                return True
        return False
        

