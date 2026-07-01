import requests

city = input("Enter city name: ")

# Get latitude and longitude of the city
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

geo_response = requests.get(geo_url)

geo_data = geo_response.json()

if "results" not in geo_data:
    print("City not found!")
else:
    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    # Get weather data
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m"
    )

    weather_response = requests.get(weather_url)

    weather_data = weather_response.json()

    current = weather_data["current"]

    print("\nWeather Report")
    print("-" * 30)
    print("City:", city)
    print("Temperature:", current["temperature_2m"], "°C")
    print("Humidity:", current["relative_humidity_2m"], "%")