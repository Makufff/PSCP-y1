"""Coffee Shop"""
def calculate_promotion_1(a: float, b: float, e: int) -> float:
    """Calculate promotion 1."""
    return a + (e - 1) * a * (1 - b / 100)

def calculate_promotion_2(a: float, c: float, d: float, e: int) -> float:
    """Calculate promotion 2."""
    total = a * e
    if total >= d:
        return total * (1 - c / 100)
    return total

def main():
    """Main fn"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = int(input())

    price_1 = calculate_promotion_1(a, b, e)
    price_2 = calculate_promotion_2(a, c, d, e)

    if price_1 < price_2:
        best_promotion = 1
        best_price = price_1
    else:
        best_promotion = 2
        best_price = price_2

    # Print results
    print(best_promotion)
    print(f"{best_price:.2f}")

main()
