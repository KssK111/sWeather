import requests
import configparser
import Functions

settings = configparser.ConfigParser()
settings.read("settings.ini")

api_key = settings.get("basic_settings", "api_key")
city = settings.get("basic_settings", "city")
link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
multiplier = 1

data = requests.get(link)
if data.status_code == 200:
    data = data.json()
else:
    print(f"Error: {data.status_code}")

Functions.print_weatherAPI(data, settings)
input("End:")
