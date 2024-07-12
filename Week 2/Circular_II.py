"""2circle"""
x1 = float(input())
y1 = float(input())
r1 = float(input())
x2 = float(input())
y2 = float(input())
r2 = float(input())
if ((x2 - x1)**2 + (y2 - y1)**2)**0.5 < r1 + r2:
    print("Yes")
else:
    print("No")
