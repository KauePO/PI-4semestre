from django.contrib import admin

from .models import Raca, Subraca, Personagem, Classe, Magia, Proficiencia, Truque, Antecedente, Armadura, TipoArmadura, Idiomas, Arma, ConjuntoEquipamento, EquipamentoDeAventura, Ferramenta, IncrementoHabilidade, Usuario, Cobranca, HabilidadeEspecial


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
class ArmaAdmin(admin.ModelAdmin):
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
    
@admin.register(IncrementoHabilidade)
class IncrementoHabilidadeAdmin(admin.ModelAdmin):
        list_display = ("nome","valor_incremento")
        

@admin.register (Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("user","plano_ativo")
    
@admin.register (Cobranca)
class CobrancaAdmin(admin.ModelAdmin):
    list_display = ("usuario","status_cobranca")

# =============================
# Admin para ConjutoEquipamento
# =============================
@admin.register(ConjuntoEquipamento)
class ConjuntoEquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome', 'descricao')
    list_filter = ('classe',)

# =============================
# Admin para EquipamentoAventura
# =============================
@admin.register(EquipamentoDeAventura)
class EquipamentoAventuraAdmin(admin.ModelAdmin):
    list_display = ( 'nome', 'descricao', 'custo', 'peso')
    search_fields = ('nome', 'custo')
    list_filter = ('classe',)

# =============================
# Admin para Ferramenta
# =============================
@admin.register(Ferramenta)
class FerramentaAdmin(admin.ModelAdmin):
    list_display = ('nome_ferramenta', 'custo', 'peso')
    search_fields = ('nome_ferramenta', 'custo')
    list_filter = ('classe',)
    
# =============================
# Admin para Habilidade Especial
# =============================
@admin.register(HabilidadeEspecial)
class HabilidadeEspecialAdmin(admin.ModelAdmin):
    list_display = ('id_habilidade_especial', 'nome', 'descricao', )
    search_fields = ('nome',)
    list_filter = ('nome',)

# =============================
# Admin para Idiomas
# =============================
@admin.register(Idiomas)
class IdiomasAdmin(admin.ModelAdmin):
    list_display = ('id_idioma', 'subraca', 'nome', 'descricao', )
    search_fields = ('nome',)
    list_filter = ('nome',)

# =============================
# Admin para Proficiencias
# =============================
@admin.register(Proficiencia)
class ProficienciaAdmin(admin.ModelAdmin):
    list_display = ('id_proficiencia', 'nome', 'tipo',)
    search_fields = ('nome',)
    list_filter = ('nome',)
