from config import GROUP_ID, ADMINS
from loader import bot,db
from telebot.types import Message,ReplyKeyboardRemove
from keyboards.default import *
from keyboards.inline import *


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    bot.send_message(chat_id,"""Choose the language!""",reply_markup = language_btn())

    db.save_user(user_id, user_name)

