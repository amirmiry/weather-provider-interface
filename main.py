#modules and global variables
from  abc import ABC, abstractmethod
import requests

class WeatherAbstract(ABC):
    @abstractmethod
    def get_current_weather(self , latitude, longitude):
        pass




class OpenWeatherProvider(WeatherAbstract):

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