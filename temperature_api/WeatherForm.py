from django import forms

class WeatherForm(forms.Form):
    temperature = forms.FloatField(label='TEMPERATURA')
    city = forms.CharField(label='CIDADE', max_length=255)
    atmosphericPressure = forms.FloatField(label='PRESSÃO ATMOSFÉRICA')
    humidity = forms.FloatField(label='HUMIDADE')
    weather = forms.CharField(label='CONDIÇÃO CLIMÁTICA', max_length=255)