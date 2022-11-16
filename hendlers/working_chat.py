from aiogram import types, Dispatcher
from create_bot import bot
from keyboards.keyboard_for_working_chat import kb_week
from data_base.base_workout import sq_read


async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выбирай день недели и начинай фигачить!',reply_markup=kb_week)

async def get_workout_for_monday(message: types.Message):
    await sq_read(message)

async def get_workout_for_tuesday(message: types.Message):
    await sq_read(message)

async def get_workout_for_wednesday(message: types.Message):
    await sq_read(message)

async def get_workout_for_thursday(message: types.Message):
    await sq_read(message)

async def get_workout_for_friday(message: types.Message):
    await sq_read(message)

async def get_workout_for_saturday(message: types.Message):
    await sq_read(message)

async def get_workout_for_sunday(message: types.Message):
    await sq_read(message)


def register_hendlers(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(get_workout_for_monday, commands=['Понедельник'])
    dp.register_message_handler(get_workout_for_tuesday, commands=['Вторник'])
    dp.register_message_handler(get_workout_for_wednesday, commands=['Среда'])
    dp.register_message_handler(get_workout_for_thursday, commands=['Четверг'])
    dp.register_message_handler(get_workout_for_friday, commands=['Пятница'])
    dp.register_message_handler(get_workout_for_saturday, commands=['Суббота'])
    dp.register_message_handler(get_workout_for_sunday, commands=['Воскресенье'])
