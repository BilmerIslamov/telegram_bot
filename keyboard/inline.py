# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def play_bot():
    markup = InlineKeyboardMarkup(row_width=1)
    btn_1 = InlineKeyboardButton("создать фото пость 🖼", callback_data="create_foto_post")
    btn_2 = InlineKeyboardButton("создать видео пость 📹", callback_data="create_video_post")
    markup.add(btn_1, btn_2)
    return markup

def send_photo():
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("отправте фото", callback_data="photo_photo")
    markup.add(btn)
    return markup
def send_video():
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("отправте видео", callback_data="photo_video")
    markup.add(btn)
    return markup

def retry_message():
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("Повторить попытку", callback_data="retry_message")
    markup.add(btn)
    return markup
#
def addition_composition_btn():
    markup = InlineKeyboardMarkup(row_width=1)
    btn_1 = InlineKeyboardButton("хэш-тек", callback_data="hash_tek")
    btn_2 = InlineKeyboardButton("ссылка на сайт", callback_data="website_link")
    btn_3 = InlineKeyboardButton("ссылка на канал", callback_data="channel_link")
    btn_4 = InlineKeyboardButton("ссылка пользователя", callback_data="user_link")
    btn_5 = InlineKeyboardButton("нет, спасибо", callback_data="no_thanks")
    markup.add(btn_1, btn_2, btn_3, btn_4)

    return markup

def generate_website_button_link(link):
    markup = InlineKeyboardMarkup(row_width=1)
    btn_1 = InlineKeyboardButton("website link", url=f"{link}")
    markup.add(btn_1)
    return markup