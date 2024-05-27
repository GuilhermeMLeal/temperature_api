from datetime import datetime

class WeatherEntity:
    def __init__(self, temperature, date,
                 city='', atmosphericPressure=0,
                 humidity=0, weather='', id='') -> None:
        self.id = id
        self.temperature = temperature
        self.city = city
        self.atmosphericPressure = atmosphericPressure
        self.humidity = humidity
        self.weather = weather
        self.date = date if isinstance(date, datetime) else datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z")

    def __str__(self) -> str:
        return f"Weather <{self.temperature}>"

    def to_dict(self):
        return {
            'id': self.id,
            'temperature': self.temperature,
            'city': self.city,
            'atmosphericPressure': self.atmosphericPressure,
            'humidity': self.humidity,
            'weather': self.weather,
            'date': self.date.strftime("%d/%m/%Y %H:%M:%S") if self.date else ''
        }
