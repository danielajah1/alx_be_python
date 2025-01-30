class BankAccount:
    def __init__(self, initial_balance=0.0):
        """
        Initializes a bank account with an optional initial balance.
        """
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """
        Deducts the amount from the account balance if funds are sufficient.
        Returns True if withdrawal was successful, otherwise False.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
