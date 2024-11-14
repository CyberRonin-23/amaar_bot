from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot
def platform_btn():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.row(InlineKeyboardButton("Android",url="https://play.google.com/store/apps/details?id=com.ats.amaar"),
               InlineKeyboardButton("iOS",url = "https://apps.apple.com/us/app/amaar-plus/id6736830527"))
    markup.row(InlineKeyboardButton("Website",url="https://amaar.uz/"))
    return markup

def cabinet_btn_inline():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Operator bilan bog'lanish📞",callback_data="recontact_uz"))
    markup.add(InlineKeyboardButton("Kabinetga o'tish💼",url="https://amaar.uz/auth/login"))
    return markup

def cabinet_btn_inline_eng():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Contact the operator📞",callback_data="recontact_eng"))
    markup.add(InlineKeyboardButton("Personal cabinet💼",url="https://amaar.uz/auth/login"))
    return markup

def cabinet_btn_inline_ru():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Связаться с оператором📞",callback_data="recontact_ru"))
    markup.add(InlineKeyboardButton("Личный кабинет💼",url="https://amaar.uz/auth/login"))
    return markup

def language_btn():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🇺🇸",callback_data="lang_eng"),InlineKeyboardButton("🇺🇿",callback_data="lang_uz"),
               InlineKeyboardButton("🇷🇺",callback_data="lang_ru"))
    return markup

