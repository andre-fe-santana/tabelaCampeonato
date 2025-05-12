from django.contrib import admin
from times import models

# Register your models here.
@admin.register(models.Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'imagem', 'data_cadastro',)