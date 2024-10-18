"""BusStop I"""
def busstop(m_pp, bus_stop):
    """count station"""
    ans = 0
    lst1, lst2 = [], []
    for _ in range(bus_stop):
        lst1.append(input().strip().split())
    lst1.sort(key=lambda x: int(x[0]))
    for i in lst1:
        del i[0]
    for station in range(1, bus_stop+1):
        if station != 1 and len(lst2) > 0:
            if str(station) in lst2:
                for _ in range(lst2.count(str(station))):
                    lst2.remove(str(station))
                    ans += 1
        for i in lst1[station-1]:
            if int(i) > station and len(lst2) < m_pp:
                lst2.append(i)
    print(ans)
busstop(int(input()), int(input()))
