from django.contrib import admin
from .models import Raca, Subraca, Personagem, Classe, Magia, Truque, Antecedente, Armadura, TipoArmadura

# =============================
# Admin otimizado para Raca
# =============================
@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('id_raca', 'nome', 'velocidade', 'tamanho', 'icone')
    search_fields = ('nome',)
    list_filter = ('tamanho',)

# =============================
# Admin otimizado para Subraca
# =============================
@admin.register(Subraca)
class SubracaAdmin(admin.ModelAdmin):
    list_display = ('id_subraca', 'nome', 'raca')
    search_fields = ('nome', 'raca__nome')  # permite buscar pelo nome da raça
    list_filter = ('raca',)

# =============================
# Admin otimizado para Personagem
# =============================
@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    list_display = ('id_personagem', 'nome', 'idade', 'raca', 'classe', 'forca', 'destreza')
    search_fields = ('nome', 'raca', 'classe')
    list_filter = ('raca', 'classe')

# =============================
# Admin para Classe
# =============================
@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('id_classe', 'nome', 'nivel')
    search_fields = ('nome',)

# =============================
# Admin para Magia
# =============================
@admin.register(Magia)
class MagiaAdmin(admin.ModelAdmin):
    list_display = ('id_magia', 'nome_magia', 'escola', 'nivel', 'descricao')
    search_fields = ('nome_magia', 'escola', 'descricao')
    list_filter = ('escola', 'nivel')
# =============================
# Admin para Truque
# =============================
@admin.register(Truque)
class TruqueAdmin(admin.ModelAdmin):
    list_display = ('id_truque', 'escola', 'alcance', 'duracao')
    search_fields = ('escola', 'descricao')
    list_filter = ('escola',)

# =============================
# Admin para Antecedente
# =============================
@admin.register(Antecedente)
class AntecedenteAdmin(admin.ModelAdmin):
    list_display = ('id_antecedente', 'nome', 'descricao')
    search_fields = ('nome',)
    list_filter = ('nome',)

    
# =============================
# Admin para Arma
# =============================

@admin.register(Arma)
class ArmaAdmin(admin.modelAdmin):
    list_display = ('id_arma', 'nome', 'tipo', 'custo', 'peso', 'numero_dado_dano', 'dado_dano', 'tipo_dano')
    search_fields = ('nome', 'tipo')
    list_filter = ('custo', 'tipo_dano')
    

# =============================
# Admin para Tipo Armadura
# =============================
@admin.register(TipoArmadura)
class TipoArmaduraAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_armadura', 'nome_tipo_armadura', )
    search_fields = ('nome_tipo_armadura',)
    list_filter = ('nome_tipo_armadura',)

# =============================
# Admin para Armadura
# =============================
@admin.register(Armadura)
class ArmaduraAdmin(admin.ModelAdmin):
    list_display = ('id_armadura', 'nome', 'descricao', 'tipo_armadura', 'classe_de_armadura')
    search_fields = ('nome',)
    list_filter = ('nome',)

# =============================
# Admin para ConjutoEquipamento
# =============================
@admin.register(ConjuntoEquipamento)
class ConjuntoEquipamentoAdmin(admin.modelAdmin):
    list_display = ('id_conjuto_equipamento', 'nome', 'descricao', 'classe')
    search_fields = ('nome', 'descricao')
    list_filter = ('classe',)

# =============================
# Admin para EquipamentoAventura
# =============================
@admin.register(EquipamentoAventura)
class EquipamentoAventuraAdmin(admin.modelAdmin):
    list_display = ('id_equipamento_de_aventura', 'nome_ferramenta', 'descricao', 'custo', 'peso', 'classe', 'conjunto_equipamento')
    search_fields = ('nome', 'custo')
    list_filter = ('classe',)

# =============================
# Admin para Ferramenta
# =============================
@admin.register(Ferramenta)
class FerramentaAdmin(admin.modelAdmin):
    list_display = ('id_ferramenta', 'nome_ferramenta', 'custo', 'peso', 'classe')
    search_fields = ('', '')
    list_filter = ('', '')