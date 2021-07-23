# coding: utf-8
import random


list_tasks = {}
random_tasks = [
    'Прочесть одну главу книги по программированию',
    'Отжаться 50 раз',
    'Приготовить лазанью',
    'Пойти в бассей',
    'Пробежать 5 км'
]


def input_date():
    return input("Введите дату: ")


def input_task():
    return input("Введите задачу: ")


def input_command():
    return input("Введите команду: ")


def get_commands():
    return {
        'Помощь': print_help,
        'Добавить': add_task,
        'Дела': print_tasks,
        'Что поделать?': add_random_task,
        'Выход': exit_app
    }


def print_tasks(_date=''):
    if not list_tasks:
        return 'Список дел пуст!'

    while not _date:
        _date = input_date()

    if _date not in list_tasks:
        print(f'На {_date} дел нет.')
        return True

    text = f'На {_date}:\n'
    for _task in list_tasks[_date]:
        text += f'"{_task}"\n'
    print(text)
    return True


def add_task(_date='', _task=''):
    if not _date:
        _date = input_date()
        _task = input_task()
    if _date in list_tasks:
        list_tasks[_date].append(_task)
    else:
        list_tasks[_date] = [_task]
    print('Задание добавлено.\n')
    return True


def add_random_task():
    random_task = random.choice(random_tasks)
    add_task('Сегодня', random_task)
    print_tasks('Сегодня')
    return True


def print_help():
    help_text = '''
Доступные команды:
Помощь - выводит список команд
Добавить - добавляет задание
Дела - выводит список дел
Выход - заканчивает работу программы
'''
    print(help_text)
    return True


def exit_app(text='Спасибо за использование! До свидания!'):
    print(text)
    return False
