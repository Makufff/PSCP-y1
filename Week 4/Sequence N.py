"""Damm"""
def main(n):
    """Not Love Sequence"""
    for i in range(n):
        for j in range(n):
            if j in {n - 1, 0, i}:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
