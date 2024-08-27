"""[Mock Midterm 2023] Bonus"""
def bonus(r, y, m):
    """[Mock Midterm 2023] Bonus"""
    y += 1*(1 if m >= 10 else 0)
    y = 20 if y > 20 else y
    total = r*y
    total = 1000000 if total > 1000000 else total
    total = 5000 if total < 5000 else total
    print(total)
bonus(int(input()), int(input()), int(input()))
