"""Fizz"""
def main(count):
    """Buzz"""
    for i in range(1, count + 1):
        if not i % 3 and not i % 5:
            print("FizzBuzz")
        elif not i % 3:
            print("Fizz")
        elif not i % 5:
            print("Buzz")
        else:
            print(i)
main(int(input()))
