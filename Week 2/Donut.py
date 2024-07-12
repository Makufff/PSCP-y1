"""Donut"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
promotion_sets = (d - 1) // (b + c) + 1 if b + c > 0 else d
total_donuts = promotion_sets * (b + c)
total_cost = promotion_sets * b * a
if total_donuts < d:
    extra_donuts = d - total_donuts
    total_cost += extra_donuts * a
    total_donuts = d
print(f"{total_cost} {total_donuts}")
