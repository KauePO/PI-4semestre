from django.contrib import admin
from .models import Raca, Subraca, Personagem, Classe, Magia, Truque

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
