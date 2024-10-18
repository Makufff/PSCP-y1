"""Sort"""
def sort_(n:list):
    """sort"""
    n.sort()
    for x in n:
        print(x)
sort_([int(input()) for _ in range(int(input()))])
