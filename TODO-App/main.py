# coding: utf-8
from lib import *

run = True
list_commands = get_commands()

while run:
    command = input_command()
    if command in list_commands.keys():
        run = list_commands[command]()
    else:
        run = exit_app('Неизвестная команда!')
