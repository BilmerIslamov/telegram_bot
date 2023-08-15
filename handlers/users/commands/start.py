from data.loader import bot
from telebot.types import Message
from keyboard.inline import play_bot
import requests

@bot.message_handler(commands=['start'])
def start_commands(message: Message):
    chat_id = message.chat.id
    telegram_id = message.from_user.id

    bot.send_message(chat_id, f"Привет Билмер", reply_markup=play_bot())



