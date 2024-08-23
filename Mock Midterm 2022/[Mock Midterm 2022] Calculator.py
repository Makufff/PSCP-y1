"""[Mock Midterm 2022] Calculator"""
def cal_press_btn(n : int) -> None :
    """calculate press button"""
    ans = 0
    for number in range(1, n+1 , 1):
        ans += len(str(number)) + 1
    if n == 1 :
        print(1)
    else:
        print(ans)
cal_press_btn(int(input()))
