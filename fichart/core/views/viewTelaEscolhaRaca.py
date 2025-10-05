
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import nomeForm

from core.models import Raca, Subraca


class viewTelaEscolhaRaca(LoginRequiredMixin,View):

    def get(self,request):
        form = nomeForm()

        racas = Raca.objects.all()
        subRacas = Subraca.objects.all()


        return render(request,"templateEscolhaRaca.html",{'form':form, 'racas':racas, "subRacas":subRacas})

