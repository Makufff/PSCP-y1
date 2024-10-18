"""Tuple's Sad life"""
def dont_have_life():
    """dont_have_life"""
    word = tuple(input().split())
    num = str(input())
    for _ in range(word.count(num)):
        for _ in range(word.count(num)):
            print(word.index(num), end=" ")
        print()
dont_have_life()
