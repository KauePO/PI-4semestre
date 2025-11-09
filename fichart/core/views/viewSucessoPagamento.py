from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from core.models import Usuario

class viewSucessoPagamento (LoginRequiredMixin, View):
    
    def get(self, request):
        errors = []
        
        
        try:
            usuario = Usuario.objects.get(user = request.user)
            usuario.plano_ativo = True
            usuario.save()
        
        except Exception as e:
            errors.append(e)
        
        
        return redirect("paginaInicial")
        