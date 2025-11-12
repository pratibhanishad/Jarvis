import requests
import json
from FUNCTION.JARVIS_SPEAK.speak import speak


def get_temperature_openweathermap(city):
    api_key = "3a1d3209792e818454a51eb52459eac7"
    endpoint = "https://api.openweathermap.org/data/2.5/weather"

    response = requests.get(endpoint, params={"q": city,"appid": api_key,"units": "metric"})
    if response.status_code ==200:
        data = json.loads(response.text)

        if 'main' in data:
            temperature_celsius = data["main"]["temp"]
            return temperature_celsius
        else:
            print("Error:'main'key not found in API response")
    else:
        print(f"Error:Failed to fetch data from API. Status code:{response.status_code}")

    return None

def Temp():
    city = "Gorakhpur, Mirzapur, Lucknow"
    temperature_celsius =  get_temperature_openweathermap(city)

    if temperature_celsius is not None:
        speak(f"The weather in {city} is {temperature_celsius}°C")
    else:
        print("Temperature data not available.")

