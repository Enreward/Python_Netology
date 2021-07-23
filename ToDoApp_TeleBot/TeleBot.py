# coding: utf-8
import telebot
import random
import datetime
# from TeleBot import *


list_tasks = {}
random_tasks = [
    'Прочесть одну главу книги по программированию',
    'Отжаться 50 раз',
    'Приготовить лазанью',
    'Пойти в бассей',
    'Пробежать 5 км'
]


def get_commands():
    return {
        'Помощь': print_help,
        'Добавить': add_task,
        'Дела': print_tasks,
        'Что поделать?': add_random_task,
    }


def print_tasks(*arg, _date=''):
    if not list_tasks:
        return 'Список дел пуст!'

    # while not _date:
    #     _date = get_date

    if _date not in list_tasks:
        return f'На {_date} дел нет.'

    text = f'На {_date}:'
    for _task in list_tasks[_date]:
        text += f'\n"{_task}"'
    return text


def add_task(*arg, _date='', _task=''):
    _data = arg[0]
    if not _date:
        arg[1].send_message(_data.chat.id, "Введите дату: ")
        _date = get_date()
        arg[1].send_message(_data.chat.id, "Введите задачу: ")
        _task = get_task()
    if _date in list_tasks:
        list_tasks[_date].append(_task)
    else:
        list_tasks[_date] = [_task]
    return 'Задание добавлено.'


def add_random_task(*arg):
    random_task = random.choice(random_tasks)
    add_task(_date='Сегодня', _task=random_task)
    return print_tasks(_date='Сегодня')


def print_help(*arg):
    help_text = '''
Доступные команды:
Помощь - выводит список команд
Добавить - добавляет задание
Дела - выводит список дел
Выход - заканчивает работу программы
'''
    return help_text


TOKEN = '1932491823:AAF2nCsRuctL4kFpb7rMi4NPFzogoC-WejA'
bot = telebot.TeleBot(TOKEN)    # Создание объекта класса ToDoApp_TeleBot


@bot.message_handler(content_types=["text"])
def get_date(_data):
    date = datetime.datetime.strptime(_data.text, "%d.%m.%Y")
    return date


@bot.message_handler(content_types=["text"])
def get_task(_data):
    return _data.text


@bot.message_handler(content_types=["text"])
def echo(data):
    list_commands = get_commands()
    command = data.text
    if command in list_commands.keys():
        message = list_commands[command](data, bot)
    else:
        message = 'Неизвестная команда!'

    bot.send_message(data.chat.id, message)


bot.polling(none_stop=False)
