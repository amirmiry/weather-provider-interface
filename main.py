#modules and global variables
from  abc import ABC, abstractmethod
import requests

class WeatherAbstract(ABC):
    @abstractmethod
    def get_current_weather(self , latitude, longitude):
        pass




class OpenWeatherProvider(WeatherAbstract):
    base_url ="https://pro.openweathermap.org/data/2.5/forecast"
    def __init__(self,  api_key):
        self.api_key = api_key


    def get_current_weather(self , latitude, longitude ):
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": self.api_key
        }
        respond = requests.get(self.base_url, params=params)
        normalize_data = {"temp": float(respond.json()["main"]["temp"])-273.15 , "humidity": respond.json()["main"]["humidity"] }
        return normalize_data


class OpenMeteoWeatherProvider(WeatherAbstract):
    base_url ="https://api.open-meteo.com/v1/forecast?"

    def get_current_weather(self, latitude, longitude):
        params = {
        "latitude" :latitude ,
        "longitude" :longitude ,
        "current" : "temperature_2m,relative_humidity_2m"
        }
        respond  = requests.get(self.base_url, params = params  )
        normalize_data = {"temp": respond.json()["current"]["temperature_2m"] , "humidity": respond.json()["current"]["relative_humidity_2m"] }
        return normalize_data
    

def get_user_input():
    while True:
        print("which one of the provider would you like to use?")
        print("1. OpenWeatherProvider")
        print("2. OpenMeteoWeatherProvider")
        answer = input("Enter your choice: ")
        try:
            answer = int(answer)
        except ValueError:
            print("Please enter a number")
            continue
        if 1<= answer<= 2:
            print("Please enter a number between choices")
        else:
            return answer