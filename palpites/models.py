from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from partidas.models import Partida

# Create your models here.
class Palpite(models.Model):
    jogo = models.ForeignKey(Partida, on_delete=models.CASCADE)
    placar_casa = models.IntegerField()
    placar_fora = models.IntegerField()
    jogador_gol = models.CharField(max_length=50)
    minuto_gol = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, default="Errado")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

def __str__(self):
    return f"Casa {self.placar_casa} x {self.placar_fora} Fora"
