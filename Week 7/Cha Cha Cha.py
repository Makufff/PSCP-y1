"""Cha Cha Cha"""
import math
def main(n) :
    """Cha Cha Cha"""
    money = 0
    for _ in range(n) :
        h = math.ceil(float(input()))
        money += h * 8720
    print(int(money))
main(int(input()))
