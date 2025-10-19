from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from ..forms import nomeForm


class viewTelaAtributos( LoginRequiredMixin, View):
    
    def get(self, request):
        
        form = nomeForm()
        
       
        
        return render(request,"templateTelaAtributos.html",{"form":form})