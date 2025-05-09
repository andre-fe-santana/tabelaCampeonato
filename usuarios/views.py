from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm
from usuarios.models import Usuario

# Create your views here.
def index(request):
    usuarios = Usuario.objects.all()

    context = {
        'usuarios': usuarios
    }
    

    return render(
        request,
        'usuarios/index.html',
        context,
    )

def criarUsuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/usuarios/login')
    else:
        form = UsuarioForm()

    return render(
        request,
        'usuarios/cadastro.html',
        {'form': form}
    )

def login(request):
    return render(
        request,
        'usuarios/login.html',
    )

def meuPerfil(request):
    pass