from Main.module.inputModule import clear_screen, press_enter, input_number
from Main.module.visual.menu import main_menu
from Main.main.choise1 import choice_first
from Main.main.choise2 import choice_second
from Main.main.choise3 import choice_third
from Main.data.SQL import active_user
from Main.module.visual.error import *
from Main.module.inputModule import *

def main_part(User):
    User = active_user(User)
    if not User:
        print("Session expired or invalid user.")
        press_enter()
        return

    while True:
        clear_screen()
        print(main_menu)
        Answer = input_number()

        if Answer == 1:
            choice_first(User)
        elif Answer == 2:
            choice_second(User)
        elif Answer == 3:
            choice_third(User)
        elif Answer == 4:
            break
        else:
            press_error(Error_Index)
