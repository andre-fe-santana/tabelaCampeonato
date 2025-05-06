from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    imagem = models.ImageField(blank=True, upload_to='imagens/%Y/%m')
    username = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    data_cadastro = models.DateField(default=timezone.now)
    data_nascimento = models.DateField()
    acesso = models.CharField(max_length=100)
    ativo = models.CharField(max_length=20)
    pontos = models.IntegerField(default=0) #todo novo jogador começa zerado

    def __str__(self):
        return f"{self.name} ({self.username}) foi criado(a) no sistema!"
    
