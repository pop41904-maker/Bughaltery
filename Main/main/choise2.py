from Main.data.SQL import *
from Main.module.visual.error import *
from Main.module.visual.menu import *
from Main.module.inputModule import *
from prettytable import PrettyTable

def choice_second(User):
    clear_screen()
    result = get_user(User)

    if not result["massage"]:
        press_error("Unable to retrieve user data.")
        return

    uid, uname, ubalance = result["User"]
    history = result["History"]
    balance_table = PrettyTable()
    balance_table.title = f'Balance for {uname}'
    balance_table.field_names = ['Balance']
    balance_table.add_row([f'{ubalance:.2f}'])
    print(balance_table)
    if history:
        hist_table = PrettyTable()
        hist_table.title = 'Transaction History'
        hist_table.field_names = ['ID', 'Operation', 'Amount', 'Type', 'Date']
        for row in history:
            tid, op, amt, ttype, date = row
            type_str = '+' if ttype == 1 else '-'
            hist_table.add_row([tid, op, f'{amt:.2f}', type_str, date])
        print(hist_table)
    else:
        print("No transactions found.")

    input('Press enter : ')
    os.system('cls')
