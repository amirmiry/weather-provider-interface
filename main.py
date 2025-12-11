#modules and global variables
from  abc import ABC, abstractmethod

class WeatherAbstract(ABC):
    @abstractmethod
    def get_current_weather(self , latitude, longitude):
        pass