from django.contrib import admin
from partidas import models

# Register your models here.
@admin.register(models.Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_partida', 'time_casa', 'time_fora', 'campeonato', 'estadio')