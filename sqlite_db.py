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
    except Exception as e:
        print(e)
    
 
# Function to create cardholder and insert into database
def create_cardholder_insert_db(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor):
    """ Create cardholder and insert cardholders table

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
    """
    firstName = input_validation("string", "Enter your first name:\n")
    lastName = input_validation("string", "Enter your last name:\n")
    balance = input_validation("number", "Enter your balance:\n")
    
    cardholder = Cardholder(random_num_generator(16), random_num_generator(6), balance, firstName, lastName)
    
    values = {"cardNum":cardholder.cardNum, "pin":cardholder.pin, "balance":cardholder.balance, "firstName":cardholder.firstName, "lastName":cardholder.lastName}
    
    insert_cardholder(db_conn, db_cursor, values)     
    
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
    
    
    create_cardholder_insert_db(db.conn, db.cursor)
    
    
    

        
        
        
        
        
        
    #### testing
    # db.cursor.execute("""
    #                   INSERT INTO cardholders (cardNum, pin, balance, firstName, lastName)
    #                   VALUES (5462573831192908, 874269, 123456.78, 'Clement', 'Lee'); 
    #                   """)
    
    # db.conn.commit()
    
    
    # db.cursor.execute("SELECT * FROM cardholders")
    
    # print(db.cursor.fetchall())
    

    ### testing
        
        





    
    
    # db.close_conn()


    
    
    
    
    
    
    



# conn (attribute)
    # cursor (attribute)
    # commit (method) - no need (use context manager)
    # close (method)
    
    
# methods (CRUD)
# create table
# read table
# update table
# delete table 

