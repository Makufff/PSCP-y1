"""Post Office"""
def calculate_boxx(weight):
    """Calculate weight."""
    bath = 0
    if weight <= 500:
        bath =  45
    elif weight <= 1000:
        bath = 55
    else:
        bath = 70
    return bath

def calculate_soong(weight):
    """Calculate weight."""
    bath = 0
    if weight <= 10:
        bath =  16
    elif weight <= 20:
        bath = 18
    elif weight <= 100:
        bath = 23
    elif weight <= 250:
        bath = 28
    elif weight <= 500:
        bath = 33
    elif weight <= 1000:
        bath = 48
    else:
        bath = 68
    return bath

def main():
    "main function"
    n = int(input())
    m = int(input())

    total_fee = 0

    for _ in range(n):
        weight = float(input())
        total_fee += calculate_soong(weight) + 13

    for _ in range(m):
        weight = float(input())
        total_fee += calculate_boxx(weight) + 15
    print(int(total_fee))

main()
