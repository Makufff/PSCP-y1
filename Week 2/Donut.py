"""Donut"""
price = int(input())
amount = int(input())
free = int(input())
want = int(input())
in_want = want // (amount + free)
# base case
if not want:
    print("0 0")
elif want > 0:
    donut = in_want*(amount + free)
    t_l = want - donut
    if t_l > amount:
        t_l = amount
    if t_l >= amount:
        donut = donut + (amount + free)
    else:
        donut = donut + t_l
    print(f"{(price*in_want*amount) + (t_l*price)} {donut}")
