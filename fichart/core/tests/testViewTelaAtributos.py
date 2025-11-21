from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse as r


class TestViewTelaAtributos(TestCase):
    USERNAME = "john"
    EMAIL = "teste@teste.com"
    PASSWORD = "1234"
    
    def setUp(self):
        
        
        self.user = User.objects.create_user(self.USERNAME, self.EMAIL, self.PASSWORD)
        
        self.client = Client()
        self.client.login(username = self.USERNAME, password = self.PASSWORD)
        
        self.resposta = self.client.get(r("TelaAtributos"))
    
    def test_200_response(self):
        self.assertEqual(self.resposta.status_code,200)