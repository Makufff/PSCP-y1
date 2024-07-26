"""Right Arrow"""
def main(width , height):
    """Mirror"""
    star_line = "*" * width
    mid = height // 2
    for i in range(height):
        spaces = i if i <= mid else height - i - 1
        print(" " * spaces + star_line)
main(int(input()),int(input()))
