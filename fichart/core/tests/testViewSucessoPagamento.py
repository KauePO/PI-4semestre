
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from core.models import Cobranca, Usuario
from django.contrib.messages import get_messages


class testViewSucessoPagamento(TestCase):
    
    def setUp(self):
        USERNAME = "john"
        EMAIL = "teste@teste.com"
        PASSWORD = "1234"
        
        self.user = User.objects.create_user(USERNAME, EMAIL, PASSWORD)
        self.usuario = Usuario.objects.get(user = self.user)
        
        
        
        self.client = Client()
        self.client.login(username = USERNAME, password = PASSWORD)
    
    def test_302_response(self):
        resposta = self.client.get(reverse("sucessoPagamento"))
        
        self.assertEqual(resposta.status_code, 302)
    
    def test_alteracao_cobranca(self):
        Cobranca.objects.create(usuario=self.usuario, status_cobranca="PENDING", id_cobranca_externo="abc456")
        
        self.client.get(reverse("sucessoPagamento"))
        
        cobranca = Cobranca.objects.get(usuario = self.usuario)
        
        self.assertIn(cobranca.status_cobranca, "PAID")
    
    def test_exception(self):
        resposta = self.client.get(reverse("sucessoPagamento"))
        
        messages = list(get_messages(resposta.wsgi_request))
        
        self.assertTrue(len(messages) > 0)
        self.assertIn(str(messages[0]), "Não foi possivel registrar o seu pagamento")