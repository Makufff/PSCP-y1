"""Diginity"""
def diginity() -> None:
    """
    Calculate and print the digital root of input numbers.

    Args:
        None

    Returns:
        None
    """
    while True:
        num = input()
        if num == "0":
            break
        digital_root = (int(num) - 1) % 9 + 1 if int(num) else 0
        print(digital_root)

if __name__ == "__main__":
    diginity()
