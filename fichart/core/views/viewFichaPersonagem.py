from django.views import View
from django.shortcuts import render
from django.templatetags.static import static
from ..forms import personagemForm
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import urllib.parse


from core.models import Personagem

class viewFichaPersonagem(LoginRequiredMixin,View):
    def get(self, request):
        lista_proficiencias = request.COOKIES.get('proficiencias')

        if lista_proficiencias:
            lista_decodificada = urllib.parse.unquote(lista_proficiencias)
            proficiencias = json.loads(lista_decodificada)

        #=========================================================================
        lista_idiomas = request.COOKIES.get('idiomas')

        if lista_idiomas:
            lista_decodificada = urllib.parse.unquote(lista_idiomas)
            idiomas = json.loads(lista_decodificada)
        #=========================================================================
        lista_truques = request.COOKIES.get('truques')

        if lista_truques:
            lista_decodificada = urllib.parse.unquote(lista_truques)
            truques = json.loads(lista_decodificada)
        #=========================================================================
        lista_magias = request.COOKIES.get('magias')
        if lista_magias:
            lista_decodificada = urllib.parse.unquote(lista_magias)
            magias = json.loads(lista_decodificada)


        personagem = Personagem.objects.get(id_personagem=1)

        form = personagemForm()
        return render(request, 'templateFichaPersonagem.html', {'personagem': personagem, 'form': form, 'proficiencias': proficiencias, 'idiomas': idiomas, 'truques': truques, 'magias': magias})