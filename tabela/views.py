from django.shortcuts import render
from usuarios.models import Usuario

def mostrarTabela(request):
    usuarios = Usuario.objects.order_by('-pontos') # "-pontos" -> ordem decrescente

    posicao_usuarios = [] #cria uma lista
    for index, usuario in enumerate(usuarios, start=1):
        usuario.posicao = index
        posicao_usuarios.append(usuario)

    context = {
        'usuarios': posicao_usuarios
    }

    return render (
        request,
        'tabela.html',
        context,
    )