from data.loader import bot
from telebot.types import Message


@bot.message_handler(commands=['language'])
def start_commands(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Hello Bro commands language")