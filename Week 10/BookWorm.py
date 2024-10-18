"""Book worm"""
def max_books():
    """Book worm"""
    T = int(input())
    for _ in range(T):
        available_time = float(input())
        k = int(input())
        reading_times = [float(input()) for _ in range(k)]
        reading_times.sort()
        count, total_time = 0, 0
        for time in reading_times:
            if total_time + time <= available_time:
                total_time += time
                count += 1
            else:
                break
        print(count)
max_books()
