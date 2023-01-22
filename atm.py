import sqlite3
from sqlite_db import SQLite_DB, input_validation, get_cardholder_by_cardnum_pin, update_cardholder_info_by_cardnum, error_msg
    
def print_menu(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor):
    
    print(f"""{'#'*5} Huat Bank ATM {'#'*5}
    1. Withdraw
    2. Deposit
    3. Check Balance
    4. Exit
{'#'*25}\n""")
    
    while True:
        option = input_validation("number", "Please enter your option:\n")
        if isinstance(option, int):
            if option in [1, 2, 3, 4]:
                break
            else:
                error_msg("Invalid option. Please try again")
        else:
            error_msg("Invalid option. Option cannot be decimal. Please try again.")
    
    if option == 1:
        withdraw(db.conn, db.cursor)
    elif option == 2:
        pass
    elif option == 3:
        pass
    else:
        exit()
        
        
def withdraw(db_conn: sqlite3.Connection, db_cursor: sqlite3.Cursor):
    
    while True:
        while True:
            cardNum = input_validation("number", "Enter your card number:\n")
            if isinstance(cardNum, int):
                if len(str(cardNum)) == 16:
                    break
                else:
                    error_msg("Card number must contain 16 digits")
            else:
                error_msg("Invalid option. Card number cannot be decimal")
            
        while True:
            pin = input_validation("number", "Enter your PIN:\n")
            if isinstance(pin, int):
                if len(str(pin)) == 6:
                    break
                else:
                    error_msg("PIN must contain 6 digits")
            else:
                error_msg("Invalid option. PIN cannot be decimal")
    
        cardholder = get_cardholder_by_cardnum_pin(db_conn, db_cursor, cardNum, pin)
        if cardholder != None:
            current_balance = cardholder[3]
            break
        else:
            error_msg("Information not found. Please check your card number & PIN")
    
    print(current_balance)
    
    while True:
        withdrawal_amount = input_validation("number", "Enter your withdrawal amount:\n")
        if current_balance - withdrawal_amount < 0:
            error_msg("Withdrawal amount exceeded account balance. Please enter a lower amount.")
        else:
            new_balance = current_balance - withdrawal_amount
            break
    
    print(new_balance)
    # still testing
    # update_cardholder_info_by_cardnum(db.conn, db.cursor, cardNum, "balance")
            
 

    
    
    
    #if not None: get current balance
    # ask how much to withdraw
    # get new balance
    # update new balance
    




# print menu, fast cash or targeted amount
# if fast cash, update database
# if targeted, get input, update database

    
    





# enter cardnum
# choose fast cash or targeted number
# minus balance






if __name__ == "__main__":
    
    db = SQLite_DB()
    
    print_menu(db.conn, db.cursor)