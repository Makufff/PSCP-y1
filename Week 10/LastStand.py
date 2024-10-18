"""json"""
from json import loads
def main():
    """main"""
    lst = loads(input())
    for i in lst:
        print(str(i)[-1])
main()
