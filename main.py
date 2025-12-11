#modules and global variables
from  abc import ABC, abstractmethod

class WeatherAbstract(ABC):
    @abstractmethod
    def get_current_weather(self , latitude, longitude):
        pass




class OpenWeatherProvider(WeatherAbstract):

    def __init__(self,  api_key):
        self.api_key = api_key


    def get_current_weather(self , latitude, longitude ):
        pass



class OpenMeteoWeatherProvider(WeatherAbstract):
    base_url ="https://api.open-meteo.com/v1/forecast?"

    def get_current_weather(self, latitude, longitude):
        respond  = requests.get(self.base_url + "&lat=" + str(latitude) + "&lon=" + str(longitude))
