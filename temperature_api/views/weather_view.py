from datetime import datetime
from random import randrange
from django.views import View
from django.shortcuts import render, redirect
from temperature_api.models.weather_model import WeatherEntity
from temperature_api.repositories import WeatherRepository
from temperature_api.weatherSerializer import WeatherSerializer

class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weathers = repository.getAll()
        serializer = WeatherSerializer(weathers, many=True)
        return render(request, "home_data.html", {"weathers": serializer.data})

class WeatherGenerate(View):
    def post(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather_data = {
            "temperature": randrange(start=17, stop=40),
            "date": datetime.now()
        }
        serializer = WeatherSerializer(data=weather_data)
        if serializer.is_valid():
            repository.insert(serializer.validated_data)
        return redirect('Weather View')

class WeatherReset(View):
    def delete(self, request):
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteAll()
        return redirect('Weather View')