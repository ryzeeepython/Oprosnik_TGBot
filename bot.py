from aiogram import executor
from dispatcher import dp
import handlers

from utils.Set_bot_commands import set_default_commands


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)