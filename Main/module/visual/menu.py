from prettytable import *

start_menu = PrettyTable()
start_menu.title = 'Start Menu'
start_menu.field_names = ['№', 'Description']
start_menu.add_rows(
    [
        [1, 'Create Account'],
        [2, 'Sign In Account'],
        [3, 'Exit']
    ]
)

main_menu = PrettyTable()
main_menu.title = 'Main Menu'
main_menu.field_names = ['№', 'Description']
main_menu.add_rows(
    [
        [1, 'Create new operation'],
        [2, 'Get history'],
        [3, 'Check balance'],
        [4, 'Exit']
    ]
)