import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100.0)  # Example initial balance

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        if account.deposit(amount):
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command. Use 'deposit:<amount>', 'withdraw:<amount>', or 'display'.")

if __name__ == "__main__":
    main()
