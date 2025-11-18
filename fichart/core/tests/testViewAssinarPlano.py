from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Usuario, Cobranca
import responses

class testViewAssinarPlano(TestCase):
    
    def setUp(self):
        USERNAME = "teste"
        PASSWORD = "1234"
        
        self.user = User.objects.create_user(USERNAME,"teste@teste.com",PASSWORD)
        self.usuario = Usuario.objects.get(user = self.user)
        self.client = Client()
        self.client.login(username= USERNAME, password= PASSWORD)
        self.api_base = "https://api.abacatepay.com/v1/billing"
        
    @responses.activate
    def testCobrancaExistente(self):
        
        cobranca = Cobranca.objects.create(usuario=self.usuario, status_cobranca="PENDING", id_cobranca_externo="abc123")
        
        responses.add(responses.GET,
                    f"{self.api_base}/list",
                    json={"data":[
                            {
                                "status":"PENDING", "url":"https://pagamento.com/checkout123" 
                            }
                        
                        ]},
                    status = 200
                    
                    )

        resposta = self.client.get(reverse("assinarPlano"))
        
        self.assertRedirects(resposta,"https://pagamento.com/checkout123", fetch_redirect_response=False)
        
    
    @responses.activate
    def testCobrancaExistenteDesatualizada(self):
        
        Cobranca.objects.create(usuario=self.usuario, status_cobranca="PENDING", id_cobranca_externo="abc456")
        
        responses.add(responses.GET,
                    f"{self.api_base}/list",
                    json={"data":[
                            {
                                "status":"PAID"
                            }
                        
                        ]},
                    status = 200
                    
                    )
        
        responses.add(
            responses.POST,
            f"{self.api_base}/create",
            json={
                    "data":{
                        "url":"https://pagamento.com/checkout456",
                        "id": "5678",
                        "status": "PENDING"
                    }
                    
                },
            
            status = 200
        )

        self.client.get(reverse("assinarPlano"))
        
        cobranca = Cobranca.objects.get(id_cobranca_externo = "abc456")
        
        
        self.assertEqual(cobranca.status_cobranca, "PAID")
        
        
        
    @responses.activate
    def testCobrancaNaoExistente(self):
        responses.add(
            responses.POST,
            f"{self.api_base}/create",
            json={
                    "data":{
                        "url":"https://pagamento.com/checkout456",
                        "id": "12345678",
                        "status": "PENDING"
                    }
                    
                },
            
            status = 200
        )
        
        resposta = self.client.get(reverse("assinarPlano"))
        
        self.assertRedirects(resposta, "https://pagamento.com/checkout456", fetch_redirect_response=False)
        
        cobranca = Cobranca.objects.get(id_cobranca_externo = "12345678")
        
        self.assertTrue(cobranca)
        
    @responses.activate
    def testErroCobrancaNaoExistente(self):
        
        resposta = self.client.get(reverse("assinarPlano"))
        
        self.assertRedirects(resposta, reverse("paginaInicial"))
        
        cobranca = Cobranca.objects.filter(id_cobranca_externo = "12345678")
        
        self.assertFalse(cobranca)
        
        