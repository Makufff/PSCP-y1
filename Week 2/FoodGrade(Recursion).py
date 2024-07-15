"""Food"""
def check_weight(weight,curr_cnt = 0,loop=24):
    """Recursive"""
    if 50 <= weight <= 70:
        curr_cnt += 1
    loop -= 1
    if loop > 0 :
        return check_weight(int(input()) , curr_cnt , loop)
    return curr_cnt
print(check_weight(int(input())))
