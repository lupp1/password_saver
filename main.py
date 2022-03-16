from getpass import getpass
from mysql.connector import connect, Error
from pass_queries import *

# QUERIES

try:
    # Gets mySQL connection object
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password = getpass("Enter password: "),
        database="online_movie_rating") as connection: 
        # Creates and opens a cursor object that interacts with mySQL
            with connection.cursor() as cur:
                cur.execute(SELECT_MOVIES_QUERY)
                result = cur.fetchall()
                for movie in result:
                    print(movie[1])
                
except Error as e:
    print(e)