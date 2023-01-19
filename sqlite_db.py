import os
import time
import sqlite3
from typing import Union
from cardholder import Cardholder, random_num_generator

class sqlite_db:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cardholder.db")
        self.cursor = self.conn.cursor()
        
    def close_conn(self):
        self.conn.close()
        
        
    
        




        
# create cardholder
# 1. enter first, last, balance
# 2. check with database, cardnum must be unique
# 3. if not unique, re-generate, else proceed to insert into database




# def create_cardholder_save_db():
#     firstName = input("Enter your first name:\n")

#     ch = Cardholder(random_num_generator(16), random_num_generator(6), 123456.78, "Clement", "Lee")
#     print(ch.cardNum)
#     print(ch.pin)
#     print(ch.balance)
#     print(ch.firstName)
#     print(ch.lastName)


# Function to clear screen in terminal
def clear_screen(before_sec: int, after_sec: int) -> None:
    """ Clear screen in terminal

    Args:
        before_sec (int): number of seconds of sleep before clear screen
        after_sec (int): number of seconds of sleep after clear screen
    """
    time.sleep(before_sec)
    os.system("cls")
    time.sleep(after_sec)


# Function to validate user input
def input_validation(type: str, msg: str) -> Union[str, float, int]:
    """ Validate user input

    Args:
        type (str): string or number
        msg (str): user input message

    Returns:
        Union[str, float, int]: return user input in string or float or integer
    """
    while True:
        clear_screen(0,0)
        user_input = input(msg)
        if not ' ' in user_input: # if user input don't have whitespace
            if len(user_input) > 0: # if user input not empty/blank
                if type == "string":
                    if user_input.isalpha(): # if user input are all alphabet letters
                        return str(user_input.title())
                    else:
                        print(f"{'*'*10} Only alphabets are allowed {'*'*10}")
                        clear_screen(1,0)
                elif type == "number":
                    if user_input.isdigit(): # if user input is digit
                        return int(user_input)
                    elif "." in user_input: # if user input contains decimal point
                        try:
                            float(user_input)
                            return float(user_input)
                        except Exception as e:
                            print(e)
                    else:
                        print(f"{'*'*10} Only numbers are allowed {'*'*10}")
                        clear_screen(1,0)
            else:
                print(f"{'*'*10} Field cannot be blank {'*'*10}")
                clear_screen(1,0)
        else:
            print(f"{'*'*10} Whitespace is not allowed {'*'*10}")
            clear_screen(1,0)
            
            
# Function to insert cardholder into cardholders table            
def insert_cardholder(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor, values: dict):
    """ Insert cardholder into cardholders table

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
        values (dict): values to be inserted into cardholders table
    """
    query = """
        INSERT INTO cardholders (cardNum, pin, balance, firstName, lastName)
        VALUES (:cardNum, :pin, :balance, :firstName, :lastName)
        """
    try:
        with db_conn:
            db_cursor.execute(query, values)
        return True
    except sqlite3.IntegrityError as e:
        print(e)
        return False
    
    
# Function to delete cardholder by card number       
def delete_cardholder_by_cardnum(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor, cardnum: int):
    """ Delete cardholder by cardnum

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
        cardnum (int): card number to delete
    """
    query = f"""
            DELETE FROM cardholders
            WHERE cardNum = {cardnum}
            """
    try:
        with db_conn:
            db_cursor.execute(query)
    except Exception as e:
        print(e)


# Function to create cardholder and insert into database
def create_cardholder_insert_table(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor):
    """ Create cardholder and insert cardholders table

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
    """
    firstName = input_validation("string", "Enter your first name:\n")
    lastName = input_validation("string", "Enter your last name:\n")
    balance = input_validation("number", "Enter your balance:\n")
    
    # cardholder = Cardholder(random_num_generator(16), random_num_generator(6), balance, firstName, lastName)
    
    # testing
    cardholder = Cardholder(6736150184784223, random_num_generator(6), balance, firstName, lastName)
    
    
    # testing not confirmed
    while not insert_cardholder(db_conn, db_cursor, {"cardNum":cardholder.cardNum, "pin":cardholder.pin, "balance":cardholder.balance, "firstName":cardholder.firstName, "lastName":cardholder.lastName}):
        print(cardholder.cardNum)
        cardholder.cardNum = random_num_generator(16)
        print(cardholder.cardNum)
        
        print("hello world")
        time.sleep(1)
    
    

    
    
    
    
    
    
    
    
    
    
    # values = {"cardNum":cardholder.cardNum, "pin":cardholder.pin, "balance":cardholder.balance, "firstName":cardholder.firstName, "lastName":cardholder.lastName}
    
    # print({"cardNum":cardholder.cardNum, "pin":cardholder.pin, "balance":cardholder.balance, "firstName":cardholder.firstName, "lastName":cardholder.lastName})
    
    # cardholder.cardNum = 1231242
    # print({"cardNum":cardholder.cardNum, "pin":cardholder.pin, "balance":cardholder.balance, "firstName":cardholder.firstName, "lastName":cardholder.lastName})
    
    
    
    
    
    
    
    
    # while not insert_cardholder(db_conn, db_cursor, values):
    #     print("hello")
    #     time.sleep(1)
    
    
    # while loop
    # insert false - retry with new num
    # insert true exit loop
    
    
    
    
    # a = insert_cardholder(db_conn, db_cursor, values)     
    # print(a)
    
    # TODO: 
    # 1. cardNum must be unique, check object against db data before insert
 
    
    









if __name__ == "__main__":
    
    db = sqlite_db()
    
    # Create cardholders table
    try:
        with db.conn:
            db.cursor.execute("""
                              CREATE TABLE IF NOT EXISTS cardholders(
                                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                                  cardNum INTEGER NOT NULL UNIQUE,
                                  pin INTEGER NOT NULL,
                                  balance REAL NOT NULL,
                                  firstName TEXT NOT NULL,
                                  lastName TEXT NOT NULL
                              )
                              """)
    except Exception as e:
        print(e)
    
    
    delete_cardholder_by_cardnum(db.conn, db.cursor, 3986569510732480)
    
    
    # ad hoc SQL queries
    # try:
    #     with db.conn:
    #         db.cursor.execute("""
    #                           ALTER TABLE cardholders AUTO_INCREMENT = 4;
    #                           """)
    #     print(db.cursor.fetchall())
    # except Exception as e:
    #     print(e)
    
    
    
    
    
    
    
    
    # create_cardholder_insert_table(db.conn, db.cursor)
    
    
    db.close_conn()


    
    
    
    
    



# conn (attribute)
    # cursor (attribute)
    # commit (method) - no need (use context manager)
    # close (method)
    
    
# methods (CRUD)
# create table
# read table
# update table
# delete table 




