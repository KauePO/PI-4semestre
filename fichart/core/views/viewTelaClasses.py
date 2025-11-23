from django.views import View
from django.shortcuts import render
from django.templatetags.static import static
from ..forms import nomeForm
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.http import JsonResponse

from core.models import Classe

class viewTelaClasses(LoginRequiredMixin,View):
    def get(self, request):
        avatarAtual = request.session.get("avatar","")
        
        classes = Classe.objects.all()

        form = nomeForm()
        return render(request, 'templateTelaClasses.html', {'classes': classes, 'form': form, "avatar":avatarAtual})
    
    def post(self, request):
        print("chegou")
        data = json.loads(request.body)
        request.session["avatar"] = data.get("avatar")
        return JsonResponse({"status":"ok"})