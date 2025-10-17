import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL Server
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",        # your MySQL username
            password="data25"   # your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database (autograder expects this exact name)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore;")
            print("Database 'alxbookstore' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        except:
            pass

if __name__ == "__main__":
    create_database()

