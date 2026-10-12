import os, time
from Main.data.SQL import *
from Main.module.visual.error import *
from Main.module.hashing.hashing import *
from Main.module.inputModule import *

def choise_first():
    while True:
        clear_screen()
        print('+---- Create New Account ----+\n')
        Name_New_User = input('Write name: ').strip()
        Check = check_name(Name_New_User)
        time.sleep(0.25)
        if Check:
            press_error(Error_Name_User)
            continue
        else:
            if len(Name_New_User) < 2 or len(Name_New_User) > 18:
                press_error(Error_Len_Name)
                continue
            else:
                time.sleep(0.25)
                Password_New_User = input('Write password: ').strip()
                time.sleep(0.25)
                if len(Password_New_User) < 6:
                    press_error(Error_Len_Password)
                    continue
                else:
                    clear_screen()
                    Check_Password = input('Check Password: ').strip()
                    time.sleep(0.25)
                    clear_screen()
                    if Check_Password != Password_New_User:
                        print('\nIncorrect password\n')
                        time.sleep(0.15)
                        input('Press enter: ')
                        continue
                    else:
                        Salt = create_salt()
                        Password = hashing_data(Password_New_User, Salt)
                        Date = get_data()
                        User = UserCreate(Name=Name_New_User, Password=Password, Salt=Salt, Balance=0.0, Time_Reg=Date)
                        success = create_user(User)
                        if success:
                            print('User was created!')
                            press_enter()
                            break
                        else:
                            press_error('Failed to create user name might be taken.')
