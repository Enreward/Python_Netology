# coding: utf-8
from lib import *

count_repeat = 3
list_tasks = {}


for i in range(count_repeat):
    date = input_date()
    task = input_task()
    list_tasks = add_task(list_tasks, date, task)

for key in list_tasks.keys():
    for str_task in list_tasks[key]:
        print(output_tasks(key, str_task))
