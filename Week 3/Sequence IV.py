"""Square"""
n = int(input())
for i in range(n):
    print(*range(i*n + 1, (i+1)*n + 1), sep=' ')
