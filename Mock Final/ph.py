"""ph"""
def find_ph(value):
    """find ph"""
    ans = ""
    if value == 7 :
        ans = "neutral"
    elif 0 <= value < 7 :
        ans = "acidic"
    elif 14 >= value > 7 :
        ans = "akaline"
    else : ans = "error"
    return ans
print(find_ph(float(input())))
