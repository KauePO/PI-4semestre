from django.views import View
from django.shortcuts import render
from django.templatetags.static import static
from ..forms import nomeForm
from django.contrib.auth.mixins import LoginRequiredMixin

class viewPaginaInicial(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "templatePaginaInicial.html")
    