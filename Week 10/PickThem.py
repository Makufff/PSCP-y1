"""json"""
from json import loads
def main():
    """main"""
    cnt = 0
    lst = loads(input())
    for i in lst:
        if not i % 2 :
            cnt+=1
            print(i)
    if not cnt :
        print("Nope")
main()
