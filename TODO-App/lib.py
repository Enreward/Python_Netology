# coding: utf-8

list_tasks = {}


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
        'Выход': exit_app
    }


def print_tasks():
    text = ''
    for date in list_tasks.keys():
        text += f'{date}:'
        for task in list_tasks[date]:
            text += f'\n"{task}"'
        text += '\n'
    if text:
        print(text)
    else:
        print('Список дел пуст.')
    return True


def add_task():
    _date = input_date()
    _task = input_task()
    if _date in list_tasks:
        list_tasks[_date].append(_task)
    else:
        list_tasks[_date] = [_task]
    print('Задание добавлено.\n')
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
