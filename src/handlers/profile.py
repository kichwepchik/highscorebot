from aiogram import Bot, types

async def get_user_profile_photos(message: types.Message, bot: Bot):
    user_id = message.from_user.id

    try:
        # Получение фотографий профиля пользователя
        user_profile_photos = await bot.get_user_profile_photos(user_id)

        if user_profile_photos.total_count > 0:
            photo = user_profile_photos.photos[0][-1]  # Получаем фотографию с наибольшим размером
            file_info = await bot.get_file(photo.file_id)
            file_path = file_info.file_path
            file_url = f'https://api.telegram.org/file/bot{bot.token}/{file_path}'

            await message.reply(f"Ваше фото профиля доступно по ссылке: {file_url}")
        else:
            await message.reply("У вас нет фотографий профиля.")
    except Exception as e:
        await message.reply(f"Произошла ошибка: {str(e)}")
