"""Sqfree"""
def is_square_free(num):
    """Sqfree"""
    i = 2
    while i * i <= num:
        if not num % (i * i):
            return False
        i += 1
    return True

def count_square_free(n):
    """cnt Sqfree"""
    count = 0
    for num in range(1, n + 1):
        if is_square_free(num):
            count += 1
    return count

print(count_square_free(int(input())))
