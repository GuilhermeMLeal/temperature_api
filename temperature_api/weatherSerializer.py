from rest_framework import serializers
from temperature_api.models.weather_model import WeatherEntity 

class WeatherSerializer(serializers.Serializer):
    temperature = serializers.IntegerField()
    city = serializers.CharField(required=False)
    atmosphericPressure = serializers.CharField(required=False)
    humidity = serializers.CharField(required=False)
    weather = serializers.CharField(required=False)
    date = serializers.DateTimeField()

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
