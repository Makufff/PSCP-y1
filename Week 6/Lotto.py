"""Lottery"""
def lottery(f_n, sec, t1_n, t2_n, t3_n):
    """find balance"""
    t4_n = input()
    lot = input()
    balance = 0

    if lot == f_n:
        balance += 6000000

    if f_n == "000000" and lot in {"000001", "999999"}:
        balance += 100000
    elif f_n == "999999" and lot in {"000000", "999998"}:
        balance += 100000
    else:
        lot_int = int(lot)
        f_n_int = int(f_n)
        if f"{lot_int:06d}" in {f"{f_n_int-1:06d}", f"{f_n_int+1:06d}"}:
            balance += 100000

    if lot[-2:] == sec:
        balance += 2000
    if lot[0:3] == t1_n:
        balance += 4000
    if lot[0:3] == t2_n:
        balance += 4000
    if lot[-3:] == t3_n:
        balance += 4000
    if lot[-3:] == t4_n:
        balance += 4000
    print(balance)
lottery(input(), input(), input(), input(), input())
