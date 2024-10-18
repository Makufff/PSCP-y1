"""Difference"""
def difference(numa, numb):
    """Learn to use set"""
    set_a = set(int(input()) for _ in range(numa))
    set_b = set(int(input()) for _ in range(numb))
    print(*sorted(set_a.difference(set_b)))
difference(int(input()), int(input()))
