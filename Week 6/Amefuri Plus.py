"""Calculate wetness levels"""
def calculate_wetness(start_time, weather_pattern):
    """
    Calculate the wetness level based on the given weather pattern.

    Args:
    start_time (str): The starting hour as a string (0-23)
    weather_pattern (str): A string of weather conditions

    Returns:
    float or str: The final wetness level or "Lost" if a hurricane occurs
    """

    wetness = 8.0
    current_time = int(start_time)

    for weather in weather_pattern:
        current_time %= 24

        if 6 <= current_time < 18:  # Daytime
            drying_rates = {'C': 0.50, 'N': 1.00, 'W': 1.50}
        else:  # Nighttime
            drying_rates = {'C': 0.25, 'N': 0.50, 'W': 0.75}

        wetness -= drying_rates.get(weather.upper(), 0)

        if weather.upper() == 'R':
            wetness += 2.00
        elif weather.upper() == 'S':
            wetness += 3.00
        elif weather.upper() == 'H':
            return "Lost"

        wetness = max(0, min(wetness, 16))
        current_time += 1

    return wetness

def main():
    """Read input"""
    start_time = input().strip()
    weather_pattern = input().strip()

    result = calculate_wetness(start_time, weather_pattern)

    if result == "Lost":
        print("Lost")
    elif result == 0:
        print("Dry")
    else:
        print(f"Still Wet (Wet Level: {result:.2f})")

if __name__ == "__main__":
    main()
