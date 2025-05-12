from django.db import models
from django.utils import timezone

# Create your models here.
class Estadio(models.Model):
    nome = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to="imagens/estadios/")
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome