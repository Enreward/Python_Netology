def input_date():
    return input("Введите дату: ")


def input_task():
    return input("Введите задачу: ")


def output_tasks(_date, _task):
    return f"{_date} {_task}"


def add_task(_list_tasks, _date, _task):
    if _date in _list_tasks:
        _list_tasks[_date].append(_task)
    else:
        _list_tasks[_date] = [_task]
    return _list_tasks
