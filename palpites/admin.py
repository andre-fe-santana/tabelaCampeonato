from django.contrib import admin
from palpites import models

# Register your models here.
@admin.register(models.Palpite)
class PalpiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'jogo', 'placar_casa', 'placar_fora', 'jogador_gol', 'minuto_gol', 'data_cadastro', 'status', 'usuario')