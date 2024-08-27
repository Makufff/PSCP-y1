"""ELO"""
def calculate_win_probability(rating_a: int, rating_b: int) -> tuple[float, float]:
    """
    Calculate win probabilities for two players based on their Elo ratings.

    Args:
        rating_a (int): Elo rating of player A
        rating_b (int): Elo rating of player B

    Returns:
        tuple[float, float]: Win probabilities for player A and player B
    """

    probability_a = 1 / (1 + (10 ** ((rating_b - rating_a) / 400)))
    probability_b = 1 / (1 + (10 ** ((rating_a - rating_b) / 400)))

    return probability_a, probability_b

def main():
    """Main function"""
    rating_a = int(input())
    rating_b = int(input())
    player = input()

    prob_a, prob_b = calculate_win_probability(rating_a, rating_b)

    if player == "A":
        print(f"{prob_a:.2f}")
    else:
        print(f"{prob_b:.2f}")

if __name__ == "__main__":
    main()
