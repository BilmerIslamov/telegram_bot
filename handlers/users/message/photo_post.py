from data.loader import *
from telebot.types import *
from keyboard.inline import *
from telegram.constants import ParseMode

@bot.callback_query_handler(func=lambda call: call.data == "create_foto_post")
def create_foto_post(call: CallbackQuery):

    present_id = call.message.chat.id
    user_id = call.from_user.id
    answer = bot.send_message(present_id, f"Отправте фото")
    bot.register_next_step_handler(answer, create_foto_post_answer)


@bot.message_handler(content_types=['photo'])
def create_foto_post_answer(message: Message):
    present_id = message.chat.id
    user_id = message.from_user.id

    if message.photo:
        answer_text = bot.send_message(present_id, f"Хорошо 😄\n" f"Введите любой текст 🫠🫠")
        bot.register_next_step_handler(answer_text, create_text_answer)
    else:
        bot.send_message(present_id, f"у тебя есть еще один шанс 🙃")
        bot.send_message(present_id, f"Отправте фото")





@bot.message_handler(content_types=['text'])
def create_text_answer(message: Message):
    present_id = message.chat.id
    user_id = message.from_user.id
    if message.text:
        add_text = bot.send_message(present_id, f"Хорошо 😄\n" f"Есть что добавить или нет", reply_markup=addition_composition_btn())
        bot.register_next_step_handler(add_text, general_message)
    else:
        bot.send_message(present_id, f"у тебя есть еще один шанс 🙃")
        bot.send_message(present_id, f"Отправте текст")




@bot.callback_query_handler(func=lambda call: call.data == "hash_tek")
def add_hash_tek(call: CallbackQuery):
    present_id = call.message.chat.id
    user_id = call.from_user.id
    answer = bot.send_message(present_id, f"Напишите несколько примеров, \n" f"которые соответствуют названию хэш-тек.")
    bot.register_next_step_handler(answer, check_hash_tec)
def check_hash_tec(message: Message):
    present_id = message.chat.id
    user_id = message.from_user.id
    hash_tek_list = message.text.split(" ")
    hash_tek = ["#" + h for h in hash_tek_list]
    hash_tek_plus = " ".join(hash_tek)
    bot.send_message(present_id, hash_tek_plus)
# print(hash_tek_plus)



@bot.callback_query_handler(func=lambda call: call.data == "website_link")
def add_website_link(call: CallbackQuery):
    present_id = call.message.chat.id
    user_id = call.from_user.id
    answer = bot.send_message(present_id, f"Отправте ссылку на веб-сайт")
    bot.register_next_step_handler(answer, answer_website_link )

def answer_website_link(message: Message):
    present_id = message.chat.id
    user_id = message.from_user.id
    link = message.text
    id_blog = "800094041"
    bot.send_message(present_id, text=f"""<b>Website link
===============================</b>""", parse_mode=ParseMode.HTML,
                     reply_markup=generate_website_button_link(link))






@bot.callback_query_handler(func=lambda call: call.data == "channel_link")
def add_user_link(call: CallbackQuery):
    present_id = call.message.chat.id
    user_id = call.from_user.id
    answer = bot.send_message(present_id, f"Отправте имя пользователя")
    bot.register_next_step_handler(answer, answer_user_link)

def answer_user_link(message: Message):
    present_id = message.chat.id
    user_id = message.from_user.id
    user_link = message.text
    if user_link[0] == "@":
        minus_message = user_link[0] - "@"
        # print(user_link[0])
        try:
            message_sender = "https://t.me/" + user_link
            bot.send_message(present_id, message_sender)
        except:
            bot.send_message(present_id, "Пользователь не найден")
    else:
        message_sender = "https://t.me/" + user_link
        bot.send_message(present_id, message_sender)
    pass


# @bot.callback_query_handler(func=lambda call: call.data == "user_link")



















@bot.callback_query_handler(func=lambda call: call.data == "no_thanks")
def general_message(message: Message):
    pass