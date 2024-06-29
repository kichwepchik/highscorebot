from aiogram import types
from aiogram.exceptions import TelegramForbiddenError
from src.database.db_connect import insert_user
from src.keyboards.inline import get_main_menu


async def handle_start_command(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    response = insert_user(user_id, username)
    try:
        username = message.from_user.username
        await message.answer(f"Добро пожаловать, {username}, в наш магазин", reply_markup=get_main_menu())
    except TelegramForbiddenError:
        print(
            f"Не удалось отправить сообщение пользователю {message.from_user.id}: бот был заблокирован пользователем.")
