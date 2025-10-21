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
    })
)
    
class personagemForm(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = ['nome', 'idade', 'raca', 'classe', 'antecedente', 'forca', 'destreza', 'sabedoria', 'inteligencia', 'carisma', 'constituicao', 'altura', 'peso', 'cor_cabelo', 'cor_pele', 'cor_olhos', 'defeitos', 'traco_personalidade', 'ideais', 'ligacoes']
        