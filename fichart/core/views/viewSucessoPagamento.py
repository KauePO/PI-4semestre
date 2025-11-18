from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from core.models import Usuario, Cobranca
from datetime import date
from django.contrib import messages

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
            messages.success(request, "O pagamento foi um sucesso")
        
        except Exception as e:
            errors.append(e)
            messages.error(request, "Não foi possivel registrar o seu pagamento")
        
        
        return redirect("paginaInicial")
        