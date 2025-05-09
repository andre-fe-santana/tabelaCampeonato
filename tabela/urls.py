from django.urls import path
from usuarios.models import Usuario
from tabela import views

urlpatterns = [
    path('', views.mostrarTabela, name="mostrarTabela"),
]
