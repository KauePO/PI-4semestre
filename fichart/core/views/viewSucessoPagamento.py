from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from core.models import Usuario, Cobranca
from datetime import date

class viewSucessoPagamento (LoginRequiredMixin, View):
    
    def get(self, request):
        errors = []
        
        
        try:
            usuario = Usuario.objects.get(user = request.user)
            cobranca = Cobranca.objects.filter(usuario = usuario, status_cobranca = "PENDING").first()
            
            usuario.plano_ativo = True
            usuario.data_ativacao = date.today()
            usuario.save()
            
            cobranca.status_cobranca = "PAID"
            
            cobranca.save()
        
        except Exception as e:
            errors.append(e)
        
        
        return redirect("paginaInicial")
        