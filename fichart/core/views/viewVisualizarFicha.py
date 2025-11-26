from django.views import View
from django.shortcuts import render, redirect
from django.templatetags.static import static
from ..forms import personagemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


from core.models import Personagem, Truque, Classe, Raca, HabilidadeEspecial, Usuario, Antecedente, Proficiencia, Idiomas, ProficienciaSalvaguardas_Pericias

class viewVisualizarFicha(LoginRequiredMixin,View):
    def get(self, request, idPersonagem):
        personagem = Personagem.objects.get(id_personagem=idPersonagem)
        raca = Raca.objects.get(nome= personagem.raca)

        form = personagemForm()
    

        #Puxar informações salvas nos cookies
        
        #Classe=========================================================================
        classe = Classe.objects.get(nome = personagem.classe)
        
        #Antecedente======================================================================
        antecedente = Antecedente.objects.get(nome = personagem.antecedente)

        #Proficiencias======================================================================
        
        proficiencias = Proficiencia.objects.filter(nome__in=classe.proficiencia_set.values_list('nome', flat=True)
)

        #Idiomas======================================================================
        
        idiomas = Idiomas.objects.all().filter(nome__in = raca.idioma.values_list('nome', flat=True))
        

        #Truques======================================================================
        truques = Truque.objects.all().filter(personagem = personagem.id_personagem)

        #Magias=========================================================================
        magias = personagem.magia.all()

        
        
        #Raça=========================================================================
        raca = Raca.objects.get(nome= personagem.raca)

        #Atributos=========================================================================

        atributos = {
            "Forca": personagem.forca, "Destreza": personagem.destreza, "Constituicao": personagem.constituicao,
            "Inteligencia": personagem.inteligencia, "Sabedoria": personagem.sabedoria, "Carisma": personagem.carisma
        }
        #Salvaguardas(Proficiencia)=========================================================================
        salvaguardas = {
            "forca": "forca",
            "destreza": "destreza",
            "constituicao": "constituicao",
            "inteligencia": "inteligencia",
            "sabedoria": "sabedoria",
            "carisma": "carisma",
        }

        #Habilidades Especiais=========================================================================
        habilidade_especiais = HabilidadeEspecial.objects.none()  # QuerySet vazia inicial

        if personagem.classe == "Bardo":
            habilidades_bardo = HabilidadeEspecial.objects.filter(
                nome__in=["Inspiração de Bardo", "Conjuração como Ritual"]
            )
            habilidade_especiais = habilidade_especiais | habilidades_bardo  # Concatena

        if personagem.raca == "Elfo":
            habilidades_elfo = HabilidadeEspecial.objects.filter(
                nome__in=["Ascensão Feérica", "Transe"]
            )
            habilidade_especiais = habilidade_especiais | habilidades_elfo  # Concatena

        #ProficienciasSalvaguardas_Pericias=========================================================================
        proficiencias_salvaguardas_pericias = personagem.proficienciaSalvaguardas_Pericias.all()
        nomes_proficiencias_salvas = [p.nome for p in proficiencias_salvaguardas_pericias]

        form = personagemForm()
    
        return render(request, 'templateVisualizarFicha.html', {"proficiencias_salvaguardas_pericias": proficiencias_salvaguardas_pericias, "nomes_proficiencias_salvas": nomes_proficiencias_salvas, "habilidade_especiais": habilidade_especiais, "personagem": personagem, "salvaguardas":salvaguardas, 'form': form, 'classe': classe, 'raca': raca, 'antecedente': antecedente,"atributos": atributos, 'idiomas': idiomas, 'proficiencias': proficiencias, 'truques': truques, 'magias': magias})
    
    def post(self, request):
        return redirect('paginaInicial')