"""BrickBridge"""
a = int(input())
b = int(input())
goal = int(input())
if goal - (min(b, goal // 5) * 5) <= a:
    print(goal - (min(b, goal // 5) * 5))
else:
    print(-1)
