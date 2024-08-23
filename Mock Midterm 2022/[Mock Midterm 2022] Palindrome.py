"""[Mock Midterm 2022] Palindrome"""
def palindrome( n : int , time : str):
    time.remove(":")
    cnt = 0
    while  cnt != n :
        if time == time[::-1]:
            cnt += 1
            print(time)
        time