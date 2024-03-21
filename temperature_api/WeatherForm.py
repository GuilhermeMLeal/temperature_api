from django import forms
from temperature_api.models.weather_model import WeatherEntity

class WeatherEntityForm(forms.Form):
    temperature = forms.DecimalField()
    city = forms.CharField(required=False)
    atmosphericPressure = forms.CharField(required=False)
    humidity = forms.CharField(required=False)
    weather = forms.CharField(required=False)
    date = forms.DateTimeField()

    def save(self):
        cleaned_data = self.cleaned_data
        weather_entity = WeatherEntity(
            temperature=cleaned_data.get('temperature'),
            city=cleaned_data.get('city', ''),
            atmosphericPressure=cleaned_data.get('atmosphericPressure', ''),
            humidity=cleaned_data.get('humidity', ''),
            weather=cleaned_data.get('weather', ''),
            date=cleaned_data.get('date')
        )
        return weather_entity
