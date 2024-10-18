"""PickThemAgain"""
def numbers_divisible():
    """divisible"""
    input_numbers = input().split()
    divisible_numbers = [int(num) for num in input_numbers if not int(num) % 3 or not int(num) % 5]
    if divisible_numbers:
        for number in reversed(divisible_numbers):
            print(number)
    else:
        print("Nope")
numbers_divisible()
