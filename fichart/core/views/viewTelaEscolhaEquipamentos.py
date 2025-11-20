from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import nomeForm
from core.models import Arma, Armadura, TipoArmadura, ConjuntoEquipamento, EquipamentoDeAventura, Ferramenta



class viewTelaEquipamentos(LoginRequiredMixin, View):
    def get(self, request):
        
        classeAtual = request.COOKIES.get("classe")
        print(classeAtual)
        armaObjects = Arma.objects.all()

        tipo_armaduraobjects = TipoArmadura.objects.all().filter(classe__nome = classeAtual)


        armaduraObjects = Armadura.objects.all()
        
        listaArmaduras = {
                        "Leves":armaduraObjects.filter(tipo_armadura__nome_tipo_armadura = 'Leve'),
                        "Medias":armaduraObjects.filter(tipo_armadura__nome_tipo_armadura = 'Media'),
                        "Pesadas":armaduraObjects.filter(tipo_armadura__nome_tipo_armadura = 'Pesada'),
        }

        
        
        conjuntoEquipamentoObjects = ConjuntoEquipamento.objects.all().filter(classe__nome = classeAtual)

        equipamentoDeAventuraObjects = EquipamentoDeAventura.objects.all().filter(classe__nome = classeAtual)
        
        ferramentaObjects = Ferramenta.objects.all().filter(classe__nome = classeAtual)
        
        form = nomeForm()
        
        context = {
            "form":form, 
            "armaObjects":armaObjects, 
            'armaduraObjects':listaArmaduras,
            "conjuntoEquipamentoObjects":conjuntoEquipamentoObjects, 
            "equipamentoDeAventuraObjects":equipamentoDeAventuraObjects, 
            "ferramentasobjects":ferramentaObjects
        }
        
        return render(request, "templateEscolhaEquipamentos.html", context)