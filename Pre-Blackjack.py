"""Blackjack"""
cnt_card = int(input())
cards = [input().upper() for _ in range(cnt_card)]
def score(cards):
    """Hamburger"""
    current_score = 0
    ace_count = 0
    for card in cards:
        if card in ["J", "Q", "K"]:
            current_score += 10
        elif card == "A":
            current_score += 11
            ace_count += 1
        else:   
            current_score += int(card)
    while current_score > 21 and ace_count > 0:
        current_score -= 10
        ace_count -= 1
    return current_score
print(score(cards))
