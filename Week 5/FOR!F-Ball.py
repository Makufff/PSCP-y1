"""FOR!F-Ball problem aka Swap Ball"""
def ball_swap(text):
    """
    Find the last position of the ball after a series of swaps.

    The ball starts at position 1. Swaps are performed according to the following rules:
    - 'A' swaps positions 1 and 2
    - 'B' swaps positions 2 and 3
    - 'C' swaps positions 1 and 3

    Args:
    text (str): A string of characters representing the sequence of swaps.

    Returns:
    None: The function prints the final position of the ball.
    """
    last_pos = 1
    for char in text:
        if char == "A":
            if last_pos == 1:
                last_pos = 2
            elif last_pos == 2:
                last_pos = 1
        elif char == "B":
            if last_pos == 2:
                last_pos = 3
            elif last_pos == 3:
                last_pos = 2
        elif char == "C":
            if last_pos == 1:
                last_pos = 3
            elif last_pos == 3:
                last_pos = 1
    print(last_pos)

if __name__ == "__main__":
    ball_swap(input())
