"""Squre"""
n = int(input())
for _ in range(n):
    n = n *((_*0)+1)
    print(*range(1, n+1), sep=' ')
