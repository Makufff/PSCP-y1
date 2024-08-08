"""Parallelogram.py"""
def print_parallelogram(text):
    """
    Print the given text in a parallelogram shape.

    Args:
    text (str): The input string to be printed as a parallelogram.
    """
    text_length = len(text)

    # Print upper half of the parallelogram
    for i in range(text_length):
        spaces = " " * (text_length - i - 1)
        print(f"{spaces}{text[:i+1]}")

    # Print lower half of the parallelogram
    for i in range(1, text_length):
        print(text[i:])

def main():
    """Main function to run the parallelogram printer."""
    input_text = input().strip()
    print_parallelogram(input_text)

if __name__ == "__main__":
    main()
