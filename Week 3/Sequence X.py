"""I want Mirror"""
n = int(input())
def make_line(lines):
    """I Lazy line"""
    numbers = [f'{j:02d}' for j in range(1, i+1)] + [f'{j:02d}' for j in range(lines-1, 0, -1)]
    return ' '.join(numbers)
for i in range(1, n+1):
    spaces = ' ' * (3 * (n - i))
    print(spaces + make_line(i))
for i in range(n-1, 0, -1):
    spaces = ' ' * (3 * (n - i))
    print(spaces + make_line(i))
