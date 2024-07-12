"""CMP"""
def cmp(val_1, val_2):
    """cmp"""
    if val_1 > val_2:
        return val_1
    return val_2
a,b,c = input(),input(),input()
curr = a + b + c
curr = cmp((a + c + b), curr)
curr = cmp((b + a + c), curr)
curr = cmp((b + c + a), curr)
curr = cmp((c + b + a), curr)
curr = cmp((c + a + b), curr)
print(int(curr))
