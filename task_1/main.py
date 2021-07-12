# coding: utf-8

def input_date():
    return input("Введите дату:")


def input_task():
    return input("Введите задачу:")


def print_tasks(_date, _task):
    print(f"{_date} {_task}")


if __name__ == '__main__':
    date = input_date()
    task = input_task()
    print_tasks(date, task)
