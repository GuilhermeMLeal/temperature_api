from rest_framework import serializers
from temperature_api.models.weather_model import WeatherEntity 


class WeatherSerializer(serializers.Serializer):
    id = serializers.CharField(allow_blank=True, required=False)
    city_name = serializers.CharField(required=False, allow_blank=True)
    temperature = serializers.FloatField()
    atmospheric_pressure = serializers.FloatField(required=False)
    humidity = serializers.FloatField(required=False)
    precipitation_percentage = serializers.FloatField(required=False)
    weather_conditions = serializers.CharField(required=False, allow_blank=True)
    date_time = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return WeatherEntity(**validated_data)

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.city = validated_data.get('city', instance.city)
        instance.atmosphericPressure = validated_data.get('atmosphericPressure', instance.atmosphericPressure)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.weather = validated_data.get('weather', instance.weather)
        instance.date = validated_data.get('date', instance.date)
        return instance