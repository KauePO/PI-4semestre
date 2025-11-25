from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from urllib.parse import unquote
from ..forms import nomeForm
from core.models import Magia, Truque



class viewTelaMagia(LoginRequiredMixin, View):
    def get(self, request):
        
        classeAtual = request.COOKIES.get("classe")
        listaMagiasAtuais = unquote(request.COOKIES.get("magias",""))
        listaTruquesAtuais = unquote(request.COOKIES.get("truques",""))
        
        magiasObjects = Magia.objects.all().filter(classe__nome = classeAtual)
        listaMagias = {
                        "1":magiasObjects.filter(nivel = 1),
                        "2":magiasObjects.filter(nivel = 2),
                        "3":magiasObjects.filter(nivel = 3),
                        "4":magiasObjects.filter(nivel = 4),
                        "5":magiasObjects.filter(nivel = 5),
                        "6":magiasObjects.filter(nivel = 6),
                        "7":magiasObjects.filter(nivel = 7),
                        "8":magiasObjects.filter(nivel = 8),
                        "9":magiasObjects.filter(nivel = 9)
        }
        truquesObjects = Truque.objects.all().filter(classes__nome = classeAtual)
        
        form = nomeForm()
        
        avatarAtual = request.session.get("avatar", "")
        
        context =  {
            "form":form, 
            "listaMagias":listaMagias,
            "truquesObjects":truquesObjects,
            "avatar":avatarAtual,
            "listaMagiasAtuais":listaMagiasAtuais,
            "listaTruquesAtuais":listaTruquesAtuais
            
        }
        
        return render(request, "templateTelaSelecaoMagia.html",context)