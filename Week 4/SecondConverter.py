"""Time"""
def main(k, s, m, h):
    """Savarudo !!"""
    seconds_per_minute = s
    seconds_per_hour = s * m
    seconds_per_day = s * m * h
    k %= seconds_per_day
    hours, k = divmod(k, seconds_per_hour)
    minutes, seconds = divmod(k, seconds_per_minute)
    return f"{hours}:{minutes}:{seconds}"
print(main(*[int(input()) for _ in range(4)]))
