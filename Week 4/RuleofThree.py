"""RuleofThree"""
def main(n):
    """Hello Guy"""
    best_value = 0
    best_price = 2e9
    best_size = 0
    for _ in range(n):
        price = float(input())
        weight = float(input())
        value = weight / price
        if value > best_value or (value == best_value and price < best_price):
            best_value = value
            best_price = price
            best_size = weight
    return f"{best_price:.2f} {best_size:.2f}"
print(main(int(input())))
