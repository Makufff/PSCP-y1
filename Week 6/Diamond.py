"""diamond_pattern"""
def diamond_pattern(num):
    """Bruhhh"""
    for i in range(num):
        for j in range(num):
            if i == num//2 or j - i == num//2 or i + j == num//2 \
            or i - j == num//2 or j+i == num+(num//2)-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
diamond_pattern(int(input()))
