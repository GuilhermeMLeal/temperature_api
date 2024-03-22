# models.py
from django.db import models

class WeatherEntity:

    def __init__(self, temperature=0, date='',
                 city='', atmosphericPressure=0,
                 humidity=0, weather='') -> None:
        self.temperature = temperature
        self.city = city
        self.atmosphericPressure = atmosphericPressure
        self.humidity = humidity
        self.weather = weather
        self.date = date

    def __str__(self) -> str:
        return (f"Weather <{self.temperature}>")
    
    def __getattribute__(self, __name: str) :
        if (__name=='date'):
            return object.__getattribute__(self, __name).strftime("%d/%m/%Y %H:%M:%S")
        else:
            return object.__getattribute__(self, __name)