from django.views import View
from django.shortcuts import render
from django.templatetags.static import static
from ..forms import personagemForm
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import urllib.parse


from core.models import Personagem, Magia, Truque

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
        idtruques = request.COOKIES.get('idtruques')
        lista_decodificada = urllib.parse.unquote(idtruques)
        id = json.loads(lista_decodificada)

        truques = Truque.objects.all().filter(id_truque__in = id)
        #=========================================================================
        idmagias = request.COOKIES.get('idmagias')
        lista_decodificada = urllib.parse.unquote(idmagias)
        id = json.loads(lista_decodificada)

        magias = Magia.objects.all().filter(id_magia__in = id)
        #=========================================================================

        personagem = Personagem.objects.get(id_personagem=1)

        form = personagemForm()
        return render(request, 'templateFichaPersonagem.html', {'personagem': personagem, 'form': form, 'proficiencias': proficiencias, 'idiomas': idiomas, 'truques': truques, 'magias': magias})