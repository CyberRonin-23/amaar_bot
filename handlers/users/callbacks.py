from telebot.types import CallbackQuery, ReplyKeyboardRemove
from keyboards.default import *
from keyboards.inline import *
from loader import bot, db


@bot.callback_query_handler(func=lambda call:call.data.startswith("recontact_"))
def reaction_contact_inline(call: CallbackQuery):
    chat_id = call.message.chat.id
    if "eng" in call.data:
        bot.send_message(chat_id, "Send your number so that our operators can contact you.",
                     reply_markup=send_contact("eng"))
    elif "uz" in call.data:
        bot.send_message(chat_id, "Operatorlar siz bilan bog'lanishlari uchun raqamingizni yuboring.",
                         reply_markup=send_contact("uz"))
    else :
        bot.send_message(chat_id, "Отправьте свой номер, чтобы операторы могли с вами связаться.",
                         reply_markup=send_contact("ru"))
    bot.delete_message(chat_id, call.message.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("recontacted:"))
def handle_recontacted_callback(call: CallbackQuery):
    user_id = call.data.split("|")[1]
    phone_num = call.data.split("|")[2]
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f"""Mijoz TelegramID: {user_id}
Mijozning Username: @{call.from_user.username if call.from_user.username else "No username"}
Mijozning kontakti: {phone_num}


Status: Bog'lanildi✅"""
    )


"""choose the lang"""


@bot.callback_query_handler(func=lambda call: call.data == "lang_eng")
def lang_eng_menu(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_name = call.from_user.first_name
    user_id = call.from_user.id
    db.edit_language("eng",user_id)
    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, f"Hi {user_name}, welcome to the telegram bot of the Amaar uz!",
                     reply_markup=main_menu_eng())


@bot.callback_query_handler(func=lambda call: call.data == "lang_ru")
def lang_ru_menu(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_name = call.from_user.first_name
    user_id = call.from_user.id
    db.edit_language("ru", user_id)
    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, f"Привет {user_name}, добро пожаловать в телеграм-бот Amaar uz!",
                     reply_markup=main_menu_ru())


@bot.callback_query_handler(func=lambda call: call.data == "lang_uz")
def lang_uz_menu(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_name = call.from_user.first_name
    user_id = call.from_user.id
    db.edit_language("uz", user_id)
    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, f"Salom {user_name}, Amaar uz loyihasining telegram botiga xush kelibsiz!",
                     reply_markup=main_menu_uz())


"""end of the choose the lang"""
