from datetime import datetime


# -------------------------
# Amount Class
# -------------------------
class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = float(amount)
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.timestamp} | {self.transaction_type} | ${self.amount:.2f}"


# -------------------------
# PersonalAccount Class
# -------------------------
class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        self.balance += amount
        print(f"Deposited ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        transaction = Amount(amount, "WITHDRAWAL")
        self.transactions.append(transaction)
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}")

    def print_transaction_history(self):
        if not self.transactions:
            print("No transactions found.")
            return

        print("\n--- Transaction History ---")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: ${self.balance:.2f}")


# -------------------------
# Interactive Menu
# -------------------------
if __name__ == "__main__":

    print("==== Personal Account System ====")
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")

    account = PersonalAccount(account_number, account_holder)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Show Transaction History")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except:
                print("Invalid amount.")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except:
                print("Invalid amount.")

        elif choice == "3":
            print(f"Current Balance: ${account.get_balance():.2f}")

        elif choice == "4":
            account.print_transaction_history()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
