"""Square"""
n = int(input())
for i in range(n):
    print(*range(i+2, i+n+2), sep=' ')
