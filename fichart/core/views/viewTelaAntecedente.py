from django.views import View
from django.shortcuts import render
from django.templatetags.static import static
from ..forms import nomeForm
from django.contrib.auth.mixins import LoginRequiredMixin


from core.models import Antecedente

class viewTelaAntecedente(LoginRequiredMixin,View):
    def get(self, request):
        
        antecedentes = Antecedente.objects.all()

        form = nomeForm()
        return render(request, 'templateTelaAntecedentes.html', {'antecedentes': antecedentes, 'form': form})



