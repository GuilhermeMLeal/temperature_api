from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from temperature_api.views.weather_view import WeatherViewSet


router = DefaultRouter()

router.register(r'data_weather', WeatherViewSet)

urlpatterns = [
    path('', include(router.urls))
]
