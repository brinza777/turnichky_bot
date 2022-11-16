from aiogram.utils import executor
from create_bot import dp

from hendlers import working_chat
from data_base import base_workout

working_chat.register_hendlers(dp)

base_workout.sq_start()

executor.start_polling(dp, skip_updates=True)


