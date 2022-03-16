from getpass import getpass
from mysql.connector import connect, Error
from pass_queries import *

try:
    with connect(
            host="localhost",
            user="root",
            password=input('Insert password: '),
            database="passwords_db") as connection:
        with connection.cursor() as cur:
            pass

except Error() as err:
    print(err)