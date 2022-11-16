from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()


TOKEN = '5657161743:AAHc_tle8Ue9AXQX5yv7QwaQHVwyBVPwzDw'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


