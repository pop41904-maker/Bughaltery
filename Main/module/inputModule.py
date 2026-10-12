import os, time
from prettytable import PrettyTable
from Main.module.visual.error import Error_Number

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    clear_screen()
    input('Press enter :  ')
    time.sleep(0.15)
    clear_screen()


def press_error(Error):
    clear_screen()
    if isinstance(Error, str):
        t = PrettyTable()
        t.title = 'Error'
        t.header = False
        t.add_row([Error])
        print(t)
    else:
        print(Error)
    time.sleep(0.5)
    input('Press enter to continue : ')
    time.sleep(0.15)
    clear_screen()

def input_number():
    while True:
        try:
            answer = int(input('Choice: '))
            time.sleep(0.15)
            clear_screen()
            return answer
        except ValueError:
            press_error(Error_Number)
