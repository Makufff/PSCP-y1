"""Waku Waku"""
def main():
    """Waku Waku"""
    order_food = float(input())
    promotion = float(input())
    discount = float(input())
    add = float(input())
    total = order_food + add
    discounted_total = total * (1 - discount/100) if total >= promotion else total
    discounted_order = order_food * (1 - discount/100) if order_food >= promotion else order_food
    difference = discounted_order - discounted_total
    if difference > 0:
        print(f"Yes {difference:.3f}")
    elif difference < 0:
        print(f"No {-difference:.3f}")
    else:
        print("Yes")
main()
