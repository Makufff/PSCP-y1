"""CMP"""
num1 = input()
num2 = input()
num3 = input()
def cmp(a, b):
    """cmp"""
    return a + b > b + a
if cmp(num1, num2) and cmp(num1, num3):
    if cmp(num2, num3):
        result = num1 + num2 + num3
    else:
        result = num1 + num3 + num2
elif cmp(num2, num1) and cmp(num2, num3):
    if cmp(num1, num3):
        result = num2 + num1 + num3
    else:
        result = num2 + num3 + num1
else:
    if cmp(num1, num2):
        result = num3 + num1 + num2
    else:
        result = num3 + num2 + num1
print(result)
