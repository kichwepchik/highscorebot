import mysql.connector
from mysql.connector import Error
from datetime import datetime


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='shoesplus',
            user='user',
            password='X531z-dahigh-24dD',
            charset='utf8'
        )
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None


def insert_user(telegram_id, username):
    connection = connect_to_database()
    if connection is None:
        return "Connection to database failed"

    try:
        cursor = connection.cursor()
        query = "SELECT id FROM users WHERE telegram_id = %s"
        cursor.execute(query, (telegram_id,))
        user = cursor.fetchone()

        if user:
            cursor.close()
            connection.close()
            return "User already exists"

        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = """INSERT INTO users (telegram_id, username, created_at)
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (telegram_id, username, created_at))
        connection.commit()
        cursor.close()
        connection.close()
        return "User inserted successfully"
    except Error as e:
        print("Failed to insert into MySQL table", e)
        return str(e)


def update_user(telegram_id, username):
    connection = connect_to_database()
    if connection is None:
        return "Connection to database failed"

    try:
        cursor = connection.cursor()
        query = "SELECT id FROM users WHERE telegram_id = %s"
        cursor.execute(query, (telegram_id,))
        user = cursor.fetchone()

        if not user:
            cursor.close()
            connection.close()
            return "User does not exist"

        query = "UPDATE users SET username = %s WHERE telegram_id = %s"
        cursor.execute(query, (username, telegram_id))
        connection.commit()
        cursor.close()
        connection.close()
        return "User updated successfully"
    except Error as e:
        print("Failed to update MySQL table", e)
        return str(e)
