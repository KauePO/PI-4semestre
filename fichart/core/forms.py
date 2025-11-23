from django import forms
from .models import Personagem

class nomeForm(forms.Form):
    nome = forms.CharField(
    max_length=100,
    required=True,
    label='nome',
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Insira o nome',
    }),
)
    avatar_personagem = forms.ImageField(   #
        required=True,
        widget=forms.FileInput(attrs={       
            'class': 'form-control',
            'accept': 'image/*'              
        })
    )
    
class personagemForm(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = ['nome', 'idade', 'raca', 'classe', 'antecedente', 'forca', 'destreza', 'sabedoria', 'inteligencia', 'carisma', 'constituicao', 'aparencia_do_personagem', 'historia_do_personagem', 'aliados_e_organizacoes', 'tracos_e_caracteristicas_adicionais', 'tesouro']
        