from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse as r

class testViewTelaCadastroPost(TestCase):
    def setUp(self):
        
        data = {
            "username":"jonhTestes",
            "password1":"fvc123456@",
            "password2":"fvc123456@"
        }
        
        self.client_invalido = Client()
        self.client_valido = Client()
        
        self.resposta_invalido = self.client_invalido.post(r("telaCadastro"))
        self.resposta_valido = self.client_valido.post(r("telaCadastro"),data)
        
        
    
    def test_200_reponse_invalido(self):
        self.assertEqual(self.resposta_invalido.status_code, 200)
    
    def test_template_invalido(self):
        self.assertTemplateUsed(self.resposta_invalido, "templateCadastro.html")

    def test_302_reponse_valido(self):
        self.assertEqual(self.resposta_valido.status_code, 302)
    
    def test_valido_redirect_target_url(self):
        self.assertRedirects(self.resposta_valido, r("telaLogin"))
        
    def test_criacao_user(self):
        user = User.objects.get(username = "jonhTestes")
        self.assertTrue(user)
    
