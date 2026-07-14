import asyncio
import aiosqlite
from datetime import datetime
from pathlib import Path

PATH_DB = Path(__file__).parent.parent / 'DATA' / 'user_notes.db'
my_time = datetime.now().strftime("%d.%m.%Y")


async def create_table():
    async with aiosqlite.connect('../DATA/user.db') as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id BIGINT, user_name TEXT)")


async def add_column():
    async with aiosqlite.connect('../DATA/user.db') as db:
        await db.execute("ALTER TABLE users ADD user_surname TEXT")


async def cmd_start_db(us_id, us_name, us_surname="None"):
    async with aiosqlite.connect('DATA/user.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE user_id == ?", (us_id,))
        data = await cursor.fetchone()
        if not data:
            await db.execute("INSERT INTO users (user_id, user_name, user_surname) VALUES (?, ?, ?)",
                             (us_id, us_name, us_surname))
            await db.commit()


async def db_update(us_id, us_surname):
    async with aiosqlite.connect('DATA/user.db') as db:
        await db.execute("UPDATE users SET user_surname = ? WHERE user_id = ?", (us_surname, us_id))
        await db.commit()


async def db_check(us_id, us_surname):
    async with aiosqlite.connect('DATA/user.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE user_id == ? AND user_surname == ?", (us_id, us_surname))
        return await cursor.fetchone()


async def db_surname_check(us_id):
    async with aiosqlite.connect('DATA/user.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE user_id == ?", (us_id,))
        return list(await cursor.fetchone())[3]


async def db_select():
    async with aiosqlite.connect('DATA/user.db') as db:
        cursor = await db.execute("SELECT * FROM users")
        users = await cursor.fetchall()

        return [(el[1], el[2], el[3]) for el in users]


async def db_delete(del_id):
    async with aiosqlite.connect('DATA/user.db') as db:
        await db.execute("DELETE FROM users WHERE user_id = ?", (del_id,))
        await db.commit()


# -------------------------------- notes -------------------------------------

async def add_note(tg_id, note_name, note_text=None, note_type=None, file_id=None):
    async with aiosqlite.connect(PATH_DB) as db:
        await db.execute("INSERT INTO notes (tg_id, note_name, note_text, note_data, note_type, file_id) "
                         "VALUES (?, ?, ?, ?, ?, ?)",
                         (tg_id, note_name, note_text, my_time, note_type, file_id))
        await db.commit()


async def update_note_name(tg_id, new_name, note_name, note_text):
    async with aiosqlite.connect(PATH_DB) as db:
        await db.execute("UPDATE notes SET note_name = ? WHERE tg_id = ? AND note_name = ? AND note_text = ?",
                         (new_name, tg_id, note_name, note_text))
        await db.commit()


async def update_note_text(tg_id, new_text, note_name, note_text):
    async with aiosqlite.connect(PATH_DB) as db:
        await db.execute("UPDATE notes SET note_text = ? WHERE tg_id = ? AND note_name = ? AND note_text = ?",
                         (new_text, tg_id, note_name, note_text))
        await db.commit()


async def select_note(tg_id):
    async with aiosqlite.connect(PATH_DB) as db:
        cursor = await db.execute(
            "SELECT note_name, note_text, note_type, file_id FROM notes WHERE tg_id == ?",
            (tg_id,))
        users = await cursor.fetchall()
        data_dict = {}
        for num, el in enumerate(users, 1):
            data_dict[num] = [el[0], el[1], el[2], el[3]]
        return data_dict


async def note_delete(tg_id, note_name, note_text):
    async with aiosqlite.connect(PATH_DB) as db:
        await db.execute("DELETE FROM notes WHERE tg_id = ? AND note_name = ? AND note_text = ?",
                         (tg_id, note_name, note_text))
        await db.commit()


async def edit_note_text(tg_id, number):
    async with aiosqlite.connect(PATH_DB) as db:
        cursor = await db.execute(
            "SELECT note_text, note_data FROM notes WHERE tg_id == ? ORDER BY note_data ASC",
            (tg_id,))
        users = await cursor.fetchall()
        data_dict = {}
        for num, el in enumerate(users, 1):
            data_dict[num] = [el[0], el[1]]
        return data_dict[number]

if __name__ == '__main__':
    pass
    # asyncio.run(create_table())
    # asyncio.run(add_column())

    # asyncio.run(db_update(428030603, 'Admin'))
    print(asyncio.run(db_select()))
    # print(asyncio.run(db_check(5194830049, 'Ивано')))
