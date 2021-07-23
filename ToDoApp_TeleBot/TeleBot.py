# coding: utf-8
import telebot
from libTeleBot import *


TOKEN = '1932491823:AAF2nCsRuctL4kFpb7rMi4NPFzogoC-WejA'
bot = telebot.TeleBot(TOKEN)    # Создание объекта класса ToDoApp_TeleBot


@bot.message_handler(content_types=["text"])
def echo(data):
    list_commands = get_commands()
    command = data.text
    if command in list_commands.keys():
        message = list_commands[command](data, bot)
    else:
        message = 'Неизвестная команда!'

    bot.send_message(data.chat.id, message)


bot.polling(none_stop=True)
