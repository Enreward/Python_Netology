# coding: utf-8
import telebot
import random
import datetime as dt
from libTeleBot import *


TOKEN = '1932491823:AAF2nCsRuctL4kFpb7rMi4NPFzogoC-WejA'
bot = telebot.TeleBot(TOKEN)    # Создание объекта класса ToDoApp_TeleBot
list_tasks = {}
random_tasks = [
    'Прочесть одну главу книги по программированию',
    'Отжаться 50 раз',
    'Приготовить лазанью',
    'Пойти в бассей',
    'Пробежать 5 км'
]


@bot.message_handler(commands=['Добавить'])
def get_date(message):
    msg = bot.reply_to(message, "Введите дату: ")
    bot.register_next_step_handler(msg, get_task)

def get_task(message):
    msg = bot.reply_to(message, "Введите задачу: ")
    date = message.text.lower()
    bot.register_next_step_handler(msg, add_task, date)


def add_task(message, *args):
    date = args[0]
    task = message.text
    if date in list_tasks:
        list_tasks[date].append(task)
    else:
        list_tasks[date] = [task]


@bot.message_handler(commands=['Дела'])
def get_date(message):
    if not list_tasks:
        text = 'Список дел пуст!'
        bot.send_message(message.chat.id, text)
        return
    msg = bot.reply_to(message, "Введите дату: ")
    bot.register_next_step_handler(msg, print_tasks)


def print_tasks(message):
    date = message.text.lower()
    if date == "сегодня":
        date = dt.datetime.now().strftime("%d.%m.%Y")

    text = f'На {date}:'
    for _task in list_tasks[date]:
        text += f'\n"{_task}"'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['?'])
def add_random_task(message):
    message.text = random.choice(random_tasks)
    date = dt.datetime.now().strftime("%d.%m.%Y")

    add_task(message, date)


@bot.message_handler(commands=['Помощь'])
def print_help(message):
    text = '''
    Доступные команды:
    Помощь - выводит список команд
    Добавить - добавляет задание
    Дела - выводит список дел
    Выход - заканчивает работу программы
    '''
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
