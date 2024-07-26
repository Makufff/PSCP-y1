"""Chrimas"""
def main(width,height):
    """Kiss mas"""
    for i in range(1, width + 1):
        print(f"{' '*(width-i)}{'*'*(2*i-1)}")
    trunk = f"{' '*(width-2)}---\n"
    print(trunk * height, end='')
main(int(input()), int(input()))
