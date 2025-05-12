from django.urls import path
from partidas import views

urlpatterns = [
    path('', views.partidasHoje, name='partidasHoje'),
]
