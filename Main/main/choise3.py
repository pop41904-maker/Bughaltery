from Main.data.SQL import get_user
from Main.module.visual.error import Error_Index
from Main.module.inputModule import clear_screen, press_error
from prettytable import PrettyTable
import os

def choice_third(User):
    clear_screen()
    result = get_user(User)

    if not result["massage"]:
        press_error("Unable to retrieve user data.")
        return
    
    uid, uname, ubalance = result["User"]
    balance_table = PrettyTable()
    balance_table.title = f'Current Balance for {uname}'
    balance_table.field_names = ['Currency', 'Amount']
    balance_table.add_row(['Balnance', f'{ubalance:.2f}'])
    print(balance_table)
    input('Press enter : ')
    os.system('cls')