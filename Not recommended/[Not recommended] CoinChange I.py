"""Coin Change I"""
def min_coins(m):
    """use dp"""
    cache = [2e9] * (m + 1)
    cache[0] = 0
    for i in range(1, m + 1):
        if i >= 1:
            cache[i] = min(cache[i], cache[i - 1] + 1)
        if i >= 7:
            cache[i] = min(cache[i], cache[i - 7] + 1)
        if i >= 11:
            cache[i] = min(cache[i], cache[i - 11] + 1)
    return cache[m]
print(min_coins(int(input())))
