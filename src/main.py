from aiogram import Bot, Dispatcher
import asyncio
import logging
from aiogram.client.default import DefaultBotProperties
from src.handlers.basic import handle_start_command
from src.handlers.profile import get_user_profile_photos
from src.settings import settings
from src.utils.commands import set_commands
from aiogram.filters import CommandStart
from src.keyboards.callback import process_callback_query


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot ON!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot OFF!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    bot = Bot(token=settings.bots.bot_token, default=DefaultBotProperties(parse_mode='HTML'))

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(handle_start_command, CommandStart())
    dp.callback_query.register(process_callback_query)
    dp.message.register(get_user_profile_photos)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
