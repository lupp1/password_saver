import PyQt5
from Queries import *
from getpass import getpass
from mysql.connector import connect, Error


# TODO: Create tables, insert values, algorithm to insert and display using PyQT5

try:
    connection = connect(
                host="localhost",
                user="root",
                password=getpass("insert password: "),
                database="passwords_db")

    cur = connection.cursor()
except Exception as err:
    print(err)

# TODO: Insert new e_mail

# TODO: Learn OOP to build this project

    
