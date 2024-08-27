"""[Mock Midterm 2022] Palindrome"""
def main(n, time) :
    """TIme"""
    time = time[:time.find(":")] + time[time.find(":") + 1:]
    count = 0
    while count < n :
        time = str(int(time) + 1)
        if int(time[-2:]) > 59 :
            time = str((int(time) - 60) + 100)
        if int(time) > 2359 :
            time = "0" + str(int(time) - 2400)
        if len(time) < 3 :
            time = f"{time:>03}"
        time_b = time[::-1]
        if time == time_b :
            count += 1
            print(f"{time[:-2]:>01}:{time[-2:]:>02}")
main(int(input()), input())
