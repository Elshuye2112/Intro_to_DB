import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'  
        )
        cursor = connection.cursor()

        # Try to create database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Error creating database: {err}")

    except mysql.connector.Error as err:
        print(f"Failed to connect to MySQL Server: {err}")

    finally:
        # Ensure cleanup
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
