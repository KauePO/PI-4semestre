from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse as r


class testViewPaginaInicial(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = "john",email = "teste@teste.com",password = "1234")
        self.client = Client()
        
        self.client.login(username = "john", password = "1234")
        self.resposta = self.client.get(r("paginaInicial"))
    
    def test_200_response(self):
        self.assertEqual(self.resposta.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.resposta, "templatePaginaInicial.html")
        