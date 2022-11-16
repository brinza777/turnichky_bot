from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_start_command = KeyboardButton('/start')

button_monday = KeyboardButton('/Понедельник')
button_tuesday = KeyboardButton('/Вторник')
button_wednesday = KeyboardButton('/Среда')
button_thursday = KeyboardButton('/Четверг')
button_friday = KeyboardButton('/Пятница')
button_saturday = KeyboardButton('/Суббота')
button_sunday = KeyboardButton('/Воскресенье')

kb_start_command = ReplyKeyboardMarkup()

kb_week = ReplyKeyboardMarkup()

kb_start_command.add(button_start_command)
kb_week.row(button_monday, button_tuesday).row(button_wednesday, button_thursday).row(button_friday, button_saturday).add(button_sunday)