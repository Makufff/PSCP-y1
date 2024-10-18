"""Max Diamond"""
def max_diamond_value(m,n):
    """calu max diamond"""
    diamond_values = [list(map(int, input().split())) for _ in range(m)]
    max_value = 0
    for col in range(n):
        total = sum(diamond_values[row][col] for row in range(m))
        max_value = max(max_value, total)
    print(max_value)
max_diamond_value(int(input()),int(input()))
