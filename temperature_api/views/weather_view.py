from datetime import datetime
from random import randrange
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from temperature_api.models.weather_model import WeatherEntity

class WeatherView(View):
    def get(self, request):
        weathers = []
        for i in range(10):
            weathers.append(
                WeatherEntity(
                    temperature=randrange(start=17, stop=40),
                    date=datetime.now()
                )
            )
        return render(request, "html/home_data.html", {"weathers": weathers})
