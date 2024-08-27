"""turnstile machine"""
def count_turnstile_passes() -> int:
    """
    Count the number of successful passes through a turnstile.

    Returns:
        int: The number of successful passes through the turnstile.
    """
    coin_inserted = False
    pass_count = 0

    while True:
        action = input().strip().upper()

        if action == "END":
            break

        if action == "C":
            coin_inserted = True
        elif action == "P" and coin_inserted:
            pass_count += 1
            coin_inserted = False

    return pass_count


def main():
    """Main function"""
    print(count_turnstile_passes())

if __name__ == "__main__":
    main()
