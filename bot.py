from data.loader import bot

from handlers.users.commands import start
from handlers.users.commands import help
from handlers.users.commands import main
from handlers.users.commands import language

if __name__ == "__main__":
    bot.infinity_polling()

