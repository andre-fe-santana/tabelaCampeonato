from django.utils import timezone
from django.db import models

# Create your models here.
class Time(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="imagens/times/")
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome