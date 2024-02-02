from rest_framework.serializers import ModelSerializer
from temperature_api.models.weather_model import WeatherEntity

class WeatherSerializer(ModelSerializer):
    class Meta:
        model = WeatherEntity;
        fields = '__all__'