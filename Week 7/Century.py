"""century"""
from math import ceil

def find_century(lap):
    """Find the century"""

    for _ in range(lap):
        num = ""
        txt = input()

        for i in txt:
            if i.isnumeric():
                num += i

        if txt.startswith("A.D."):
            print(ceil(int(num) * 0.01))
        elif txt.startswith("B.E."):
            if int(num) < 544:
                print("ERROR")
            else:
                num = int(num) - 543
                print(ceil(num * 0.01))

if __name__ == "__main__":
    find_century(int(input()))
