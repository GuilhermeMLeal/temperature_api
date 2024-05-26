from typing import Any
from django.utils import timezone
from datetime import datetime
from random import randrange
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from user.authenticationUser import *
from .weatherModel import WeatherEntity
from .weatherRepository import WeatherRepository
from .weatherSerializer import WeatherSerializer
from .WeatherForm import WeatherForm
from .weatherExceptions import WeatherException
from django.forms.models import model_to_dict


class WeatherView(View):
    def verify_authenticated(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            return False
        try:
            user = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user_id = user.get('id')
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False

    def dispatch(self, request, *args, **kwargs):
        request.authenticate = self.verify_authenticated(request)
        if not request.authenticate:
            return HttpResponse('Unauthorized - No token provided', status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not request.authenticate:
            return HttpResponse('Unauthorized - User not authenticated', status=401)

        repository = WeatherRepository(collectionName='weathers')
        try:
            weathers = list(repository.getAll())
            serializer = WeatherSerializer(data=weathers, many=True)
            if serializer.is_valid():
                modelWeather = serializer.save()
                objectReturn = {"weathers": modelWeather, "user_id": request.user_id}
            else:
                objectReturn = {"error": serializer.errors, "user_id": request.user_id}
        except WeatherException as e:
            objectReturn = {"error": e.message, "user_id": request.user_id}

        return render(request, "home_weather.html", objectReturn)


class WeatherGenerate(View):

    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather = WeatherEntity(
            temperature=randrange(start=17, stop=40),
            date=datetime.now(),
            city='Sorocaba'
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
    

class WeatherInsert(View):

    def get(self, request):
        weatherForm = WeatherForm()
        return render(request, "create_weather.html", {"form": weatherForm})

    def post(self, request):
        weatherForm = WeatherForm(request.POST)
        if weatherForm.is_valid():
            weather_data = weatherForm.cleaned_data
            weather_data['date'] = datetime.now()

            serializer = WeatherSerializer(data=weather_data)
            if serializer.is_valid():
                repository = WeatherRepository(collectionName='weathers')
                repository.insert(serializer.data)
                return redirect('Weather View')
            else:
                print(serializer.errors)
        else:
            print(weatherForm.errors)

        return redirect('Weather View')

class WeatherEdit(View):

    def get(self, request, id):
        repository = WeatherRepository(collectionName='weathers')
        weather_data = repository.getByID(id)
        weather_entity = WeatherEntity(**weather_data) if weather_data else None
        weather_dict = weather_entity.to_dict() if weather_entity else {}
        weatherForm = WeatherForm(initial=weather_dict)

        return render(request, "form_edit_weather.html", {"form": weatherForm, "id": id})


    def post(self, request, id):
        repository = WeatherRepository(collectionName='weathers')
        weather = repository.getByID(id)
        temperature = request.POST.get('temperature', weather['temperature'])
        city = request.POST.get('city', weather['city'])
        atmosphericPressure = request.POST.get('atmosphericPressure', weather.get('atmosphericPressure', 0))
        humidity = request.POST.get('humidity', weather.get('humidity', 0))
        weather_condition = request.POST.get('weather', weather.get('weather', ''))

        # Atualize os dados no banco de dados
        repository.update({
            'temperature': temperature,
            'city': city,
            'atmosphericPressure': atmosphericPressure,
            'humidity': humidity,
            'weather': weather_condition,
        }, id)

        # Redirecione para a página de visualização de dados meteorológicos
        return redirect('Weather View')


class WeatherDelete(View):
    
    def get(self, request, id):
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteByID(id)

        return redirect('Weather View')


class WeatherFilter(View):
    def post(self, request):
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')

        repository = WeatherRepository(collectionName='weathers')
        try:
            weathers = list(repository.get(data))
            serializer = WeatherSerializer(data=weathers, many=True)
            if (serializer.is_valid()):
                modelWeather = serializer.save()
                objectReturn = {"weathers": modelWeather}
            else:
                objectReturn = {"error": serializer.errors}
        except WeatherException as e:
            objectReturn = {"error": e.message}
  
        return render(request, "home_weather.html", objectReturn)