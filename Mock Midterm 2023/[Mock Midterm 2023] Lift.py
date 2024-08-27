"""lift"""
def safe(pp, weight):
    """Check older."""
    agecheck = False
    total_weight = 0.0
    for _ in range(pp):
        if int(input()) >= 12:
            agecheck = True
        total_weight += float(input())
    if not pp or (agecheck and total_weight <= weight):
        print("Safe")
    else:
        print("Not Safe")

safe(int(input()), float(input()))
