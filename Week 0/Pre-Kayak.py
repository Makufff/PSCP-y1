"""kaya"""
def kayak(n, lst, ans=0):
    """kaya"""
    for _ in range(n-1):
        m = [abs(lst[i]-lst[i+1]) for i in range(len(lst)-1)]
        ans += min(m)
        del lst[m.index(min(m)):m.index(min(m))+2]
    print(ans)
kayak(int(input()), sorted(list(map(int, input().split()))))
