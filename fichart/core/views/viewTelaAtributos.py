from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from ..forms import nomeForm


class viewTelaAtributos( LoginRequiredMixin, View):
    
    def get(self, request):
        
        form = nomeForm()
        
        atributos = {
            "forca": "Força",
            "destreza": "Destreza",
            "constituicao": "Constituição",
            "inteligencia": "Inteligência",
            "sabedoria": "Sabedoria",
            "carisma": "Carisma",
        }
        
        salvaguardas = {
            "forca": "forca",
            "destreza": "destreza",
            "constituicao": "constituicao",
            "inteligencia": "inteligencia",
            "sabedoria": "sabedoria",
            "carisma": "carisma",
        }
        
        pericias = {
            "acrobacia": "destreza",
            "arcanismo": "inteligencia",
            "atletismo": "forca",
            "atuacao": "carisma",
            "enganacao": "carisma",
            "furtividade": "destreza",
            "historia": "inteligencia",
            "intimidacao": "carisma",
            "intuição": "sabedoria",
            "investigacao": "inteligencia",
            "lidar com animais": "sabedoria",
            "medicina": "sabedoria",
            "natureza": "inteligencia",
            "percepcao": "sabedoria",
            "persuasao": "carisma",
            "prestidigitacao": "destreza",
            "religiao": "inteligencia",
            "sobrevivencia": "sabedoria",
        }
        
        return render(request,"templateTelaAtributos.html",{"form":form, "pericias":pericias, "salvaguardas":salvaguardas, "atributos":atributos })