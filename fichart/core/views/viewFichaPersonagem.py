from django.views import View
from django.shortcuts import render, redirect
from django.templatetags.static import static
from ..forms import personagemForm
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import urllib.parse


from core.models import Personagem, Magia, Truque, Classe, Raca, PersonagemHasMagia

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
        classeNome = request.COOKIES.get('classe')
        classe = Classe.objects.get(nome = classeNome)

        racaNome = request.COOKIES.get('raca')
        raca = Raca.objects.get(nome = racaNome)

        #=========================================================================
        atrForca = request.COOKIES.get('forca')
        atrDestreza = request.COOKIES.get('destreza')
        atrConstituicao = request.COOKIES.get('constituicao')
        atrInteligencia = request.COOKIES.get('inteligencia')
        atrSabedoria = request.COOKIES.get('sabedoria')
        atrCarisma = request.COOKIES.get('carisma')
        

        #=========================================================================

        personagem = Personagem.objects.get(id_personagem=1)

        form = personagemForm()
        return render(request, 'templateFichaPersonagem.html', {'personagem': personagem, 'form': form, 'proficiencias': proficiencias, 'idiomas': idiomas, 'truques': truques, 'magias': magias, 'classe': classe, 'raca': raca, 'atrForca': atrForca, 'atrDestreza': atrDestreza, 'atrConstituicao': atrConstituicao, 'atrInteligencia': atrInteligencia, 'atrSabedoria': atrSabedoria, 'atrCarisma': atrCarisma})
    
    def post(self, request):
        form = personagemForm(request.POST)
        
        
        # Salva o formulário mas não commita ainda (para adicionar dados extras)
        personagem = Personagem()
        
        # CONVERSÃO DOS ATRIBUTOS PARA INTEIRO (importante!)
        personagem.forca = int(request.COOKIES.get('forca', 10))
        personagem.destreza = int(request.COOKIES.get('destreza', 10))
        personagem.constituicao = int(request.COOKIES.get('constituicao', 10))
        personagem.inteligencia = int(request.COOKIES.get('inteligencia', 10))
        personagem.sabedoria = int(request.COOKIES.get('sabedoria', 10))
        personagem.carisma = int(request.COOKIES.get('carisma', 10))
        
        # Classe - como seu model Personagem.classe é CharField, armazena o nome
        classe_nome = request.COOKIES.get('classe')
        if classe_nome:
            personagem.classe = classe_nome  # Armazena apenas o nome como string

        # Raça - como seu model Personagem.raca é CharField, armazena o nome
        raca_nome = request.COOKIES.get('raca')
        if raca_nome:
            personagem.raca = raca_nome  # Armazena apenas o nome como string

        # ANTECEDENTE - você precisa adicionar isso também
        antecedente_nome = request.COOKIES.get('antecedente')
        if antecedente_nome:
            personagem.antecedente = antecedente_nome

        # NÍVEL - você precisa definir um nível padrão
        personagem.nivel = 1  # Ou obtenha do cookie se disponível

        # DADOS DO FORMULÁRIO DO TEMPLATE
        personagem.cor_cabelo = request.POST.get('cor_cabelo', '')
        personagem.cor_pele = request.POST.get('cor_pele', '')
        personagem.cor_olhos = request.POST.get('cor_olhos', '')
        personagem.defeitos = request.POST.get('defeitos', '')
        personagem.traco_personalidade = request.POST.get('traco_personalidade', '')
        personagem.ideais = request.POST.get('ideais', '')
        personagem.ligacoes = request.POST.get('ligacoes', '')

        

        # CAMPOS ADICIONAIS DO TEMPLATE (você precisa adicionar ao modelo)
        # Se você quiser salvar esses, precisa adicionar campos ao modelo Personagem:
        # aparencia = models.TextField(blank=True, null=True)
        # historia = models.TextField(blank=True, null=True)
        # aliados_organizacoes = models.TextField(blank=True, null=True)
        # tracos_caracteristicas = models.TextField(blank=True, null=True)
        # tesouro = models.TextField(blank=True, null=True)
        personagem.nome = request.POST.get('nome', 'Personagem Sem Nome')

        # NOME - deve ser definido ANTES de salvar
        #if not personagem.nome:  # Se não foi preenchido no form
        #    personagem.nome = "Personagem Sem Nome"
        
        # Salva o objeto completo no banco de dados
        personagem.save()

            # AGORA ADICIONAMOS AS MAGIAS SELECIONADAS USANDO SUA ABORDAGEM
        try:
            idmagias = request.COOKIES.get('idmagias')
            if idmagias:
                # Decodifica a string URL e converte para lista de IDs
                lista_decodificada = urllib.parse.unquote(idmagias)
                ids_magias = json.loads(lista_decodificada)
                
                # Filtra as magias no banco de dados
                magias = Magia.objects.filter(id_magia__in=ids_magias)
                
                # Adiciona cada magia ao personagem
                for magia in magias:
                    PersonagemHasMagia.objects.create(
                        personagem=personagem, 
                        magia=magia
                    )
                
                print(f"Adicionadas {magias.count()} magias ao personagem {personagem.nome}")
            else:
                print("Nenhuma magia encontrada nos cookies")
                
        except Exception as e:
            print(f"Erro ao adicionar magias: {e}")
            # Não impedir a criação do personagem se houver erro nas magias


        # Redireciona para evitar reenvio do formulário
        return redirect('TelaClasses')