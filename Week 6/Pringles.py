"""Pringles"""
def pringles(l1, pringle, l2, lenght):
    """princles"""
    n_pring = 0
    for i in pringle:
        if i == ")":
            n_pring += 1
    pring = 0
    for i in pringle:
        if i == ")":
            pring += 1
        lenght -= 1
        if not lenght:
            break
    print(pring)
    print("None." if pring == n_pring else "There are still some left.")
    print(l1)
    for i in range(len(pringle)-1):
        if pringle[i] == ")":
            if not pring:
                print(")", end="")
            else:
                print(" ", end="")
                pring -= 1
        else:
            print(" ", end="")
    print("|")
    print(l2)
pringles(str(input()), str(input()), str(input()), int(input()))
