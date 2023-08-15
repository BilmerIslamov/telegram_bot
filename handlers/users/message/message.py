from data.loader import bot
from telebot.types import Message, CallbackQuery
from keyboard.inline import *

# import telegram
# @bot.callback_query_handler(func=lambda call: call.data == "play")
# def send_message_channel(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     # channel_id = "-1001834752320"
#     # bot.send_message(channel_id,  "hello channel")
#     answer =  bot.send_message(chat_id, f"Отправить фото")
#     bot.register_next_step_handler(answer, answer_send_message)





# @bot.callback_query_handler(func=lambda call: call.data == "")
# def create_post(call: CallbackQuery):
#     pass

# @bot.message_handler(content_types=['video', 'photo'])
# def answer_send_message(message: Message):
#     chat_id = message.chat.id
#     from_user_id = message.from_user.id
#     if message.photo:
#         bot.send_message(chat_id,        f"Отправить фото", reply_markup=send_photo())
#     elif message.video:
#         bot.send_message(chat_id,      f"отправлять видео", reply_markup=send_video())
#     elif message.text:
#         bot.send_message(chat_id,       f"Не отправлять текст", reply_markup=retry_message())
#     elif message.voice:
#         bot.send_message(chat_id,      f"Не отправлять голоса", reply_markup=retry_message())
#     elif message.sticker:
#         bot.send_message(chat_id,    f"Не отправлять наклейки", reply_markup=retry_message())
#     elif message.animation:
#         bot.send_message(chat_id,  f"Не отправлять анимации", reply_markup=retry_message())
#     elif message.audio:
#         bot.send_message(chat_id,      f"Не отправлять аудио", reply_markup=retry_message())
#     elif message.document:
#         bot.send_message(chat_id,   f"Не отправлять документа", reply_markup=retry_message())
#     elif message.video_note:
#         bot.send_message(chat_id, f"Не отправлять видео_примечание", reply_markup=retry_message())
#     else:
#         bot.send_message(chat_id,                    f"В отправленном сообщении есть ошибка /help", )



