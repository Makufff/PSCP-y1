"""[Mock Midterm 2022] Volleyball.py"""
def volleyball(txt):
    """Play volleyball."""
    point_a = 0
    point_b = 0
    sets = 1
    a_win = 0
    b_win = 0
    draw_check = 0

    for i in txt:
        point_a += 1 * (1 if i == "A" else 0)
        point_b += 1 * (1 if i == "B" else 0)

        if point_a == 24 and point_b == 24 and sets != 5:
            draw_check = 1

        if (point_b == 25 or point_a == 25) and not draw_check and sets != 5:
            print(f"Set {sets}: A ({point_a}) | B ({point_b})")
            a_win += 1 * (1 if point_a > point_b else 0)
            b_win += 1 * (1 if point_b > point_a else 0)
            point_b, point_a, sets = 0, 0, sets + 1

        if draw_check and abs(point_a - point_b) == 2 and sets != 5:
            print(f"Set {sets}: A ({point_a}) | B ({point_b})")
            a_win += 1 * (1 if point_a > point_b else 0)
            b_win += 1 * (1 if point_b > point_a else 0)
            point_b, point_a, sets, draw_check = 0, 0, sets + 1, 0

        if point_a == 14 and point_b == 14 and sets == 5:
            draw_check = 1

        if (point_b == 15 or point_a == 15) and not draw_check and sets == 5:
            print(f"Set {sets}: A ({point_a}) | B ({point_b})")
            a_win += 1 * (1 if point_a > point_b else 0)
            b_win += 1 * (1 if point_b > point_a else 0)
            point_b, point_a, sets = 0, 0, sets + 1

        if draw_check and abs(point_a - point_b) == 2 and sets == 5:
            print(f"Set {sets}: A ({point_a}) | B ({point_b})")
            a_win += 1 * (1 if point_a > point_b else 0)
            b_win += 1 * (1 if point_b > point_a else 0)
            point_b, point_a, sets, draw_check = 0, 0, sets + 1, 0

        if a_win == 3 or b_win == 3:
            break

    if sets != 6 and a_win != 3 and b_win != 3:
        print(f"Set {sets}: A ({point_a}) | B ({point_b})")

    if a_win == 3:
        print(f"A won {a_win}:{b_win} set")
    elif b_win == 3:
        print(f"B won {b_win}:{a_win} set")
    else:
        print("The game has not finished yet.")

volleyball(input())
