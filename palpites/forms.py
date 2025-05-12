from django import forms
from palpites.models import Palpite

class PalpiteForm(forms.ModelForm):
    class Meta:
        model = Palpite
        fields = [
            'placar_casa',
            'placar_fora',
            'jogador_gol',
            'minuto_gol',
            'usuario',
        ]