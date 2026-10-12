from Main.data.SQL import *
from Main.module.hashing.hashing import *
from Main.module.visual.error import *
from Main.module.visual.menu import *
from Main.module.inputModule import *

def choice_first(User):
    while True:
        clear_screen()
        print('<----- New operation ----->\n')
        Operation = input('Operation: ').strip()
        time.sleep(0.15)
        if len(Operation) > 45:
            press_error('Operation name must be shorter than 45 characters.')
            continue

        try:
            Count_Operation = float(input('Write amount: '))
            time.sleep(0.15)
            if Count_Operation < 0:
                press_error('Amount must be non-negative.')
                continue
        except ValueError:
            press_error('Please enter a valid number for amount')
            continue

        Type = input('\nType operation + or -\nChoice: ').strip()
        time.sleep(0.15)
        if Type == '+':
            Type_Int = 1
        elif Type == '-':
            Type_Int = 0
        else:
            press_error('Invalid type. Please enter + or -')
            continue
        Data = get_data()
        Transaction = TransactionCreate(
            Id_User=User.Id,
            Operation=Operation,
            Count_Operation=Count_Operation,
            Type=Type_Int,
            Data=Data
        )
        create_new_transaction(Transaction)
        try:
            con = connect_DB()
            cur = cursor_connect(con)
            if Type_Int == 1:
                cur.execute("UPDATE Users SET Balance = Balance + ? WHERE Id = ?",
                            (Count_Operation, User.Id))
            else:
                cur.execute("SELECT Balance FROM Users WHERE Id = ?", (User.Id,))
                row = cur.fetchone()
                if row and row[0] >= Count_Operation:
                    cur.execute("UPDATE Users SET Balance = Balance - ? WHERE Id = ?",
                                (Count_Operation, User.Id))
                else:
                    press_error('Insufficient funds for this operation')
                    con.rollback()
                    return
            con.commit()
        except Exception as e:
            print(f"Error updating balance: {e}")
            con.rollback()
        finally:
            con.close()
        press_enter()
        break