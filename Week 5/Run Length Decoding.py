"""run length decode"""
def run_length_decode(encoded_text):
    """
    Perform run-length decoding on the input text.

    Args:
    encoded_text (str): The input string to be decoded.

    Returns:
    str: The run-length decoded string.
    """
    decoded = []
    count = ''
    for char in encoded_text:
        if char.isdigit():
            count += char
        else:
            decoded.append(int(count) * char)
            count = ''
    return ''.join(decoded)

def main():
    """Main function to run the run-length decoding program."""
    encoded_text = input().strip()
    decoded_text = run_length_decode(encoded_text)
    print(decoded_text, end='')

if __name__ == "__main__":
    main()
