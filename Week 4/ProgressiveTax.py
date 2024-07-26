""" money EIEI"""
def main():
    """Waku Waku"""
    money = int(input())
    tax = 0
    if money > 4000000:
        cal = money - 4000000
        money -= cal
        tax += cal * 0.35
    if money > 2000000:
        cal = money - 2000000
        money -= cal
        tax += cal * 0.30
    if money > 1000000:
        cal = money - 1000000
        money -= cal
        tax += cal * 0.25
    if money > 750000:
        cal = money - 750000
        money -= cal
        tax += cal * 0.20
    if money > 500000:
        cal = money - 500000
        money -= cal
        tax += cal * 0.15
    if money > 300000:
        cal = money - 300000
        money -= cal
        tax += cal * 0.10
    if money > 150000:
        cal = money - 150000
        money -= cal
        tax += cal * 0.05
    if money > 0:
        pass
    print(int(tax))
main()
