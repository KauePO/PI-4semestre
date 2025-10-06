from django.views import View
from django.shortcuts import render
from django.templatetags.static import static
from ..forms import nomeForm
from django.contrib.auth.mixins import LoginRequiredMixin


from core.models import Classe

class viewTelaClasses(LoginRequiredMixin,View):
    def get(self, request):
        
        classes = Classe.objects.all()

        form = nomeForm()
        return render(request, 'templateTelaClasses.html', {'classes': classes, 'form': form})