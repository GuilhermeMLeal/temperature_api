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
from temperature_api.weatherView import *
from user.userView import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('weather/', WeatherView.as_view(), name='Weather View'),
    path('weather/insert/', WeatherInsert.as_view(), name='Weather Insert'),
    path('weather/filter/', WeatherFilter.as_view(), name='Weather Filter'),
    path('weather/edit/<id>/', WeatherEdit.as_view(), name='Weather Edit'),
    path('weather/delete/<id>/', WeatherDelete.as_view(), name='Weather Delete'),
    path('weather/generate/', WeatherGenerate.as_view(), name='Weather Generate'),
    path('weather/reset/', WeatherReset.as_view(), name='Weather Reset'),
    path('', UserLogin.as_view(), name='User Login'),
    path('user/insert/', UserInsert.as_view(), name='User Insert'),
    path('user/forget/', UserForget.as_view(), name="User Forget"),
    path('user/edit/<user_id>/', UserEdit.as_view(), name='User Edit'),
    path('user/delete/<user_id>/', UserDelete.as_view(), name='User Delete'),
]