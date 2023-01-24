# Import modules
import os
import time
import sqlite3
from sqlite_db import SQLite_DB, input_validation, get_cardholder_by_cardnum_pin, update_cardholder_info_by_cardnum, format_msg, block_unblock_all_keyboard_keys


# Function to clear screen in between sleeps
def clear_screen(before_sec: int, after_sec: int):
    """ Clear screen in between sleeps

    Args:
        before_sec (int): number of seconds to sleep before clear screen
        after_sec (int): number of seconds to sleep after clear screen
    """
    time.sleep(before_sec)
    os.system("cls")
    time.sleep(after_sec)


# Function to print main menu
def print_menu(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor) -> None:
    """ Print main menu

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
    """ 
    
    print(f"""{'#'*5} Huat Bank ATM {'#'*5}
    1. Withdraw
    2. Deposit
    3. Check Balance
    4. Exit
{'#'*25}\n""")
    
    while True:
        option = input_validation(type="number", skip_input=False, msg="Enter your option:\n")
        if isinstance(option, int):
            if option in [1, 2, 3, 4]:
                break
            else:
                print(format_msg("Invalid option. Please try again."))
                block_unblock_all_keyboard_keys(1)
        else:
            print(format_msg("Invalid option. Option cannot be decimal. Please try again."))
            block_unblock_all_keyboard_keys(1)

    if option == 1:
        withdraw(db_conn, db_cursor)
    elif option == 2:
        deposit(db_conn, db_cursor)
    elif option == 3:
        check_balance(db_conn, db_cursor)
    else:
        exit()


# Function to get user card credentials input (card number & PIN)
def get_card_credentials(type: str, msg: str, max_length: int) -> int:
    """ Get user card credentials input (card number & PIN)

    Args:
        type (str): "card" or "pin"
        msg (str): prompt message
        max_length (int): maximum credential length

    Returns:
        int: credential (card number or PIN)
    """
    if type == "card":
        msg_type = "Card number"
    elif type == "pin":
        msg_type = "PIN"

    while True:
        credential = input_validation(type="number", skip_input=False, msg=f"{msg}")
        if isinstance(credential, int):
            if len(str(credential)) == max_length:
                break
            else:
                print(format_msg(f"{msg_type} must contain {max_length} digits"))
                block_unblock_all_keyboard_keys(1)
        else:
            print(format_msg(f"Invalid option. {msg_type} cannot be decimal."))
            block_unblock_all_keyboard_keys(1)
    
    return credential


# Function for ATM withdrawal       
def withdraw(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor) -> None:
    """ ATM withdrawal

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
    """
    while True:
        cardNum = get_card_credentials("card", "\nEnter your card number:\n", 16)
        pin = get_card_credentials("pin", "\nEnter your PIN:\n", 6)
        
        cardholder = get_cardholder_by_cardnum_pin(db_conn, db_cursor, cardNum, pin)
        if cardholder != None:
            current_balance = cardholder[3]
            break
        else:
            print(format_msg("Information not found. Please check your card number & PIN"))
    
    print(f'\n{format_msg(f"Your current balance is: {current_balance}")}')
    
    while True:
        withdraw_amount = input_validation(type="number", skip_input=False, msg="Enter your withdrawal amount:\n")
        if current_balance - withdraw_amount < 0:
            print(format_msg("Withdrawal amount exceeded account balance. Please enter a lower amount."))
        else:
            new_balance = current_balance - withdraw_amount
            break
    
    if update_cardholder_info_by_cardnum(db_conn, db_cursor, cardNum, "balance", input_validation(type="number", skip_input=True, user_input=str(new_balance))):
        print(f'\n{format_msg("Transaction completed. Please take your cash.")}')
    
    clear_screen(5, 0)
    print_menu(db.conn, db.cursor)


# Function for ATM deposit
def deposit(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor) -> None:
    """ ATM deposit

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
    """
    while True:
        cardNum = get_card_credentials("card", "\nEnter your card number:\n", 16)
        pin = get_card_credentials("pin", "\nEnter your PIN:\n", 6)
        
        cardholder = get_cardholder_by_cardnum_pin(db_conn, db_cursor, cardNum, pin)
        if cardholder != None:
            current_balance = cardholder[3]
            break
        else:
            print(format_msg("Information not found. Please check your card number & PIN"))
        
    print(f'\n{format_msg(f"Your current balance is: {current_balance}")}')
    
    deposit_amount = input_validation(type="number", skip_input=False, msg="Enter your deposit amount:\n")
    new_balance = current_balance + deposit_amount
    
    if update_cardholder_info_by_cardnum(db_conn, db_cursor, cardNum, "balance", input_validation(type="number", skip_input=True, user_input=str(new_balance))):
        print(f'\n{format_msg("Transaction completed. Cash has been deposited.")}')
        print(f'\n{format_msg(f"Your new current balance is: {new_balance}")}')

    clear_screen(5, 0)
    print_menu(db.conn, db.cursor)


# Function to check current balance
def check_balance(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor) -> None:
    """ Check current balance

    Args:
        db_conn (sqlite3.Connection): database connection
        db_cursor (sqlite3.Cursor): database cursor
    """
    while True:
        cardNum = get_card_credentials("card", "\nEnter your card number:\n", 16)
        pin = get_card_credentials("pin", "\nEnter your PIN:\n", 6)
        
        cardholder = get_cardholder_by_cardnum_pin(db_conn, db_cursor, cardNum, pin)
        
        if cardholder != None:
            current_balance = cardholder[3]
            break
        else:
            print(format_msg("Information not found. Please check your card number & PIN"))
            
    print(f'\n{format_msg(f"Your current balance is: {current_balance}")}')

    clear_screen(5, 0)
    print_menu(db.conn, db.cursor)
    
    
if __name__ == "__main__":
      
    db = SQLite_DB()
    
    print_menu(db.conn, db.cursor)
    
    
    