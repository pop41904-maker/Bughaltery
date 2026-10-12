from prettytable import PrettyTable

Error_Number = PrettyTable()
Error_Number.title = 'Number Error'
Error_Number.header = False
Error_Number.add_row(['Write number in writeplace.'])

Error_Len_Name = PrettyTable()
Error_Len_Name.title = 'Name Error'
Error_Len_Name.header = False
Error_Len_Name.add_row(['Uncorrect format name. Must be 2–18 letters.'])

Error_Len_Password = PrettyTable()
Error_Len_Password.title = 'Password Error'
Error_Len_Password.header = False
Error_Len_Password.add_row(['Password must be at least 6 characters.'])

Error_Name_User = PrettyTable()
Error_Name_User.title = 'Name Error'
Error_Name_User.header = False
Error_Name_User.add_row(['This name is already taken. Please choose another.'])

Error_SignIn = PrettyTable()
Error_SignIn.title = 'Data Error'
Error_SignIn.header = False
Error_SignIn.add_row(['Incorrect data. Try again. Max attempts: 5.'])

Error_Index = PrettyTable()
Error_Index.title = 'Index Error'
Error_Index.header = False
Error_Index.add_row(['Please choose a valid option from the menu.'])
