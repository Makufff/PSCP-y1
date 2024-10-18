"""water"""
def calculate_water_bill(usage, a, b, c, d):
    """calculate water bill sing band :3"""
    if usage <= b:
        bill = usage * a
    else:
        bill = b * a + (usage - b) * c
    
    if bill <= d:
        return 0
    else:
        return bill
def main (n:int , a:float , b:float , c:float , d:float):
    """main function"""
    total_bill = 0
    for _ in range(n):
        usage = float(input())
        bill = calculate_water_bill(usage, a, b, c, d)
        total_bill += bill
    return total_bill
print(f"{main(int(input()),float(input()),float(input()),float(input()),float(input())):.2f}")
