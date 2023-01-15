import sqlite3
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




# first & last name must be string 
# balance must be int or float 


def input_validation(type, msg):
    input_1 = input(f"{msg}\n") # input default string
    print(input_1)
    
    if type == "name":
        return input_1
    else:
        return float(input_1)






  
    

if __name__ == "__main__":
    
    
    input_validation("name", "enter your f name")
    
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

