
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import nomeForm

from core.models import Raca, Subraca


class viewTelaEscolhaRaca(LoginRequiredMixin,View):

    def get(self,request):
        
        raca_escolhida = request.COOKIES.get("raca_escolhida", "") 
        subraca_escolhida = request.COOKIES.get("subraca_escolhida", "") 
        
        form = nomeForm()

        racas = Raca.objects.all()
        subRacas = Subraca.objects.all()
        avatarAtual = request.session.get("avatar","")
        
        context = {
            'form':form, 
            'racas':racas, 
            "subRacas":subRacas, 
            "raca_escolhida":raca_escolhida, 
            "subraca_escolhida":subraca_escolhida,
            "avatar":avatarAtual
        }


        return render(request,"templateEscolhaRaca.html",context)

