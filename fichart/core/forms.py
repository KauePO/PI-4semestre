from django import forms

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