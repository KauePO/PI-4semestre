from django.views import View
from django.shortcuts import render, redirect
from django.templatetags.static import static
from ..forms import personagemForm
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import urllib.parse


from core.models import Personagem, Magia, Truque, Classe, Raca, HabilidadeEspecial, Usuario, Antecedente, Proficiencia, Idiomas

class viewFichaPersonagem(LoginRequiredMixin,View):
    def get(self, request):
        #Puxar informações salvas nos cookies
        #Antecedente======================================================================
        antecedenteNome = request.COOKIES.get('antecedente')
        antecedente = Antecedente.objects.get(nome = antecedenteNome)

        #Proficiencias======================================================================
        idproficiencias = request.COOKIES.get('idproficiencias')
        lista_decodificada = urllib.parse.unquote(idproficiencias)
        id = json.loads(lista_decodificada)

        proficiencias = Proficiencia.objects.all().filter(id_proficiencia__in = id)

        #Idiomas======================================================================
        ididiomas = request.COOKIES.get('idiomas')
        lista_decodificada = urllib.parse.unquote(ididiomas)
        id = json.loads(lista_decodificada)

        idiomas = Idiomas.objects.all().filter(id_idioma__in = id)

        #Truques======================================================================
        idtruques = request.COOKIES.get('truques')
        lista_decodificada = urllib.parse.unquote(idtruques)
        id = json.loads(lista_decodificada)

        truques = Truque.objects.all().filter(id_truque__in = id)
        #Magias=========================================================================
        idmagias = request.COOKIES.get('magias')
        lista_decodificada = urllib.parse.unquote(idmagias)
        id = json.loads(lista_decodificada)

        magias = Magia.objects.all().filter(id_magia__in = id)
        #Classe=========================================================================
        classeNome = request.COOKIES.get('classe')
        classe = Classe.objects.get(nome = classeNome)
        
        #Raça=========================================================================
        idraca = request.COOKIES.get('raca_escolhida')
        id = json.loads(idraca)
        raca = Raca.objects.get(id_raca= id)

        #Atributos=========================================================================
        atrForca = request.COOKIES.get('forca')
        atrDestreza = request.COOKIES.get('destreza')
        atrConstituicao = request.COOKIES.get('constituicao')
        atrInteligencia = request.COOKIES.get('inteligencia')
        atrSabedoria = request.COOKIES.get('sabedoria')
        atrCarisma = request.COOKIES.get('carisma')

        atributos = {
            "Forca": atrForca, "Destreza": atrDestreza, "Constituicao": atrConstituicao,
            "Inteligencia": atrInteligencia, "Sabedoria": atrSabedoria, "Carisma": atrCarisma
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
        idhabilidade_especiais = request.COOKIES.get('idhabilidade_especiais')
        lista_decodificada = urllib.parse.unquote(idhabilidade_especiais)
        id = json.loads(lista_decodificada)

        habilidade_especiais = HabilidadeEspecial.objects.all().filter(id_habilidade_especial__in = id)


        form = personagemForm()
        return render(request, 'templateFichaPersonagem.html', {"habilidade_especiais": habilidade_especiais,"salvaguardas":salvaguardas, 'form': form, 'proficiencias': proficiencias, 'idiomas': idiomas, 'truques': truques, 'magias': magias, 'classe': classe, 'raca': raca, 'antecedente': antecedente,"atributos": atributos})
    
    def post(self, request):
        form = personagemForm(request.POST)
        personagem = Personagem()
        
        # CONVERSÃO DOS ATRIBUTOS PARA INTEIRO
        personagem.forca = int(request.COOKIES.get('forca', 10))
        personagem.destreza = int(request.COOKIES.get('destreza', 10))
        personagem.constituicao = int(request.COOKIES.get('constituicao', 10))
        personagem.inteligencia = int(request.COOKIES.get('inteligencia', 10))
        personagem.sabedoria = int(request.COOKIES.get('sabedoria', 10))
        personagem.carisma = int(request.COOKIES.get('carisma', 10))
        
        # Classe
        classe_nome = request.COOKIES.get('classe')
        if classe_nome:
            personagem.classe = classe_nome

        # Raça
        idraca = request.COOKIES.get('raca_escolhida')
        id = json.loads(idraca)
        raca = Raca.objects.get(id_raca= id)

        raca_nome = raca.nome
        if raca_nome:
            personagem.raca = raca_nome

        # ANTECEDENTE
        antecedente_nome = request.COOKIES.get('antecedente')
        if antecedente_nome:
            personagem.antecedente = antecedente_nome

        # NÍVEL
        personagem.nivel = 1

        # DADOS DO FORMULÁRIO DO TEMPLATE
        personagem.aparencia_do_personagem = request.POST.get('aparencia_do_personagem', '')
        personagem.historia_do_personagem = request.POST.get('historia_do_personagem', '')
        personagem.aliados_e_organizacoes = request.POST.get('aliados_e_organizacoes', '')
        personagem.tracos_e_caracteristicas_adicionais = request.POST.get('tracos_e_caracteristicas_adicionais', '')
        personagem.tesouro = request.POST.get('tesouro', '')
        
        personagem.nome = request.POST.get('nome', 'Personagem Sem Nome')

        # Usuario
        usuario = Usuario.objects.get(user=request.user)
        personagem.usuario_id = usuario.id_usuario
        
        # Salva o objeto completo no banco de dados
        personagem.save()

        # Adiciona Magias e Truques ao personagem
        try:
            idmagias = request.COOKIES.get('idmagias')
            if idmagias:
                lista_decodificada = urllib.parse.unquote(idmagias)
                ids_magias = json.loads(lista_decodificada)
                
                magias = Magia.objects.filter(id_magia__in=ids_magias)
                
                personagem.magia.add(*magias)
                
                print(f"Adicionadas {magias.count()} magias ao personagem {personagem.nome}")
            else:
                print("Nenhuma magia encontrada nos cookies")
                
        except Exception as e:
            print(f"Erro ao adicionar magias: {e}")

        try:
            idtruques = request.COOKIES.get('idtruques')
            if idtruques:
                lista_decodificada = urllib.parse.unquote(idtruques)
                ids_truques = json.loads(lista_decodificada)
                
                truques = Truque.objects.filter(id_truque__in=ids_truques)
                print(truques)
                
                personagem.truque_set.add(*truques)
                
                print(f"Adicionados {truques.count()} truques ao personagem {personagem.nome}")
            else:
                print("Nenhum truque encontrado nos cookies")

        except Exception as e:
            print(f"Erro ao adicionar truques: {e}")

        return redirect('paginaInicial')