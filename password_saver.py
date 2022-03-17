import PyQt5
from Queries import *
from getpass import getpass
from mysql.connector import connect, Error

insert_into_emails = """INSERT INTO emails(email, pass) VALUES ( 
    {0},
    {1}
    )"""

# TODO: Create tables, insert values, algorithm to insert and display using PyQT5

try:
    with connect(
            host="localhost",
            user="root",
            password=getpass("insert password: "),
            database="passwords_db") as connection:
        with connection.cursor() as cur:
            # 1064 (42000) mySQL syntax error
                cur.execute(insert_into_emails.format(str("test_email1@test.com"), str("potato33")))
    
except Exception as err:
    print(err)
    
