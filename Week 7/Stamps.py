"""Stamps"""
def calculate_promotion(n, a, b, c, d):
    """
    Calculate the total amount paid and the remaining stamps after applying a promotion.

    Args:
        n (int): The number of bills.
        a (int): The amount of money spent to earn stamps.
        b (int): The number of stamps earned per 'a' amount spent.
        c (int): The number of stamps required for a discount.
        d (int): The discount amount per 'c' stamps used.

    Returns:
        None: The function prints the total amount paid and the remaining stamps.
    """

    total_paid = 0
    remaining_stamps = 0

    bills = [int(input().strip()) for _ in range(n)]

    for bill in bills:
        while remaining_stamps >= c and bill > 0:
            bill -= d
            remaining_stamps -= c

        if bill < 0:
            bill = 0

        total_paid += bill

        new_stamps = (bill // a) * b
        remaining_stamps += new_stamps

    print(total_paid)
    print(remaining_stamps)

calculate_promotion(int(input().strip()),
                    int(input().strip()),
                    int(input().strip()),
                    int(input().strip()),
                    int(input().strip()))
