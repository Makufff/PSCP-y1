"""US Interstate Number System"""
def major(street) :
    """Major"""
    if not (int(street) // 5) % 2 :
        print("Horizontal Major Interstate")
        print(f"I-{street}")
    else :
        print("Vertical Major Interstate")
        print(f"I-{street}")

def main(street) :
    """County road"""
    if int(street) % 5 or not int(street) :
        print("Others")
    elif len(street) < 3 :
        major(street)
    else :
        s1 = street[:-2]
        s23 = int(street[-2:])
        if not s23 :
            print("Others")
        elif not int(s1) % 2 :
            print("Even Minor Interstate")
            print(f"I-{s23}")
        else :
            print("Odd Minor Interstate")
            print(f"I-{s23}")
main(str(int(input())))
