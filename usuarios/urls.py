from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.index, name="usuarios"), #pagina principal (mostra os usuários)
    path('cadastrar/', views.criarUsuario, name="cadastro"),
    path('login/', views.login, name="login"),
]