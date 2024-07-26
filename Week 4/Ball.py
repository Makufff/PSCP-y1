"""ball"""
def main(height):
    """sigma"""
    count = -1 #โยนไม่นับ
    while height >= 0.01:
        height = height * 3 / 5
        count += 1
    print(count)
main(float(input()))
