import os, time
from Main.data.SQL import init_table_users, init_table_history
from Main.module.visual.error import Error_Index
from Main.module.visual.menu import start_menu
from Main.module.inputModule import clear_screen, input_number, press_error
from Main.start.choise1 import choise_first
from Main.start.choise2 import choise_second
from Main.secondPart import main_part

init_table_users()
init_table_history()


while True:
    clear_screen()
    print(start_menu)
    Answer = input_number()

    if Answer == 1:
        choise_first()
    elif Answer == 2:
        User = choise_second()
        if User:
            main_part(User)
        else:
            press_error("Login failed after maximum attempts.")
    elif Answer == 3:
        break
    else:
        press_error(Error_Index)
        continue