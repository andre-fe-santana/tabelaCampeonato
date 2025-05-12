from django.contrib import admin
from campeonatos import models

# Register your models here.
@admin.register(models.Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano', 'imagem', 'data_cadastro',)