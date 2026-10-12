import sqlite3 as sq, os, time, datetime as dt
from pathlib import Path

DB_PATH = Path("Main/data/Tables.db")
DB_DIR = DB_PATH.parent
DB_DIR.mkdir(parents=True, exist_ok=True)

def connect_DB():
    return sq.connect(str(DB_PATH))

def cursor_connect(con):
    return con.cursor()

def init_table_users():
    try:
        con = connect_DB()
        cur = cursor_connect(con)
        cur.execute("""CREATE TABLE IF NOT EXISTS Users(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL UNIQUE,
            Password TEXT NOT NULL,
            Salt TEXT NOT NULL,
            Balance REAL DEFAULT 0.0,
            Time_Registrate TEXT NOT NULL
        )""")
        con.commit()
    except Exception as e:
        print(f"Error initializing Users table: {e}")
    finally:
        con.close()

def init_table_history():
    try:
        con = connect_DB()
        cur = cursor_connect(con)
        cur.execute("""CREATE TABLE IF NOT EXISTS History(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_User INTEGER NOT NULL,
            Name_Operation TEXT NOT NULL,
            Count_Transaction REAL NOT NULL,
            Type_Transaction INTEGER NOT NULL,
            Data_Transaction TEXT
        )""")
        con.commit()
    except Exception as e:
        print(f"Error initializing History table: {e}")
    finally:
        con.close()

class UserCreate:
    def __init__(self, Name, Password, Salt, Balance, Time_Reg):
        self.Name = Name
        self.Password = Password
        self.Salt = Salt
        self.Balance = Balance
        self.Time_Reg = Time_Reg

class TransactionCreate:
    def __init__(self, Id_User, Operation, Count_Operation, Type, Data):
        self.Id_User = Id_User
        self.Operation = Operation
        self.Count_Operation = Count_Operation
        self.Type = Type
        self.Data = Data

class UserSign:
    def __init__(self, Name, Password, Salt, Id=None):
        self.Name = Name
        self.Password = Password
        self.Salt = Salt
        self.Id = Id

def create_user(User: UserCreate) -> bool:
    try:
        con = connect_DB()
        cur = cursor_connect(con)
        cur.execute(
            """INSERT INTO Users(Name, Password, Salt, Balance, Time_Registrate)
               VALUES(?,?,?,?,?)""",
            (User.Name, User.Password, User.Salt, User.Balance, User.Time_Reg)
        )
        con.commit()
        return True
    except sq.IntegrityError:
        return False
    except Exception as e:
        print(f"Error creating user: {e}")
        return False
    finally:
        con.close()

def check_name(Name: str):
    try:
        con = connect_DB()
        cur = cursor_connect(con)
        cur.execute("SELECT Name FROM Users WHERE Name = ?", (Name,))
        User = cur.fetchone()
        return User is not None
    except Exception as e:
        print(f"Error checking name: {e}")
        return False
    finally:
        con.close()

def create_new_transaction(Transaction: TransactionCreate):
    try:
        con = connect_DB()
        cur = cursor_connect(con)
        cur.execute(
            """INSERT INTO History(Id_User, Name_Operation, Count_Transaction, Type_Transaction, Data_Transaction)
               VALUES(?,?,?,?,?)""",
            (Transaction.Id_User, Transaction.Operation, Transaction.Count_Operation,
             Transaction.Type, Transaction.Data)
        )
        con.commit()
    except Exception as e:
        print(f"Error creating transaction: {e}")
    finally:
        con.close()

def get_salt(Name: str):
    try:
        con = connect_DB()
        cur = cursor_connect(con)
        cur.execute("SELECT Salt FROM Users WHERE Name = ?", (Name,))
        Salt = cur.fetchone()
        if Salt:
            return Salt[0]
        return None
    except Exception as e:
        print(f"Error getting salt: {e}")
        return None
    finally:
        con.close()

def sign_in(User: UserSign):
    Salt = get_salt(User.Name)
    if not Salt:
        return False
    import hashlib
    hashed_input = hashlib.sha512((User.Password + Salt).encode()).hexdigest()
    try:
        con = connect_DB()
        cur = cursor_connect(con)
        cur.execute("SELECT Id, Name, Password, Salt FROM Users WHERE Name = ? AND Password = ?",
                    (User.Name, hashed_input))
        row = cur.fetchone()
        if row:
            return UserSign(Name=row[1], Password=row[2], Salt=row[3], Id=row[0])
        return False
    except Exception as e:
        print(f"Error signing in: {e}")
        return False
    finally:
        con.close()

def active_user(User: UserSign):
    try:
        con = connect_DB()
        cur = cursor_connect(con)
        cur.execute("SELECT * FROM Users WHERE Id = ?", (User.Id,))
        row = cur.fetchone()
        if row:
            return UserSign(Name=row[1], Password=row[2], Salt=row[3], Id=row[0])
        return None
    except Exception as e:
        print(f"Error active_user: {e}")
        return None
    finally:
        con.close()

def get_data() -> str:
    return str(dt.date.today())

def get_user(User: UserSign):
    try:
        con = connect_DB()
        cur = cursor_connect(con)
        cur.execute("SELECT Id, Name, Balance FROM Users WHERE Id = ?", (User.Id,))
        urow = cur.fetchone()
        if not urow:
            return {"massage": False, "User status found": False}
        uid, uname, ubalance = urow
        cur.execute("""SELECT Id, Name_Operation, Count_Transaction, Type_Transaction, Data_Transaction
                       FROM History WHERE Id_User = ? ORDER BY Id DESC""", (uid,))
        history = cur.fetchall()
        return {"massage": True, "User": (uid, uname, ubalance), "History": history}
    except Exception as e:
        print(f"Error get_user: {e}")
        return {"massage": False, "User status found": False}
    finally:
        con.close()