# models.py
from django.db import models

class WeatherEntity:

    def __init__(self, temperature, date_time='', atmospheric_pressure='', humidity='', precipitation_percentage='', weather_conditions='',city_name="Sorocaba", id='' ) -> None:
        self.id = id
        self.city_name = city_name
        self.temperature = temperature
        self.atmospheric_pressure = atmospheric_pressure
        self.humidity = humidity
        self.precipitation_percentage = precipitation_percentage
        self.weather_conditions = weather_conditions
        self.date_time = date_time

    def __str__(self) -> str:
        return (f"Weather <{self.temperature}>")

    
    def __getattribute__(self, __name: str) :
        if (__name=='date'):
            return object.__getattribute__(self, __name).strftime("%d/%m/%Y %H:%M:%S")
        else:
            return object.__getattribute__(self, __name)