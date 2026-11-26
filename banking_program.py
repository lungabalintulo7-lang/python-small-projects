
def show_balance():
    print(f"Your balance is: R{balance:.2f}")

def deposit():
    amount = float(input("Enter the amount you want to deposit: R"))

    if amount < 0:
        print("Invalid amount. Please enter a positive value.")
        return 0 
    else:
        print(f"R{amount:.2f} has been deposited successfully. Your new balance is: R{balance + amount:.2f}")
        return amount

def withdraw():

    amount = float(input("Enter the amount you want to withdraw: R"))

    if amount > balance:
        print("Insufficient funds. Please enter a smaller amount.")
        return 0
    elif amount < 0:
        print("Invalid amount. Please enter a positive value.")
        return 0
    else:
        print(f"R{amount:.2f} has been withdrawn successfully. Your new balance is: R{balance - amount:.2f}")
        return amount

balance = 0 
is_running = True

while is_running:
    print("------------------------------")
    print("Welcome to Lunga's Bank")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4.Exit")
    print("------------------------------")
    
    choice = input("Enter your choice (1 - 4): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
       balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        print("Thank you for using Lunga's Bank. Goodbye!")
        is_running = False
    else:
        print("Invalid choice. Please try again.")
        
