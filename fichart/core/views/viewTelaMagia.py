from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import nomeForm
from core.models import Magia, Truque



class viewTelaMagia(LoginRequiredMixin, View):
    def get(self, request):
        
        classeAtual = request.COOKIES.get("classe")
        print(classeAtual)
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
        
        return render(request, "templateTelaSelecaoMagia.html", {"form":form, "listaMagias":listaMagias,"truquesObjects":truquesObjects})