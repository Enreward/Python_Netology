# coding: utf-8
from libTeleBot import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = '1932491823:AAF2nCsRuctL4kFpb7rMi4NPFzogoC-WejA'


def main():
    list_commands = get_commands()
    bot = Updater(TOKEN, use_context=True)
    # Диспетчер сообщений
    dp = bot.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, command_unknown))
    dp.add_handler(CommandHandler(dp.text, list_commands[dp.context.message.text]))
    pass
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
