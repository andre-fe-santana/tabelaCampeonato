from django.shortcuts import render, redirect, get_object_or_404
from palpites.models import Palpite
from palpites.forms import PalpiteForm
from partidas.models import Partida
from django.utils import timezone
from datetime import timedelta

# Create your views here.
def partidasHoje(request):
    hoje = timezone.now()
    # print(hoje)
    inicio_dia = hoje.replace(hour=0, minute=0, second=0, microsecond=0)
    fim_dia = inicio_dia + timedelta(days=1)

    partidas = Partida.objects.filter(
        data_partida__gte=inicio_dia,
        data_partida__lt=fim_dia,
        )

    context = {
        'partidas': partidas,
        'dia_atual': inicio_dia.date(),
    }

    return render(
        request,
        'partidas/hoje.html',
        context,
    )
