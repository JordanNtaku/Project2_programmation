class BankAccount:
    def __init__(self, initial_balance=0, pin=0):
        self.balance = initial_balance
        self.pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Current balance: ${self.balance}")


def set_pin():
    pin = input("Set a 4-digit PIN for your account: ")
    while not pin.isdigit() or len(pin) != 4:
        print("Invalid PIN. Please enter a 4-digit number.")
        pin = input("Set a 4-digit PIN for your account: ")
    return int(pin)


def authenticate_user(account):
    entered_pin = input("Enter your 4-digit PIN to access your account: ")
    while entered_pin != str(account.pin):
        print("Incorrect PIN. Please try again.")
        entered_pin = input("Enter your 4-digit PIN to access your account: ")
    print("\nAccess granted. Welcome to your bank account!")


def main():
    # Set a PIN for the bank account
    pin = set_pin()

    # Create a new bank account with an initial balance of $1000 and the specified PIN
    account = BankAccount(initial_balance=1000, pin=pin)

    # Authenticate the user before proceeding to operations
    authenticate_user(account)

    while True:
        print("\nBanking Operations:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
