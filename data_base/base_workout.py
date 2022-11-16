import sqlite3 as sq
from create_bot import bot


def sq_start():
    global cur, base
    base = sq.connect('workout.db')
    cur = base.cursor()
    if base:
        print('Data base is entered')
    base.commit()

async def sq_read(message):
    #print(day)
    day = message.text[1:]
    workout_this_day = cur.execute('SELECT img, description FROM workout WHERE day == ?', (day,)).fetchone()
    #print(workout_this_day)
    await bot.send_photo(message.from_user.id, workout_this_day[0], workout_this_day[1])
