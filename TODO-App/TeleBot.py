# coding: utf-8
import telebot
from libTeleBot import *

LIST_COMMANDS = get_commands()

TOKEN = '1932491823:AAF2nCsRuctL4kFpb7rMi4NPFzogoC-WejA'

bot = telebot.TeleBot(TOKEN)    # Создание объекта класса TeleBot


@bot.message_handler(content_types=["text"])
def echo(command):
    if command in LIST_COMMANDS.keys():
        message = LIST_COMMANDS[command]()
    else:
        message = 'Неизвестная команда!'

    bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.polling(none_stop=False)
