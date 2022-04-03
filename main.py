import PyQt5
from Queries import *
from getpass import getpass
from mysql.connector import connect, Error


# TODO: Insert new e_mail-password
# TODO: Learn OOP to build this project
# TODO: Work on GUI

""" try:
    connection = connect(
                host="localhost",
                user=input("inser user: "),
                password=getpass("insert password: "),
                database="passwords_db")
    cur = connection.cursor()
except Error as err:
    print(err) """

""" def store_email(email_input, password):
    cur.execute(INSERT_INTO_EMAILS.format(email_input, password))
    connection.commit() """
""" 
store_email("test_potato@potato.com", "potato")
 """