"""easy"""
n = int(input())
for i in range(1, n+1):
    print(*range(1, i+1), sep=' ')
for i in range(n-1, 0, -1):
    print(*range(1, i+1), sep=' ')
