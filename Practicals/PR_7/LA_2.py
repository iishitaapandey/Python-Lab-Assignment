balance = 0

def show_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amt = float(input("Enter amount to deposit: "))
    balance += amt
    print("Deposited successfully")

def withdraw():
    global balance
    amt = float(input("Enter amount to withdraw: "))
    if amt <= balance:
        balance -= amt
        print("Withdraw successful")
    else:
        print("Insufficient balance")

while True:
    print("\n--- BANK MENU ---")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 4:
        break
    elif ch == 1:
        show_balance()
    elif ch == 2:
        deposit()
    elif ch == 3:
        withdraw()
    else:
        print("Invalid choice")