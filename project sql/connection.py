import mysql.connector
from datetime import datetime
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chennarao_42",
        database="employee"
    )

def register_user(acc_no, name, account_type, balance, pin):
    db = get_connection()
    cursor = db.cursor()

    query = """
        INSERT INTO users (acc_no, name, account_type, balance, pin, credited_at)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    data = (acc_no, name, account_type, balance, pin, datetime.now())

    cursor.execute(query, data)
    db.commit()

    print(" User registered successfully!")

    cursor.close()
    db.close()

def login_user(acc_no, pin):
    db = get_connection()
    cursor = db.cursor()

    query = "SELECT acc_no, name, account_type, balance FROM users WHERE acc_no = %s AND pin = %s"
    cursor.execute(query, (acc_no, pin))
    user = cursor.fetchone()

    cursor.close()
    db.close()

    if user:
        print(" Login successful!")
        print("Welcome,", user[1])
        print("Account Type:", user[2])
        print("Balance:", user[3])
        return True
    else:
        print(" Invalid Account Number or PIN!")
        return False

def get_user(acc_no):
    db = get_connection()
    cursor = db.cursor()

    query = "SELECT * FROM users WHERE acc_no = %s"
    cursor.execute(query, (acc_no,))
    user = cursor.fetchone()

    cursor.close()
    db.close()

    return user
def admin_login(username, password):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM admin WHERE username=%s AND password=%s",
        (username, password)
    )
    admin = cursor.fetchone()

    cursor.close()
    db.close()

    if admin:
        print("\n Admin login successful!")
        return True
    else:
        print("\n Invalid admin username or password")
        return False

