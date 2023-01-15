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



def input_validation(type: str, msg: str) -> Union[str, float, int]:
    """ User input validation

    Args:
        type (str): string or number
        msg (str): user input message

    Returns:
        Union[str, float, int]: return user input in string or float or integer
    """
    while True:
        user_input = input(msg)
        if not ' ' in user_input:
            if len(user_input) > 0:  
                if type == "string":
                    if user_input.isalpha():
                        return str(user_input)
                    else:
                        print(f"{'*'*10} Only alphabets are allowed {'*'*10}")
                elif type == "number":
                    if user_input.isdigit():
                        if "." in user_input:
                            return float(user_input)
                        else:
                            return int(user_input)
                    else:
                        print(f"{'*'*10} Only numbers are allowed {'*'*10}") 
            else:
                print(f"{'*'*10} Field cannot be blank {'*'*10}")
        else:
            print(f"{'*'*10} Whitespace is not allowed {'*'*10}")



if __name__ == "__main__":
    a = input_validation("string", "Enter your first name:\n")
    print(a)
    
    b = input_validation("number", "Enter your balance:\n")
    print(b)
    
    # db = sqlite_db()
    
    # # Create cardholders table
    # try:
    #     with db.conn:
    #         db.cursor.execute("""
    #                           CREATE TABLE IF NOT EXISTS cardholders(
    #                               cardNum INTEGER PRIMARY KEY,
    #                               pin INTEGER NOT NULL,
    #                               balance REAL NOT NULL,
    #                               firstName TEXT NOT NULL,
    #                               lastName TEXT NOT NULL
    #                           )
    #                           """)
    # except Exception as e:
    #     print(e)
    
    
    
    
    
    

        
        
        
        
        
        
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

