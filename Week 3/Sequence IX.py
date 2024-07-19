"""feat : Fomat"""
n = int(input())
for i in range(1, n+1):
    numbers = [f'{j:02d}' for j in range(1, i+1)] + [f'{j:02d}' for j in range(i-1, 0, -1)]
    LINE = ' '.join(numbers)
    SPACES = ' ' * (3 * (n - i))
    print(SPACES + LINE)
