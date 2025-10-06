# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Antecedente(models.Model):
    id_antecedente = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField()
    icone = models.ImageField( upload_to="racas/" ,blank=True, null=True)

    class Meta:
        db_table = 'antecedente'


class AntecedenteHasEquipamentoDeAventura(models.Model):
    pk = models.CompositePrimaryKey('antecedente_id', 'equipamento_de_aventura_id')
    antecedente = models.ForeignKey(Antecedente, models.DO_NOTHING)
    equipamento_de_aventura = models.ForeignKey('EquipamentoDeAventura', models.DO_NOTHING)

    class Meta:
        db_table = 'antecedente_has_equipamento_de_aventura'


class AntecedenteHasFerramenta(models.Model):
    pk = models.CompositePrimaryKey('antecedente_id', 'ferramenta_id')
    antecedente = models.ForeignKey(Antecedente, models.DO_NOTHING)
    ferramenta = models.ForeignKey('Ferramenta', models.DO_NOTHING)

    class Meta:
        db_table = 'antecedente_has_ferramenta'


class AntecedenteHasProficiencia(models.Model):
    pk = models.CompositePrimaryKey('antecedente_id', 'proficiencia_id')
    antecedente = models.ForeignKey(Antecedente, models.DO_NOTHING)
    proficiencia = models.ForeignKey('Proficiencia', models.DO_NOTHING)

    class Meta:
        db_table = 'antecedente_has_proficiencia'


class Arma(models.Model):
    id_arma = models.AutoField(primary_key=True)
    tipo = models.CharField()
    custo = models.IntegerField()
    peso = models.FloatField()
    numero_dado_dano = models.IntegerField()
    dado_dano = models.IntegerField()
    tipo_dano = models.CharField()

    class Meta:
        db_table = 'arma'


class ArmaHasClasse(models.Model):
    pk = models.CompositePrimaryKey('arma_id', 'classe_id')
    arma = models.ForeignKey(Arma, models.DO_NOTHING)
    classe = models.ForeignKey('Classe', models.DO_NOTHING)

    class Meta:
        db_table = 'arma_has_classe'


class ArmaHasPersonagem(models.Model):
    pk = models.CompositePrimaryKey('arma_id', 'personagem_id')
    arma = models.ForeignKey(Arma, models.DO_NOTHING)
    personagem = models.ForeignKey('Personagem', models.DO_NOTHING)

    class Meta:
        db_table = 'arma_has_personagem'


class Armadura(models.Model):
    id_armadura = models.AutoField(primary_key=True)
    tipo_armadura = models.ForeignKey('TipoArmadura', models.DO_NOTHING)
    nome = models.CharField()
    descricao = models.TextField()
    classe_de_armadura = models.IntegerField()
    forca = models.IntegerField()
    furtividade_desvantagem = models.BooleanField()
    peso = models.IntegerField()
    custo = models.IntegerField()

    class Meta:
        db_table = 'armadura'
        
    def __str__(self):
        return self.nome
        

class Classe(models.Model):
    id_classe = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField()
    hp_n_dados = models.IntegerField()
    hp_dado = models.IntegerField()
    hb_base = models.IntegerField()
    hp_modificador = models.CharField()
    nivel = models.IntegerField()
    icone = models.ImageField( upload_to="classes/" ,blank=True, null=True)
    armadura = models.ManyToManyField(Armadura)
    

    class Meta:
        db_table = 'classe'
    
    def __str__(self):
        return self.nome


class ClasseHasProficiencia(models.Model):
    pk = models.CompositePrimaryKey('classe_id', 'proficiencia_id')
    classe = models.ForeignKey(Classe, models.DO_NOTHING)
    proficiencia = models.ForeignKey('Proficiencia', models.DO_NOTHING)

    class Meta:
        db_table = 'classe_has_proficiencia'
        
        


class ConjuntoEquipamento(models.Model):
    id_conjunto_equipamento = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField()

    class Meta:
        db_table = 'conjunto_equipamento'


class ConjuntoEquipamentoHasClasse(models.Model):
    pk = models.CompositePrimaryKey('conjunto_equipamento_id', 'classe_id')
    conjunto_equipamento = models.ForeignKey(ConjuntoEquipamento, models.DO_NOTHING)
    classe = models.ForeignKey(Classe, models.DO_NOTHING)

    class Meta:
        db_table = 'conjunto_equipamento_has_classe'


class EquipamentoDeAventura(models.Model):
    id_equipamento_de_aventura = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField(blank=True, null=True)
    custo = models.IntegerField()
    peso = models.FloatField()

    class Meta:
        db_table = 'equipamento_de_aventura'


class EquipamentoDeAventuraHasClasse(models.Model):
    pk = models.CompositePrimaryKey('classe_id', 'equipamento_de_aventura_id')
    classe = models.ForeignKey(Classe, models.DO_NOTHING)
    equipamento_de_aventura = models.ForeignKey(EquipamentoDeAventura, models.DO_NOTHING)

    class Meta:
        db_table = 'equipamento_de_aventura_has_classe'


class EquipamentoDeAventuraHasConjuntoEquipamento(models.Model):
    pk = models.CompositePrimaryKey('conjunto_equipamento_id', 'equipamento_de_aventura_id')
    conjunto_equipamento = models.ForeignKey(ConjuntoEquipamento, models.DO_NOTHING)
    equipamento_de_aventura = models.ForeignKey(EquipamentoDeAventura, models.DO_NOTHING)

    class Meta:
        db_table = 'equipamento_de_aventura_has_conjunto_equipamento'


class Ferramenta(models.Model):
    id_ferramenta = models.AutoField(primary_key=True)
    nome_ferramenta = models.CharField()
    custo = models.IntegerField()
    peso = models.IntegerField()

    class Meta:
        db_table = 'ferramenta'


class FerramentaHasClasse(models.Model):
    pk = models.CompositePrimaryKey('classe_id', 'ferramenta_id')
    classe = models.ForeignKey(Classe, models.DO_NOTHING)
    ferramenta = models.ForeignKey(Ferramenta, models.DO_NOTHING)

    class Meta:
        db_table = 'ferramenta_has_classe'


class HabilidadeEspecial(models.Model):
    id_habilidade_especial = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField()

    class Meta:
        db_table = 'habilidade_especial'


class IdiomaHasRaca(models.Model):
    pk = models.CompositePrimaryKey('idioma_id', 'raca_id')
    idioma = models.ForeignKey('Idiomas', models.DO_NOTHING)
    raca = models.ForeignKey('Raca', models.DO_NOTHING)

    class Meta:
        db_table = 'idioma_has_raca'


class Idiomas(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    subraca = models.ForeignKey('Subraca', models.DO_NOTHING)
    nome = models.CharField()
    descricao = models.TextField()

    class Meta:
        db_table = 'idiomas'


class IncrementoHabilidade(models.Model):
    id_incremento_habilidade = models.AutoField(primary_key=True)
    subraca = models.ForeignKey('Subraca', models.DO_NOTHING)
    nome = models.CharField()
    valor_incremento = models.IntegerField()

    class Meta:
        db_table = 'incremento_habilidade'


class Magia(models.Model):
    id_magia = models.AutoField(primary_key=True)
    nome_magia = models.CharField()
    escola = models.CharField()
    tempo_conjuracao = models.CharField()
    alcance = models.IntegerField()
    componentes = models.CharField()
    duraca = models.CharField()
    descricao = models.CharField()
    nivel = models.IntegerField(blank=True, null=True)
    classe = models.ManyToManyField(Classe)

    class Meta:
        db_table = 'magia'


class Personagem(models.Model):
    id_personagem = models.AutoField(primary_key=True)
    nome = models.CharField()
    idade = models.IntegerField(blank=True, null=True)
    raca = models.CharField()
    classe = models.CharField()
    antecedente = models.CharField(blank=True, null=True)
    forca = models.IntegerField()
    destreza = models.IntegerField()
    sabedoria = models.IntegerField()
    inteligencia = models.IntegerField()
    carisma = models.IntegerField()
    constituicao = models.IntegerField()
    altura = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    cor_cabelo = models.CharField(blank=True, null=True)
    cor_pele = models.CharField(blank=True, null=True)
    cor_olhos = models.CharField(blank=True, null=True)
    defeitos = models.CharField(blank=True, null=True)
    traco_personalidade = models.CharField(blank=True, null=True)
    ideais = models.CharField(blank=True, null=True)
    ligacoes = models.CharField(blank=True, null=True)

    class Meta:
        db_table = 'personagem'


class PersonagemHasEquipamentoDeAventura(models.Model):
    pk = models.CompositePrimaryKey('personagem_id', 'equipamento_de_aventura_id')
    personagem = models.ForeignKey(Personagem, models.DO_NOTHING)
    equipamento_de_aventura = models.ForeignKey(EquipamentoDeAventura, models.DO_NOTHING)

    class Meta:
        db_table = 'personagem_has_equipamento_de_aventura'


class PersonagemHasMagia(models.Model):
    pk = models.CompositePrimaryKey('personagem_id', 'magia_id')
    personagem = models.ForeignKey(Personagem, models.DO_NOTHING)
    magia = models.ForeignKey(Magia, models.DO_NOTHING)

    class Meta:
        db_table = 'personagem_has_magia'


class PersonagemHasTipoArmadura(models.Model):
    pk = models.CompositePrimaryKey('personagem_id', 'tipo_armadura_id')
    personagem = models.ForeignKey(Personagem, models.DO_NOTHING)
    tipo_armadura = models.ForeignKey('TipoArmadura', models.DO_NOTHING)

    class Meta:
        db_table = 'personagem_has_tipo_armadura'


class Proficiencia(models.Model):
    id_proficiencia = models.AutoField(primary_key=True)
    nome = models.CharField()
    tipo = models.CharField()

    class Meta:
        db_table = 'proficiencia'


class Propriedade(models.Model):
    id_propriedade = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField()

    class Meta:
        db_table = 'propriedade'


class PropriedadeHasArma(models.Model):
    pk = models.CompositePrimaryKey('propriedade_id', 'arma_id')
    propriedade = models.ForeignKey(Propriedade, models.DO_NOTHING)
    arma = models.ForeignKey(Arma, models.DO_NOTHING)

    class Meta:
        db_table = 'propriedade_has_arma'


class Raca(models.Model):
    id_raca = models.AutoField(primary_key=True)
    nome = models.CharField()
    velocidade = models.FloatField()
    tamanho = models.IntegerField()
    id_subraca = models.IntegerField()
    descricao = models.TextField()
    icone = models.ImageField( upload_to="racas/" ,blank=True, null=True)

    class Meta:
        db_table = 'raca'


class RacaHasHabilidadeEspecial(models.Model):
    pk = models.CompositePrimaryKey('raca_id', 'habilidade_especial_id')
    raca = models.ForeignKey(Raca, models.DO_NOTHING)
    habilidade_especial = models.ForeignKey(HabilidadeEspecial, models.DO_NOTHING)

    class Meta:
        db_table = 'raca_has_habilidade_especial'


class RacaHasIncrementoHabilidade(models.Model):
    pk = models.CompositePrimaryKey('raca_id', 'incremento_habilidade_id')
    raca = models.ForeignKey(Raca, models.DO_NOTHING)
    incremento_habilidade = models.ForeignKey(IncrementoHabilidade, models.DO_NOTHING)

    class Meta:
        db_table = 'raca_has_incremento_habilidade'


class RacaHasTruque(models.Model):
    pk = models.CompositePrimaryKey('raca_id', 'truque_id')
    raca = models.ForeignKey(Raca, models.DO_NOTHING)
    truque = models.ForeignKey('Truque', models.DO_NOTHING)

    class Meta:
        db_table = 'raca_has_truque'


class Subraca(models.Model):
    id_subraca = models.AutoField(primary_key=True)
    raca = models.ForeignKey(Raca, models.DO_NOTHING)
    nome = models.CharField()

    class Meta:
        db_table = 'subraca'


class SubracaHasHabilidadeEspecial(models.Model):
    pk = models.CompositePrimaryKey('subraca_id', 'habilidade_especial_id')
    subraca = models.ForeignKey(Subraca, models.DO_NOTHING)
    habilidade_especial = models.ForeignKey(HabilidadeEspecial, models.DO_NOTHING)

    class Meta:
        db_table = 'subraca_has_habilidade_especial'


class SubracaHasTruque(models.Model):
    pk = models.CompositePrimaryKey('subraca_id', 'truque_id')
    subraca = models.ForeignKey(Subraca, models.DO_NOTHING)
    truque = models.ForeignKey('Truque', models.DO_NOTHING)

    class Meta:
        db_table = 'subraca_has_truque'


class TipoArmadura(models.Model):
    id_tipo_armadura = models.AutoField(primary_key=True)
    nome_tipo_armadura = models.CharField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tipo_armadura'


class Truque(models.Model):
    id_truque = models.AutoField(primary_key=True)
    nome_truque = models.CharField()
    escola = models.CharField()
    tempo_conjuracao = models.IntegerField()
    alcance = models.IntegerField()
    componentes = models.CharField()
    duracao = models.CharField()
    descricao = models.CharField()
    classes = models.ManyToManyField(Classe)

    class Meta:
        db_table = 'truque'

