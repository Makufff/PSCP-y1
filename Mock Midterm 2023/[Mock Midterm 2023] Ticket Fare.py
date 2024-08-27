"""[Mock Midterm 2023] Ticket Fare"""
def ticket():
    """tickets"""
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    if f > n or g > n:
        print("Error")
    else:
        if g < f:
            f, g = g, f
        if g <= f+a:
            print(b)
        elif g <= f+a+c:
            print(b+((g-(f+a))*d))
        elif g > f+a+c:
            print(b+(c*d)+((g-(f+a+c))*e))
ticket()
