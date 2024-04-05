"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from temperature_api.views.weather_view import WeatherView
from rest_framework.routers import DefaultRouter



from django.urls import path
from temperature_api.views.weather_view import WeatherView, WeatherGenerate, WeatherReset,WeatherInsert, WeatherEdit

urlpatterns = [
    path('api/', WeatherView.as_view(), name='Weather View'),
    path('api/insert/', WeatherInsert.as_view(), name='Weather Insert'),
    path('api/generate/', WeatherGenerate.as_view(), name='Weather Generate'),
    path('api/reset/', WeatherReset.as_view(), name='Weather Reset'),
    path('api/update/<id>', WeatherEdit.as_view(), name ='Weather Edit' )
    
]