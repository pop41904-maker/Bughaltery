import os, time
from Main.data.SQL import *
from Main.module.visual.error import *
from Main.module.hashing.hashing import *
from Main.module.inputModule import *

def choise_second():
    Atteps = 0
    while Atteps < 5:
        clear_screen()
        print('<----- Sign In ----->\n')
        Name = input('Name: ').strip()
        time.sleep(0.25)
        Password = input('Password: ').strip()
        time.sleep(0.25)

        User = UserSign(Name=Name, Password=Password, Salt="")
        User = sign_in(User)
        if User:
            clear_screen()
            return User
        else:
            press_error(Error_SignIn)
            Atteps += 1
    return False
