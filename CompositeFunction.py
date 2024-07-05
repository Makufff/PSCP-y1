"""function"""
def f(x):
    """f(x)"""
    return 2 * x
def g(x):
    """g(x)"""
    return x / 2 + 1
inputs = int(input())
fgx = f(g(inputs))
gfx = g(f(inputs))
print(f"{fgx:.2f}")
print(f"{gfx:.2f}")
