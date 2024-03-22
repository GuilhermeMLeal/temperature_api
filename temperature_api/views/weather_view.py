from datetime import datetime
from random import randrange
from django.views import View
from django.shortcuts import render, redirect
from temperature_api.models.weather_model import WeatherEntity
from temperature_api.repositories import WeatherRepository
from temperature_api.weatherSerializer import WeatherSerializer
from temperature_api.WeatherForm import WeatherEntityForm


class WeatherView(View):
  def get(self, request):
    repository = WeatherRepository(collectionName='weathers')
    weathers = list(repository.getAll())
    serializer = WeatherSerializer(data=weathers, many=True)
    weathersData = []  # Defina um valor padrão para weathersData
    if serializer.is_valid():
        weathersData = serializer.data
        print(serializer.data)
    else:
        print(serializer.errors)
    return render(request, "home_data.html", {"weathers": weathersData})


class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather = WeatherEntity(
            temperature=randrange(start=17, stop=40),
            date=datetime.now()
        )
        serializer = WeatherSerializer(data=weather.__dict__)
        if (serializer.is_valid()):
            repository.insert(serializer.data)
        else:
            print(serializer.errors)

        return redirect('Weather View')
    
class WeatherReset(View):
    def get(self, request): 
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteAll()

        return redirect('Weather View')
        