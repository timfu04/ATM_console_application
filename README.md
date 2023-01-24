# __ATM Console Application__
A Python console application that simulates functions of an Automated Teller Machine (ATM). These functions include withdrawal, deposit and check balance.

# __Installation and Usage__
1. Create Virtual Environment in Python
   
   `python -m venv venv`

2. Install all dependencies from requirements.txt
   
   `pip install -r requirements.txt`

3. Run `atm.py` to initiate the console application.


# __Extras__
- Refer `sqlite_db.py` for administrator level functions that interacts with the database
  - Functions included:
    1. Create cardholder
    2. Get all cardholder information
    3. Get current balance by card number
    4. Update cardholder information (first name or lastname or balance)
    5. Delete cardholder