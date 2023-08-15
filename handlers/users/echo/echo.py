from data.loader import bot
from telebot.types import Message

@bot.message_handler(content_types=['text'])
def text_copy_send_message(message: Message):
    chat_id = message.from_user.id
    bot.copy_message(chat_id, chat_id, message.message_id)
    pass