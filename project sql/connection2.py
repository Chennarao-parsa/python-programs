from connection import register_user, login_user, admin_login
from connection1 import credit, debit, check_balance, change_pin, view_all_users, view_all_transactions

while True:
    print("\n1. Register User")
    print("2. Login")
    print("3. Credit")
    print("4. Debit")
    print("5. Check Balance")
    print("6. Change PIN")
    print("7. Admin Login")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        account_type = input("Enter Account Type (savings/current): ")
        balance = float(input("Enter Opening Balance: "))
        pin = input("Enter 4-Digit PIN: ")

        register_user(acc_no, name, account_type, balance, pin)

    elif choice == 2:
        acc_no = input("Enter Account Number: ")
        pin = input("Enter PIN: ")
        login_user(acc_no, pin)

    elif choice == 3:
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Credit: "))
        credit(acc_no, amount)

    elif choice == 4:
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Debit: "))
        debit(acc_no, amount)

    elif choice == 5:
        acc_no = input("Enter Account Number: ")
        check_balance(acc_no)

    elif choice == 6:
        acc_no = input("Enter Account Number: ")
        old_pin = input("Enter Old PIN: ")
        new_pin = input("Enter New PIN: ")
        change_pin(acc_no, old_pin, new_pin)


    elif choice == 7:
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")

        if admin_login(username, password):
            while True:
                print("\n--- ADMIN PANEL ---")
                print("1. View All Users")
                print("2. View All Transactions")
                print("3. Back to Main Menu")

                admin_choice = int(input("Enter choice: "))

                if admin_choice == 1:
                    view_all_users()

                elif admin_choice == 2:
                    view_all_transactions()

                elif admin_choice == 3:
                    break

                else:
                    print("Invalid admin choice!")
    elif choice == 8:
        print("Thank you! Exiting program...")
        break

    else:
        print("Invalid choice, try again!")
