"""Squid Game 3 - Tug-of-War"""
def main() :
    """Tug-of-War Rule"""
    a = 0
    b = 0
    for _ in range(10) :
        a += int(input())
    for _ in range(10) :
        b += int(input())
    if a > b :
        print("B")
    elif b > a :
        print("A")
    else :
        print("AB")
main()
