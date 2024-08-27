"""books"""
from math import ceil as c

def books(n, k, x, y):
    """read all"""
    pages = k
    day_count = 0
    checktimeout = False
    while n:
        if c(k*(x/y)) >= k:
            checktimeout = True
            break
        pages -= c(k*(x/y))
        day_count += 1
        x += 1
        y += 1
        if pages <= 0:
            n -= 1
            pages = k
    if checktimeout:
        day_count += n
    print(day_count)

books(int(input()), int(input()), int(input()), int(input()))
