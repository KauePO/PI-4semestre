# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Antecedente(models.Model):
    id_antecedente = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField()
    icone = models.ImageField( upload_to="racas/" ,blank=True, null=True)

    class Meta:
        db_table = 'antecedente'
    
    def __str__(self):
        return self.nome
class Arma(models.Model):
    id_arma = models.AutoField(primary_key=True)
    nome = models.CharField()
    tipo = models.CharField()
    custo = models.IntegerField()
    peso = models.FloatField()
    numero_dado_dano = models.IntegerField()
    dado_dano = models.IntegerField()
    tipo_dano = models.CharField()

    class Meta:
        db_table = 'arma'


    
    def __str__(self):
        return self.nome
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
    arma = models.ManyToManyField(Arma)
    
    

    class Meta:
        db_table = 'classe'
    
    def __str__(self):
        return self.nome
    
class ConjuntoEquipamento(models.Model):
    id_conjunto_equipamento = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField()
    classe = models.ManyToManyField(Classe)

    class Meta:
        db_table = 'conjunto_equipamento'

    
    def __str__(self):
        return self.nome

class EquipamentoDeAventura(models.Model):
    id_equipamento_de_aventura = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField(blank=True, null=True)
    custo = models.IntegerField()
    peso = models.FloatField()
    antecedente = models.ManyToManyField(Antecedente)
    classe = models.ManyToManyField(Classe)
    conjunto_equipamento = models.ManyToManyField(ConjuntoEquipamento)

    class Meta:
        db_table = 'equipamento_de_aventura'
    
    def __str__(self):
        return self.nome

class Ferramenta(models.Model):
    id_ferramenta = models.AutoField(primary_key=True)
    nome_ferramenta = models.CharField()
    custo = models.IntegerField()
    peso = models.IntegerField()
    antecedente = models.ManyToManyField(Antecedente)
    classe = models.ManyToManyField(Classe)

    class Meta:
        db_table = 'ferramenta'
    
    def __str__(self):
        return self.nome_ferramenta

class HabilidadeEspecial(models.Model):
    id_habilidade_especial = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField()

    class Meta:
        db_table = 'habilidade_especial'
        
    def __str__(self):
        return self.nome

class Idiomas(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    subraca = models.ForeignKey('Subraca', models.DO_NOTHING)
    nome = models.CharField()
    descricao = models.TextField()

    class Meta:
        db_table = 'idiomas'
    
    def __str__(self):
        return self.nome

class IncrementoHabilidade(models.Model):
    id_incremento_habilidade = models.AutoField(primary_key=True)
    subraca = models.ForeignKey('Subraca', models.DO_NOTHING, blank=1, null=1)
    nome = models.CharField()
    valor_incremento = models.IntegerField()

    class Meta:
        db_table = 'incremento_habilidade'
        
    def __str__(self):
        return self.nome

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
        
    def __str__(self):
        return self.nome_magia


class Usuario (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plano_ativo = models.BooleanField(default=False)
    data_ativacao = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return  self.user.username
    
class Cobranca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_cobranca_externo = models.CharField()
    status_cobranca = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'cobranca'
    

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
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    arma = models.ManyToManyField(Arma)
    magia = models.ManyToManyField(Magia)
    equipamento_de_aventura = models.ManyToManyField(EquipamentoDeAventura)

    class Meta:
        db_table = 'personagem'
        
    def __str__(self):
        return self.nome

class Proficiencia(models.Model):
    id_proficiencia = models.AutoField(primary_key=True)
    nome = models.CharField()
    tipo = models.CharField()
    antecedente = models.ManyToManyField(Antecedente)
    classe = models.ManyToManyField(Classe)

    class Meta:
        db_table = 'proficiencia'
    
    def __str__(self):
        return self.nome

class Propriedade(models.Model):
    id_propriedade = models.AutoField(primary_key=True)
    nome = models.CharField()
    descricao = models.TextField()
    arma = models.ManyToManyField(Arma)

    class Meta:
        db_table = 'propriedade'
        
    def __str__(self):
        return self.nome

class Raca(models.Model):
    id_raca = models.AutoField(primary_key=True)
    nome = models.CharField()
    velocidade = models.FloatField()
    tamanho = models.IntegerField()
    descricao = models.TextField()
    icone = models.ImageField( upload_to="racas/" ,blank=True, null=True)
    incremento_habilidade = models.ManyToManyField(IncrementoHabilidade)
    idioma = models.ManyToManyField('Idiomas')
    habilidade_especial = models.ManyToManyField(HabilidadeEspecial)
    incremento_habilidade = models.ManyToManyField(IncrementoHabilidade)

    class Meta:
        db_table = 'raca'
    
    def __str__(self):
        return self.nome

class Subraca(models.Model):
    id_subraca = models.AutoField(primary_key=True)
    raca = models.ForeignKey(Raca, models.DO_NOTHING)
    nome = models.CharField()
    habilidade_especial = models.ManyToManyField(HabilidadeEspecial)

    class Meta:
        db_table = 'subraca'
        
    def __str__(self):
        return self.nome

class TipoArmadura(models.Model):
    id_tipo_armadura = models.AutoField(primary_key=True)
    nome_tipo_armadura = models.CharField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    classe = models.ManyToManyField(Classe, blank=True)
    personagem = models.ManyToManyField(Personagem, blank=True)

    class Meta:
        db_table = 'tipo_armadura'
    
    def __str__(self):
        return self.nome_tipo_armadura
        

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
    raca = models.ManyToManyField(Raca)
    subraca = models.ManyToManyField(Subraca)

    class Meta:
        db_table = 'truque'
        
    def __str__(self):
        return self.nome_truque

