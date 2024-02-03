import requests


def _is_rainy(weather_data):
    # Check for rain in the weather conditions
    weather_conditions = weather_data.get("weather", [])
    for condition in weather_conditions:
        if "rain" in condition["description"].lower() or condition["id"] in range(500, 532):
            return True

    if "rain" in weather_data:
        return True

    return False


def get_current_weather():
    api_key = "YOUR_API_KEY_FROM_THE_OPEN_WEATHER_WEBSITE"  # todo move this to env
    city = "New York"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    return _is_rainy(data)
