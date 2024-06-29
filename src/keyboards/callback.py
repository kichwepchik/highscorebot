from aiogram import types
from src.handlers.help import handle_help_command, handle_qa_command, handle_back_to_main, handle_qa_next, handle_qa_back

async def process_callback_query(callback_query: types.CallbackQuery):
    data = callback_query.data
    if data == "help":
        await handle_help_command(callback_query)
    elif data == "qa":
        await handle_qa_command(callback_query)
    elif data == "back_to_main":
        await handle_back_to_main(callback_query)
    elif data == "qa_next":
        await handle_qa_next(callback_query)
    elif data == "qa_back":
        await handle_qa_back(callback_query)
    elif data == "back_to_help":
        await handle_help_command(callback_query)
