# Import modules
import time
import pandas as pd
import sqlite3
import keyboard
from typing import Union
from cardholder import Cardholder, random_num_generator


# Constants
STDOUT_PREFIX = '*'*10
STDOUT_SUFFIX = '*'*10


# SQLite Database class
class SQLite_DB:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("cardholder.db")
        self.cursor = self.conn.cursor()
        
    def close_conn(self):
        """ Close database connection
        """
        self.conn.close()


# Function to print error message
def error_msg(msg: str):
    """ Print error message

    Args:
        msg (str): error message
    """
    print(f"{STDOUT_PREFIX} {msg} {STDOUT_SUFFIX}\n\n")
    
        
# Function to block all keyboard keys
def block_all_keyboard_keys() -> None:
    """ Block all keyboard keys
    """
    for i in range(150):
        keyboard.block_key(i)
    
        
# Function to validate user input
def input_validation(type: str, skip_input: bool, msg: str = "", user_input: str = "") -> Union[str, int, float]:
    """ Validate user input

    Args:
        type (str): string or number
        skip_input (bool): whether to skip user input
        msg (str, optional): user input message. Defaults to "".
        user_input (str, optional): user input. Defaults to "".

    Returns:
        Union[str, int, float]: return user input in string or integer or float
    """
    while True:
        if not skip_input:
            user_input = input(msg)
        if not ' ' in user_input: # if user input don't have whitespace
            if len(user_input) > 0: # if user input not empty/blank
                if type == "string":
                    if user_input.isalpha(): # if user input are all alphabet letters
                        return str(user_input.title())
                    else:
                        error_msg("Only alphabets are allowed")
                        block_all_keyboard_keys()
                        time.sleep(1)
                        keyboard.unhook_all() # remove all keyboard hooks in use
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
                        error_msg("Only numbers are allowed")    
                        block_all_keyboard_keys()
                        time.sleep(1)
                        keyboard.unhook_all() # remove all keyboard hooks in use
                elif type == "boolean":
                    if user_input.lower() in ["yes", "y"]:
                        return True
                    else:
                        return False
            else:
                error_msg("Field cannot be blank")
                block_all_keyboard_keys()
                time.sleep(1)
                keyboard.unhook_all() # remove all keyboard hooks in use
        else:
            error_msg("Whitespace is not allowed")
            block_all_keyboard_keys()
            time.sleep(1)
            keyboard.unhook_all() # remove all keyboard hooks in use


# Function to get cardholder by card number and PIN
def get_cardholder_by_cardnum_pin(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor, cardnum: int, pin: int) -> Union[tuple, None]:
    """ Get cardholder by card number and PIN

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
        cardnum (int): card number
        pin (int): PIN

    Returns:
        Union[tuple, None]: cardholder information or None
    """
    query = f"""
            SELECT *
            FROM cardholders
            WHERE cardNum = {cardnum}
            AND pin = {pin}
            """
    try:
        with db_conn:
            db_cursor.execute(query)
        data = db_cursor.fetchall()
        if len(data) > 0:
            return data[0]
        else:
            return None   
    except Exception as e:
        print(e)


# Function to get all cardholders in DataFrame
def get_all_cardholders(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor) -> pd.DataFrame:
    """ Get all cardholders in DataFrame

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor

    Returns:
        pd.DataFrame: SQL result in DataFrame
    """
    query = """
            SELECT * FROM cardholders
            """  
    try:
        with db_conn:
            db_cursor.execute(query)
        
        data = db_cursor.fetchall()
        columns = ["id", "cardNum", "pin", "balance", "firstName", "lastName"]
        
        df = pd.DataFrame(data, columns=columns)
        return df
    except Exception as e:
        print(e)


# Function to update cardholder information by card number
def update_cardholder_info_by_cardnum(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor, cardnum: int, col_to_update: str, new_value: Union[str, int]):
    """ Update cardholder information by card number

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
        cardnum (int): card number to update
        col_to_update (str): column to update
        new_value (Union[str, int]): new value to update (string or integer)
    """
    if not col_to_update == "balance":
        new_value = f"'{new_value}'"
    
    if input_validation("boolean", False, "Do you wish to proceed data update? (Yes / No)\n"):
        query = f"""
                UPDATE cardholders
                SET {col_to_update} = {new_value}
                WHERE cardNum = {cardnum}  
                """
        try:
            with db_conn:
                db_cursor.execute(query)
        except Exception as e:
            print(e)
    
        
# Function to delete cardholder by card number       
def delete_cardholder_by_cardnum(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor, cardnum: int):
    """ Delete cardholder by card number

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

            
# Function to insert cardholder into table            
def insert_cardholder(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor, values: dict) -> Union[bool, bool]:
    """ Insert cardholder into table

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
        error_msg("Data successfully inserted")
        return True
    except sqlite3.IntegrityError as e:
        print(e)
        return False
    

# Function to create cardholder and insert into database
def create_cardholder_insert_table(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor):
    """ Create cardholder and insert cardholders table

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
    """
    firstName = input_validation("string", False, "Enter your first name:\n")
    lastName = input_validation("string", False, "Enter your last name:\n")
    balance = input_validation("number", False, "Enter your balance:\n")
    
    if input_validation("boolean", False, "Do you wish to proceed data insertion? (Yes / No)\n"):
        cardholder = Cardholder(random_num_generator(16), random_num_generator(6), balance, firstName, lastName)
        
        while not insert_cardholder(db_conn, db_cursor, {"cardNum":cardholder.cardNum, "pin":cardholder.pin, "balance":cardholder.balance, "firstName":cardholder.firstName, "lastName":cardholder.lastName}):
            cardholder.cardNum = random_num_generator(16)
        

if __name__ == "__main__":
    
    db = SQLite_DB()
    
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
    
    # Call CRUD functions
    
    # 1. Create and insert cardholder
    # create_cardholder_insert_table(db.conn, db.cursor)
    
    # # 2. Get all cardholders
    # df = get_all_cardholders(db.conn, db.cursor)
    # print(df)
    
    # # 3. Get current balance by card number
    # print(get_cardholder_by_cardnum_pin(db.conn, db.cursor, 9700924436352881, 289163))
    
    # 4. Update cardholder information
    update_cardholder_info_by_cardnum(db.conn, db.cursor, 2071983763069452, "firstName", input_validation(type="string", skip_input=True, user_input="walaoehF"))
    update_cardholder_info_by_cardnum(db.conn, db.cursor, 2071983763069452, "lastName", input_validation(type="string", skip_input=True, user_input="walaoehL"))
    update_cardholder_info_by_cardnum(db.conn, db.cursor, 2071983763069452, "balance", input_validation(type="number", skip_input=True, user_input="1000"))
    
    
    
    
    # update_cardholder_info_by_cardnum(db.conn, db.cursor, 2071983763069452, "lastName", "testingL")
    # update_cardholder_info_by_cardnum(db.conn, db.cursor, 2071983763069452, "balance", 12345678)
    
    # # 5. Delete cardholder by card number
    # delete_cardholder_by_cardnum(db.conn, db.cursor, 764415931362058)
    
    db.close_conn()


