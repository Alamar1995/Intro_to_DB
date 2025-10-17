import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="127.0.0.1",      # or "localhost"
            user="root",           # replace with your MySQL username
            password="data25"      # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database (autograder expects this exact name)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore;")
            print("Database 'alxbookstore' created successfully!")

    except Error as e:
        # Handle any errors that occur during connection or execution
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Safely close cursor and connection
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        except:
            pass


# Run the function if this file is executed directly
if __name__ == "__main__":
    create_database()

