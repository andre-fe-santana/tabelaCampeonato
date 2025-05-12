from django.contrib import admin
from estadios import models

# Register your models here.
@admin.register(models.Estadio)
class EstadioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'imagem', 'data_cadastro',)