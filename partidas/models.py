from django.db import models
from times.models import Time 
from campeonatos.models import Campeonato 
from estadios.models import Estadio 

# Create your models here.
class Partida(models.Model):
    data_partida = models.DateTimeField()
    time_casa = models.ForeignKey(Time, related_name="time_casa", on_delete=models.CASCADE) # preencher obrigatoriamente por padrão
    time_fora = models.ForeignKey(Time, related_name="time_fora", on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)