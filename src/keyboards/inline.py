from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Магазин", web_app=WebAppInfo(url="https://highscoreshop.ru")),
         InlineKeyboardButton(text="Отзывы", url="https://t.me/+uVn1rmoT_ygwOTFi")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")]
    ])


def get_help_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Вопрос-ответ", callback_data="qa")],
        [InlineKeyboardButton(text="Связь с менеджером", url="https://t.me/TonyYakim")],
        [InlineKeyboardButton(text="Связь с тех.специалистом", url="https://t.me/highscore_tech")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_main")]
    ])

def get_qa_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="←", callback_data="qa_back"),
        InlineKeyboardButton(text="→", callback_data="qa_next")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_help")]
    ])
