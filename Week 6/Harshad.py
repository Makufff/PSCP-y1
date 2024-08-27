"""Harshad"""
def hashs():
    """check hashs"""
    for _ in range(10):
        check = 0
        num = abs(int(input()))
        for i in range(0, len(str(num))):
            check += int(str(num)[i])
        if  not num:
            print("No")
        elif not num%check:
            print("Yes")
        else:
            print("No")
hashs()
