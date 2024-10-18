"""Runner"""
def find_winner():
    """speed and distance"""
    d = int(input())
    n = int(input())
    winner_index = -1
    min_time = float('inf')
    for i in range(n):
        speed, start = map(int, input().split())
        distance = d - start
        if distance <= 0:
            continue
        time = distance / speed
        if time < min_time or (time == min_time and speed > runner_speed):
            min_time = time
            winner_index = i + 1
            runner_speed = speed
    print(winner_index)
find_winner()
