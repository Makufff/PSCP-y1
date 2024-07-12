"""rec"""
def find_area(h, w):
    """area"""
    return h * w
def find_perimeter(h, w):
    """perimeter"""
    return 2 * (h + w)
x = int(input())
y = int(input())
print(find_area(x, y))
print(find_perimeter(x, y))
