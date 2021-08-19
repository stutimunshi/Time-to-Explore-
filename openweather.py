from geopy.geocoders import Nominatim
import requests
import json

api_key = "05877ccc9ebd018c3ef5d8cc5f7d6806"

geolocator = Nominatim(user_agent="outdoor_activity_planner")
address = input("Enter Address: ")
location = geolocator.geocode(address)
lat = location.latitude
lon = location.longitude
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

response = requests.get(url)
data = json.loads(response.text)

current_temp = data["current"]["temp"] 
current_weather = data["current"]["weather"]
for dict in current_weather:
    for value in dict.values():
        weather_list = list(dict.values())
    print(weather_list[1] + "," + weather_list[2])
# weathertest = dict.fromkeys(current_weather)
print("Temperature is", current_temp, "degrees Celsius")
# print("The current weather is:", current_weather)


