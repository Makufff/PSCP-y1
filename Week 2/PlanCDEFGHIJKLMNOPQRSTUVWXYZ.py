"""I want Sorting"""
order = input()
a = float(input())
b = float(input())
c = float(input())
if order == "Ascend":
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
elif order == "Descend":
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
print(f"{a:.2f}, {b:.2f}, {c:.2f}")
