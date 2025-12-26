class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def get_balance(self):
        return self.__balance


# ---------------- MAIN PROGRAM ----------------

try:
    name = input("Enter account holder name: ")
    balance = int(input("Enter initial balance: "))

    account = BankAccount(name, balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amt = int(input("Enter deposit amount: "))
            account.deposit(amt)

        elif choice == "2":
            amt = int(input("Enter withdraw amount: "))
            account.withdraw(amt)

        elif choice == "3":
            print("Current Balance:", account.get_balance())

        elif choice == "4":
            print("Thank you for using the bank system")
            break

        else:
            print("Invalid choice")

except ValueError:
    print("❌ Please enter valid numbers only")
