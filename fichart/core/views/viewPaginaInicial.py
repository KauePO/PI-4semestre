from django.views import View
from django.shortcuts import render
from django.templatetags.static import static
from ..forms import nomeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Personagem, Usuario

class viewPaginaInicial(LoginRequiredMixin, View):
    def get(self, request):
       
        personagens = Personagem.objects.filter(usuario__user=request.user)
        usuario = Usuario.objects.get(user=request.user)
        
        context = {
            "personagens":personagens,
            "QTD_fichas": personagens.count(),
            "plano_ativo":usuario.plano_ativo
            
        }
        return render(request, "templatePaginaInicial.html",context)
    