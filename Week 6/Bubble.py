"""bb"""
def main(bb) :
    """Simulate Jump"""
    cnt = 0
    n = 0
    while n < len(bb) - 1 :
        c = 0
        if bb[n] == "^" :
            cnt += 1
            n += 1
        elif bb[n].islower() :
            cnt += 1
            n += 1
        elif bb[n].isupper() :
            cnt += 1
            n += 3
            if n >= len(bb) - 1 :
                break
            if bb[n].islower() :
                n -= 1
                c += 1
            if bb[n].islower() :
                n -= 1
                c += 1
            if not bb[n].isupper() :
                n += c
            if bb[n].isspace() :
                n -= 1
            if bb[n].isspace() :
                n -= 1
        if bb[n].isspace() :
            print("IMPOSSIBLE")
            print(len(bb) - n)
            return
    print("POSSIBLE")
    print(cnt)
main(input())
