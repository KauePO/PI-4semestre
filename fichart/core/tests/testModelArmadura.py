from django.test import TestCase
from core.models import Armadura,TipoArmadura

class testModelArmadura(TestCase):
    def setUp(self):
        self.nome_armadura="chain_mail"
        tipoArmadura = TipoArmadura(nome_tipo_armadura="leve", descricao="ssdgsgdjhgjs")
        self.armadura = Armadura(tipo_armadura=tipoArmadura,nome=self.nome_armadura,descricao="resistente",classe_de_armadura=2,forca=10,furtividade_desvantagem=True,peso=1,custo=5)


    def test_armadura_str(self):
        self.assertEqual(self.armadura.__str__(),self.nome_armadura)
        