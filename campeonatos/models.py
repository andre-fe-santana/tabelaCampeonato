from django.utils import timezone
from django.db import models

# Create your models here.
class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    imagem = models.ImageField(upload_to="imagens/campeonatos/")
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome