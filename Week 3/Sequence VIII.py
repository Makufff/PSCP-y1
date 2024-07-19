"""feat : Fomat"""
n = int(input())
width = 3 * n - 1
for i in range(1, n+1):
    LINE = ' '.join(f'{j:02d}' for j in range(1, i+1))
    spaces = ' ' * (width - len(LINE))
    print(spaces + LINE)
