from django import forms
from temperature_api.models.weather_model import WeatherEntity

class WeatherForm(forms.Form):
    temperature = forms.FloatField()
    date = forms.DateTimeField()
    city = forms.CharField(max_length=255)
    atmosphericPressure = forms.FloatField(required=False)
    humidity = forms.FloatField(required=False)
    weather = forms.CharField(max_length=255, required=False)
