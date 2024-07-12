"""Plan"""
a = float(input())
b = float(input())
c = float(input())
c1 = abs(a**2 + b**2 - c**2) <= 0.01
c2 = abs(b**2 + c**2 - a**2) <= 0.01
c3 = abs(c**2 + a**2 - b**2) <= 0.01
if c1 or c2 or c3:
    print("Yes")
else:
    print("No")
