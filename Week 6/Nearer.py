"""Find Near"""
def find_nearer(alice: int, bob: int, icecream: int) -> None:
    """
    Find and print the person closer to the ice cream stand.

    Args:
        alice: Alice's position
        bob: Bob's position
        icecream: Ice cream stand's position

    Returns:
        None
    """
    distance_alice = abs(icecream - alice)
    distance_bob = abs(icecream - bob)

    if distance_alice < distance_bob:
        print(f"Alice {distance_alice}")
    elif distance_bob < distance_alice:
        print(f"Bob {distance_bob}")
    else:
        print(f"Sundaes {distance_alice}")

if __name__ == "__main__":
    find_nearer(int(input()), int(input()), int(input()))
