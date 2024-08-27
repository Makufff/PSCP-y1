"""Saint Seiya"""
def saintseiya(seconds, punch):
    """One Punch"""
    total_punch = 0
    for i in range(2, seconds + 1, 2):
        if total_punch >= punch:
            total_punch += 12 * (seconds - i + 1)
            break
        if not i % 6:
            total_punch += 1
        else:
            total_punch += 165
    return total_punch

print(saintseiya(int(input()), int(input())))
