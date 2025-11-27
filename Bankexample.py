import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chennarao_42",  
    database="bankdb"
)
cursor = conn.cursor()

def create_account():
    while True:
        acc_no = input("Enter new account number (8–15 digits): ").strip()
        if acc_no.isdigit() and 8 <= len(acc_no) <= 15:
            break
        else:
            print("❌ Invalid account number! It must contain 8–15 digits only.")

    name = input("Enter customer name: ").strip()

    while True:
        pin = input("Set 4 digit PIN: ").strip()
        if len(pin) == 4 and pin.isdigit():
            break
        else:
            print("❌ Invalid PIN! It must be exactly 4 digits.")

    cursor.execute("INSERT INTO accounts (account_no, name, pin, balance) VALUES (%s, %s, %s, %s)",
                   (acc_no, name, pin, 0))
    conn.commit()
    print("\n✅ Account Created Successfully!\n")

def login():
    acc_no = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    cursor.execute("SELECT * FROM accounts WHERE account_no=%s AND pin=%s", (acc_no, pin))
    result = cursor.fetchone()

    if result:
        print(f"\n✅ Login Successful! Welcome, {result[1]}\n")
        banking_menu(acc_no)
    else:
        print("❌ Invalid Account Number or PIN")

def deposit(acc_no):
    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
        print("❌ Invalid amount.")
        return
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_no=%s", (amount, acc_no))
    cursor.execute("INSERT INTO transactions (account_no, type, amount) VALUES (%s, %s, %s)",
                   (acc_no, "deposit", amount))
    conn.commit()
    print("✅ Amount Deposited Successfully")

def withdraw(acc_no):
    amount = float(input("Enter withdrawal amount: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc_no,))
    balance = cursor.fetchone()[0]

    if amount <= 0:
        print("❌ Invalid amount.")
    elif amount <= balance:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_no=%s", (amount, acc_no))
        cursor.execute("INSERT INTO transactions (account_no, type, amount) VALUES (%s, %s, %s)",
                       (acc_no, "withdraw", amount))
        conn.commit()
        print("✅ Cash Withdrawn Successfully")
    else:
        print("❌ Insufficient Balance")

def check_balance(acc_no):
    cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc_no,))
    balance = cursor.fetchone()[0]
    print(f"\n💰 Current Balance: ₹{balance}\n")

def banking_menu(acc_no):
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout")

        try:
            choice = int(input("Choose option: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if choice == 1:
            deposit(acc_no)
        elif choice == 2:
            withdraw(acc_no)
        elif choice == 3:
            check_balance(acc_no)
        elif choice == 4:
            print("🔒 Logged out...\n")
            break
        else:
            print("❌ Invalid option. Try again.")

while True:
    print("\n=== BANKING SYSTEM ===")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    try:
        option = int(input("Choose option: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    if option == 1:
        create_account()
    elif option == 2:
        login()
    elif option == 3:
        print("👋 Thank you for using our bank application.")
        break
    else:
        print("❌ Invalid choice. Try again.")
