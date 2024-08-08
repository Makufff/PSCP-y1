"""sequence xxx problem"""
def print_sequence_xxx(height, width):
    """
    Print a sequence of patterns based on given height and width.

    Args:
    height (int): The height of each pattern (number of rows).
    width (int): The number of patterns to print in each row.
    """
    for row in range(height):
        if row in (0, height - 1):
            # Print top and bottom rows
            print(f"{'*' * height} " * width)
        else:
            # Print middle rows
            for _ in range(width):
                for col in range(height):
                    if col in {row, 0, height - 1, height - 1 - row}:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print(" ", end="")
            print()

def main():
    """Main function to run the sequence XXX printer."""
    height = int(input().strip())
    width = int(input().strip())
    print_sequence_xxx(height, width)

if __name__ == "__main__":
    main()
