"""Drying Na Krub"""
def drying_simulation(start_hour: int, weather_log: str) -> None:
    """Drying Simulation"""
    wetness = 8.0
    hour = start_hour % 24

    day_weather = {'c': -0.5, 'n': -1.0, 'w': -1.5}
    night_weather = {'c': -0.25, 'n': -0.5, 'w': -0.75}
    rain_weather = {'r': 2.0, 's': 3.0}

    for weather in weather_log.lower():
        if weather == 'h':
            print("Lost")
            return

        if weather in rain_weather:
            wetness += rain_weather[weather]
        elif weather in day_weather or weather in night_weather:
            if 6 <= hour < 18:
                wetness += day_weather.get(weather, 0)
            else:
                wetness += night_weather.get(weather, 0)

        wetness = max(0, min(wetness, 16))

        if not wetness:
            print("Dry")
            return

        hour = (hour + 1) % 24

    if not wetness:
        print("Dry")
    else:
        print(f"Still Wet (Wet Level: {wetness:.2f})")

drying_simulation(int(input()), input())
