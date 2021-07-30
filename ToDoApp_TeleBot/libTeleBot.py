# coding: utf-8
import random
import datetime


list_tasks = {}
random_tasks = [
    'Прочесть одну главу книги по программированию',
    'Отжаться 50 раз',
    'Приготовить лазанью',
    'Пойти в бассей',
    'Пробежать 5 км'
]


def command_unknown(bot, context):
    bot.message.reply_text(bot.message.text)
    return bot.message.text


def hello(bot, context):
    bot.message.reply_text('hello')
    return bot.message.text


def get_commands():
    return {
        'start': hello
    }
#
#
# def get_date():
#     _date = str(datetime.datetime.strptime(_msg_date.text, "%d.%m.%Y").strftime("%d.%m.%Y"))
#
#
# def print_tasks(*arg, _date=''):
#     _data = arg[0]
#     _bot = arg[1]
#     text = ''
#
#     text = f'На {_date}:'
#     for _task in list_tasks[_date]:
#         text += f'\n"{_task}"'
#
#     if not list_tasks:
#         return 'Список дел пуст!'
#
#     if not _date:
#         msg_date = _bot.reply_to(_data, "Введите дату: ")
#         _bot.register_next_step_handler(msg_date, get_date)
#
#     if _date not in list_tasks:
#         return f'На {_date} дел нет.'
#
#     return text
#
#
# def get_date(_msg_date):
#     nonlocal _date
#     _date = str(datetime.datetime.strptime(_msg_date.text, "%d.%m.%Y").strftime("%d.%m.%Y"))
#     msg_task = _bot.reply_to(_msg_date, "Введите задачу: ")
#     _bot.register_next_step_handler(msg_task, get_task)
#
#
# def get_task(_msg_task):
#     nonlocal _task
#     _task = _msg_task.text
#     if _date in list_tasks:
#         list_tasks[_date].append(_task)
#     else:
#         list_tasks[_date] = [_task]
#
#
# def add_task(*arg, _date='', _task=''):
#     _data = arg[0]
#     _bot = arg[1]
#
#         _bot.send_message(_data.chat.id, f"Задание \"{_task}\" добавлено на \"{_date}\".")
#
#     if not _date:
#         msg_date = _bot.reply_to(_data, "Введите дату: ")
#         _bot.register_next_step_handler(msg_date, get_date)
#
#
# def add_random_task(*arg):
#     random_task = random.choice(random_tasks)
#     add_task(_date='Сегодня', _task=random_task)
#     return print_tasks(_date='Сегодня')
#
#
# def print_help(*arg):
#     help_text = '''
# Доступные команды:
# Помощь - выводит список команд
# Добавить - добавляет задание
# Дела - выводит список дел
# Выход - заканчивает работу программы
# '''
#     return help_text
