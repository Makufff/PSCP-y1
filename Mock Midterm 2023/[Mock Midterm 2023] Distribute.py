"""Distribute"""
def distribute(money, people):
    """Distribute money among people such that each person receives at least 8 units of money"""
    total = 0
    if money < people:
        print("-1")
    else:
        required_money = people * 8
        if money == required_money:
            total += people
        elif money > required_money:
            total += (people - 1)
        else:
            remaining_money = money - people
            total += remaining_money // 7
            if remaining_money % 7 == 3 and people - (remaining_money // 7) == 1:
                total -= 1
        print(total)

if __name__ == "__main__":
    distribute(int(input()), int(input()))