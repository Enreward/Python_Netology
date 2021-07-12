# coding: utf-8
from lib import *

count_repeat = 3
list_tasks = {}


for i in range(count_repeat):
    date = input_date()
    task = input_task()
    list_tasks[date] = task

for key, value in list_tasks.items():
    print(output_tasks(key, value))
