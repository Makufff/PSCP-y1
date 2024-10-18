"""APARTMENT"""
def revenue(a, b, c, d, e):
    """
    Problem
    # Case 1: Reduce price
    # Case 2: Increase price
    """
    m_ic = 0
    opt_rooms = c
    # Case 1
    curr_price = b
    rooms = c
    while curr_price > 0 and rooms <= a:
        income = curr_price * rooms
        if income > m_ic or (income == m_ic and rooms < opt_rooms):
            m_ic = income
            opt_rooms = rooms
        curr_price -= d
        rooms += 1
    # Case 2
    curr_price = b
    rooms = c
    while rooms >= 0:
        income = curr_price * rooms
        if income > m_ic or (income == m_ic and rooms < opt_rooms):
            m_ic = income
            opt_rooms = rooms
        curr_price += e
        rooms -= 1
    print(m_ic)
    print(opt_rooms)
revenue(int(input()),int(input()),int(input()),int(input()),int(input()))
