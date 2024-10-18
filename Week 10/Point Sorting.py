"""point sort"""
def sort_points():
    """point sort"""
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = []
        for _ in range(N):
            x, y = map(int, input().split())
            points.append((x, y))
        sorted_points = sorted(points, key=lambda p: (p[0] + p[1], -p[1]))
        for x, y in sorted_points:
            print(x, y)
sort_points()
