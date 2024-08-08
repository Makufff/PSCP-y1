"""Run legth Encode"""
def run_length_encode(text):
    """
    Perform run-length encoding on the input text.

    Args:
    text (str): The input string to be encoded.

    Returns:
    str: The run-length encoded string.
    """
    if not text:
        return ""

    encoded = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            encoded.append(f"{count}{text[i-1]}")
            count = 1

    encoded.append(f"{count}{text[-1]}")
    return "".join(encoded)

def main():
    """Main function to run the run-length encoding program."""
    input_text = input().strip()
    encoded_text = run_length_encode(input_text)
    print(encoded_text, end='')

if __name__ == "__main__":
    main()
