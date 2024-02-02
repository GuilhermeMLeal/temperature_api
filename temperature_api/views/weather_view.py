from rest_framework import viewsets
from temperature_api.models.weather_model import WeatherEntity
from temperature_api.serializer.weather_serializer import WeatherSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = WeatherEntity.objects.all()
    serializer_class = WeatherSerializer