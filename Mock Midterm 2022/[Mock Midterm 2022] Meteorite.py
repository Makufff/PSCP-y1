"""ทำไรผิด? [Mock Midterm 2022] Meteorite"""
def meteorite(a, b, c):
    """shoot meteorite"""
    count = 0
    num_meteor = 1
    weigh = a
    if not a :
        print(0)
    elif a < c:
        print(0)
    else:
        while True:
            weigh /= b
            count += num_meteor
            if weigh < c:
                print(count)
                break
            num_meteor *= b
meteorite(float(input()), int(input()), float(input()))
