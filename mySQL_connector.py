import mysql.connector
from mysql.connector import Error
import random

def get_random_field_from_column(database, table, column):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='your_host',       # e.g., 'localhost'
            database=database,      # your database name
            user='your_username',   # your MySQL username
            password='your_password') # your MySQL password

        if connection.is_connected():
            cursor = connection.cursor()
            # SQL query to select a random field from a specified column
            query = f"SELECT {column} FROM {table} ORDER BY RAND() LIMIT 1"

            cursor.execute(query)
            # Fetch one result
            record = cursor.fetchone()
            print(f"Random field from {column}: {record[0]}")
            return record[0]

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # Close the connection and cursor
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Usage example
database_name = 'puppy_subreddits'
table_name = 'subreddits'
column_name = 'subreddit_names'
get_random_field_from_column(database_name, table_name, column_name)
