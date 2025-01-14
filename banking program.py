def show_balance(balance):
    print(f"Your balance is: $ {balance:.2f}")

def deposit():
    amount = float(input("Please enter the amount to deposit: "))

    if amount <= 0:
        print("Invalid amount, please try again!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Please enter the amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds!")
    elif amount <= 0:
        print("Invalid amount, please try again!")
        return 0
    else:
        return amount
    if amount <= 0:
        print("Invalid amount, please try again!")
        return 0
    elif amount > balance:
        print("Insufficient funds!")
        return 0
    else:
        return amount
def main():

    balance = 0
    is_running = True
    print()
    print("**********************************")
    print("Welcome to our banking program!")
    print("You can check your balance, deposit or withdraw money.")
    print("Please choose from the following menu:")
    print("**********************************")
    while is_running:
        print()
        print("Banking program")
        print()
        print("1 - Balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Exit")
        print()
        print("**********************************")
        
        choice = input("Please choose (1-4): ")

        print("**********************************")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice, please try again!")

    print("Thank you for using our banking program! Have a nice day!")

if __name__ == "__main__":
    main()