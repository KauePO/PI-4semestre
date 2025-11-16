from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse as r

class TestViewTelaCadastroGet(TestCase):
    USERNAME = "john"
    EMAIL = "teste@teste.com"
    PASSWORD = "1234"
    
    def setUp(self):
        
        self.user = User.objects.create_user(self.USERNAME,self.EMAIL,self.PASSWORD)
        self.client_deslogado = Client()
        self.client_logado = Client()
        
        self.client_logado.login(username = self.USERNAME, password = self.PASSWORD)
        
        self.resposta_deslogado = self.client_deslogado.get(r("telaCadastro"))
        self.resposta_logado = self.client_logado.get(r("telaCadastro"))
    
    def test_200_reponse_deslogado(self):
        self.assertEqual(self.resposta_deslogado.status_code, 200)
    
    def test_template_deslogado(self):
        self.assertTemplateUsed(self.resposta_deslogado, "templateCadastro.html")
    
    def test_302_reponse_logado(self):
        self.assertEqual(self.resposta_logado.status_code, 302)
    
    def test_redirect_target_url(self):
        self.assertRedirects(self.resposta_logado, r("paginaInicial"))