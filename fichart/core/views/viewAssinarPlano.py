from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect
from core.models import Usuario, Cobranca
import requests

class viewAssinarPlano(LoginRequiredMixin, View):
    def get(self, request):
        
        error = []
        url = ""
        token = "abc_dev_RJh2nXJLpFtyKGRt0BDNBxAk"
        
        
        usuario = Usuario.objects.get(user = request.user)
        cobrancaExistente = Cobranca.objects.filter(status_cobranca = "PENDING").first()
        
        if cobrancaExistente:
            
            print("Ta devendo")
            url = "https://api.abacatepay.com/v1/billing/list"
            
            headers ={
                "Authorization":f"Bearer {token}"
            }
            
            response = requests.get(url, headers=headers).json()
            
            if (response.get("data",{})[0].get("status") == "PENDING"){
                urlPagamento = response.get("data",{})[0].get("url")
                return redirect(urlPagamento)
            }
            
            cobrancaExistente.status_cobranca = response.get("data",{})[0].get("status")
            
            
            
        
        headers ={
            "Authorization":f"Bearer {token}",
            "Content-Type":"application/json"
        }
        
        url = "https://api.abacatepay.com/v1/billing/create"
        
        
        data = {
            "frequency": "ONE_TIME",
            "methods": ["PIX"],
            "products": [
                {
                    "externalId": "1",
                    "name": "Assinatura Aventureiro",
                    "description": "Acesso a 50 fichas.",
                    "quantity": 1,
                    "price": 1399
                }
            ],
            "returnUrl": "http://localhost:8000/paginaInicial/",
            "completionUrl": "http://localhost:8000/sucessoPagamento/",
        }
        
        try:
            print("criando nova")
            
            response = requests.post(url, headers=headers, json=data)
            responseData = response.json()
            urlPagamento = responseData.get("data",{}).get("url")
            id_cobranca = responseData.get("data",{}).get("id")
            status_cobranca = responseData.get("data",{}).get("status")
            
            novaCobranca = Cobranca(usuario = usuario, id_cobranca_externo = id_cobranca, status_cobranca = status_cobranca)
            
            novaCobranca.save()
        
        except Exception as e:
            error.append(e)
        
        return redirect(urlPagamento)
        
    