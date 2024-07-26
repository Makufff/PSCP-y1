"""Main"""
def main(width , height):
    """Mirror"""
    mid = height // 2
    for i in range(height):
        spaces = abs(mid - i)
        print(" " * spaces + "*" * width)
main(int(input()),int(input()))
