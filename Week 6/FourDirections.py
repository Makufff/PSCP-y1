"""FourDirections"""
def lines1(text):
    """1"""
    for _ in text:
        print("  *  ", end=" ")
def lines2(text):
    """2"""
    for i in text:
        if i == "L":
            print(" *   ", end=" ")
        elif i == "R":
            print("   * ", end=" ")
        elif i == "U":
            print(" *** ", end=" ")
        elif i == "D":
            print("  *  ", end=" ")
def lines3(text):
    """3"""
    for i in text:
        if i == "L":
            print("*****", end=" ")
        elif i == "R":
            print("*****", end=" ")
        elif i == "U":
            print("* * *", end=" ")
        elif i == "D":
            print("* * *", end=" ")
def lines4(text):
    """4"""
    for i in text:
        if i == "L":
            print(" *   ", end=" ")
        elif i == "R":
            print("   * ", end=" ")
        elif i == "U":
            print("  *  ", end=" ")
        elif i == "D":
            print(" *** ", end=" ")
def fourdiractionmain(text):
    """Simulation"""
    lines1(text)
    print()
    lines2(text)
    print()
    lines3(text)
    print()
    lines4(text)
    print()
    lines1(text)
fourdiractionmain(input())
