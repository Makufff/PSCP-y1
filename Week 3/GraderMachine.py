"""HS"""
def main(start,stop) :
    """main"""
    Ps , Sm = "" , 0
    z = -1 if start > stop else 1
    for i in range(start,stop + z,z) :
        if not i % 2 :
            Ps += str(i) + " "
            Sm += i
    print(f"pass : {Ps}")
    print(f"Sum : {Sm}")
main(int(input()),int(input()))
