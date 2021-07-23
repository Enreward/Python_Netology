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


def get_commands():
    return {
        'Помощь': print_help,
        'Добавить': add_task,
        'Дела': print_tasks,
        'Что поделать?': add_random_task,
    }


def print_tasks(*arg, _date=''):
    _data = arg[0]
    _bot = arg[1]
    text = ''

    @_bot.message_handler(content_types=["text"])
    def get_date(_msg_date):
        nonlocal _date
        _date = str(datetime.datetime.strptime(_msg_date.text, "%d.%m.%Y").strftime("%d.%m.%Y"))

        nonlocal text
        text = f'На {_date}:'
        for _task in list_tasks[_date]:
            text += f'\n"{_task}"'

    if not list_tasks:
        return 'Список дел пуст!'

    if not _date:
        msg_date = _bot.reply_to(_data, "Введите дату: ")
        _bot.register_next_step_handler(msg_date, get_date)

    if _date not in list_tasks:
        return f'На {_date} дел нет.'


    return text


def add_task(*arg, _date='', _task=''):
    _data = arg[0]
    _bot = arg[1]

    @_bot.message_handler(content_types=["text"])
    def get_date(_msg_date):
        nonlocal _date
        _date = str(datetime.datetime.strptime(_msg_date.text, "%d.%m.%Y").strftime("%d.%m.%Y"))
        msg_task = _bot.reply_to(_msg_date, "Введите задачу: ")
        _bot.register_next_step_handler(msg_task, get_task)

    @_bot.message_handler(content_types=["text"])
    def get_task(_msg_task):
        nonlocal _task
        _task = _msg_task.text
        if _date in list_tasks:
            list_tasks[_date].append(_task)
        else:
            list_tasks[_date] = [_task]

        _bot.send_message(_data.chat.id, f"Задание \"{_task}\" добавлено на \"{_date}\".")

    if not _date:
        msg_date = _bot.reply_to(_data, "Введите дату: ")
        _bot.register_next_step_handler(msg_date, get_date)


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
