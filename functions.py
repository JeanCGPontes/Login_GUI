import sqlite3


def check_user_exists(email, password):
    database = sqlite3.connect('database_Login_GUI.db')
    cursor = database.cursor()
    cursor.execute("SELECT * FROM user_data WHERE email = '{}' AND password = '{}'".format(email, password))
    return cursor.fetchone()


def check_email(email):
    database = sqlite3.connect('database_Login_GUI.db')
    cursor = database.cursor()
    cursor.execute("SELECT * FROM user_data WHERE email = '{}'".format(email))
    return cursor.fetchone()
