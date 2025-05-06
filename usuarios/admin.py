from django.contrib import admin
from usuarios import models

# Register your models here.
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagem', 'username', 'nome', 'email', 'data_nascimento','data_cadastro', 'acesso', 'ativo', 'pontos')