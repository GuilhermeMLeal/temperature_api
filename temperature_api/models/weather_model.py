from django.db import models

class WeatherEntity(models.Model):
    cidade = models.CharField(max_length=100)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    pressao_atmosferica = models.DecimalField(max_digits=7, decimal_places=2)
    umidade = models.DecimalField(max_digits=5, decimal_places=2)
    precipitacao = models.DecimalField(max_digits=5, decimal_places=2)
    condicao_tempo = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.cidade, self.temperatura