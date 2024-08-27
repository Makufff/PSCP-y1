"""STAMPS"""
def calculate_promotion(n, a, b, c, d, bills):
    """
    ขี้เกียจแล้วใส่ไรก็ใส่มาเลย dynamic type ละ

    Args:
        ขี้เกียจแล้วใส่ไรก็ใส่มาเลย dynamic type ละ

    Returns:
        ขี้เกียจแล้วบอกแล้ว dynamic type ละ
    """
    total_spent = 0
    stamps = 0

    for bill in bills:
        if bill >= a:
            stamps += b

        while stamps >= c and bill >= d:
            stamps -= c
            bill -= d
        total_spent += bill
    return total_spent, stamps

def main():
    # Read input
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    bills = [int(input()) for _ in range(n)]

    total_spent, remaining_stamps = calculate_promotion(n, a, b, c, d, bills)

    print(total_spent)
    print(remaining_stamps)

if __name__ == "__main__":
    main()
