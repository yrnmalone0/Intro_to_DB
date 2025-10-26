import mysql.connector
from mysql.connector import Error


try:
    #Establishing the connection to MySQL Server
    db_connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "P@ssw0rd$$"
    )

    #Checking if the connection is established
    if db_connection.is_connected():
        #print("Successfully connected to MySQL DB")

        mycursor = db_connection.cursor()

        sql_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        mycursor.execute(sql_query)
        result = mycursor.fetchone()

        if result:
            print("Database 'alx_book_store' created successfully!")
        else:
            print("Database already exists.")

except mysql.connector.Error as e:
    print(f"Error while connecting to database: {e}")


finally:
    if db_connection and db_connection.is_connected():
        mycursor.close()
        db_connection.close()

        print("Database connection closed successfully!")