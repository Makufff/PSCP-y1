"""IT Business"""
def decompress_transaction(transactions):
    """decompress"""
    transaction_type = ""
    amount = ""
    for char in transactions:
        if char.isalpha():
            transaction_type += char
        elif char.isdigit() or char == '.':
            amount += char
        elif char.isspace():
            continue
    amount = float(amount)
    return transaction_type, amount

def atm_simulation(account_balance:float ,cash_on_hand:float):
    """Simulate ATM"""
    failure_count = 0

    while True:
        transaction = input()
        if transaction.lower() == "end":
            break

        transaction_type, amount = decompress_transaction(transaction)

        if transaction_type == 'D':
            # Deposit
            if amount > cash_on_hand:
                failure_count += 1
            else:
                cash_on_hand -= amount
                account_balance += amount
                failure_count = 0

        elif transaction_type == 'W':
            # Withdraw
            if amount > account_balance:
                failure_count += 1
            else:
                account_balance -= amount
                cash_on_hand += amount
                failure_count = 0
        if failure_count >= 3:
            # chk failure
            break

    print(f"{account_balance:.2f}")
    print(f"{cash_on_hand:.2f}")

atm_simulation(float(input()) , float(input()))
