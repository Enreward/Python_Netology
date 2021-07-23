# coding: utf-8
import telebot

# TOKEN = '1932491823:AAF2nCsRuctL4kFpb7rMi4NPFzogoC-WejA'

bot = telebot.TeleBot(TOKEN)    # Создание объекта класса ToDoApp_TeleBot


@bot.message_handler(content_types=["text"])
def echo(message):
    if message.text in ['Игорь']:
        answer = 'Ба! Знакомые все лица!'
    else:
        answer = message.text
    bot.send_message(message.chat.id, answer)


if __name__ == "__main__":
    bot.polling(none_stop=False)
