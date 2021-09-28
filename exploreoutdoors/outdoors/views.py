from django.shortcuts import render
import json
import requests
import geopy.geocoders
from geopy.geocoders import Nominatim


# Create your views here.
def index(request):
    if request.method == "POST":
        api_key = "05877ccc9ebd018c3ef5d8cc5f7d6806"
        address = request.POST['address']
        geolocator = Nominatim(user_agent="outdoor_activity")
        location = geolocator.geocode(address)
        latitude = location.latitude
        longitude = location.longitude
        
        
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (latitude, longitude, api_key)
        
        response = requests.get(url)
        data = json.loads(response.text)

       
        current_weather = data["current"]["weather"]
        for dict in current_weather:
            for value in dict.values():
                weather_list = list(dict.values())
                # print(weather_list[1] + "," + weather_list[2])

        data = {
            "current_temp": data["current"]["temp"],
            "current_weather": weather_list[1] + "," + weather_list[2]
        }
        # print("Temperature is", current_temp, "degrees Celsius")    
    else:
        data = {}
    return render(request, 'index.html')
        
