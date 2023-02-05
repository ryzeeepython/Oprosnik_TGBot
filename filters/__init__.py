from aiogram import Dispatcher
from .isAdmin import isAdmin

def setup(dp:Dispatcher):
    dp.filters_factory.bind(isAdmin)

    
