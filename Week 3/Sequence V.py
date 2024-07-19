"""Square"""
n = int(input())
for i in range(0, n, 7):
    print(*range(n-i, max(n-i-7, 0), -1), sep=' ')
