from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import nomeForm
import json
from urllib.parse import unquote
from core.models import Arma, Armadura, TipoArmadura, ConjuntoEquipamento, EquipamentoDeAventura, Ferramenta



class viewTelaEquipamentos(LoginRequiredMixin, View):
    def get(self, request):
        
        classeAtual = request.COOKIES.get("classe")
        listaArmasAtuais = unquote(request.COOKIES.get("armas",""))
        listaArmadurasAtuais = unquote(request.COOKIES.get("armadura",""))
        listaConjuntosAtuais = unquote(request.COOKIES.get("conjuntoEquipamento",""))
        listaFerramentasAtuais = unquote(request.COOKIES.get("ferramenta",""))
        
        armaObjects = Arma.objects.all()

        armaduraObjects = Armadura.objects.all()
        
        listaArmaduras = {
            "Leves":armaduraObjects.filter(tipo_armadura__nome_tipo_armadura = 'LEVE'),
            "Medias":armaduraObjects.filter(tipo_armadura__nome_tipo_armadura = 'MEDIA'),
            "Pesadas":armaduraObjects.filter(tipo_armadura__nome_tipo_armadura = 'PESADA'),
        }
        # conjuntoEquipamentoObjects = ConjuntoEquipamento.objects.all().filter(classe__nome = classeAtual)
        conjuntoEquipamentoObjects = ConjuntoEquipamento.objects.all()
        
        equipamentoDeAventuraObjects = EquipamentoDeAventura.objects.all().filter(classe__nome = classeAtual)
        
        ferramenta = Ferramenta.objects.all()
        
        categoriasFerramentas = ferramenta.values_list("categoria", flat=True).distinct()
        
        ferramentasObjects = {
            nomecategoria : ferramenta.filter(categoria = nomecategoria)
            for nomecategoria in categoriasFerramentas
            
        }
        
        print(ferramentasObjects)
        form = nomeForm()
        
        avatarAtual = request.session.get("avatar","")
        
        context = {
            "form":form, 
            "armaObjects":armaObjects, 
            'armaduraObjects':listaArmaduras,
            "conjuntoEquipamentoObjects":conjuntoEquipamentoObjects, 
            "equipamentoDeAventuraObjects":equipamentoDeAventuraObjects, 
            "ferramentasObjects":ferramentasObjects,
            "avatar":avatarAtual,
            "listaArmasAtuais":listaArmasAtuais,
            "listaArmadurasAtuais": listaArmadurasAtuais,
            "listaConjuntosAtuais":listaConjuntosAtuais,
            "listaFerramentasAtuais": listaFerramentasAtuais
        }
        
        return render(request, "templateEscolhaEquipamentos.html", context)