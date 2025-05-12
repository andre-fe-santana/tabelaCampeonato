from django.shortcuts import render, redirect, get_object_or_404
from palpites.models import Palpite
from palpites.forms import PalpiteForm
from partidas.models import Partida
from django.utils import timezone

# Create your views here.
def mostrarPalpite(request):
    palpites = Palpite.objects.all()

    context = {
        'palpites': palpites
    }

    # verificar se o usuário já fez o palpite já

    return render(
        request,
        'palpites/mostrar.html',
        context,
    )

def criarPalpite(request, partida_id):
    partida = get_object_or_404(Partida, pk=partida_id)

    if request.method == "POST":
        form = PalpiteForm(request.POST)
        print(form.data)

        if form.is_valid():
            palpite = form.save(commit=False)
            palpite.jogo = partida
            palpite.data_cadastro = timezone.now()
            palpite.save()
            
            return redirect('/palpite/')
        
    else: 
        form = PalpiteForm()

    # Contexto aqui é basicamente o que você tá levando pro template
    context = {
        'form': form,
        'partida': partida,
        'time_casa': partida.time_casa,
        'time_fora': partida.time_fora,
        'campeonato': partida.campeonato,
        'estadio': partida.estadio,
    }

    return render(
        request,
        'palpites/cadastrar.html',
        context
    )

def editarPalpite(request, palpite_id):
    palpite = get_object_or_404(Palpite, pk=palpite_id)
    partida = palpite.jogo

    if request.method == "POST":
        form = PalpiteForm(request.POST, instance=palpite)

        if form.is_valid():
            palpite = form.save(commit=False)
            palpite.jogo = partida
            palpite.save()
            return redirect('/palpite/')
        
    else:
        form = PalpiteForm(instance=palpite)

    context = {
        'form': form,
        'partida': partida,
        'time_casa': partida.time_casa,
        'time_fora': partida.time_fora,
        'campeonato': partida.campeonato,
        'estadio': partida.estadio,
    }

    return render(
        request,
        'palpites/editar.html',
        context,
    )

def excluirPalpite(request, palpite_id):
    palpite = get_object_or_404(Palpite, pk=palpite_id)
    partida = palpite.jogo

    if request.method == "POST":
        palpite.delete()
        return redirect('/palpite')
    
    context = {
        'partida': partida,
        'time_casa': partida.time_casa,
        'time_fora': partida.time_fora,
        'campeonato': partida.campeonato,
        'estadio': partida.estadio,
    }

    return render(
        request,
        'palpites/excluir.html',
        context,
    )