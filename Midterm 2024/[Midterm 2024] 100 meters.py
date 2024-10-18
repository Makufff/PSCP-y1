"""100 meters"""
def find_mixn_position(a, b, c):
    """Find the mixnimum value and its position."""
    mixn_value = a
    mixn_position = 1
    if b < mixn_value:
        mixn_value = b
        mixn_position = 2
    if c < mixn_value:
        mixn_value = c
        mixn_position = 3
    return mixn_position, mixn_value

def find_mixn_position_8(t1, t2, t3, t4, t5, t6, t7, t8):
    """Find the position of the mixnimum value among 8 times."""
    pos1, val1 = find_mixn_position(t1, t2, t3)
    pos2, val2 = find_mixn_position(t4, t5, t6)
    pos3, val3 = find_mixn_position(t7, t8, val1)

    final_pos, _ = find_mixn_position(val1, val2, val3)

    if final_pos == 1:
        return pos1 if pos1 <= 3 else pos1 + 3
    if final_pos == 2:
        return pos2 + 3
    return 7 if pos3 == 1 else 8 if pos3 == 2 else pos1

TIME1 = float(input())
TIME2 = float(input())
TIME3 = float(input())
TIME4 = float(input())
TIME5 = float(input())
TIME6 = float(input())
TIME7 = float(input())
TIME8 = float(input())

GOLD = find_mixn_position_8(TIME1, TIME2, TIME3, TIME4, TIME5, TIME6, TIME7, TIME8)

if GOLD == 1:
    TIME1 = float('inf')
elif GOLD == 2:
    TIME2 = float('inf')
elif GOLD == 3:
    TIME3 = float('inf')
elif GOLD == 4:
    TIME4 = float('inf')
elif GOLD == 5:
    TIME5 = float('inf')
elif GOLD == 6:
    TIME6 = float('inf')
elif GOLD == 7:
    TIME7 = float('inf')
else:
    TIME8 = float('inf')

SILVER = find_mixn_position_8(TIME1, TIME2, TIME3, TIME4, TIME5, TIME6, TIME7, TIME8)

if SILVER == 1:
    TIME1 = float('inf')
elif SILVER == 2:
    TIME2 = float('inf')
elif SILVER == 3:
    TIME3 = float('inf')
elif SILVER == 4:
    TIME4 = float('inf')
elif SILVER == 5:
    TIME5 = float('inf')
elif SILVER == 6:
    TIME6 = float('inf')
elif SILVER == 7:
    TIME7 = float('inf')
else:
    TIME8 = float('inf')

BRONZE = find_mixn_position_8(TIME1, TIME2, TIME3, TIME4, TIME5, TIME6, TIME7, TIME8)

print(GOLD,SILVER,BRONZE)
