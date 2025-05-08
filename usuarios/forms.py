from django import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'imagem',
            'username',
            'nome',
            'email',
            'data_nascimento'
        ]