from django.urls import path, include
from palpites import views

urlpatterns = [
    path('', views.mostrarPalpite, name='mostrarPalpite'), # home(ver o seu palpite)
    path('criar/<int:partida_id>/', views.criarPalpite, name='criarPalpite'),
    path('editar/<int:palpite_id>/', views.editarPalpite, name='editarPalpite'),
    path('excluir/<int:palpite_id>/', views.excluirPalpite, name='excluirPalpite'),
]
