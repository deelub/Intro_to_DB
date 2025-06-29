import mysql.connector
from mysql.connector import Error

def connection():
    try:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dee99_Christelle#6",
            database="alx_book_store"
        )

        if mydb.is_connected():
            cursor=connection.cursor()
            cursor.executed("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print(mydb.server_info)

    except mysql.connector.Error:
        print(mysql.connector.Error)

    finally:
         if mydb.is_connected():
            cursor.close()
            mydb.close() # type: ignore

if __name__== "__main__":
    connection()