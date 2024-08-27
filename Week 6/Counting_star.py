"""Counting Stars"""
def count_celestial_objects(sky_pattern: str) -> None:
    """
    Count and print the number of constellations, comets, and shooting stars in the sky.

    Args:
    sky_pattern (str): A string representing the sky pattern.

    Returns:
    None: Prints the counts of celestial objects or a message for a quiet night.
    """
    constellation = 0
    comet = 0
    shooting_star = 0
    current_pattern = ""

    for char in sky_pattern:
        current_pattern += char
        if current_pattern in ("~*", "*~"):
            comet += 1
            current_pattern = ""
        elif current_pattern == "*/":
            shooting_star += 1
            current_pattern = ""
        elif current_pattern == "**":
            constellation += 1
            current_pattern = ""
        elif len(current_pattern) == 2:
            current_pattern = current_pattern[1]

    if not any([comet, shooting_star, constellation]):
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting_star}")

if __name__ == "__main__":
    count_celestial_objects(input())
