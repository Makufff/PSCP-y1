"""Easy Histogram No Dict"""
from collections import Counter
def histogram(s):
    """Easy Histogram No Dict - Separate Uppercase and Lowercase"""
    counts = Counter(c for c in s if c.isalpha())
    for c in range(97, 123):
        lower = chr(c)
        upper = lower.upper()
        if lower in counts:
            print(f"{lower} = {counts[lower]}")
        if upper in counts:
            print(f"{upper} = {counts[upper]}")
histogram(input())
