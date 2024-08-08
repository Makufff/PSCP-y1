"""RockPaperScissor Game"""
def play_game(moves):
    """Play the Rock Paper Scissors game and return the scores."""
    rules = {
        'R': {'S': 1, 'P': -1, 'R': 0},
        'P': {'R': 1, 'S': -1, 'P': 0},
        'S': {'P': 1, 'R': -1, 'S': 0}
    }

    score_a = score_b = 0
    for move_a, move_b in moves:
        result = rules[move_a][move_b]
        if result > 0:
            score_a += 1
        elif result < 0:
            score_b += 1

    return score_a,score_b

def parse_input(input_string):
    """Parse the input string into a list of move pairs."""
    moves = []
    for i in range(0, len(input_string), 2):
        if i + 1 < len(input_string):
            moves.append((input_string[i], input_string[i+1]))
    return moves

def main():
    """Main function to run the Rock Paper Scissors game."""
    input_string = input().strip()
    moves = parse_input(input_string)
    score_a, score_b = play_game(moves)

    if score_a == score_b:
        print(f"DRAW {score_a}")
    elif score_a > score_b:
        print(f"A win {score_a}-{score_b}")
    else:
        print(f"B win {score_b}-{score_a}")

if __name__ == "__main__":
    main()
