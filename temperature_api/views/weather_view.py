from datetime import datetime
from random import randrange
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from temperature_api.models.weather_model import WeatherEntity


class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weathers = repository.getAll()
        return render(request, "home.html", {"weathers":weathers})
    

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        wheater = {
            "temperature" : 28,
            "date": "hoje"
            }
        repository.insert(wheater)

        return redirect('Weather View')