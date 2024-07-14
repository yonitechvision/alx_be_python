import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_input = sys.argv[1]
    command, *params = command_input.split(':')

    if command not in ["deposit", "withdraw", "display"]:
        print("Invalid command.")
        sys.exit(1)

    if command in ["deposit", "withdraw"] and not params:
        print("Amount is required for deposit and withdraw commands.")
        sys.exit(1)

    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()

if __name__ == "__main__":
    main()

