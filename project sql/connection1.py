import mysql.connector
from datetime import datetime
from connection import get_connection
from decimal import Decimal

def check_balance(acc_no):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT balance FROM users WHERE acc_no=%s", (acc_no,))
    bal = cur.fetchone()[0]

    cur.close()
    conn.close()

    print(f"Balance for {acc_no}: {bal}")
    return bal

def credit(acc_no, amount, description="credited"):
    amount = Decimal(str(amount))
    old_balance = check_balance(acc_no)
    new_balance = old_balance + amount

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET balance=%s, credited_at=%s WHERE acc_no=%s",
        (new_balance, datetime.now(), acc_no)
    )

    cur.execute(
        """
        INSERT INTO transactions (acc_no, to_acc, transaction_type, description, credited_at)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (acc_no, None, "credit", description, datetime.now())
    )

    conn.commit()
    print(f"{amount} credited to {acc_no}")

    cur.close()
    conn.close()

def debit(acc_no, amount, description="debited"):
    amount = Decimal(str(amount))
    old_balance = check_balance(acc_no)

    if old_balance < amount:
        print(" Insufficient balance!")
        return

    new_balance = old_balance - amount

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET balance=%s WHERE acc_no=%s",
        (new_balance, acc_no)
    )

    cur.execute(
        """
        INSERT INTO transactions (acc_no, to_acc, transaction_type, description, credited_at)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (acc_no, None, "debit", description, datetime.now())
    )

    conn.commit()
    print(f"{amount} debited from {acc_no}")

    cur.close()
    conn.close()

def change_pin(acc_no, old_pin, new_pin):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT pin FROM users WHERE acc_no=%s", (acc_no,))
    current_pin = cur.fetchone()[0]

    if current_pin != old_pin:
        print(" Old PIN is incorrect!")
        return

    cur.execute("UPDATE users SET pin=%s WHERE acc_no=%s", (new_pin, acc_no))
    conn.commit()

    print(" PIN updated successfully!")

    cur.close()
    conn.close()



def view_all_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT acc_no, name, account_type, balance FROM users")
    rows = cur.fetchall()

    print("\n--- All Users ---")
    for row in rows:
        print(f"Account: {row[0]}, Name: {row[1]}, Type: {row[2]}, Balance: {row[3]}")

    cur.close()
    conn.close()


def view_all_transactions():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM transactions")
    rows = cur.fetchall()

    print("\n--- All Transactions ---")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

